from typing import List
# Import scripts from above folder
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from terminal_UI_utils import PrintUtils, ExitUtils

from DefenseClasses.Defense import Defense

class DefensesTogether:
    '''
    Is it merely a list of Defense objects.
    A class is used to simplify the rule generation process.
    '''

    print_diagnostics = True

    def __init__(self,
                defenses_together_ids : List[int] = None, # A list of IDs linking to existing Defense objects through their ID
                name : str = None, # The name given in defense name=""
                id : int = None,
                ):
        self.defenses_together_ids = defenses_together_ids
        self.id = id

    # ============================================
    # name operations
    # ============================================

    def get_name(self) -> str:
        return self.name

    def validate_name(self) -> bool:
        return self.get_name() is None or isinstance(self.get_name(), str)
    
    def validate_name_with_error_launch(self):
        if not self.validate_name():
            error_prefix = f"DefenseTogether named {self.get_name()} failed validation on"
            error_suffix = f"was given instead."
            ExitUtils.exit_with_error(f'{error_prefix} <defense name="">. {Defense.get_name_allow_criteria()} {self.get_name()} of type {type(self.get_name())} {error_suffix}')

    @staticmethod
    def get_name_allow_criteria() -> str:
        return "It must be a string."

    def set_name(self, name : str):
        self.name = name

        self.validate_name_with_error_launch()
        
        if self.print_diagnostics:
            PrintUtils.print_in_green(f'- <defense name=""> assignment of DefenseTogether named {self.get_name()} has been succesfully set to {self.get_name()}')


    # ============================================
    # defenses_together_ids operations
    # ============================================

    def get_defenses_together_ids(self) -> List[int]:
        return self.defenses_together_ids

    def validate_defenses_together_ids(self) -> bool:
        if self.get_defenses_together_ids() is None:
            return True
        for id in self.get_defenses_together_ids():
            if not isinstance(id, int):
                return False
        return True
    
    def validate_defenses_together_ids_with_error_launch(self):
        if not self.validate_defenses_together_ids():
            error_prefix = f"One DefensesTogether failed validation on"
            error_suffix = f"was given instead."
            ExitUtils.exit_with_error(f"{error_prefix} <defenses_together> inside of <DefensesTogether>. {DefensesTogether.get_defenses_together_ids_allow_criteria()} {self.get_defenses_together_ids()} of type {type(self.get_defenses_together_ids())} {error_suffix}")

    @staticmethod
    def get_defenses_together_ids_allow_criteria() -> str:
        return "It must be a list of int ."

    def set_defenses_together_ids(self, defenses_together_ids : List[int]):
        self.defenses_together_ids = defenses_together_ids

        self.validate_defenses_together_ids_with_error_launch()
        
        if self.print_diagnostics:
            PrintUtils.print_in_green(f"- Inside <defense>, <defenses_together> assignment of one DefensesTogether has been succesfully set to {self.get_defenses_together_ids()}")

    # ============================================
    # id operations
    # ============================================

    def get_id(self) -> int:
        return self.id

    def validate_id(self) -> bool:
        return self.get_id() is None or isinstance(self.get_id(), int)
    
    def validate_id_with_error_launch(self):
        if not self.validate_id():
            error_prefix = f"DefensesTogether id {self.get_id()} failed validation on"
            error_suffix = f"was given instead."
            ExitUtils.exit_with_error(f'{error_prefix} <defense id="">. {DefensesTogether.get_id_allow_criteria()} {self.get_id()} of type {type(self.get_id())} {error_suffix}')

    @staticmethod
    def get_id_allow_criteria() -> str:
        return "It must be a int."

    def set_id(self, id : int):
        self.id = id

        self.validate_id_with_error_launch()
        
        if self.print_diagnostics:
            PrintUtils.print_in_green(f'- <defense id=""> assignment of DefenseTogether id {self.get_id()} has been succesfully set to {self.get_id()}')

