import validations

# Import scripts from above folder
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from terminal_UI_utils import PrintUtils, ExitUtils

class Srcip:
    
    print_diagnostics = True

    def __init__(self, 
                 negate : str = "no", 
                 srcip  : str = None, #Set this to None by default because it is not mandatory and can be omitted
                 relative_node_name : str = "unspecified" #Useful for prints
                ):
        self.negate = negate
        self.srcip = srcip
        self.relative_node_name = relative_node_name

    # ============================================
    # <srcip negate=""> operations
    # ============================================
    
    def get_wrc_srcip_negate(self) -> str:
        return self.negate

    def validate_wrc_srcip_negate(self) -> bool:
        # Type check
        if not isinstance(self.get_wrc_srcip_negate(), str):
            return False
        # Allowed values check
        return validations.is_yes_or_no(self.get_wrc_srcip_negate())

    @staticmethod
    def get_wrc_srcip_negate_allow_criteria():
        return "It must be 'yes' or 'no'."

    def set_wrc_srcip_negate(self, negate : str):
        self.negate = negate
        if self.validate_wrc_srcip_negate():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f'- Inside <wazuh_rule_config>, <srcip negate=""> of node {self.relative_node_name} has been succesfully set to {negate}')
        else:
            ExitUtils.exit_with_error(f'You cannot set <srcip negate=""> of node {self.relative_node_name} to {negate} of type {type(negate)}. {Srcip.get_wrc_srcip_negate_allow_criteria()}')


    # ============================================
    # <freq_srcip> operations
    # ============================================
    
    def get_wrc_srcip_srcip(self) -> str:
        return self.srcip

    def validate_wrc_srcip_srcip(self) -> bool:
        # Type check
        if not isinstance(self.get_wrc_srcip_srcip(), str):
            return False
        # Allowed values check
        return validations.is_ip_address(string=self.get_wrc_srcip_srcip())

    @staticmethod
    def get_wrc_srcip_srcip_allow_criteria():
        return "It must be a valid IPv4 or IPv6 ip address, given as a string."

    def set_wrc_srcip_srcip(self, srcip : str):
        self.srcip = srcip
        if self.validate_wrc_srcip_srcip():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f'- Inside <wazuh_rule_config>, <freq_srcip> of node {self.relative_node_name} has been succesfully set to {srcip}')
        else:
            ExitUtils.exit_with_error(f'You cannot set <freq_srcip> of node {self.relative_node_name} to {srcip} of type {type(srcip)}. {Srcip.get_wrc_srcip_srcip_allow_criteria()}')

    # ============================================
    # Validate All
    # ============================================

    def validate_all(self):
        error_prefix = f"The node {self.relative_node_name} failed validation on"
        error_suffix = f"was given instead."
        if not self.validate_wrc_srcip_negate():
            ExitUtils.exit_with_error(f'{error_prefix} <srcip negate="{self.get_wrc_srcip_negate()}"> in <wazuh_rule_config>. {Srcip.get_wrc_srcip_negate_allow_criteria()} {self.srcip} of type {type(self.srcip)} {error_suffix}')
        if not self.validate_wrc_srcip_srcip():
            ExitUtils.exit_with_error(f'{error_prefix} <srcip> in <wazuh_rule_config>. {Srcip.get_wrc_srcip_srcip_allow_criteria()} {self.get_wrc_srcip_srcip()} of type {type(self.get_wrc_srcip_srcip())} {error_suffix}')
        #PrintUtils.print_in_green(f"- Validation of a <regex> related to {self.relative_node_name} was succesful!")

    # ============================================
    # Print
    # ============================================

    def to_string(self):
        print(f'<srcip negate="{self.get_wrc_srcip_negate()}">{self.get_wrc_srcip_srcip()}</srcip>')



def test():
    f = Srcip()
    f.validate_all()
    f.to_string()



if __name__ == '__main__':
    test()