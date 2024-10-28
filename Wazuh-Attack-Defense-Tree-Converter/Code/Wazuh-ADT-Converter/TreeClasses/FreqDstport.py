import validations

# Import scripts from above folder
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from terminal_UI_utils import PrintUtils, ExitUtils


class FreqDstport:
    
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

    @staticmethod
    def get_wrc_dstport_negate_allow_criteria():
        return "It must be 'yes' or 'no'."

    def set_wrc_dstport_negate(self, negate : str):
        self.negate = negate
        if self.validate_wrc_dstport_negate():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f'- Inside <wazuh_rule_config>, <freq_dstport negate=""> of node {self.relative_node_name} has been succesfully set to {negate}')
        else:
            ExitUtils.exit_with_error(f'You cannot set <freq_dstport negate=""> of node {self.relative_node_name} to {negate} of type {type(negate)}. {FreqDstport.get_wrc_dstport_negate_allow_criteria()}')


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

    @staticmethod
    def get_wrc_dstport_type_allow_criteria():
        return "It must be 'osmatch' or 'osregex' or 'pcre2'."

    def set_wrc_dstport_type(self, type_ : str):
        self.type = type_
        if self.validate_wrc_dstport_type():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f'- Inside <wazuh_rule_config>, <freq_dstport type=""> of node {self.relative_node_name} has been succesfully set to {type_}')
        else:
            ExitUtils.exit_with_error(f'You cannot set <freq_dstport type=""> of node {self.relative_node_name} to {type_} of type {type(type_)}. {FreqDstport.get_wrc_dstport_type_allow_criteria()}')


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

    @staticmethod
    def get_wrc_dstport_dstport_allow_criteria():
        return "It must be a string."

    def set_wrc_dstport_dstport(self, dstport : str):
        self.dstport = dstport
        if self.validate_wrc_dstport_dstport():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, <freq_dstport> of node {self.relative_node_name} has been succesfully set to {dstport}")
        else:
            ExitUtils.exit_with_error(f"You cannot set <freq_dstport> of node {self.relative_node_name} to {dstport} of type {type(dstport)}. {FreqDstport.get_wrc_dstport_dstport_allow_criteria()}")

    # ============================================
    # Validate All
    # ============================================

    def validate_all(self):
        error_prefix = f"The node {self.relative_node_name} failed validation on"
        error_suffix = f"was given instead."

        if not self.validate_wrc_dstport_negate():
            ExitUtils.exit_with_error(f'{error_prefix} <freq_dstport negate="{self.get_wrc_dstport_negate()}"> in <wazuh_rule_config>. {FreqDstport.get_wrc_dstport_negate_allow_criteria()} {self.get_wrc_dstport_negate()} of type {type(self.get_wrc_dstport_negate())} {error_suffix}')
        if not self.validate_wrc_dstport_type():
            ExitUtils.exit_with_error(f'{error_prefix} <freq_dstport type="{self.get_wrc_dstport_type()}"> in <wazuh_rule_config>. {FreqDstport.get_wrc_dstport_type_allow_criteria()} {self.get_wrc_dstport_type()} of type {type(self.get_wrc_dstport_type())} {error_suffix}')
        if not self.validate_wrc_dstport_dstport():
            ExitUtils.exit_with_error(f'{error_prefix} <freq_dstport>{self.get_wrc_dstport_dstport()}</freq_dstport> in <wazuh_rule_config>. {FreqDstport.get_wrc_dstport_dstport_allow_criteria()} {self.get_wrc_dstport_dstport()} of type {type(self.get_wrc_dstport_dstport())} {error_suffix}')
        #PrintUtils.print_in_green(f"- Validation of a <freq_dstport> related to {self.relative_node_name} was succesful!")

    # ============================================
    # Print
    # ============================================

    def to_string(self):
        print(f'<dstport negate="{self.get_wrc_dstport_negate()}" type="{self.get_wrc_dstport_type()}">{self.get_wrc_dstport_dstport()}</dstport>')




def test():
    f = FreqDstport()
    f.validate_all()
    f.to_string()



if __name__ == '__main__':
    test()