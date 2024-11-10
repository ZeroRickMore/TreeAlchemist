def parse_alert_log_line(log_line : str) -> dict[str, str]:
    '''
    From the given log, parse the important informations:

        parsed_data = {
            'rule_id' : 'unknown',
            'agent' : 'unknown',
            'tree_name' : 'unknown',
        }

    '''


    parsed_data = {
        'rule_id' : 'unknown',
        'agent' : 'unknown',
        'tree_name' : 'unknown',
    }

    # rule_id gathering
    rule_index = log_line.index('Rule: ') # Previous information is useless
    log_line = log_line[rule_index + len('Rule : ') - 1:]

    rule_index = log_line.index(" ") # Until the next space, it's all rule_id
    rule_id = int(log_line[:rule_index])

    # location gathering
    location_index = log_line.index('Location: (' ) # Previous information is already parsed
    log_line = log_line[location_index + len('Location: ('):]

    location_index = log_line.index(")") # Until the next ), it's all location value
    location = log_line[:location_index]

    # classification gathering
    classification_index = log_line.index('classification: ') # Previous information is already parsed
    log_line = log_line[classification_index + len('classification: ') - 1:]

    classification_index = log_line.index(";") # Until the next ;, it's all classification value
    classification = log_line[:classification_index]  
    classification = classification.replace("TreeAlchemized", "").replace(" ", "").replace(",", "")

    parsed_data['rule_id'] = rule_id
    parsed_data['agent'] = location
    parsed_data['tree_name'] = classification

    return parsed_data










def test():
    # Test with the provided example
    log_line = 'Nov  7 00:01:52 WazuhServer ossec: Alert Level: 14; Rule: 100017 - An attacker has reached "Child4_1" node.; Location: (Ubuntu-Victim) any->/var/log/absolute_testing.log; classification: Root, TreeAlchemized, ; evil Child4_1 log'
    parsed_result = parse_alert_log_line(log_line)
    from pprint import pprint
    pprint(parsed_result)

if __name__ == '__main__':
    test()