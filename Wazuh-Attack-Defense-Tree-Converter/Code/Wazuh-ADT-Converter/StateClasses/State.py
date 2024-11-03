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
                node_ids : tuple[int] = None, # <node_ids>
                state_defense : StateDefense = None, # <defense>
                ):
        
        self.description = description
        self.node_ids = node_ids

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
            error_prefix = f"The State with description [ {self.get_description()} ] failed validation on"
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



    # ============================================
    # <node_ids> operations
    # ============================================
    
    def get_node_ids(self) -> tuple[int]:
        return self.node_ids

    def validate_node_ids(self) -> bool:
        if not isinstance(self.get_node_ids(), tuple):
            return False
        
        for node_id in self.get_node_ids():
            if not isinstance(node_id, int):
                return False
            
        return True

    def validate_node_ids_with_error_launch(self):
        if not self.validate_node_ids():
            error_prefix = f"The State with description [ {self.get_description()} ] failed validation on"
            error_suffix = f"was given instead."
            ExitUtils.exit_with_error(f'{error_prefix} <nodes> in <state>. {State.get_node_ids_allow_criteria()} {self.get_node_ids()} of type {type(self.get_node_ids())} {error_suffix}')

    @staticmethod
    def get_node_ids_allow_criteria() -> str:
        return "It must be a string of numbers separated by comma, without spaces.\nFor example: <nodes>1,5,8,10</nodes> ."

    def set_node_ids(self, node_ids : str) -> None:
        self.node_ids = node_ids

        self.validate_node_ids_with_error_launch()

        if self.print_diagnostics:
            PrintUtils.print_in_green(f'- Inside <state>, <nodes> has been succesfully set to {node_ids}')
