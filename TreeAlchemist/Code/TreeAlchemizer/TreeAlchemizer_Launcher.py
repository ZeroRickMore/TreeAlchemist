'''
Launcher for the whole script to convert an ADT written in an xml file, that is given as input through -path,
and obtain the Wazuh implementation of it.

'''

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))
import user_input_parser
import TreeAlchemist.Code.TreeAlchemizer.tree_xml_parser as tree_xml_parser
import defense_definition_xml_parser
import wazuh_ready_printer
import states_to_defense_parser
import ultimate_generator
from write_on_files import FilesWriter




def main():  

    tree_dir_path,output_dir = user_input_parser.get_user_input() # The path to the directory containing the ADT files used for execution.

    if output_dir is None:
        cwd = os.getcwd()
        splitter = os.path.join("TreeAlchemist", "TreeAlchemist")
        if splitter in cwd:
            ind = cwd.index(splitter)
            cwd = cwd[:ind]
            output_dir = os.path.join(cwd, 'TreeAlchemist', 'TreeAlchemist', 'Code', 'TreeAlchemizer', 'Output-Files')
        else:
            output_dir = os.path.join(cwd, 'TreeAlchemist', 'Code', 'TreeAlchemizer', 'Output-Files')
            

    adt, node_id_to_node = tree_xml_parser.get_ADT_from_tree_xml(tree_dir_path = tree_dir_path)
    root_name = adt.get_root().get_informations().get_name()

    wazuh_ready_atk_nodes_no_states : str = wazuh_ready_printer.to_string_all_attacks_single_nodes(adt)

    writer = FilesWriter()

    writer.create_rules_xml_file(root_name=root_name, all_rules_as_string=wazuh_ready_atk_nodes_no_states, output_folder=output_dir)


    #print(wazuh_ready_atk_nodes_no_states)

    all_defenses, id_to_defense = defense_definition_xml_parser.get_all_defenses_from_defense_definition_xml(tree_dir_path = tree_dir_path, adt_name=root_name)

    wazuh_ready_def_nodes = wazuh_ready_printer.to_string_all_defenses_wazuh_ready(tree_name=root_name, all_defenses=all_defenses, tab_times=0)

    writer.create_command_activeres_xml_file(root_name=root_name, all_defenses_as_string=wazuh_ready_def_nodes, output_folder=output_dir)

    #print(wazuh_ready_def_nodes)


    all_states, state_id_to_state = states_to_defense_parser.get_all_states_to_defense_from_states_to_defense_xml(tree_dir_path=tree_dir_path)

    #print(states_to_defense_parser.to_string_all_states_pretty(all_states=all_states))
    #print(states_to_defense_parser.to_string_state_id_to_state_pretty(state_id_to_state=state_id_to_state))

    # This is just to check if the ids were correct or not
    ultimate_generator.map_states_to_defense(state_id_to_state=state_id_to_state, id_to_defense=id_to_defense, all_defenses=all_defenses, all_states=all_states)


    #print(states_to_defense_parser.to_string_all_states_pretty(all_states=all_states))

    ultimate_generator.map_states_to_nodes(node_id_to_node, all_states)
    # The node rules are placed inside of the State's node_ids


    for _ in all_states:
        print(_.get_description(),_.get_node_ids(), _.get_state_defense().get_defense().get_name())



    wazuh_ready_def_nodes = wazuh_ready_printer.to_string_all_defenses_wazuh_ready(tree_name=root_name, all_defenses=all_defenses, tab_times=0)

    

    print(wazuh_ready_def_nodes)

    daemon_readable_file = wazuh_ready_printer.to_string_tree_for_daemon_read(adt=adt, all_states=all_states, node_id_to_node=node_id_to_node)
    print(daemon_readable_file)
    writer.create_daemon_readable_file(root_name=root_name, output_folder=output_dir, daemon_readable_file=daemon_readable_file)

    print(writer.generate_guide_file_string())
    writer.generate_guide_file()


if __name__ == '__main__':
    main()