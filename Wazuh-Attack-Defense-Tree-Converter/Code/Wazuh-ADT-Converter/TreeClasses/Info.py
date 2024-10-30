import validations

# Import scripts from above folder
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from terminal_UI_utils import PrintUtils, ExitUtils


class Info:
    
    print_diagnostics = True

    def __init__(self,
                 type   : str = "text", 
                 info  : str = None, #Set this to None by default because it is not mandatory and can be omitted
                 relative_node_name : str = "unspecified" #Useful for prints
                ):
        self.type = type
        self.info = info
        self.relative_node_name = relative_node_name

    # ============================================
    # <info type=""> operations
    # ============================================
    
    def get_wrc_info_type(self) -> str:
        return self.type

    def validate_wrc_info_type(self) -> bool:
        # Type check
        if not isinstance(self.get_wrc_info_type(), str):
            return False
        # Allowed values check
        allowed_values=["text", "cve", "link", "ovsdb"]
        return validations.is_allowed(allowed_values=allowed_values, string=self.get_wrc_info_type())

    def validate_wrc_info_type_with_error_launch(self):
        if not self.validate_wrc_info_type():
            error_prefix = f"The node {self.relative_node_name} failed validation on"
            error_suffix = f"was given instead."
            ExitUtils.exit_with_error(f'{error_prefix} <freq_info type="{self.get_wrc_info_type()}"> in <wazuh_rule_config>. {Info.get_wrc_info_type_allow_criteria()} {self.get_wrc_info_type()} of type {type(self.get_wrc_info_type())} {error_suffix}')
        

    @staticmethod
    def get_wrc_info_type_allow_criteria():
        return "It must be 'text' or 'cve' or 'link' or 'ovsdb'."

    def set_wrc_info_type(self, type_ : str):
        self.type = type_

        self.validate_wrc_info_type_with_error_launch()

        if self.print_diagnostics:
            PrintUtils.print_in_green(f'- Inside <wazuh_rule_config>, <info type=""> of node {self.relative_node_name} has been succesfully set to {type_}')


    # ============================================
    # <info> operations
    # ============================================
    
    def get_wrc_info_info(self) -> str:
        return self.info

    def validate_wrc_info_info(self) -> bool:
        # Type check
        if not (self.get_wrc_info_info() is None or isinstance(self.get_wrc_info_info(), str) ):
            return False
        return True

    def validate_wrc_info_info_with_error_launch(self):
        if not self.validate_wrc_info_info():
            error_prefix = f"The node {self.relative_node_name} failed validation on"
            error_suffix = f"was given instead."
            ExitUtils.exit_with_error(f'{error_prefix} <freq_info>{self.get_wrc_info_info()}</freq_info> in <wazuh_rule_config>. {Info.get_wrc_info_info_allow_criteria()} {self.get_wrc_info_info()} of type {type(self.get_wrc_info_info())} {error_suffix}')
        

    @staticmethod
    def get_wrc_info_info_allow_criteria():
        return "It must be a string."

    def set_wrc_info_info(self, info : str):
        self.info = info

        self.validate_wrc_info_info_with_error_launch()

        if self.print_diagnostics:
            PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, <info> of node {self.relative_node_name} has been succesfully set to {info}")

    # ============================================
    # Validate All
    # ============================================

    def validate_all(self):
        
        self.validate_wrc_info_type_with_error_launch()
            
        self.validate_wrc_info_info_with_error_launch()
            
        #PrintUtils.print_in_green(f"- Validation of a <freq_info> related to {self.relative_node_name} was succesful!")

    # ============================================
    # Print
    # ============================================

    def to_string(self):
        return f'<info type="{self.get_wrc_info_type()}">{self.get_wrc_info_info()}</info>'




def test():
    f = Info()
    f.validate_all()
    f.to_string()



if __name__ == '__main__':
    test()