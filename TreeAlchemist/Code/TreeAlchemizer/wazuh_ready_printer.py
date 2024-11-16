from typing import List, Union

from TreeClasses.Tree import Tree
from TreeClasses.TreeNode import TreeNode
from DefenseClasses.Defense import Defense
from DefenseClasses.DefensesTogether import DefensesTogether
from StateClasses.State import State


def to_string_all_attacks_single_nodes(ADT : Tree):
    return ADT.to_string_group_and_single_nodes()


def to_string_all_defenses_wazuh_ready(tree_name : str = 'unspecified', all_defenses : List[Union[Defense, DefensesTogether]] = None, tab_times : int = 0) -> str:
    give_tabs = '\t'*tab_times

    string = ''
    
    string += f'{give_tabs}<!-- Start of Commands and Active-Response for ADT: [ {tree_name} ] .-->\n'

    string = f'{give_tabs}<ossec_config>\n'

    for defense in all_defenses:
        # DefensesTogether has no effect over the generation of the commands, it actually bugs stuff duplicating commands. Just use it for the daemon
        if isinstance(defense, DefensesTogether):
            continue

        defense : Defense
        string += f'\n{give_tabs}<!-- Start of <defense name="{defense.get_name()}" id="{defense.get_id()}" -->\n\n'
        string += defense.to_string_total(tab_times = tab_times + 1)
        string += f'\n{give_tabs}<!-- End of <defense name="{defense.get_name()}" id="{defense.get_id()}" -->\n\n'

    string += f'\n{give_tabs}</ossec_config>\n\n'

    string += f'<!-- End of Commands and Active-Response for ADT: [ {tree_name} ] .-->\n\n'

    return string



def to_string_node_rule_ids_to_defense_id(all_states : List[State],
                                          node_id_to_node : dict[int, TreeNode]
                                          ):
    string = ''

    for state in all_states:
        curr_node_ids_string = '['
        for id in state.get_node_ids():
            curr_node_ids_string += str(node_id_to_node[id].get_informations().get_wazuh_rule_config().get_rule_id()) + ','
        
        curr_node_ids_string = curr_node_ids_string[:-1]
        curr_node_ids_string += '] :: ['
        # We add a zero at the end because Wazuh API for some reason appends a 0 at the end of the command name to trigger it...
        curr_defense =  state.get_state_defense().get_defense()
        if isinstance(curr_defense, Defense):
            curr_node_ids_string += state.get_state_defense().get_defense().get_comm_name() + '0'
        else:
            defenses = curr_defense.get_defenses()
            for defense in defenses:
                curr_node_ids_string += defense.get_comm_name() + '0,'
            curr_node_ids_string = curr_node_ids_string[:-1]
        
        curr_node_ids_string += ']' 
        string += curr_node_ids_string + '\n'
    
    return string



def to_string_tree_for_daemon_read( adt : Tree,
                                    all_states : List[State],
                                    node_id_to_node : dict[int, TreeNode]
                                    ):
    
    string = '===START OF ADT===\n'

    string += adt.print_adt_name_with_node_ids()

    string += '\n'

    string += to_string_node_rule_ids_to_defense_id(all_states=all_states, node_id_to_node=node_id_to_node)

    string += '===END OF ADT===\n'

    return string