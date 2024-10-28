import validations

# Import scripts from above folder
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from terminal_UI_utils import PrintUtils, ExitUtils


class FreqSrcport:
    
    print_diagnostics = True

    def __init__(self, 
                 negate : str = "no", 
                 type   : str = "osmatch", 
                 srcport  : str = None, #Set this to None by default because it is not mandatory and can be omitted
                 relative_node_name : str = "unspecified" #Useful for prints
                ):
        self.negate = negate
        self.type = type
        self.srcport = srcport
        self.relative_node_name = relative_node_name

    # ============================================
    # <srcport negate=""> operations
    # ============================================
    
    def get_wrc_srcport_negate(self) -> str:
        return self.negate

    def validate_wrc_srcport_negate(self) -> bool:
        # Type check
        if not isinstance(self.get_wrc_srcport_negate(), str):
            return False
        # Allowed values check
        return validations.is_yes_or_no(self.get_wrc_srcport_negate())

    @staticmethod
    def get_wrc_srcport_negate_allow_criteria():
        return "It must be 'yes' or 'no'."

    def set_wrc_srcport_negate(self, negate : str):
        self.negate = negate
        if self.validate_wrc_srcport_negate():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f'- Inside <wazuh_rule_config>, <freq_srcport negate=""> of node {self.relative_node_name} has been succesfully set to {negate}')
        else:
            ExitUtils.exit_with_error(f'You cannot set <freq_srcport negate=""> of node {self.relative_node_name} to {negate} of type {type(negate)}. {FreqSrcport.get_wrc_srcport_negate_allow_criteria()}')


    # ============================================
    # <srcport type=""> operations
    # ============================================
    
    def get_wrc_srcport_type(self) -> str:
        return self.type

    def validate_wrc_srcport_type(self) -> bool:
        # Type check
        if not isinstance(self.get_wrc_srcport_type(), str):
            return False
        # Allowed values check
        return validations.is_osmatch_osregex_pcre2(self.get_wrc_srcport_type())

    @staticmethod
    def get_wrc_srcport_type_allow_criteria():
        return "It must be 'osmatch' or 'osregex' or 'pcre2'."

    def set_wrc_srcport_type(self, type_ : str):
        self.type = type_
        if self.validate_wrc_srcport_type():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f'- Inside <wazuh_rule_config>, <freq_srcport type=""> of node {self.relative_node_name} has been succesfully set to {type_}')
        else:
            ExitUtils.exit_with_error(f'You cannot set <freq_srcport type=""> of node {self.relative_node_name} to {type_} of type {type(type_)}. {FreqSrcport.get_wrc_srcport_type_allow_criteria()}')


    # ============================================
    # <srcport> operations
    # ============================================
    
    def get_wrc_srcport_srcport(self) -> str:
        return self.srcport

    def validate_wrc_srcport_srcport(self) -> bool:
        # Type check
        if not (self.get_wrc_srcport_srcport() is None or isinstance(self.get_wrc_srcport_srcport(), str) ):
            return False
        return True

    @staticmethod
    def get_wrc_srcport_srcport_allow_criteria():
        return "It must be a string."

    def set_wrc_srcport_srcport(self, srcport : str):
        self.srcport = srcport
        if self.validate_wrc_srcport_srcport():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, <freq_srcport> of node {self.relative_node_name} has been succesfully set to {srcport}")
        else:
            ExitUtils.exit_with_error(f"You cannot set <freq_srcport> of node {self.relative_node_name} to {srcport} of type {type(srcport)}. {FreqSrcport.get_wrc_srcport_srcport_allow_criteria()}")

    # ============================================
    # Validate All
    # ============================================

    def validate_all(self):
        error_prefix = f"The node {self.relative_node_name} failed validation on"
        error_suffix = f"was given instead."

        if not self.validate_wrc_srcport_negate():
            ExitUtils.exit_with_error(f'{error_prefix} <freq_srcport negate="{self.get_wrc_srcport_negate()}"> in <wazuh_rule_config>. {FreqSrcport.get_wrc_srcport_negate_allow_criteria()} {self.get_wrc_srcport_negate()} of type {type(self.get_wrc_srcport_negate())} {error_suffix}')
        if not self.validate_wrc_srcport_type():
            ExitUtils.exit_with_error(f'{error_prefix} <freq_srcport type="{self.get_wrc_srcport_type()}"> in <wazuh_rule_config>. {FreqSrcport.get_wrc_srcport_type_allow_criteria()} {self.get_wrc_srcport_type()} of type {type(self.get_wrc_srcport_type())} {error_suffix}')
        if not self.validate_wrc_srcport_srcport():
            ExitUtils.exit_with_error(f'{error_prefix} <freq_srcport>{self.get_wrc_srcport_srcport()}</freq_srcport> in <wazuh_rule_config>. {FreqSrcport.get_wrc_srcport_srcport_allow_criteria()} {self.get_wrc_srcport_srcport()} of type {type(self.get_wrc_srcport_srcport())} {error_suffix}')
        #PrintUtils.print_in_green(f"- Validation of a <freq_srcport> related to {self.relative_node_name} was succesful!")

    # ============================================
    # Print
    # ============================================

    def to_string(self):
        print(f'<srcport negate="{self.get_wrc_srcport_negate()}" type="{self.get_wrc_srcport_type()}">{self.get_wrc_srcport_srcport()}</srcport>')




def test():
    f = FreqSrcport()
    f.validate_all()
    f.to_string()



if __name__ == '__main__':
    test()