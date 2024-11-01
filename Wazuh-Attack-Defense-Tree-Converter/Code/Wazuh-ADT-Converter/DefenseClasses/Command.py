# Import scripts from above folder
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from terminal_UI_utils import PrintUtils, ExitUtils
import validations



class Command:
    '''
    A class that represents the command that gets launched
    by the active-response.
    '''
    print_diagnostics = True

    def __init__(self,
                 extra_args : str = None, # Set this to None by default because it is not mandatory and can be omitted
                 timeout_allowed : str = None "  # Set this to False by default because it is not mandatory and can be omitted
                 ):
        
        self.name = None
        self.executable = None

        self.extra_args = extra_args
        self.timeout_allowed = timeout_allowed


    # ============================================
    # name operations
    # ============================================

    def get_name(self) -> str:
        return self.name

    def validate_name(self) -> bool:
        return  isinstance(self.get_name(), str)
    
    def validate_name_with_error_launch(self):
        if not self.validate_name():
            error_prefix = f"The command {self.get_name()} failed validation on"
            error_suffix = f"was given instead."
            ExitUtils.exit_with_error(f"{error_prefix} name of Command. {Command.get_name_allow_criteria()} {self.get_name()} of type {type(self.get_name())} {error_suffix}")

    @staticmethod
    def get_name_allow_criteria() -> str:
        return "It must be a string."

    def set_name(self, name : int):
        self.name = name

        self.validate_name_with_error_launch()
        
        if self.print_diagnostics:
            PrintUtils.print_in_green(f"- Backend name assignment of command {self.get_name()} has been succesfully set to {self.get_name()}")


    # ============================================
    # executable operations
    # ============================================

    def get_executable(self) -> str:
        return self.executable

    def validate_executable(self) -> bool:
        return  isinstance(self.get_executable(), str)
    
    def validate_executable_with_error_launch(self):
        if not self.validate_executable():
            error_prefix = f"The command {self.get_name()} failed validation on"
            error_suffix = f"was given instead."
            ExitUtils.exit_with_error(f"{error_prefix} executable of Command. {Command.get_executable_allow_criteria()} {self.get_executable()} of type {type(self.get_executable())} {error_suffix}")

    @staticmethod
    def get_executable_allow_criteria() -> str:
        return "It must be a string."

    def set_executable(self, executable : int):
        self.executable = executable

        self.validate_executable_with_error_launch()
        
        if self.print_diagnostics:
            PrintUtils.print_in_green(f"- Backend executable assignment of command {self.get_name()} has been succesfully set to {self.get_executable()}")



    # ============================================
    # extra_args operations
    # ============================================

    def get_extra_args(self) -> str:
        return self.extra_args

    def validate_extra_args(self) -> bool:
        return self.get_extra_args() is None or isinstance(self.get_extra_args(), str)
    
    def validate_extra_args_with_error_launch(self):
        if not self.validate_extra_args():
            error_prefix = f"The command {self.get_name()} failed validation on"
            error_suffix = f"was given instead."
            ExitUtils.exit_with_error(f"{error_prefix} <extra_args> inside of <command>. {Command.get_extra_args_allow_criteria()} {self.get_extra_args()} of type {type(self.get_extra_args())} {error_suffix}")

    @staticmethod
    def get_extra_args_allow_criteria() -> str:
        return "It must be a string."

    def set_extra_args(self, extra_args : int):
        self.extra_args = extra_args

        self.validate_extra_args_with_error_launch()
        
        if self.print_diagnostics:
            PrintUtils.print_in_green(f"- Inside <command>, <extra_args> assignment of command {self.get_name()} has been succesfully set to {self.get_extra_args()}")




    # ============================================
    # timeout_allowed operations
    # ============================================

    def get_timeout_allowed(self) -> str:
        return self.timeout_allowed

    def validate_timeout_allowed(self) -> bool:
        return self.get_timeout_allowed() is None or( isinstance(self.get_timeout_allowed(), str) and validations.is_allowed(allowed_values=['yes', 'no'], string=self.get_timeout_allowed()))
    
    def validate_timeout_allowed_with_error_launch(self):
        if not self.validate_timeout_allowed():
            error_prefix = f"The command {self.get_name()} failed validation on"
            error_suffix = f"was given instead."
            ExitUtils.exit_with_error(f"{error_prefix} <timeout_allowed> inside of <command>. {Command.get_timeout_allowed_allow_criteria()} {self.get_timeout_allowed()} of type {type(self.get_timeout_allowed())} {error_suffix}")

    @staticmethod
    def get_timeout_allowed_allow_criteria() -> str:
        return "It must be 'yes' or 'no' ."

    def set_timeout_allowed(self, timeout_allowed : bool):
        self.timeout_allowed = timeout_allowed

        self.validate_timeout_allowed_with_error_launch()
        
        if self.print_diagnostics:
            PrintUtils.print_in_green(f"- Inside <command>, <timeout_allowed> assignment of command {self.get_name()} has been succesfully set to {self.get_timeout_allowed()}")
  