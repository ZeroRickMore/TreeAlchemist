from typing import List

# Import scripts from above folder
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from terminal_UI_utils import PrintUtils, ExitUtils
import validations
from DefenseClasses.Command import Command
from DefenseClasses.ActiveResponse import ActiveResponse


class Defense:
    '''
    This class represents the whole defense, so it is mapped to one or more states
    and has a Command and Active response.
    '''

    print_diagnostics = True

    def __init__(self,
                name : str = None, # The name given in defense name=""
                id : int = None,
                command : Command = None,
                active_response : ActiveResponse = None,
                rules_id : str = '' 
                ):
        
        self.name = name
        self.id = id

        self.command = command

        self.active_response = active_response

        self.comm_name = None # MUST be set calling generate_extra_values()

        self.rules_id = rules_id




    # ============================================
    # name operations
    # ============================================

    def get_name(self) -> str:
        return self.name

    def validate_name(self) -> bool:
        name = self.get_name()
        # ok if None
        if name is None:
            return True
        
        # Check string and if valid
        if not isinstance(name, str):
            return False
        # Check if ascii
        if not name.isascii():
            return False
        # Check if first character is a number
        if name[0].isdigit():
            return False
        # Check if extension is given
        if '.' not in name:
            return False
        # Check if only letters, numbers and _
        return all(c.isalnum() or c == '_' or c == '.' for c in name)
    
    def validate_name_with_error_launch(self):
        if not self.validate_name():
            error_prefix = f"Defense named {self.get_name()} failed validation on"
            error_suffix = f"was given instead."
            ExitUtils.exit_with_error(f'{error_prefix} <defense name="">. {Defense.get_name_allow_criteria()} {self.get_name()} of type {type(self.get_name())} {error_suffix}')

    @staticmethod
    def get_name_allow_criteria() -> str:
        return "It must be a string, composed of ascii characters only, must NOT start with a digit, must have a file extension, and must be composed only of letters, numbers, and underscores.\nThis is a file name, after all."

    def set_name(self, name : str):
        self.name = name

        self.validate_name_with_error_launch()
        
        if self.print_diagnostics:
            PrintUtils.print_in_green(f'- <defense name=""> assignment of Defense named {self.get_name()} has been succesfully set to {self.get_name()}')

    # ============================================
    # id operations
    # ============================================

    def get_id(self) -> int:
        return self.id

    def validate_id(self) -> bool:
        return self.get_id() is None or isinstance(self.get_id(), int)
    
    def validate_id_with_error_launch(self):
        if not self.validate_id():
            error_prefix = f"Defense named {self.get_name()} failed validation on"
            error_suffix = f"was given instead."
            ExitUtils.exit_with_error(f'{error_prefix} <defense id="">. {Defense.get_id_allow_criteria()} {self.get_id()} of type {type(self.get_id())} {error_suffix}')

    @staticmethod
    def get_id_allow_criteria() -> str:
        return "It must be a int."

    def set_id(self, id : int):
        self.id = id

        self.validate_id_with_error_launch()
        
        if self.print_diagnostics:
            PrintUtils.print_in_green(f'- <defense id=""> assignment of Defense named {self.get_name()} has been succesfully set to {self.get_id()}')



    # ============================================
    # command operations
    # ============================================

    def get_command(self) -> Command:
        return self.command

    def validate_command(self) -> bool:
        return self.get_command().validate_all()
    
    def validate_command_with_error_launch(self):
        self.validate_command()

    def set_command(self, command : Command):
        self.command = command

        self.validate_command_with_error_launch()

        if self.print_diagnostics:
            PrintUtils.print_in_green(f'- <defense> <command> assignment of Defense named {self.get_name()} has been succesfully set to {self.get_command()}')


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
            PrintUtils.print_in_green(f'- <defense> <active-response> assignment of Defense named {self.get_name()} has been succesfully set to {self.get_active_response()}')
    

    # ============================================
    # rules_id operations
    # ============================================

    def get_rules_id(self) -> str:
        return self.rules_id

    def validate_rules_id(self) -> bool:
        return isinstance(self.get_rules_id(), str)
    
    def validate_rules_id_with_error_launch(self):
        if not self.validate_rules_id():
            error_prefix = f"Defense named {self.get_name()} failed validation on"
            error_suffix = f"was given instead."
            ExitUtils.exit_with_error(f'{error_prefix} rules_id. {Defense.get_rules_id_allow_criteria()} {self.get_rules_id()} of type {type(self.get_rules_id())} {error_suffix}')

    @staticmethod
    def get_rules_id_allow_criteria() -> str:
        return "It must be a string."

    def set_rules_id(self, rules_id : str):
        self.rules_id = rules_id

        self.validate_rules_id_with_error_launch()
        
        if self.print_diagnostics:
            PrintUtils.print_in_green(f'- rules_id assignment of Defense named {self.get_name()} has been succesfully set to {self.get_rules_id()}')



    # ===============================================
    # Extra values generation over object attributes
    # ===============================================

    def generate_extra_values(self, adt_name : str = ''):
        '''
        This function generates:
        of <command>:
        <name> as "Launch "+self.get_name()
        <executable> as self.get_name()

        of <active-response>
        <command>
        '''

        self.comm_name = "Launch_TA_" + adt_name + '_' + self.get_name()

    def get_comm_name(self):
        return self.comm_name

    # ============================================
    # Validate All
    # ============================================   


    def validate_all(self):
        error_prefix = f"Defense named {self.get_name()} failed validation on"

        self.validate_name_with_error_launch()

        self.validate_rules_id_with_error_launch()

        self_command = self.get_command()
        if self_command is not None:
            self.validate_command_with_error_launch()

        self_actres = self.get_active_response()
        if self_actres is not None:        
            self.validate_active_response_with_error_launch()

        if self.get_comm_name() is None:
            self.generate_extra_values()

        # Timeout validation
        if self_command is None and self_actres is None: # Both None? No issue.
            return
        if (self_command.get_timeout_allowed() == "no" or self_command is None) and self_actres.get_timeout() is not None:
            ExitUtils.exit_with_error(f'{error_prefix} <command> timeout_allowed and <active-response> timeout.\nYou have given a <timeout> but <timeout_allowed> is not "yes".')


    # ============================================
    # to_string()
    # ============================================   
    

    def to_string_command(self, tab_times : int = 0) -> str:
        '''
        Generates following the syntax

        <command>
            <name>self.get_comm_name()</name>
            <executable>self.get_name()</executable>
            <extra_args>self.get_extra_args()</extra_args>
            <timeout_allowed>self.get_timeout_allowed()</timeout_allowed>
        </command>
        
        '''
        give_tabs = '\t'*tab_times
        string = f'{give_tabs}<command>\n'

        comm_name = self.get_comm_name()
        if comm_name is not None:
            string += f'{give_tabs}\t<name>{comm_name}</name>\n'
        
        name = self.get_name()
        if name is not None:
            string += f'{give_tabs}\t<executable>{name}</executable>\n'
        
        if self.get_command() is not None:
            extra_args = self.get_command().get_extra_args()
            if extra_args is not None:
                string += f'{give_tabs}\t<extra_args>{extra_args}</extra_args>\n'

            timeout_allowed = self.get_command().get_timeout_allowed()
            if timeout_allowed is not None:
                string += f'{give_tabs}\t<timeout_allowed>{timeout_allowed}</timeout_allowed>\n'

        string += f'{give_tabs}</command>\n'

        return string
    

    def to_string_active_response(self, tab_times : int = 0) -> str:
        '''
        Generates following the syntax

        <active-response>
            <command>self.get_comm_name()</command>
            <location>self.get_active_response().get_location()</location>
            <agent_id>self.get_active_response().get_agent_id()</agent_id>
            <rules_id>GENERATION TO BE SPECIFIED</rules_id>
            <timeout>self.get_active_response().get_timeout()</timeout>
        </active-response>
        
        '''
        give_tabs = '\t'*tab_times
        string = f'{give_tabs}<active-response>\n'

        comm_name = self.get_comm_name()
        if comm_name is not None:
            string += f'{give_tabs}\t<command>{comm_name}</command>\n'
        
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

        #string += f'{give_tabs}\t<rules_id>{self.get_rules_id()}</rules_id>\n' # Useless

        string += f'{give_tabs}</active-response>\n'

        return string
    

    def to_string_total(self, tab_times : int = 0):
        string = ''

        string += self.to_string_command(tab_times=tab_times)

        string += '\n'

        string += self.to_string_active_response(tab_times=tab_times)

        return string