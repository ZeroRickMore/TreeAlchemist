'''
Script to handle the defense launch, based off the current ADT state.

It uses the same State and Tree classes used in TreeAlchemist,
and maps each agent to a list of states based on the ADT.
Realistically, it is a dictionary from {ADT_name (str) : state (list[int])

This manager gets the alerts raised from syslog

The folder Trees contains a set of text files that help recreate the tree and nodes very simply.
They are automatically generated by ADT-Generator

Tree:
[100017, 100018...] # The id of the nodes, no matter the order
States:
[100017]=Def1
[100018]=Def2
[100017,100018]=Def3


General idea:
An alert is raised on Wazuh, and delivered to rsyslog, specifically on the file tree_alchemized_alerts.log
as specified in rsyslog config.

A tool watches the log file, and gathers the informations about the file modifications.
Each line of the log contains an alert, and the only important sections are the rule ID, the Tree name, and the Agent that raised the alert.

This daemon updates the tree state (there is a dictionary containing Agent name, with value another dict mapping a Tree Name to a list, the list being the state)


Please note that this version is Linux-specific, as it uses system calls.
'''

import os
from flask import Flask, request, jsonify
import logging
import read_toml
import ADT_daemon_readable_txt_parser
import wazuh_adtmanagerd_utils
from pprint import pprint
import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime, timedelta



debug = True

app = Flask(__name__)
print("==========Gathering the Trees==========\n\n")

this_script_dir = os.path.dirname(__file__)
log_file_path = os.path.join(this_script_dir, 'Logs', 'wazuh_adtmanagerd.log')
tree_name_to_structure_dict = ADT_daemon_readable_txt_parser.parse_all_daemon_readable_files(os.path.join(this_script_dir, 'Trees'))

api_username = read_toml.get_api_username()
api_pwd = read_toml.get_api_pwd()

JWT_token = None
JWT_refresh_time = read_toml.get_JWT_refresh_time() # Time in seconds after which the JWT token expires
JWT_expire_timestamp = None



print("==========================================================================================\nThis is the dictionary that was gathered. Feel free to ignore it.\n==========================================================================================\n\n")

pprint(tree_name_to_structure_dict)

print("\n==========================================================================================\nThis is the dictionary that was gathered. Feel free to ignore it.\n==========================================================================================\n\n")


logging.basicConfig(
            filename=log_file_path,
            filemode='a',  # Append mode
            format='%(asctime)s - %(message)s',
            level=logging.INFO # This captures INFO and higher
)


app.logger = logging.getLogger()
app.logger.info("===== wazuh_adtmanagerd started =====")


@app.route('/new-alert', methods=['POST'])
def process_new_alert():
    data = request.json
    alert = data.get('alert')
    app.logger.info(f"Processing new alert: [ {alert} ] ============")

    alert_infos = wazuh_adtmanagerd_utils.parse_alert_log_line(alert)

    # Update tree state
    should_I_look_for_defense = update_tree_state(alert_infos)
    # Raise defenses if a state is matched
    if should_I_look_for_defense:
        which_defenses_ran_and_wazuh_api_response = run_defenses_if_present(alert_infos)

    if not should_I_look_for_defense:
        return jsonify({"status": "success", "message": f"Alert {alert_infos['rule_id']} was already raised, doing nothing."}), 200
    
    curr_state = tree_name_to_structure_dict[alert_infos['tree_name']]['current_state']
    if not which_defenses_ran_and_wazuh_api_response:
        return jsonify({"status": "success", "message": f"State {curr_state} was not mapped to any defense, doing nothing."}), 200
    
    return jsonify({"status": "success", "message": f"State {curr_state} led to the execution of some defenses." , "defenses_recap" : which_defenses_ran_and_wazuh_api_response}), 200


def update_tree_state(alert_infos) -> bool:
    '''
    Returns False if the state was already present (you should NOT run defenses)

    True if the state was NOT present (you MUST run defenses)
    '''
    global tree_name_to_structure_dict

    tree_name = alert_infos['tree_name']
    curr_tree_structure_dict = tree_name_to_structure_dict[tree_name]

    curr_alert_id = alert_infos['rule_id']

    if curr_alert_id in curr_tree_structure_dict['current_state']:
        app.logger.info(f"Alert with rule id {curr_alert_id} has already been triggered. Doing nothing.")

        if debug:
            print(f"DEBUG: {curr_alert_id} IS ALREADY IN CURRENT STATE : {curr_tree_structure_dict['current_state']}")
            
        return False
    
    curr_state_to_list = list(curr_tree_structure_dict['current_state'])
    curr_state_to_list.append(curr_alert_id)
    curr_tree_structure_dict['current_state'] = tuple(curr_state_to_list) # It's as a tuple because the idea that mutating it is hard is very fitting.
    
    if debug:
        print(f"DEBUG: UPDATING TREE STATE -> {curr_tree_structure_dict['current_state']}")

    return True


