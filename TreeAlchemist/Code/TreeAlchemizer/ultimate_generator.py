'''
This script contains the full view of the structures that have been generated.
It is called by wazuh_ADT_converter, and it is the very final checker and producer
that takes the structures and ultimately processes them.

All roads lead to ultimate_generator.py
'''

from typing import Union, List

from DefenseClasses.Defense import Defense
from DefenseClasses.DefensesTogether import DefensesTogether

from StateClasses.State import State

from TreeClasses.Tree import Tree
from TreeClasses.TreeNode import TreeNode

from terminal_UI_utils import PrintUtils, ExitUtils
import state_rules_generator


# =================================================================================================================================================
#                                                                  STATE <-> DEFENSE
# =================================================================================================================================================


def map_states_to_defense(state_id_to_state : dict[int, State],
                          all_states : List[State], 
                          id_to_defense : dict[int, Union[Defense, DefensesTogether]],
                          all_defenses : List[Union[Defense, DefensesTogether]],
                        ):
    
    check_validity_with_error_throw(state_id_to_state, all_states, id_to_defense, all_defenses)

    map_states_to_defense_real(state_id_to_state=state_id_to_state, id_to_defense=id_to_defense)



# ========================================================================================================
#                                VALIDATIONS AND ERROR STRING GENERATION
# ========================================================================================================


def are_they_valid(state_id_to_state : dict[int, State],
                    all_states : List[State], 
                    id_to_defense : dict[int, Union[Defense, DefensesTogether]],
                    all_defenses : List[Union[Defense, DefensesTogether]],
            ) -> bool :
    '''
    Function that checks if they are overall valid or not.
    Honestly, this is unused.
    '''
    # Invalidity code 0 is "everything is fine"
    err_code, _ = get_invalidity_code_and_error_string(state_id_to_state, all_states, id_to_defense, all_defenses)
    return bool(err_code == 0)



def get_invalidity_code_and_error_string(state_id_to_state : dict[int, State],
                                        all_states : List[State], 
                                        id_to_defense : dict[int, Union[Defense, DefensesTogether]],
                                        all_defenses : List[Union[Defense, DefensesTogether]],
                                    ) -> tuple[int, str] :
    '''
    Checks validity, and throws a code based on the invalidity type.
    0 : All good!
    1 : len(state_id_to_state.keys()) != len(all_states)
    2 : len(id_to_defense.keys()) != len(all_defenses)
    3 : len(all_defenses) > len(all_states)
    4 : len(all_states) > len(all_defenses)
    5 : found a defense ID not in state ID
    '''
    if len(state_id_to_state.keys()) != len(all_states):
        return 1, f"Too many state IDs compared to how many states you have.\nState IDs: {state_id_to_state}\nStates: {all_states}\n\nThis is a backend error..."

    if len(id_to_defense.keys()) != len(all_defenses):
        return 2, f"Too many defense IDs compared to how many defenses you have.\nDefense IDs: {id_to_defense}\nDefenses: {all_defenses}\n\nThis is a backend error..."

    if len(all_states) != len(all_defenses):
        if len(all_states)>len(all_defenses):
            return 3, f"Too many states compared to how many defenses you have.\nStates: {all_states}\nDefenses: {all_defenses}\n\nDifferences found: {to_string_error_differences(state_id_to_state, all_states, id_to_defense, all_defenses)}"
        else:
            return 4, f"Too many defenses compared to how many states you have.\nDefenses: {all_defenses}\nStates: {all_states}\n\nDifferences found: {to_string_error_differences(state_id_to_state, all_states, id_to_defense, all_defenses)}"
    
    err_string = to_string_error_differences(state_id_to_state=state_id_to_state, id_to_defense=id_to_defense)
    if err_string != '':
        return 5, f'Found a <defense id=""> not mapped between defense_definition.xml and states_to_defense.xml .\n{err_string}'

    return 0, 'All good!'


def to_string_error_differences(state_id_to_state : dict[int, State],
                                id_to_defense : dict[int, Union[Defense, DefensesTogether]],
                            ) -> str:
    '''
    Returns a pretty print of the differences found between the ids of the dictionaries.
    This is a feasible user error that we want to notify him of.
    '''
    string = ''

    for id in id_to_defense:
        to_append = ''
        if id not in state_id_to_state:
            to_append += f'<defense id="{id}" of defense_definition.xml was not found inside of states_to_defense.xml in the same tag into <state>.\n'
        if to_append != '':
            string += f'\nLOOKING AT defense_definition.xml IT SEEMS SOME OF ITS <defense id=""> WHERE NOT FOUND IN states_to_defense.xml ==============\n\n'
            string += to_append
    
    for id in state_id_to_state:
        to_append = ''
        if id not in id_to_defense:
            string += f'<defense id="{id}" into <state> of states_to_defense.xml was not found inside of defense_definition.xml in the same tag.\n'
        if to_append != '':
            string += f'\nLOOKING AT states_to_defense.xml IT SEEMS SOME OF ITS <state><defense id=""> WHERE NOT FOUND IN defense_definition.xml ==============\n\n'
            string += to_append

    return string
    


def check_validity_with_error_throw(state_id_to_state : dict[int, State],
                                    all_states : List[State], 
                                    id_to_defense : dict[int, Union[Defense, DefensesTogether]],
                                    all_defenses : List[Union[Defense, DefensesTogether]],
                                ):
    
    invalidity_code, err_str = get_invalidity_code_and_error_string(state_id_to_state, all_states, id_to_defense, all_defenses)
    if invalidity_code != 0: ExitUtils.exit_with_error(err_str)



# ========================================================================================================
#                                        TRUE MAPPING PROCESS
# ========================================================================================================



def map_states_to_defense_real(state_id_to_state : dict[int, State],
                               id_to_defense : dict[int, Union[Defense, DefensesTogether]],
                            ):
    
    for id in state_id_to_state:
        curr_state = state_id_to_state[id]
        curr_def = id_to_defense[id]

        curr_state.get_state_defense().set_defense(curr_def)
        curr_state.validate_all()
        


# =================================================================================================================================================
#                                                        END OF    STATE <-> DEFENSE
# =================================================================================================================================================



def map_states_to_nodes(node_id_to_node : dict[int, TreeNode],
                        all_states: List[State]
                        ):
    
    rules = state_rules_generator.map_states_to_nodes(node_id_to_node, all_states)