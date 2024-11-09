'''
Launcher for the whole script to convert an ADT written in an xml file, that is given as input through -path,
and obtain the Wazuh implementation of it.

'''
import user_input_parser
import ADT_xml_parser
import defense_definition_xml_parser
from TreeClasses.Tree import Tree
import wazuh_ready_printer
import states_to_defense_parser
import ultimate_generator
import write_on_files
import os
from terminal_UI_utils import ExitUtils


def main():
    # Check if I'm in the correct working directory
    cwd = os.getcwd()

    # Check if it ends with 'TreeAlchemist'
    if not cwd.endswith("TreeAlchemist"):
        ExitUtils.exit_with_error("You must launch the code from TreeAlchemist folder inside of Code")


    #tree_dir_path = user_input_parser.get_valid_tree_path() # The path to the directory containing the ADT files used for execution.

    # TEMP
    tree_dir_path = os.path.join(os.getcwd(), r'Wazuh-Attack-Defense-Tree-Converter\Code\TreeAlchemist\Input-Files\test-tree')
    # TEMP

    adt, node_id_to_node = ADT_xml_parser.get_ADT_from_tree_xml(tree_dir_path = tree_dir_path)

    wazuh_ready_atk_nodes_no_states : str = wazuh_ready_printer.to_string_all_attacks_single_nodes(adt)

    write_on_files.create_rules_xml_file(root_name=adt.get_root().get_informations().get_name(), all_rules_as_string=wazuh_ready_atk_nodes_no_states)
    print(wazuh_ready_atk_nodes_no_states)



    exit()


    all_defenses, id_to_defense = defense_definition_xml_parser.get_all_defenses_from_defense_definition_xml(tree_dir_path = tree_dir_path)

    wazuh_ready_def_nodes = wazuh_ready_printer.to_string_all_defenses_wazuh_ready(tree_name=adt.get_root().get_informations().get_name(), all_defenses=all_defenses, tab_times=0)

    print(wazuh_ready_def_nodes)

    exit()

    all_states, state_id_to_state = states_to_defense_parser.get_all_states_to_defense_from_states_to_defense_xml(tree_dir_path=tree_dir_path)

    #print(states_to_defense_parser.to_string_all_states_pretty(all_states=all_states))
    #print(states_to_defense_parser.to_string_state_id_to_state_pretty(state_id_to_state=state_id_to_state))

    ultimate_generator.map_states_to_defense(state_id_to_state=state_id_to_state, id_to_defense=id_to_defense, all_defenses=all_defenses, all_states=all_states)

    #print(states_to_defense_parser.to_string_all_states_pretty(all_states=all_states))

    ultimate_generator.generate_state_rules(node_id_to_node, adt, all_states)

    wazuh_ready_def_nodes = wazuh_ready_printer.to_string_all_defenses_wazuh_ready(tree_name='COOLEST ADT', all_defenses=all_defenses, tab_times=0)

    print(wazuh_ready_def_nodes)

    
    









if __name__ == '__main__':
    main()