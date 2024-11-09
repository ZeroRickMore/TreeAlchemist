from typing import List
# Import scripts from above folder
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from terminal_UI_utils import PrintUtils, ExitUtils

from DefenseClasses.Defense import Defense
from DefenseClasses.ActiveResponse import ActiveResponse

class DefensesTogether:
    '''
    Is it merely a list of Defense objects.
    A class is used to simplify the rule generation process.
    This class represents the need for the user to execute a set of pre-existing
    commands that have been defined in one of the other defenses.

    Basically, it generates <command> tags based on pre-existing defenses defined
    in the script, then gathers <active-response> informations like Defense.

    If a user needs to use pre-existing commands defined outside of this script,
    he can freely add them by hand after the generation. (currently unsupported)

    Note that this is a prototype, so it is up to changes
    '''

    print_diagnostics = True

    def __init__(self,
                defenses_ids : List[int] = None, # A list of IDs linking to existing Defense objects through their ID
                name : str = None, # The name given in defense name=""
                id : int = None,
                active_response : ActiveResponse = None,
                rules_id : str = ''
                ):
        self.name = name
        self.defenses_ids = defenses_ids
        self.id = id
        self.defenses : List[Defense] = []
        self.active_response = active_response
        self.rules_id = rules_id


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
    # defenses_ids operations
    # ============================================

    def get_defenses_ids(self) -> List[int]:
        return self.defenses_ids

    def validate_defenses_ids(self) -> bool:
        if self.get_defenses_ids() is None:
            return True
        for id in self.get_defenses_ids():
            if not isinstance(id, int):
                return False
        return True
    
    def validate_defenses_ids_with_error_launch(self):
        if not self.validate_defenses_ids():
            error_prefix = f"One DefensesTogether failed validation on"
            error_suffix = f"was given instead."
            ExitUtils.exit_with_error(f"{error_prefix} <defenses_together> inside of <DefensesTogether>. {DefensesTogether.get_defenses_ids_allow_criteria()} {self.get_defenses_ids()} of type {type(self.get_defenses_ids())} {error_suffix}")

    @staticmethod
    def get_defenses_ids_allow_criteria() -> str:
        return "It must be a list of int ."

    def set_defenses_ids(self, defenses_ids : List[int]):
        self.defenses_ids = defenses_ids

        self.validate_defenses_ids_with_error_launch()
        
        if self.print_diagnostics:
            PrintUtils.print_in_green(f"- Inside <defense>, <defenses_together> assignment of one DefensesTogether has been succesfully set to {self.get_defenses_ids()}")

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

    # ============================================
    # defenses operations
    # ============================================

    def get_defenses(self) -> List[Defense]:
        return self.defenses

    def validate_defenses(self) -> bool:
        if self.get_defenses() is None:
            return True
        for deff in self.get_defenses():
            if not isinstance(deff, Defense):
                return False
        return True
    
    def validate_defenses_with_error_launch(self):
        if not self.validate_defenses():
            error_prefix = f"One DefensesTogether failed validation on"
            error_suffix = f"was given instead."
            ExitUtils.exit_with_error(f"{error_prefix} <defenses_together> inside of <DefensesTogether>. {DefensesTogether.get_defenses_allow_criteria()} {self.get_defenses()} of type {type(self.get_defenses())} {error_suffix}")

    @staticmethod
    def get_defenses_allow_criteria() -> str:
        return "It must be a list of Defense ."

    def set_defenses(self, defenses : List[Defense]):
        self.defenses = defenses

        self.validate_defenses_with_error_launch()
        
        if self.print_diagnostics:
            PrintUtils.print_in_green(f"- Inside <defense>, <defenses_together> assignment of one DefensesTogether has been succesfully set to {self.get_defenses()}")

    def add_defense(self, defense : Defense = None):
        if defense is None:
            PrintUtils.print_warning(f"Tried add_defense() on object {self.get_name()} but None was given.\nSkipping the operation.")
            return

        self.get_defenses().append(defense)


    # ============================================
    # active_response operations
    # ============================================

    def get_active_response(self) -> ActiveResponse:
        return self.active_response

    def validate_active_response(self) -> bool:
        return self.get_active_response().validate_all()
    
    def validate_active_response_with_error_launch(self):
        self.validate_active_response()


    def set_active_response(self, active_response : ActiveResponse):
        self.active_response = active_response

        self.validate_active_response_with_error_launch()
        
        if self.print_diagnostics:
            PrintUtils.print_in_green(f'- <defense> <active-response> assignment of DefenseTogether named {self.get_name()} has been succesfully set to {self.get_active_response()}')


    # ============================================
    # rules_id operations
    # ============================================

    def get_rules_id(self) -> str:
        return self.rules_id

    def validate_rules_id(self) -> bool:
        return isinstance(self.get_rules_id(), str)
    
    def validate_rules_id_with_error_launch(self):
        if not self.validate_rules_id():
            error_prefix = f"DefensesTogether named {self.get_name()} failed validation on"
            error_suffix = f"was given instead."
            ExitUtils.exit_with_error(f'{error_prefix} rules_id. {DefensesTogether.get_rules_id_allow_criteria()} {self.get_rules_id()} of type {type(self.get_rules_id())} {error_suffix}')

    @staticmethod
    def get_rules_id_allow_criteria() -> str:
        return "It must be a string."

    def set_rules_id(self, rules_id : str):
        self.rules_id = rules_id

        self.validate_rules_id_with_error_launch()
        
        if self.print_diagnostics:
            PrintUtils.print_in_green(f'- rules_id assignment of DefensesTogether named {self.get_name()} has been succesfully set to {self.get_rules_id()}')




    # ============================================
    # Validate All
    # ============================================   


    def validate_all(self):

        self.validate_name_with_error_launch()

        self.validate_defenses_ids_with_error_launch()

        self.validate_id_with_error_launch()

        self.validate_defenses_with_error_launch()

        self.validate_rules_id_with_error_launch()

        self_actres = self.get_active_response()
        if self_actres is not None:  
            self.validate_active_response_with_error_launch()



    # ============================================
    # to_string()
    # ============================================   

    def to_string_total(self, tab_times : int = 0):
        give_tabs = '\t'*tab_times
        string = ''

        string = f'{give_tabs}<active_response>\n'

        for defense in self.get_defenses():
            defense_comm_name = defense.get_comm_name()
            string += f'{give_tabs}\t<command>{defense_comm_name}</command>\n'

        if self.get_active_response() is not None:
            location = self.get_active_response().get_location()
            if location is not None:
                string += f'{give_tabs}\t<location>{location}</location>\n'
            
            agent_id = self.get_active_response().get_agent_id()
            if agent_id is not None:
                string += f'{give_tabs}\t<agent_id>{agent_id}</agent_id>\n'

            timeout = self.get_active_response().get_timeout()
            if timeout != 'no':
                string += f'{give_tabs}\t<timeout>{timeout}</timeout>\n'
        else:
                string += f'{give_tabs}\t<location>local</location>\n' 


        #string += f'{give_tabs}\t<rules_id>{self.get_rules_id()}</rules_id>\n'

        string += f'{give_tabs}</active_response>\n'


        return string
