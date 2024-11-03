from DefenseClasses.Defense import Defense
from DefenseClasses.DefensesTogether import DefensesTogether
from OptimalityClasses.AbstractOptimality import AbstractOptimality

from typing import Union, Any

class StateDefense:
    '''
    This class represents a StateDefense, which is an implicit
    extension of DefenseClasses.Defense, meaning that it contains the 
    some attributes of a Defense that are strictly related to a state.

    This is just an intermediary between defense and state, let's say.
    '''
    ALLOWED_OPTIMALITY_TYPES = ['BEST_SCORE']

    print_diagnostics = True

    def __init__(self,
                 defense : Union[Defense, DefensesTogether] = None, # The Defense object linked to it 
                 optimality_type : AbstractOptimality = None, 
                 ):
        
        self.defense = defense

        self.optimality_type = optimality_type

    
    


