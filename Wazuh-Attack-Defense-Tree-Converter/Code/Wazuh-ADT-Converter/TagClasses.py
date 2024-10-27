import validations
from terminal_UI_utils import PrintUtils, ExitUtils
from typing import List

class Match:
    
    print_diagnostics = True

    def __init__(self, 
                 negate : str = "no", 
                 type   : str = "osmatch", 
                 match  : str = None, #Set this to None by default because it is not mandatory and can be omitted
                 relative_node_name : str = "unspecified" #Useful for prints
                ):
        self.negate = negate
        self.type = type
        self.match = match
        self.relative_node_name = relative_node_name

    # ============================================
    # <match negate=""> operations
    # ============================================
    
    def get_wrc_match_negate(self) -> str:
        return self.negate

    def validate_wrc_match_negate(self) -> bool:
        # Type check
        if not isinstance(self.negate, str):
            return False
        # Allowed values check
        return validations.is_yes_or_no(self.negate)

    @staticmethod
    def get_wrc_match_negate_allow_criteria():
        return "It must be 'yes' or 'no'."

    def set_wrc_match_negate(self, negate : int):
        self.negate = negate
        if self.validate_wrc_match_negate():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f'- Inside <wazuh_rule_config>, <match negate=""> of node {self.relative_node_name} has been succesfully set to {negate}')
        else:
            ExitUtils.exit_with_error(f'You cannot set <match negate=""> of node {self.relative_node_name} to {negate}. {Match.get_wrc_match_negate_allow_criteria()}')


    # ============================================
    # <match type=""> operations
    # ============================================
    
    def get_wrc_match_type(self) -> str:
        return self.type

    def validate_wrc_match_type(self) -> bool:
        # Type check
        if not isinstance(self.type, str):
            return False
        # Allowed values check
        return validations.is_osmatch_osregex_pcre2(self.type)

    @staticmethod
    def get_wrc_match_type_allow_criteria():
        return "It must be 'osmatch' or 'osregex' or 'pcre2'."

    def set_wrc_match_type(self, type : int):
        self.type = type
        if self.validate_wrc_match_type():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f'- Inside <wazuh_rule_config>, <match type=""> of node {self.relative_node_name} has been succesfully set to {type}')
        else:
            ExitUtils.exit_with_error(f'You cannot set <match type=""> of node {self.relative_node_name} to {type}. {Match.get_wrc_match_type_allow_criteria()}')


    # ============================================
    # <match> operations
    # ============================================
    
    def get_wrc_match_match(self) -> str:
        return self.match

    def validate_wrc_match_match(self) -> bool:
        # Type check
        if not (self.match is None or isinstance(self.match, str) ):
            return False
        return True

    @staticmethod
    def get_wrc_match_match_allow_criteria():
        return "It must be a string."

    def set_wrc_match_match(self, match : int):
        self.match = match
        if self.validate_wrc_match_match():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, <match> of node {self.relative_node_name} has been succesfully set to {match}")
        else:
            ExitUtils.exit_with_error(f"You cannot set <match> of node {self.relative_node_name} to {match}. {Match.get_wrc_match_match_allow_criteria()}")

    # ============================================
    # Validate All
    # ============================================

    def validate_all(self):
        error_prefix = f"The node {self.relative_node_name} failed validation on"
        if not self.validate_wrc_match_negate():
            ExitUtils.exit_with_error(f'{error_prefix} <match negate="{self.get_wrc_match_negate()}"> in <wazuh_rule_config>. {Match.get_wrc_match_negate_allow_criteria()}')
        if not self.validate_wrc_match_type():
            ExitUtils.exit_with_error(f'{error_prefix} <match type="{self.get_wrc_match_type()}"> in <wazuh_rule_config>. {Match.get_wrc_match_type_allow_criteria()}')
        if not self.validate_wrc_match_match():
            ExitUtils.exit_with_error(f'{error_prefix} <match>{self.get_wrc_match_match()}</match> in <wazuh_rule_config>. {Match.get_wrc_match_match_allow_criteria()}')
        #PrintUtils.print_in_green(f"- Validation of a <match> related to {self.relative_node_name} was succesful!")

    # ============================================
    # Print
    # ============================================

    def to_string(self):
        print(f'<match negate="{self.get_wrc_match_negate()}" type="{self.get_wrc_match_type()}">{self.get_wrc_match_match()}</match>')











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

    def set_wrc_regex_negate(self, negate : int):
        self.negate = negate
        if self.validate_wrc_regex_negate():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f'- Inside <wazuh_rule_config>, <regex negate=""> of node {self.relative_node_name} has been succesfully set to {negate}')
        else:
            ExitUtils.exit_with_error(f'You cannot set <regex negate=""> of node {self.relative_node_name} to {negate}. {Regex.get_wrc_regex_negate_allow_criteria()}')


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

    def set_wrc_regex_type(self, type : int):
        self.type = type
        if self.validate_wrc_regex_type():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f'- Inside <wazuh_rule_config>, <regex type=""> of node {self.relative_node_name} has been succesfully set to {type}')
        else:
            ExitUtils.exit_with_error(f'You cannot set <regex type=""> of node {self.relative_node_name} to {type}. {Regex.get_wrc_regex_type_allow_criteria()}')


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

    def set_wrc_regex_regex(self, regex : int):
        self.regex = regex
        if self.validate_wrc_regex_regex():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, <regex> of node {self.relative_node_name} has been succesfully set to {regex}")
        else:
            ExitUtils.exit_with_error(f"You cannot set <regex> of node {self.relative_node_name} to {regex}. {Regex.get_wrc_regex_regex_allow_criteria()}")

    # ============================================
    # Validate All
    # ============================================

    def validate_all(self):
        error_prefix = f"The node {self.relative_node_name} failed validation on"
        if not self.validate_wrc_regex_negate():
            ExitUtils.exit_with_error(f'{error_prefix} <regex negate="{self.get_wrc_regex_negate()}"> in <wazuh_rule_config>. {Regex.get_wrc_regex_negate_allow_criteria()}')
        if not self.validate_wrc_regex_type():
            ExitUtils.exit_with_error(f'{error_prefix} <regex type="{self.get_wrc_regexh_type()}"> in <wazuh_rule_config>. {Regex.get_wrc_regex_type_allow_criteria()}')
        if not self.validate_wrc_regex_regex():
            ExitUtils.exit_with_error(f'{error_prefix} <regex>{self.get_wrc_regex_regex()}</regex> in <wazuh_rule_config>. {Regex.get_wrc_regex_regex_allow_criteria()}')
        #PrintUtils.print_in_green(f"- Validation of a <regex> related to {self.relative_node_name} was succesful!")

    # ============================================
    # Print
    # ============================================

    def to_string(self):
        print(f'<regex negate="{self.get_wrc_regex_negate()}" type="{self.get_wrc_regex_type()}">{self.get_wrc_regex_regex()}</regex>')






