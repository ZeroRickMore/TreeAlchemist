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


def map_states_to_defense(state_id_to_state : List[Union[Defense, DefensesTogether]],
                          all_states : List[State], 
                          all_defenses : dict[int, State],
                        ):
    pass