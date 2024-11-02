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
                 ):
        
        self.location = location
        self.agent_id = agent_id

        self.timeout = timeout


    # ============================================
    # location operations
    # ============================================

    def get_location(self) -> str:
        return self.location

    def validate_location(self) -> bool:
        return  isinstance(self.get_location(), str) and validations.is_allowed(allowed_values=['local', 'server', 'defined-agent', 'all'], string=self.get_location())
    
    def validate_location_with_error_launch(self):
        if not self.validate_location():
            error_prefix = f"One ActiveResponse failed validation on"
            error_suffix = f"was given instead."
            ExitUtils.exit_with_error(f"{error_prefix} location of ActiveResponse. {ActiveResponse.get_location_allow_criteria()} {self.get_location()} of type {type(self.get_location())} {error_suffix}")

    @staticmethod
    def get_location_allow_criteria() -> str:
        return "It must be one of 'local', 'server', 'defined-agent', 'all' ."

    def set_location(self, location : int):
        self.location = location

        self.validate_location_with_error_launch()
        
        if self.print_diagnostics:
            PrintUtils.print_in_green(f"- <location> of one ActiveResponse has been succesfully set to {self.get_location()}")




    # ============================================
    # agent_id operations
    # ============================================

    def get_agent_id(self) -> str:
        return self.agent_id

    def validate_agent_id(self) -> bool:
        return self.get_agent_id() is None or (isinstance(self.get_agent_id(), str) and self.get_agent_id().isdigit())
    
    def validate_agent_id_with_error_launch(self):
        if not self.validate_agent_id():
            error_prefix = f"One ActiveResponse failed validation on"
            error_suffix = f"was given instead."
            ExitUtils.exit_with_error(f"{error_prefix} <agent_id> of ActiveResponse. {ActiveResponse.get_agent_id_allow_criteria()} {self.get_agent_id()} of type {type(self.get_agent_id())} {error_suffix}")

    @staticmethod
    def get_agent_id_allow_criteria() -> str:
        return "It must be a string composed of digits only."

    def set_agent_id(self, agent_id : int):
        self.agent_id = agent_id

        self.validate_agent_id_with_error_launch()
        
        if self.print_diagnostics:
            PrintUtils.print_in_green(f"- <agent_id> of one one ActiveResponse has been succesfully set to {self.get_agent_id()}")


    # ============================================
    # timeout operations
    # ============================================

    def get_timeout(self) -> int:
        return self.timeout

    def validate_timeout(self) -> bool:
        return self.get_timeout() is None or isinstance(self.get_timeout(), int)
    
    def validate_timeout_with_error_launch(self):
        if not self.validate_timeout():
            error_prefix = f"One ActiveResponse failed validation on"
            error_suffix = f"was given instead."
            ExitUtils.exit_with_error(f"{error_prefix} <timeout> of ActiveResponse. {ActiveResponse.get_timeout_allow_criteria()} {self.get_timeout()} of type {type(self.get_timeout())} {error_suffix}")

    @staticmethod
    def get_timeout_allow_criteria() -> str:
        return "It must be a int number."

    def set_timeout(self, timeout : int):
        self.timeout = timeout

        self.validate_timeout_with_error_launch()
        
        if self.print_diagnostics:
            PrintUtils.print_in_green(f"- <timeout> of one one ActiveResponse has been succesfully set to {self.get_timeout()}")




    # ============================================
    # Validate All
    # ============================================   


    def validate_all(self):

        self.validate_timeout_with_error_launch()
        self.validate_agent_id_with_error_launch()
        self.validate_location_with_error_launch()

        # Agent id if and only if location is defined-agent
        if self.get_agent_id() is not None and self.get_location() != 'defined-agent' :
            error_prefix = f"One ActiveResponse failed validation on"
            error_suffix = f"was given instead."
            ExitUtils.exit_with_error(f"{error_prefix} <agent-id> and <location> of ActiveResponse. If agent-id is given, location MUST be defined-agent.\n <agent-id>{self.get_agent_id()} and <location> {self.get_location()} {error_suffix}")