def run_defenses_if_present(alert_infos):
    '''
    Returns a dict of the defenses that were executed mapped to the raw response of Wazuh API .
    '''
    global tree_name_to_structure_dict

    tree_name = alert_infos['tree_name']
    curr_tree_structure_dict = tree_name_to_structure_dict[tree_name]
    curr_state_to_set = set(curr_tree_structure_dict['current_state']) # To allow orderless comparison
    curr_tree_states_that_have_a_defense = curr_tree_structure_dict['states_to_defenses']

    for state in curr_tree_states_that_have_a_defense:
        if curr_state_to_set == set(state):

            if debug:
                print(f"DEBUG: A defense has been matched for state [ {state} ] in ADT = [ {tree_name} ]. Trying to launch it.")

            app.logger.info(f'A defense has been matched for state [ {state} ] in ADT = [ {tree_name} ]. Trying to launch it.')
            return launch_defense_commands(defense_commands=curr_tree_states_that_have_a_defense[state], agent=alert_infos['agent'])
            
    curr_state = curr_tree_structure_dict['current_state']
    if debug:
        print(f"DEBUG: No defenses found for state [ {curr_state} ] in ADT = [ {tree_name} ]. Doing nothing.")

    app.logger.info(f'No defenses found for state [ {curr_state} ] in ADT = [ {tree_name} ]. Doing nothing.')

    return {}


def launch_defense_commands(defense_commands : list[str], agent : str) -> dict[str, dict]:
    # Insert the logic to manage the PUT inside of WazuhServer API.
    '''
    Executes the defense commands, and returns a dictionary with defense -> raw response of Wazuh API .
    '''
    defense_to_status = {}
    for defense in defense_commands:
        set_wazuh_jwt_token() # Making extra sure the token is valid. We really want that defense to work, after all !

        if defense in defense_to_status.keys():
            app.logger.warning(f"The defense {defense} is duplicated in one of the states, running it only once.")
            continue

        defense_to_status[defense] = launch_single_defense(defense=defense, agent=agent)
    
    return defense_to_status


def launch_single_defense(defense : str, agent : str):
    # Replace these placeholders with actual values
    command = defense

    # Get agent ID having name by interrogating Wazuh api
    agent = requests.get(url=f'https://127.0.0.1:55000/agents?name={agent}&select=id', headers={'Authorization' : f'Bearer {JWT_token}'}, verify=False).json()['data']['affected_items'][0]['id']

    
    url = f"https://127.0.0.1:55000/active-response?agents_list={agent}"

    headers = {
        "Authorization": f"Bearer {JWT_token}",
    }

    # Sending the command "disable"
    data = {
        "command": "Launch_TA_Root_Def1.sh0"
    }

    response = requests.put(url, headers=headers, json=data, verify=False)

    code = response.status_code

    if code == 200:
        app.logger.info(f"Defense {defense} launched with success on agent {agent}")
    else:
        app.logger.error(response.json())

    # Print the response text
    return response.json()


def set_wazuh_jwt_token():
    global JWT_expire_timestamp, JWT_token

    if JWT_refresh_time is not None and JWT_token is not None:
        # We want to be extremely sure that the JWT token is valid, hence we want a window of at least 20 seconds
        # to utilize it
        if datetime.now() < JWT_expire_timestamp - timedelta(seconds=20):
            return

    # Replace with your username and password
    username = api_username
    password = api_pwd

    # URL for authentication
    url = "https://127.0.0.1:55000/security/user/authenticate"

    # Disable SSL verification (similar to `-k` in curl)
    response = requests.post(url, auth=HTTPBasicAuth(username, password), verify=False)
    try:
        response.raise_for_status()
    except Exception as e:
        app.logger.error(f"THE API CREDENTIALS ARE WRONG OR THERE IS AN ERROR WITH THE WAZUH API: [ {e} ]")
    
    JWT_expire_timestamp = datetime.now() + timedelta(seconds=JWT_refresh_time)
    app.logger.info("Requested a new JWT token to Wazuh API succesfully.")
    # Return JWT
    JWT_token = response.json()['data']['token']



@app.route('/', methods=['GET'])
def show_dashboard():
    return 'Hello World!'        






def run_webserver(port : int):
    global app   
    app.run(threaded=True, port=port, debug=False, use_reloader=False)

if __name__ == '__main__':
    run_webserver(read_toml.get_port())