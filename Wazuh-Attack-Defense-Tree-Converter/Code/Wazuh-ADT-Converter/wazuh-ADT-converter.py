'''
Launcher for the whole script to convert an ADT written in an xml file, that is given as input through -path,
and obtain the Wazuh implementation of it.

'''
import user_input_parser
import ADT_xml_parser
from TreeClasses.Tree import *


def main():

    #tree_dir_path = user_input_parser.get_valid_tree_path() # The path to the directory containing the ADT files used for execution.

    # TEMP
    tree_dir_path = r'C:\Users\fadra\Desktop\Github\TreeAlchemist\Wazuh-Attack-Defense-Tree-Converter\Code\Wazuh-ADT-Converter\Input-Files\test-tree'
    # TEMP
    usable_ADT_structure : Tree = ADT_xml_parser.convert_xml_ADT_to_usable_structure(tree_dir_path = tree_dir_path)

    wazuh_rules_with_group_and_single_nodes_no_states = usable_ADT_structure.to_string_group_and_single_nodes()

    print(wazuh_rules_with_group_and_single_nodes_no_states)

    









if __name__ == '__main__':
    main()