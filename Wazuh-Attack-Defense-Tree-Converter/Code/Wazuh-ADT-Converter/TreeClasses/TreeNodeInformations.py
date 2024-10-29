import validations
from typing import List

# Support classes import
from WazuhRuleConfig import WazuhRuleConfig

# Import scripts from above folder
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from terminal_UI_utils import PrintUtils, ExitUtils


'''
How to add an extra tag?

1) Add it in the __init__ args
2) Add self.tag_name = tag_name in __init__
3) Define the 4 operations: get, validate, get_allowed_criteria, set
4) Add in validate_all() following the syntax of the others
'''


class TreeNodeInformations:
    '''
    This class represents all the informations that an ADT node has.
    Practically: the xml tags of it.
    '''
    print_diagnostics = True
    # This has way too many arguments...
    def __init__(self,
                node_conjuncted_children: str = "no",  # Default value
                node_root               : str = "no",  # Default value
                node_type               : str = "atk", # Default value
                path                    : str = "", # MUST be changed to a valid path, so it must end with a /. It's up to you to build it correctly, obviously!
                id                      : int = -1, # MUST be changed
                name                    : str = "undefined", # SHOULD be changed
                wazuh_rule_config       : WazuhRuleConfig = None, # MUST be changed
                ):
        
        # <node conjuncted_children="" root="" type=""
        self.node_tag_attributes = {
            "conjuncted_children" : node_conjuncted_children ,
            "root" : node_root ,
            "type" : node_type
        }

        # <path>
        self.path = path
        # <id>
        self.id = id
        # <name>
        self.name = name

        # <wazuh_rule_config>
        self.wazuh_rule_config = wazuh_rule_config

    # ============================================
    # <node conjuncted_children=""> operations
    # ============================================

    def get_conjuncted_children(self) -> str:
        return self.node_tag_attributes["conjuncted_children"]
    
    def validate_node_conjuncted_children(self) -> bool:
        # Type check
        if not isinstance(self.node_tag_attributes["conjuncted_children"], str):
            return False
        # Allowed values check
        return validations.is_yes_or_no(self.get_conjuncted_children())
    
    @staticmethod
    def get_conjuncted_children_allow_criteria() -> str:
        return "It must be 'yes' or 'no'."

    def set_conjuncted_children(self, conjuncted_children : str):
        self.node_tag_attributes["conjuncted_children"] = conjuncted_children
        if self.validate_node_conjuncted_children():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f"- conjuncted_children of node {self.get_name()} with id {self.get_id()} has been succesfully set to {conjuncted_children}")
        else:
            ExitUtils.exit_with_error(f"You cannot set conjuncted_children of node {self.get_name()} with id {self.get_id()} to {conjuncted_children}  of type {type(conjuncted_children)}. {TreeNodeInformations.get_conjuncted_children_allow_criteria()}")

    # ============================================
    # <node root=""> operations
    # ============================================
    
    def get_root(self) -> str:
        return self.node_tag_attributes["root"]

    def validate_node_root(self) -> bool:
        # Type check
        if not isinstance(self.node_tag_attributes["root"], str):
            return False
        # Allowed values check
        return validations.is_yes_or_no(self.node_tag_attributes["root"])

    @staticmethod
    def get_root_allow_criteria() -> str:
        return "It must be 'yes' or 'no'."

    def set_root(self, root : str):
        self.node_tag_attributes["root"] = root
        if self.validate_node_root():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f"- root of node {self.get_name()} with id {self.get_id()} has been succesfully set to {root}")
        else:
            ExitUtils.exit_with_error(f'You cannot set <node root=""> of node {self.get_name()} with id {self.get_id()} to {root} of type {type(root)}. {TreeNodeInformations.get_root_allow_criteria()}')
    

    # ============================================
    # <node type=""> operations
    # ============================================
    
    def get_type(self) -> str:
        return self.node_tag_attributes["type"]

    def validate_node_type(self) -> bool:
        # Type check
        if not isinstance(self.node_tag_attributes["type"], str):
            return False
        # Allowed values check
        allowed_values = ["atk", "def"]
        return validations.is_allowed(allowed_values=allowed_values, string=self.get_type())

    @staticmethod
    def get_type_allow_criteria() -> str:
        return "It must be 'atk' or 'def'."

    def set_type(self, type_ : str):
        self.node_tag_attributes["type"] = type_
        if self.validate_node_type():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f"- type of node {self.get_name()} with id {self.get_id()} has been succesfully set to {type_}")
        else:
            ExitUtils.exit_with_error(f'You cannot set <node type="" of node {self.get_name()} with id {self.get_id()} to {type_} of type {type(type_)}. {TreeNodeInformations.get_type_allow_criteria()}')



    # ============================================
    # <path> operations
    # ============================================

    def get_path(self) -> str:
        return self.path

    def validate_path(self) -> bool:
        # Type check
        if not isinstance(self.path, str):
            return False
        self.path = str(self.path) # Just to color the endswith() method. Yes.
        # Check if it ends with a /, basically that's the check we need. The existence of the path cannot be checked here.
        return self.get_path().endswith(r"/")

    @staticmethod
    def get_path_allow_criteria() -> str:
        return "It must end with a / ."

    def set_path(self, path : str):
        self.path = path
        if self.validate_path():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f"- <path> of node {self.get_name()} with id {self.get_id()} has been succesfully set to {path}")
        else:
            ExitUtils.exit_with_error(f"You cannot set <path> of node {self.get_name()} with id {self.get_id()} to {path} of type {type(path)}. {TreeNodeInformations.get_path_allow_criteria()}")


    # ============================================
    # <id> operations
    # ============================================

    def get_id(self) -> int:
        return self.id

    def validate_id(self) -> bool:
        return isinstance(self.get_id(), int) and self.get_id() >= 0

    @staticmethod
    def get_id_allow_criteria() -> str:
        return "It must be a positive integer."

    def set_id(self, id : int):
        self.id = id
        if self.validate_id():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f"- <id> of node {self.get_name()} with id {self.get_id()} has been succesfully set to {id}")
        else:
            ExitUtils.exit_with_error(f"You cannot set <id> of node {self.get_name()} with id {self.get_id()} to {id} of type {type(id)}. {TreeNodeInformations.get_id_allow_criteria()}")


    # ============================================
    # <name> operations
    # ============================================

    def get_name(self) -> str:
        return self.name

    def validate_name(self) -> bool:
        # Type check
        return isinstance(self.get_name(), str)

    @staticmethod
    def get_name_allow_criteria() -> str:
        return "It must be a string."

    def set_name(self, name : str):
        self.name = name
        if self.validate_name():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f"- <name> of node {self.get_name()} with id {self.get_id()} has been succesfully set to {name}")
        else:
            ExitUtils.exit_with_error(f"You cannot set <name> of node {self.get_name()} with id {self.get_id()} to {name} of type {type(name)}. {TreeNodeInformations.get_name_allow_criteria()}")



    # ============================================
    # <wazuh_rule_config> operations
    # ============================================

    def get_wazuh_rule_config(self) -> WazuhRuleConfig:
        return self.wazuh_rule_config

    def validate_wazuh_rule_config(self) -> bool:
        if self.get_wazuh_rule_config() is None:
            return False
        self.get_wazuh_rule_config().validate_all()
        return True    

    @staticmethod
    def get_wrc_options_allow_criteria() -> str:
        return 'Every <options> tag must contain one of the following strings: "alert_by_email", "no_email_alert", "no_log", "no_full_log", "no_counter".'

    def set_wrc_options(self, options : str):
        self.wazuh_rule_config["options"] = options
        if self.validate_wrc_options():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, <options> of node {self.get_name()} with id {self.get_id()} has been succesfully set to {options}")
        # else: is covered inside of self.validate_wrc_options() already


    # ========================================================================================
    # Out of <wazuh_rule_config>
    # ========================================================================================

    # ============================================
    # Validate All Node Tags
    # ============================================   

    def validate_all(self) -> bool:
        error_prefix = f"The node {self.get_name()} with id {self.get_id()} failed validation on"
        error_suffix = f"was given instead."

        if not self.validate_node_conjuncted_children():
            ExitUtils.exit_with_error(f"{error_prefix} node attribute [conjuncted_children]. {TreeNodeInformations.get_conjuncted_children_allow_criteria()} {self.get_conjuncted_children()} of type {type(self.get_conjuncted_children())} {error_suffix}")
        
        if not self.validate_node_root():
            ExitUtils.exit_with_error(f"{error_prefix} node attribute [root]. {TreeNodeInformations.get_root_allow_criteria()} {self.get_root()} of type {type(self.get_root())} {error_suffix}")
        
        if not self.validate_node_type():
            ExitUtils.exit_with_error(f"{error_prefix} node attribute [type]. {TreeNodeInformations.get_type_allow_criteria()} {self.get_type()} of type {type(self.get_type())} {error_suffix}")
        
        if not self.validate_path():
            ExitUtils.exit_with_error(f"{error_prefix} <path>. {TreeNodeInformations.get_path_allow_criteria()} {self.get_path()} of type {type(self.get_path())} {error_suffix}")
        
        if not self.validate_id():
            ExitUtils.exit_with_error(f"{error_prefix} <id>. {TreeNodeInformations.get_id_allow_criteria()} {self.get_id()} of type {type(self.get_id())} {error_suffix}")
        
        if not self.validate_name():
            ExitUtils.exit_with_error(f"{error_prefix} <name>. {TreeNodeInformations.get_name_allow_criteria()} {self.get_name()} of type {type(self.get_name())} {error_suffix}")
        
        if not self.validate_wrc_frequency():
            ExitUtils.exit_with_error(f"{error_prefix} <frequency> in <wazuh_rule_config>. {TreeNodeInformations.get_wrc_frequency_allow_criteria()} {self.get_wrc_frequency()} of type {type(self.get_wrc_frequency())} {error_suffix}")
        
        if not self.validate_wrc_timeframe():
            ExitUtils.exit_with_error(f"{error_prefix} <timeframe> in <wazuh_rule_config>. {TreeNodeInformations.get_wrc_timeframe_allow_criteria()} {self.get_wrc_timeframe()} of type {type(self.get_wrc_timeframe())} {error_suffix}")
        
        if not self.validate_wrc_ignore():
        
            ExitUtils.exit_with_error(f"{error_prefix} <ignore_after> in <wazuh_rule_config>. {TreeNodeInformations.get_wrc_ignore_allow_criteria()} {self.get_wrc_ignore()} of type {type(self.get_wrc_ignore())} {error_suffix}")
        
        if not self.validate_wrc_already_existing_id():
            ExitUtils.exit_with_error(f"{error_prefix} <already_existing_id> in <wazuh_rule_config>. {TreeNodeInformations.get_wrc_already_existing_id_allow_criteria()} {self.get_wrc_already_existing_id()} of type {type(self.get_wrc_already_existing_id())} {error_suffix}")
        
        self.validate_wrc_match()

        self.validate_wrc_regex()

        self.validate_wrc_srcip()

        self.validate_wrc_dstip()

        self.validate_wrc_srcport()

        self.validate_wrc_dstport()

        if not self.validate_wrc_time():
            ExitUtils.exit_with_error(f"{error_prefix} <time> in <wazuh_rule_config>. {TreeNodeInformations.get_wrc_time_allow_criteria()} {self.get_wrc_time()} of type {type(self.get_wrc_time())} {error_suffix}")

        if not self.validate_wrc_weekday():
            ExitUtils.exit_with_error(f"{error_prefix} <weekday> in <wazuh_rule_config>. {TreeNodeInformations.get_wrc_weekday_allow_criteria()} {self.get_wrc_weekday()} of type {type(self.get_wrc_weekday())} {error_suffix}")

        if not self.validate_wrc_same_srcip():
            ExitUtils.exit_with_error(f"{error_prefix} <freq_same_srcip> in <wazuh_rule_config>. {TreeNodeInformations.get_wrc_same_srcip_allow_criteria()} {self.get_wrc_same_srcip()} of type {type(self.get_wrc_same_srcip())} {error_suffix}")
  
        if not self.validate_wrc_different_srcip():
            ExitUtils.exit_with_error(f"{error_prefix} <freq_different_srcip> in <wazuh_rule_config>. {TreeNodeInformations.get_wrc_different_srcip_allow_criteria()} {self.get_wrc_different_srcip()} of type {type(self.get_wrc_different_srcip())} {error_suffix}")

        if not self.validate_wrc_same_srcport():
            ExitUtils.exit_with_error(f"{error_prefix} <freq_same_srcport> in <wazuh_rule_config>. {TreeNodeInformations.get_wrc_same_srcport_allow_criteria()} {self.get_wrc_same_srcport()} of type {type(self.get_wrc_same_srcport())} {error_suffix}")
    
        if not self.validate_wrc_different_srcport():
            ExitUtils.exit_with_error(f"{error_prefix} <freq_different_srcport> in <wazuh_rule_config>. {TreeNodeInformations.get_wrc_different_srcport_allow_criteria()} {self.get_wrc_different_srcport()} of type {type(self.get_wrc_different_srcport())} {error_suffix}")
   
        if not self.validate_wrc_same_location():
            ExitUtils.exit_with_error(f"{error_prefix} <freq_same_location> in <wazuh_rule_config>. {TreeNodeInformations.get_wrc_same_location_allow_criteria()} {self.get_wrc_same_location()} of type {type(self.get_wrc_same_location())} {error_suffix}")
   
        if not self.validate_wrc_same_srcuser():
            ExitUtils.exit_with_error(f"{error_prefix} <freq_same_srcuser> in <wazuh_rule_config>. {TreeNodeInformations.get_wrc_same_srcuser_allow_criteria()} {self.get_wrc_same_srcuser()} of type {type(self.get_wrc_same_srcuser())} {error_suffix}")
   
        if not self.validate_wrc_different_srcuser():
            ExitUtils.exit_with_error(f"{error_prefix} <freq_different_srcuser> in <wazuh_rule_config>. {TreeNodeInformations.get_wrc_different_srcuser_allow_criteria()} {self.get_wrc_different_srcuser()} of type {type(self.get_wrc_different_srcuser())} {error_suffix}")
   
        if not self.validate_wrc_description():
            ExitUtils.exit_with_error(f"{error_prefix} <description> in <wazuh_rule_config>. {TreeNodeInformations.get_wrc_description_allow_criteria()} {self.get_wrc_description()} of type {type(self.get_wrc_description())} {error_suffix}")
   
        self.validate_wrc_info()

        self.validate_wrc_options()

    # ============================================
    # General to_string
    # ============================================   

    def to_string(self):
        '''
        Method that returns a stringified version of the whole node.
        This is what will compose the rule itself.
        '''

        to_string = ''





