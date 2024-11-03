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


def main():

    #tree_dir_path = user_input_parser.get_valid_tree_path() # The path to the directory containing the ADT files used for execution.

    # TEMP
    import os
    tree_dir_path = os.path.join(os.getcwd(), r'Wazuh-Attack-Defense-Tree-Converter\Code\Wazuh-ADT-Converter\Input-Files\test-tree')
    # TEMP

    ADT : Tree = ADT_xml_parser.convert_xml_ADT_to_usable_structure(tree_dir_path = tree_dir_path)

    wazuh_ready_atk_nodes_no_states : str = wazuh_ready_printer.to_string_all_attacks_single_nodes(ADT)

    print(wazuh_ready_atk_nodes_no_states)

    all_defenses, id_to_defense = defense_definition_xml_parser.get_all_defenses(tree_dir_path = tree_dir_path)

    wazuh_ready_def_nodes = wazuh_ready_printer.to_string_all_defenses_wazuh_ready(tree_name='COOLEST ADT', all_defenses=all_defenses, tab_times=0)

    print(wazuh_ready_def_nodes)

    all_states, state_id_to_state = states_to_defense_parser.get_all_states_to_defense(tree_dir_path=tree_dir_path)

    print(states_to_defense_parser.to_string_all_states_pretty(all_states=all_states))
    print(states_to_defense_parser.to_string_state_id_to_state_pretty(state_id_to_state=state_id_to_state))

    ultimate_generator.get_invalidity_code_and_error_string(state_id_to_state=state_id_to_state, id_to_defense=id_to_defense, all_defenses=all_defenses, all_states=all_states)


    









if __name__ == '__main__':
    main()