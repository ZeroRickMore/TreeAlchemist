import validations

# Import scripts from above folder
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from terminal_UI_utils import PrintUtils, ExitUtils

class Dstip:
    
    print_diagnostics = True

    def __init__(self, 
                 negate : str = "no", 
                 dstip  : str = None, #Set this to None by default because it is not mandatory and can be omitted
                 relative_node_name : str = "unspecified" #Useful for prints
                ):
        self.negate = negate
        self.dstip = dstip
        self.relative_node_name = relative_node_name

    # ============================================
    # <dstip negate=""> operations
    # ============================================
    
    def get_wrc_dstip_negate(self) -> str:
        return self.negate

    def validate_wrc_dstip_negate(self) -> bool:
        # Type check
        if not isinstance(self.get_wrc_dstip_negate(), str):
            return False
        # Allowed values check
        return validations.is_yes_or_no(self.get_wrc_dstip_negate())

    @staticmethod
    def get_wrc_dstip_negate_allow_criteria():
        return "It must be 'yes' or 'no'."

    def set_wrc_dstip_negate(self, negate : str):
        self.negate = negate
        if self.validate_wrc_dstip_negate():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f'- Inside <wazuh_rule_config>, <dstip negate=""> of node {self.relative_node_name} has been succesfully set to {negate}')
        else:
            ExitUtils.exit_with_error(f'You cannot set <dstip negate=""> of node {self.relative_node_name} to {negate} of type {type(negate)}. {Dstip.get_wrc_dstip_negate_allow_criteria()}')


    # ============================================
    # <dstip> operations
    # ============================================
    
    def get_wrc_dstip_dstip(self) -> str:
        return self.dstip

    def validate_wrc_dstip_dstip(self) -> bool:
        # Type check
        if not isinstance(self.get_wrc_dstip_dstip(), str):
            return False
        # Allowed values check
        return validations.is_ip_address(string=self.get_wrc_dstip_dstip())

    @staticmethod
    def get_wrc_dstip_dstip_allow_criteria():
        return "It must be a valid IPv4 or IPv6 ip address, given as a string."

    def set_wrc_dstip_dstip(self, dstip : str):
        self.dstip = dstip
        if self.validate_wrc_dstip_dstip():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f'- Inside <wazuh_rule_config>, <dstip> of node {self.relative_node_name} has been succesfully set to {dstip}')
        else:
            ExitUtils.exit_with_error(f'You cannot set <dstip> of node {self.relative_node_name} to {dstip} of type {type(dstip)}. {Dstip.get_wrc_dstip_dstip_allow_criteria()}')

    # ============================================
    # Validate All
    # ============================================

    def validate_all(self):
        error_prefix = f"The node {self.relative_node_name} failed validation on"
        error_suffix = f"was given instead."

        if not self.validate_wrc_dstip_negate():
            ExitUtils.exit_with_error(f'{error_prefix} <dstip negate="{self.get_wrc_dstip_negate()}"> in <wazuh_rule_config>. {Dstip.get_wrc_dstip_negate_allow_criteria()} {self.get_wrc_dstip_negate()} of type {type(self.get_wrc_dstip_negate())} {error_suffix}')
        if not self.validate_wrc_dstip_dstip():
            ExitUtils.exit_with_error(f'{error_prefix} <dstip> in <wazuh_rule_config>. {Dstip.get_wrc_dstip_dstip_allow_criteria()} {self.get_wrc_dstip_dstip()} of type {type(self.get_wrc_dstip_dstip())} {error_suffix}')
        #PrintUtils.print_in_green(f"- Validation of a <regex> related to {self.relative_node_name} was succesful!")

    # ============================================
    # Print
    # ============================================

    def to_string(self):
        print(f'<dstip negate="{self.get_wrc_dstip_negate()}">{self.get_wrc_dstip_dstip()}</dstip>')



def test():
    f = Dstip()
    f.to_string()
    f.validate_all()
    


if __name__ == '__main__':
    test()