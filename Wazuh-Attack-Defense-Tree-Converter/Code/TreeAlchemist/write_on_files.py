

import re

def create_rules_xml_file(root_name:str, all_rules_as_string : str):

    def find_lowest_rule_id(all_rules_as_string : str):
        # Extract all rule IDs using a regular expression
        rule_ids = re.findall(r'<rule id="(\d+)"', all_rules_as_string)

        # Convert rule IDs to integers, find the minimum, and convert back to a string
        lowest_rule_id = str(min(int(rule_id) for rule_id in rule_ids))
        return lowest_rule_id
    

    lowest_rule_id = find_lowest_rule_id(all_rules_as_string)
    file_name = f'{lowest_rule_id}-TreeAlchemized-{root_name}.xml'

    with open(file_name, "w") as f:
        f.write(all_rules_as_string)