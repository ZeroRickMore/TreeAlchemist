# Import scripts from above folder
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from DefenseClasses.Defense import Defense
from DefenseClasses.DefensesTogether import DefensesTogether

from StateClasses.OptimalityClasses.AbstractOptimality import AbstractOptimality

from typing import Union, Any
# Import scripts from above folder
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from terminal_UI_utils import PrintUtils, ExitUtils

class StateDefense:
    '''
    This class represents a StateDefense, which is an implicit
    extension of DefenseClasses.Defense, meaning that it contains the 
    some attributes of a Defense that are strictly related to a state.

    This is just an intermediary between defense and state, let's say.
    '''

    print_diagnostics = True

    def __init__(self,
                 id : int = -1,
                 defense : Union[Defense, DefensesTogether] = None, # The Defense object linked to it 
                 optimality : AbstractOptimality = None, 
                 ):
        self.id = id

        self.defense = defense

        self.optimality = optimality

    
    # ============================================
    # <id> operations
    # ============================================
    
    def get_id(self) -> int:
        return self.id

    def validate_id(self) -> bool:
        if (not isinstance(self.get_id(), int)) or self.get_id < 0:
            return False
        return True
    
    def validate_id_with_error_launch(self):
        if not self.validate_id():
            error_prefix = f"The StateDefense with id [ {self.get_id()} ] failed validation on"
            error_suffix = f"was given instead."
            ExitUtils.exit_with_error(f'{error_prefix} <id> in <state>. {StateDefense.get_id_allow_criteria()} {self.get_id()} of type {type(self.get_id())} {error_suffix}')

    @staticmethod
    def get_id_allow_criteria() -> str:
        return "It must be a number higher or equal to 0."

    def set_id(self, id : int) -> None:
        self.id = id

        self.validate_id_with_error_launch()

        if self.print_diagnostics:
            PrintUtils.print_in_green(f'- Inside <defense>, <id> has been succesfully set to {id}')


    # ============================================
    # <optimality> operations
    # ============================================
    
    def get_optimality(self) -> int:
        return self.optimality

    def validate_optimailty(self) -> bool:
        if (not isinstance(self.get_optimality(), AbstractOptimality)):
            return False
        self.get_optimality().validate_all()

    def valoptimalityate_optimality_with_error_launch(self):
        if not self.valoptimalityate_optimality():
            error_prefix = f"The StateDefense with optimality [ {self.get_optimality()} ] failed valoptimalityation on"
            error_suffix = f"was given instead."
            ExitUtils.exit_with_error(f'{error_prefix} <optimality> in <state>. {StateDefense.get_optimality_allow_criteria()} {self.get_optimality()} of type {type(self.get_optimality())} {error_suffix}')

    @staticmethod
    def get_optimality_allow_criteria() -> str:
        return "It must be a number higher or equal to 0."

    def set_optimality(self, optimality : int) -> None:
        self.optimality = optimality

        self.valoptimalityate_optimality_with_error_launch()

        if self.print_diagnostics:
            PrintUtils.print_in_green(f'- Insoptimalitye <defense>, <optimality> has been succesfully set to {optimality}')

