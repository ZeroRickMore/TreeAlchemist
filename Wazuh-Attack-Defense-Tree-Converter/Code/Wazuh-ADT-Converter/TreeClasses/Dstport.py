import validations

# Import scripts from above folder
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from terminal_UI_utils import PrintUtils, ExitUtils


class Dstport:
    
    print_diagnostics = True

    def __init__(self, 
                 negate : str = "no", 
                 type   : str = "osmatch", 
                 dstport  : str = None, #Set this to None by default because it is not mandatory and can be omitted
                 relative_node_name : str = "unspecified" #Useful for prints
                ):
        self.negate = negate
        self.type = type
        self.dstport = dstport
        self.relative_node_name = relative_node_name

    # ============================================
    # <dstport negate=""> operations
    # ============================================
    
    def get_wrc_dstport_negate(self) -> str:
        return self.negate

    def validate_wrc_dstport_negate(self) -> bool:
        # Type check
        if not isinstance(self.get_wrc_dstport_negate(), str):
            return False
        # Allowed values check
        return validations.is_yes_or_no(self.get_wrc_dstport_negate())

    def validate_wrc_dstport_negate_with_error_launch(self):
        if not self.validate_wrc_dstport_negate():
            error_prefix = f"The node {self.relative_node_name} failed validation on"
            error_suffix = f"was given instead."
            ExitUtils.exit_with_error(f'{error_prefix} <dstport negate="{self.get_wrc_dstport_negate()}"> in <wazuh_rule_config>. {Dstport.get_wrc_dstport_negate_allow_criteria()} {self.get_wrc_dstport_negate()} of type {type(self.get_wrc_dstport_negate())} {error_suffix}')

    @staticmethod
    def get_wrc_dstport_negate_allow_criteria():
        return "It must be 'yes' or 'no'."

    def set_wrc_dstport_negate(self, negate : str):
        self.negate = negate

        self.validate_wrc_dstport_negate_with_error_launch()

        if self.print_diagnostics:
            PrintUtils.print_in_green(f'- Inside <wazuh_rule_config>, <dstport negate=""> of node {self.relative_node_name} has been succesfully set to {negate}')


    # ============================================
    # <dstport type=""> operations
    # ============================================
    
    def get_wrc_dstport_type(self) -> str:
        return self.type

    def validate_wrc_dstport_type(self) -> bool:
        # Type check
        if not isinstance(self.get_wrc_dstport_type(), str):
            return False
        # Allowed values check
        return validations.is_osmatch_osregex_pcre2(self.get_wrc_dstport_type())

    def validate_wrc_dstport_type_with_error_launch(self):
        if not self.validate_wrc_dstport_type():
            error_prefix = f"The node {self.relative_node_name} failed validation on"
            error_suffix = f"was given instead."
            ExitUtils.exit_with_error(f'{error_prefix} <dstport type="{self.get_wrc_dstport_type()}"> in <wazuh_rule_config>. {Dstport.get_wrc_dstport_type_allow_criteria()} {self.get_wrc_dstport_type()} of type {type(self.get_wrc_dstport_type())} {error_suffix}')
        

    @staticmethod
    def get_wrc_dstport_type_allow_criteria():
        return "It must be 'osmatch' or 'osregex' or 'pcre2'."

    def set_wrc_dstport_type(self, type_ : str):
        self.type = type_

        self.validate_wrc_dstport_type_with_error_launch()

        if self.print_diagnostics:
            PrintUtils.print_in_green(f'- Inside <wazuh_rule_config>, <dstport type=""> of node {self.relative_node_name} has been succesfully set to {type_}')


    # ============================================
    # <dstport> operations
    # ============================================
    
    def get_wrc_dstport_dstport(self) -> str:
        return self.dstport

    def validate_wrc_dstport_dstport(self) -> bool:
        # Type check
        if not (self.get_wrc_dstport_dstport() is None or isinstance(self.get_wrc_dstport_dstport(), str) ):
            return False
        return True

    def validate_wrc_dstport_dstport_with_error_launch(self):
        if not self.validate_wrc_dstport_dstport():
            error_prefix = f"The node {self.relative_node_name} failed validation on"
            error_suffix = f"was given instead."
            ExitUtils.exit_with_error(f'{error_prefix} <dstport>{self.get_wrc_dstport_dstport()}</dstport> in <wazuh_rule_config>. {Dstport.get_wrc_dstport_dstport_allow_criteria()} {self.get_wrc_dstport_dstport()} of type {type(self.get_wrc_dstport_dstport())} {error_suffix}')
        
    @staticmethod
    def get_wrc_dstport_dstport_allow_criteria():
        return "It must be a string."

    def set_wrc_dstport_dstport(self, dstport : str):
        self.dstport = dstport

        self.validate_wrc_dstport_dstport_with_error_launch()

        if self.print_diagnostics:
            PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, <dstport> of node {self.relative_node_name} has been succesfully set to {dstport}")


    # ============================================
    # Validate All
    # ============================================

    def validate_all(self):

        self.validate_wrc_dstport_negate_with_error_launch()
            
        self.validate_wrc_dstport_type_with_error_launch()
            
        self.validate_wrc_dstport_dstport_with_error_launch()
            
        #PrintUtils.print_in_green(f"- Validation of a <dstport> related to {self.relative_node_name} was succesful!")

    # ============================================
    # Print
    # ============================================

    def to_string(self):
        return f'<dstport negate="{self.get_wrc_dstport_negate()}" type="{self.get_wrc_dstport_type()}">{self.get_wrc_dstport_dstport()}</dstport>'




def test():
    f = Dstport()
    f.validate_all()
    f.to_string()



if __name__ == '__main__':
    test()