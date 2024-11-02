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
                 defenses_together_ids : List[int] = None # A list of IDs linking to existing Defense objects through their ID
                ):
        self.defenses_together_ids = defenses_together_ids


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


