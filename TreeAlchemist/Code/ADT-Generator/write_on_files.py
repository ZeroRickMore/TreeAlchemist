import os
import re
from terminal_UI_utils import ExitUtils


class FilesWriter:

    def __init__(self):
        self.has_generated_something = False

    def create_rules_xml_file(self, root_name:str, all_rules_as_string : str, output_folder : str):

        if not os.path.isdir(output_folder):
            ExitUtils.exit_with_error(f"The output folder {output_folder} does not exist.\nCannot generate anything.")

        tree_folder = os.path.join(output_folder, root_name)

        if not self.has_generated_something:
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

        full_rules_file = os.path.join(tree_folder, file_name)

        with open(full_rules_file, "w") as f:
            f.write(all_rules_as_string)

        self.rules_file = full_rules_file
        self.tree_folder = tree_folder
        self.has_generated_something = True


    def create_command_activeres_xml_file(self, root_name:str, all_defenses_as_string:str, output_folder:str):

        if not os.path.isdir(output_folder):
            ExitUtils.exit_with_error(f"The output folder {output_folder} does not exist.\nCannot generate anything.")

        tree_folder = os.path.join(output_folder, root_name)

        if not self.has_generated_something:
            try:
                os.makedirs(tree_folder)
            except:
                ExitUtils.exit_with_error(f"The folder {root_name} already exist, cannot generate the files.\nIf you want to generate the files, rename or remove the folder.")

        file_name = f'Command-Activeres-{root_name}_manually_put_into_ossec_conf.xml'

        full_defs_file = os.path.join(tree_folder, file_name)
        with open(full_defs_file, "w") as f:
            f.write(all_defenses_as_string)

        self.def_file = full_defs_file
        self.tree_folder = tree_folder
        self.has_generated_something = True

    
    def create_daemon_readable_file(self, all_states_to_defenses):
        pass


    def generate_guide_file(self):
        self.rules_file # Il file con le regole
        self.def_file # Il file con command e active-reponse
        self.tree_folder # La folder che contiene tutti questi subfiles
        string = ''

        string += 'Hello, and welcome to the TreeAlchemist guide!\nThis is an extremely short text to guide you through the upload of these files inside of Wazuh.\n\n'

        string += f'Rules File=======================\n\t- Go into /var/ossec/etc/rules/\n\t- Move the rules file {self.rules_file} inside of it, and job done!\n\n'

        string += f'Command Active-Response File=======================\n\t- Modify content of /var/ossec/etc/ossec.conf\n\t- Copypaste all of the content of {self.def_file} inside of it, at the very end, and job done!\n\n'


        string += '\nI hope everything worked for you!\nHave fun with your tree, and do not forget to launch the daemon in order to make the tree handling functional!'


        guide_file = os.path.join(self.tree_folder, 'README.txt')
        with open(guide_file, "w") as f:
            f.write(string)