from typing import List, Union

from TreeClasses.Tree import Tree
from DefenseClasses.Defense import Defense
from DefenseClasses.DefensesTogether import DefensesTogether

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



