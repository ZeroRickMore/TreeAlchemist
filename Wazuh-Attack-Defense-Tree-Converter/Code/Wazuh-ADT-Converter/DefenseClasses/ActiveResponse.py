# Import scripts from above folder
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from terminal_UI_utils import PrintUtils, ExitUtils

from DefenseClasses.Command import Command
import validations


class ActiveResponse:
    '''
    A class that represents the active-response.
    '''
    print_diagnostics = True

    def __init__(self,
                 location : str = "local", # Set this to local by default because it is not mandatory and can be omitted
                 agent_id : str = None,  # Set this to None by default because it is not mandatory and can be omitted
                 timeout  : int = None,   # Set this to None by default because it is not mandatory and can be omitted
                 command  : Command = None,
                 name     : str = "unspecified" # This is just for debug honestly
                 ):
        
        self.location = location
        self.agent_id = agent_id
        self.name = name

        self.timeout = timeout
        self.command = command


    # ============================================
    # name operations
    # ============================================

    def get_name(self) -> str:
        return self.name

    def validate_name(self) -> bool:
        return  isinstance(self.get_name(), str)
    
    def validate_name_with_error_launch(self):
        if not self.validate_name():
            error_prefix = f"The ActiveResponse {self.get_name()} failed validation on"
            error_suffix = f"was given instead."
            ExitUtils.exit_with_error(f"{error_prefix} name of ActiveResponse. {Command.get_name_allow_criteria()} {self.get_name()} of type {type(self.get_name())} {error_suffix}")

    @staticmethod
    def get_name_allow_criteria() -> str:
        return "It must be a string."

    def set_name(self, name : int):
        self.name = name

        self.validate_name_with_error_launch()
        
        if self.print_diagnostics:
            PrintUtils.print_in_green(f"- Backend name assignment of ActiveResponse {self.get_name()} has been succesfully set to {self.get_name()}")



    # ============================================
    # location operations
    # ============================================

    def get_location(self) -> str:
        return self.location

    def validate_location(self) -> bool:
        return  isinstance(self.get_location(), str) and validations.is_allowed(allowed_values=['local', 'server', 'defined-agent', 'all'], string=self.get_location())
    
    def validate_location_with_error_launch(self):
        if not self.validate_location():
            error_prefix = f"The ActiveResponse {self.get_name()} failed validation on"
            error_suffix = f"was given instead."
            ExitUtils.exit_with_error(f"{error_prefix} location of ActiveResponse. {ActiveResponse.get_location_allow_criteria()} {self.get_location()} of type {type(self.get_location())} {error_suffix}")

    @staticmethod
    def get_location_allow_criteria() -> str:
        return "It must be one of 'local', 'server', 'defined-agent', 'all' ."

    def set_location(self, location : int):
        self.location = location

        self.validate_location_with_error_launch()
        
        if self.print_diagnostics:
            PrintUtils.print_in_green(f"- <location> of ActiveResponse {self.get_name()} has been succesfully set to {self.get_location()}")




    # ============================================
    # agent_id operations
    # ============================================

    def get_agent_id(self) -> str:
        return self.agent_id

    def validate_agent_id(self) -> bool:
        return self.get_agent_id() is None or (isinstance(self.get_agent_id(), str) and self.get_agent_id().isdigit())
    
    def validate_agent_id_with_error_launch(self):
        if not self.validate_agent_id():
            error_prefix = f"The ActiveResponse {self.get_name()} failed validation on"
            error_suffix = f"was given instead."
            ExitUtils.exit_with_error(f"{error_prefix} <agent_id> of ActiveResponse. {ActiveResponse.get_agent_id_allow_criteria()} {self.get_agent_id()} of type {type(self.get_agent_id())} {error_suffix}")

    @staticmethod
    def get_agent_id_allow_criteria() -> str:
        return "It must be a string composed of digits only."

    def set_agent_id(self, agent_id : int):
        self.agent_id = agent_id

        self.validate_agent_id_with_error_launch()
        
        if self.print_diagnostics:
            PrintUtils.print_in_green(f"- <agent_id> of one ActiveResponse {self.get_name()} has been succesfully set to {self.get_agent_id()}")


    # ============================================
    # timeout operations
    # ============================================

    def get_timeout(self) -> int:
        return self.timeout

    def validate_timeout(self) -> bool:
        return self.get_timeout() is None or isinstance(self.get_timeout(), int)
    
    def validate_timeout_with_error_launch(self):
        if not self.validate_timeout():
            error_prefix = f"The ActiveResponse {self.get_name()} failed validation on"
            error_suffix = f"was given instead."
            ExitUtils.exit_with_error(f"{error_prefix} <timeout> of ActiveResponse. {ActiveResponse.get_timeout_allow_criteria()} {self.get_timeout()} of type {type(self.get_timeout())} {error_suffix}")

    @staticmethod
    def get_timeout_allow_criteria() -> str:
        return "It must be a int number."

    def set_timeout(self, timeout : int):
        self.timeout = timeout

        self.validate_timeout_with_error_launch()
        
        if self.print_diagnostics:
            PrintUtils.print_in_green(f"- <timeout> of one ActiveResponse {self.get_name()} has been succesfully set to {self.get_timeout()}")