import os
import re
from terminal_UI_utils import ExitUtils

def create_rules_xml_file(root_name:str, all_rules_as_string : str, output_folder : str):

    if not os.path.isdir(output_folder):
        ExitUtils.exit_with_error(f"The output folder {output_folder} does not exist.\nCannot generate anything.")

    tree_folder = os.path.join(output_folder, 'root_name')
    try:
        os.makedirs(tree_folder)
    except:
        ExitUtils.exit_with_error(f"The folder {root_name} already exist, cannot generate the files.\nIf you want to generate the files, rename or remove the folder.")

    def find_lowest_rule_id(all_rules_as_string : str):
        # Extract all rule IDs using a regular expression
        rule_ids = re.findall(r'<rule id="(\d+)"', all_rules_as_string)

        # Convert rule IDs to integers, find the minimum, and convert back to a string
        lowest_rule_id = str(min(int(rule_id) for rule_id in rule_ids))
        return lowest_rule_id
    

    lowest_rule_id = find_lowest_rule_id(all_rules_as_string)
    file_name = f'{lowest_rule_id}-TreeAlchemized-{root_name}.xml'

    with open(os.path.join(tree_folder, file_name), "w") as f:
        f.write(all_rules_as_string)