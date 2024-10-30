'''
Launcher for the whole script to convert an ADT written in an xml file, that is given as input through -path,
and obtain the Wazuh implementation of it.

'''
import user_input_parser
import ADT_xml_parser


def main():

    tree_dir_path = user_input_parser.get_valid_tree_path() # The path to the directory containing the ADT files used for execution.

    usable_ADT_structure = ADT_xml_parser.convert_xml_ADT_to_usable_structure(tree_dir_path = tree_dir_path)

    









if __name__ == '__main__':
    main()