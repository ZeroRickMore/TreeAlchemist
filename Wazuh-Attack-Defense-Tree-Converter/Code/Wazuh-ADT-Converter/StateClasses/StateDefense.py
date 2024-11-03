from typing import Union, Any

# Import scripts from above folder
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from DefenseClasses.Defense import Defense
from DefenseClasses.DefensesTogether import DefensesTogether
from StateClasses.OptimalityClasses.AbstractOptimality import AbstractOptimality
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
                 id : int = -1, # This is the ID of the <defense> declared in defense_definition.xml you are referencing to
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
        if (not isinstance(self.get_id(), int)) or self.get_id() < 0:
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
    
    def get_optimality(self) -> AbstractOptimality:
        return self.optimality

    def validate_optimality(self) -> bool:
        if not isinstance(self.get_optimality(), AbstractOptimality):
            return False
        
        self.get_optimality().validate_all()
        return True

    def validate_optimality_with_error_launch(self):
        if not self.validate_optimality():
            error_prefix = f"The StateDefense with optimality [ {self.get_optimality()} ] failed validation on"
            error_suffix = f"was given instead."
            ExitUtils.exit_with_error(f'{error_prefix} <optimality> in <state>. {StateDefense.get_optimality_allow_criteria()} {self.get_optimality()} of type {type(self.get_optimality())} {error_suffix}')

    @staticmethod
    def get_optimality_allow_criteria() -> str:
        return "It must be an object of a subclass of AbstractOptimality."

    def set_optimality(self, optimality : AbstractOptimality) -> None:
        self.optimality = optimality

        self.validate_optimality_with_error_launch()

        if self.print_diagnostics:
            PrintUtils.print_in_green(f'- Inside <defense>, <optimality> has been succesfully set to {optimality}')


    # ============================================
    # <defense> operations
    # ============================================
    
    def get_defense(self) -> Union[Defense, DefensesTogether]:
        return self.defense

    def validate_defense(self) -> bool:
        defense = self.get_defense()
        if defense is None:
            PrintUtils.print_warning(f"StateDefense with id {self.get_id()} has no Defense attached.\nThis is normal during preparation, and overly verbose.")
            return True

        if not ( isinstance(defense, Defense) or isinstance(defense, DefensesTogether) ) :
            return False
        
        defense.validate_all()
        return True

    def validate_defense_with_error_launch(self):
        if not self.validate_defense():
            error_prefix = f"The StateDefense with defense [ {self.get_defense()} ] failed validation on"
            error_suffix = f"was given instead."
            ExitUtils.exit_with_error(f'{error_prefix} <defense> in <state>. {StateDefense.get_defense_allow_criteria()} {self.get_defense()} of type {type(self.get_defense())} {error_suffix}')

    @staticmethod
    def get_defense_allow_criteria() -> str:
        return "It must be an object of type Defense or DefensesTogether."

    def set_defense(self, defense : Union[Defense, DefensesTogether]) -> None:
        self.defense = defense

        self.validate_defense_with_error_launch()

        if self.print_diagnostics:
            PrintUtils.print_in_green(f'- <defense> in <state> has been succesfully set to {defense}')





    # ============================================
    # Validate All
    # ============================================   


    def validate_all(self):

        self.validate_id_with_error_launch()

        self.validate_optimality_with_error_launch()

        self.validate_defense_with_error_launch()






    def to_string(self, tab_times : int = 0):
        give_tabs = '\t'*tab_times
        return f"{give_tabs}StateDefense ==========================\n\n{give_tabs}\tID: {self.get_id()}\n{self.get_optimality().to_string(tab_times=tab_times+1)}\n{give_tabs}\tDefense: {f'\n{give_tabs}\tType:{type(self.get_defense())}\n{self.get_defense().to_string_total(tab_times=tab_times+1)}' if self.get_defense() else 'unattached yet.'}"