'''
Script di lettura del file states_to_defense.xml di input, scritto dall'utente.

L'obbiettivo è ottenere le difese in strutture dati utilizzabili.
'''
import xml.etree.ElementTree as ET
import os
from terminal_UI_utils import PrintUtils, ExitUtils
from typing import List

from StateClasses.State import State
from StateClasses.StateDefense import StateDefense


def get_all_states_to_defense_from_states_to_defense_xml(tree_dir_path : str) -> tuple[List[State], dict[int, State]]:
    states_to_defense_xml_path : str = os.path.join(tree_dir_path, "states_to_defense.xml")

    validate_xml_file_and_launch_error(states_to_defense_xml_path)

    return generate_states_to_defense_from_xml(states_to_defense_xml_path)


def validate_xml_file_and_launch_error(states_to_defense_xml_path : str) -> None:
    if not validate_states_to_defense_xml_file(states_to_defense_xml_path=states_to_defense_xml_path):
        ExitUtils.exit_with_error(f"{states_to_defense_xml_path} is not a valid .xml file.")

def validate_states_to_defense_xml_file(states_to_defense_xml_path : str) -> bool:
    if not (os.path.isfile(states_to_defense_xml_path) and states_to_defense_xml_path.endswith('.xml') ):
      return False
    tree = ET.parse(states_to_defense_xml_path)
    root = tree.getroot()
    return root.tag == 'states'



def generate_states_to_defense_from_xml(states_to_defense_xml_path : str) -> tuple[List[State], dict[int, State]]:
    '''
    Read the xml and generate the real data structures.
    '''


    all_states : List[State] = []
    state_id_to_state : dict[int, State] = {}


    root = get_xml_root(states_to_defense_xml_path)

    for i, state in enumerate(root.findall("state")):
        
        exit_error_prefix = f"=== In <state> tag number [ {i} ] from the beginning of the given xml file. ===\n"

        curr_state = State()

        description = get_description(state=state, exit_error_prefix=exit_error_prefix)
        curr_state.set_description(description)

        node_ids = get_node_ids(state=state, exit_error_prefix=exit_error_prefix)

        # Try to convert nodes to a tuple of int
        try:
            node_ids = tuple(map(int, node_ids.split(',')))
        except:
            curr_state.set_node_ids(node_ids) # The given error suits well for diagnostics
        
        curr_state.set_node_ids(node_ids)

        state_defense = generate_state_defense(state=state, exit_error_prefix=exit_error_prefix)

        curr_state.set_state_defense(state_defense)

        all_states.append(curr_state)
        state_id_to_state[curr_state.get_state_defense().get_id()] = curr_state

    return all_states, state_id_to_state







# ==================================================================================
#   METHODS TO NAVIGATE AND PROCESS THE XML FILE PROVIDED
# ==================================================================================

def get_xml_root(states_to_defense_xml_path) -> ET.Element:
    try:
        t = ET.parse(states_to_defense_xml_path)
    except ET.ParseError as e:
        if "duplicate attribute" in str(e):
            ExitUtils.exit_with_error("Duplicate attribute found in XML.")
        else:
            ExitUtils.exit_with_error(f"XML Parse Error: {e}")
    return t.getroot()


def get_description(state : ET.Element, exit_error_prefix : str) -> str:
    description = state.findall('description')
    if len(description) > 1 or len(description) == 0:
        ExitUtils.exit_with_error(exit_error_prefix+"<description> must be given exactly once!")
    
    return description[0].text


def get_node_ids(state : ET.Element, exit_error_prefix : str) -> str:
    node_ids = state.findall('nodes')
    if len(node_ids) > 1 or len(node_ids) == 0:
        ExitUtils.exit_with_error(exit_error_prefix+"<nodes> must be given exactly once!")
    
    return node_ids[0].text 

def generate_state_defense(state : ET.Element, exit_error_prefix : str) -> StateDefense:
    state_defense = state.findall('defense')
    if len(state_defense) > 1 or len(state_defense) == 0:
        ExitUtils.exit_with_error(exit_error_prefix+"<defense> must be given exactly once!")
    
    state_defense = state_defense[0] # Get the first tag, which is the only one
    id = get_id(tag=state_defense, exit_error_prefix=exit_error_prefix)
    
    curr_state_def = StateDefense()
    curr_state_def.set_id(id)

    return curr_state_def



def get_id(tag : ET.Element, exit_error_prefix : str) -> int:
    # get id=""
    id = tag.get('id')
    if id is None: 
        ExitUtils.exit_with_error(exit_error_prefix+'<defense id=""> must be given!')
    try:
        id = int(id)
    except:
        ExitUtils.exit_with_error(exit_error_prefix+'<defense id=""> must be an int!')
    return id


def to_string_all_states_pretty(all_states : List[State]) -> str:
    string = ''
    for i, state in enumerate(all_states):
        string += f"\n{i}] =========\n{state.to_string(tab_times=0)}\n"
    string += "\n==========================\n\n"
    return string


def to_string_state_id_to_state_pretty(state_id_to_state : dict[int, State]) -> str:
    string = ''
    for id in state_id_to_state:
        string += f"{id} : {state_id_to_state[id].get_description()}\n"
    return string














def test():
    all_states, state_id_to_state = get_all_states_to_defense_from_states_to_defense_xml(r'Z:\GitHub\TreeAlchemist\Wazuh-Attack-Defense-Tree-Converter\Code\Wazuh-ADT-Converter\Input-Files\test-tree')
    print(to_string_all_states_pretty(all_states=all_states))
    print(to_string_state_id_to_state_pretty(state_id_to_state=state_id_to_state))
    print("\n")


if __name__ == '__main__':
    #test_properties_dict()
    test()