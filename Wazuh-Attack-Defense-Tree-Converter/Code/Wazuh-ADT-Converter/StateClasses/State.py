from StateClasses.StateDefense import StateDefense
# Import scripts from above folder
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from terminal_UI_utils import PrintUtils, ExitUtils

class State:
    '''
    This class represents a state, which is a list of node IDs
    linked to a specific "Defense" object.
    '''

    print_diagnostics = True



    def __init__(self,
                description : str = 'ungiven', # <description>
                nodes : tuple[int] = None, # <nodes>
                state_defense : StateDefense = None, # <defense>
                ):
        
        self.description = description
        self.nodes = nodes

        self.state_defense = state_defense

    
    # ============================================
    # <description> operations
    # ============================================
    
    def get_description(self) -> str:
        return self.description

    def validate_description(self) -> bool:
        if not isinstance(self.get_description(), str):
            return False

    def validate_description_with_error_launch(self):
        if not self.validate_description():
            error_prefix = f"The State with description [ {self.description} ] failed validation on"
            error_suffix = f"was given instead."
            ExitUtils.exit_with_error(f'{error_prefix} <description> in <state>. {State.get_description_allow_criteria()} {self.get_description()} of type {type(self.get_description())} {error_suffix}')

    @staticmethod
    def get_description_allow_criteria() -> str:
        return "It must be a string."

    def set_description(self, description : str) -> None:
        self.description = description

        self.validate_description_with_error_launch()

        if self.print_diagnostics:
            PrintUtils.print_in_green(f'- Inside <state>, <description> has been succesfully set to {description}')

