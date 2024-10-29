import validations

# Import scripts from above folder
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from terminal_UI_utils import PrintUtils, ExitUtils


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
        if not isinstance(self.get_wrc_match_negate(), str):
            return False
        # Allowed values check
        return validations.is_yes_or_no(self.get_wrc_match_negate())

    def validate_wrc_match_negate_with_error_launch(self):
        if not self.validate_wrc_match_negate():
            error_prefix = f"The node {self.relative_node_name} failed validation on"
            error_suffix = f"was given instead."
            ExitUtils.exit_with_error(f'{error_prefix} <match negate="{self.get_wrc_match_negate()}"> in <wazuh_rule_config>. {Match.get_wrc_match_negate_allow_criteria()} {self.get_wrc_match_negate()} of type {type(self.get_wrc_match_negate())} {error_suffix}')

    @staticmethod
    def get_wrc_match_negate_allow_criteria() -> str:
        return "It must be 'yes' or 'no'."

    def set_wrc_match_negate(self, negate : str):
        self.negate = negate
        self.validate_wrc_match_negate_with_error_launch()
        if self.print_diagnostics:
            PrintUtils.print_in_green(f'- Inside <wazuh_rule_config>, <match negate=""> of node {self.relative_node_name} has been succesfully set to {negate}')

    # ============================================
    # <match type=""> operations
    # ============================================
    
    def get_wrc_match_type(self) -> str:
        return self.type

    def validate_wrc_match_type(self) -> bool:
        # Type check
        if not isinstance(self.get_wrc_match_type(), str):
            return False
        # Allowed values check
        return validations.is_osmatch_osregex_pcre2(self.get_wrc_match_type())

    def validate_wrc_match_type_with_error_launch(self):
        if not self.validate_wrc_match_type():
            error_prefix = f"The node {self.relative_node_name} failed validation on"
            error_suffix = f"was given instead."
            ExitUtils.exit_with_error(f'{error_prefix} <match type="{self.get_wrc_match_type()}"> in <wazuh_rule_config>. {Match.get_wrc_match_type_allow_criteria()} {self.get_wrc_match_type()} of type {type(self.get_wrc_match_type())} {error_suffix}')
        

    @staticmethod
    def get_wrc_match_type_allow_criteria() -> str:
        return "It must be 'osmatch' or 'osregex' or 'pcre2'."

    def set_wrc_match_type(self, type_ : str):
        self.type = type_
        self.validate_wrc_match_type_with_error_launch()
        if self.print_diagnostics:
            PrintUtils.print_in_green(f'- Inside <wazuh_rule_config>, <match type=""> of node {self.relative_node_name} has been succesfully set to {type_}')


    # ============================================
    # <match> operations
    # ============================================
    
    def get_wrc_match_match(self) -> str:
        return self.match

    def validate_wrc_match_match(self) -> bool:
        # Type check
        if not (self.get_wrc_match_match() is None or isinstance(self.get_wrc_match_match(), str) ):
            return False
        return True

    def validate_wrc_match_match_with_error_launch(self):
        if not self.validate_wrc_match_match():
            error_prefix = f"The node {self.relative_node_name} failed validation on"
            error_suffix = f"was given instead."
            ExitUtils.exit_with_error(f'{error_prefix} <match>{self.get_wrc_match_match()}</match> in <wazuh_rule_config>. {Match.get_wrc_match_match_allow_criteria()} {self.get_wrc_match_match()} of type {type(self.get_wrc_match_match())} {error_suffix}')
        

    @staticmethod
    def get_wrc_match_match_allow_criteria() -> str:
        return "It must be a string."

    def set_wrc_match_match(self, match : str):
        self.match = match

        self.validate_wrc_match_match_with_error_launch()

        if self.print_diagnostics:
            PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, <match> of node {self.relative_node_name} has been succesfully set to {match}")


    # ============================================
    # Validate All
    # ============================================

    def validate_all(self):
        
        self.validate_wrc_match_negate_with_error_launch()
        
        self.validate_wrc_match_type_with_error_launch()
            
        self.validate_wrc_match_match_with_error_launch()
           
        #PrintUtils.print_in_green(f"- Validation of a <match> related to {self.relative_node_name} was succesful!")

    # ============================================
    # Print
    # ============================================

    def to_string(self):
        print(f'<match negate="{self.get_wrc_match_negate()}" type="{self.get_wrc_match_type()}">{self.get_wrc_match_match()}</match>')



def test():
    m = Match()
    m.validate_all()
    m.to_string()



if __name__ == '__main__':
    test()