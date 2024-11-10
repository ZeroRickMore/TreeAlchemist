import requests
import read_toml

port = read_toml.get_port()


while(True):
    rule_id = input('Insert a rule id -> ')
    agent_name = input('Insert the name of the agent -> ')
    adt_name = input('Insert the name of the ADT, aka the group other than TreeAlchemized -> ')


    alert_format = f'Rule: {rule_id} - Description of the alert, useless here ; Location: ({agent_name}) any->/var/log/absolute_testing.log; classification: {adt_name}, TreeAlchemized, ;'
    print(requests.post(url=f'http://localhost:{port}/new-alert', json={'alert' : alert_format}).json())