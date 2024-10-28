import validations

# Import scripts from above folder
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from terminal_UI_utils import PrintUtils, ExitUtils

class Regex:
    
    print_diagnostics = True

    def __init__(self, 
                 negate : str = "no", 
                 type   : str = "osregex", 
                 regex  : str = None, #Set this to None by default because it is not mandatory and can be omitted
                 relative_node_name : str = "unspecified" #Useful for prints
                ):
        self.negate = negate
        self.type = type
        self.regex = regex
        self.relative_node_name = relative_node_name

    # ============================================
    # <regex negate=""> operations
    # ============================================
    
    def get_wrc_regex_negate(self) -> str:
        return self.negate

    def validate_wrc_regex_negate(self) -> bool:
        # Type check
        if not isinstance(self.negate, str):
            return False
        # Allowed values check
        return validations.is_yes_or_no(self.negate)

    @staticmethod
    def get_wrc_regex_negate_allow_criteria():
        return "It must be 'yes' or 'no'."

    def set_wrc_regex_negate(self, negate : str):
        self.negate = negate
        if self.validate_wrc_regex_negate():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f'- Inside <wazuh_rule_config>, <regex negate=""> of node {self.relative_node_name} has been succesfully set to {negate}')
        else:
            ExitUtils.exit_with_error(f'You cannot set <regex negate=""> of node {self.relative_node_name} to {negate} of type {type(negate)}. {Regex.get_wrc_regex_negate_allow_criteria()}')


    # ============================================
    # <regex type=""> operations
    # ============================================
    
    def get_wrc_regex_type(self) -> str:
        return self.type

    def validate_wrc_regex_type(self) -> bool:
        # Type check
        if not isinstance(self.type, str):
            return False
        # Allowed values check
        return validations.is_osmatch_osregex_pcre2(self.type)

    @staticmethod
    def get_wrc_regex_type_allow_criteria():
        return "It must be 'osmatch' or 'osregex' or 'pcre2'."

    def set_wrc_regex_type(self, type_ : str):
        self.type = type_
        if self.validate_wrc_regex_type():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f'- Inside <wazuh_rule_config>, <regex type=""> of node {self.relative_node_name} has been succesfully set to {type_}')
        else:
            ExitUtils.exit_with_error(f'You cannot set <regex type=""> of node {self.relative_node_name} to {type_} of type {type(type_)}. {Regex.get_wrc_regex_type_allow_criteria()}')


    # ============================================
    # <regex> operations
    # ============================================
    
    def get_wrc_regex_regex(self) -> str:
        return self.regex

    def validate_wrc_regex_regex(self) -> bool:
        # Type check
        if not (self.regex is None or isinstance(self.regex, str) ):
            return False
        return True

    @staticmethod
    def get_wrc_regex_regex_allow_criteria():
        return "It must be a string."

    def set_wrc_regex_regex(self, regex : str):
        self.regex = regex
        if self.validate_wrc_regex_regex():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, <regex> of node {self.relative_node_name} has been succesfully set to {regex}")
        else:
            ExitUtils.exit_with_error(f"You cannot set <regex> of node {self.relative_node_name} to {regex} of type {type(regex)}. {Regex.get_wrc_regex_regex_allow_criteria()}")

    # ============================================
    # Validate All
    # ============================================

    def validate_all(self):
        error_prefix = f"The node {self.relative_node_name} failed validation on"
        error_suffix = f"was given instead."

        if not self.validate_wrc_regex_negate():
            ExitUtils.exit_with_error(f'{error_prefix} <regex negate="{self.get_wrc_regex_negate()}"> in <wazuh_rule_config>. {Regex.get_wrc_regex_negate_allow_criteria()} {self.get_wrc_regex_negate()} of type {type(self.get_wrc_regex_negate())} {error_suffix}')
        if not self.validate_wrc_regex_type():
            ExitUtils.exit_with_error(f'{error_prefix} <regex type="{self.get_wrc_regex_type()}"> in <wazuh_rule_config>. {Regex.get_wrc_regex_type_allow_criteria()} {self.get_wrc_regex_negate()} of type {type(self.get_wrc_regex_negate())} {error_suffix}')
        if not self.validate_wrc_regex_regex():
            ExitUtils.exit_with_error(f'{error_prefix} <regex>{self.get_wrc_regex_regex()}</regex> in <wazuh_rule_config>. {Regex.get_wrc_regex_regex_allow_criteria()} {self.get_wrc_regex_regex()} of type {type(self.get_wrc_regex_regex())} {error_suffix}')
        #PrintUtils.print_in_green(f"- Validation of a <regex> related to {self.relative_node_name} was succesful!")

    # ============================================
    # Print
    # ============================================

    def to_string(self):
        print(f'<regex negate="{self.get_wrc_regex_negate()}" type="{self.get_wrc_regex_type()}">{self.get_wrc_regex_regex()}</regex>')




def test():
    r = Regex()
    r.validate_all()
    r.to_string()



if __name__ == '__main__':
    test()