import validations
from typing import List

# Support classes import
from TreeClasses.WazuhRuleConfig import WazuhRuleConfig

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
                #node_type               : str = "atk", # Default value
                path                    : str = "", # MUST be changed to a valid path, so it must end with a /. It's up to you to build it correctly, obviously!
                id                      : int = -1, # MUST be changed
                name                    : str = "undefined", # SHOULD be changed
                wazuh_rule_config       : WazuhRuleConfig = WazuhRuleConfig(), # MUST be changed
                ):
        
        # <node conjuncted_children="" root="" type=""
        self.node_tag_attributes = {
            "conjuncted_children" : node_conjuncted_children ,
            "root" : node_root ,
            #"type" : node_type
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
    
    def validate_node_conjuncted_children_with_error_launch(self):
        if not self.validate_node_conjuncted_children():
            error_prefix = f"The node {self.get_name()} with id {self.get_id()} failed validation on"
            error_suffix = f"was given instead."
            ExitUtils.exit_with_error(f"{error_prefix} node attribute [conjuncted_children]. {TreeNodeInformations.get_conjuncted_children_allow_criteria()} {self.get_conjuncted_children()} of type {type(self.get_conjuncted_children())} {error_suffix}")

    @staticmethod
    def get_conjuncted_children_allow_criteria() -> str:
        return "It must be 'yes' or 'no'."

    def set_conjuncted_children(self, conjuncted_children : str):
        self.node_tag_attributes["conjuncted_children"] = conjuncted_children

        self.validate_node_conjuncted_children_with_error_launch()

        if self.print_diagnostics:
            PrintUtils.print_in_green(f"- conjuncted_children of node {self.get_name()} with id {self.get_id()} has been succesfully set to {conjuncted_children}")

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

    def validate_node_root_with_error_launch(self):
        if not self.validate_node_root():
            error_prefix = f"The node {self.get_name()} with id {self.get_id()} failed validation on"
            error_suffix = f"was given instead."
            ExitUtils.exit_with_error(f"{error_prefix} node attribute [root]. {TreeNodeInformations.get_root_allow_criteria()} {self.get_root()} of type {type(self.get_root())} {error_suffix}")


    @staticmethod
    def get_root_allow_criteria() -> str:
        return "It must be 'yes' or 'no'."

    def set_root(self, root : str):
        self.node_tag_attributes["root"] = root

        self.validate_node_root_with_error_launch()

        if self.print_diagnostics:
            PrintUtils.print_in_green(f"- root of node {self.get_name()} with id {self.get_id()} has been succesfully set to {root}")

    '''
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

    def validate_node_type_with_error_launch(self):
        if not self.validate_node_type():
            error_prefix = f"The node {self.get_name()} with id {self.get_id()} failed validation on"
            error_suffix = f"was given instead."
            ExitUtils.exit_with_error(f"{error_prefix} node attribute [type]. {TreeNodeInformations.get_type_allow_criteria()} {self.get_type()} of type {type(self.get_type())} {error_suffix}")

    @staticmethod
    def get_type_allow_criteria() -> str:
        return "It must be 'atk' or 'def'."

    def set_type(self, type_ : str):
        self.node_tag_attributes["type"] = type_

        self.validate_node_type_with_error_launch()

        if self.print_diagnostics:
            PrintUtils.print_in_green(f"- type of node {self.get_name()} with id {self.get_id()} has been succesfully set to {type_}")
    '''
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

    def validate_path_with_error_launch(self):
        if not self.validate_path():
            error_prefix = f"The node {self.get_name()} with id {self.get_id()} failed validation on"
            error_suffix = f"was given instead."
            ExitUtils.exit_with_error(f"{error_prefix} <path>. {TreeNodeInformations.get_path_allow_criteria()} {self.get_path()} of type {type(self.get_path())} {error_suffix}")

    @staticmethod
    def get_path_allow_criteria() -> str:
        return "It must end with a / ."

    def set_path(self, path : str):
        self.path = path
    
        self.validate_path_with_error_launch()

        if self.print_diagnostics:
            PrintUtils.print_in_green(f"- <path> of node {self.get_name()} with id {self.get_id()} has been succesfully set to {path}")


    # ============================================
    # <id> operations
    # ============================================

    def get_id(self) -> int:
        return self.id

    def validate_id(self) -> bool:
        return isinstance(self.get_id(), int) and self.get_id() >= 0

    def validate_id_with_error_launch(self):
        if not self.validate_id():
            error_prefix = f"The node {self.get_name()} with id {self.get_id()} failed validation on"
            error_suffix = f"was given instead."
            ExitUtils.exit_with_error(f"{error_prefix} <id>. {TreeNodeInformations.get_id_allow_criteria()} {self.get_id()} of type {type(self.get_id())} {error_suffix}")
        
    @staticmethod
    def get_id_allow_criteria() -> str:
        return "It must be a positive integer."

    def set_id(self, id : int):
        self.id = id

        self.validate_id_with_error_launch()

        if self.print_diagnostics:
            PrintUtils.print_in_green(f"- <id> of node {self.get_name()} with id {self.get_id()} has been succesfully set to {id}")


    # ============================================
    # <name> operations
    # ============================================

    def get_name(self) -> str:
        return self.name

    def validate_name(self) -> bool:
        # Type check
        return isinstance(self.get_name(), str)

    def validate_name_with_error_launch(self):
        if not self.validate_name():
            error_prefix = f"The node {self.get_name()} with id {self.get_id()} failed validation on"
            error_suffix = f"was given instead."
            ExitUtils.exit_with_error(f"{error_prefix} <name>. {TreeNodeInformations.get_name_allow_criteria()} {self.get_name()} of type {type(self.get_name())} {error_suffix}")

    @staticmethod
    def get_name_allow_criteria() -> str:
        return "It must be a string."

    def set_name(self, name : str):
        self.name = name

        self.validate_name_with_error_launch()

        if self.print_diagnostics:
            PrintUtils.print_in_green(f"- <name> of node {self.get_name()} with id {self.get_id()} has been succesfully set to {name}")


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

    def set_wazuh_rule_config(self, wrc : WazuhRuleConfig):
        self.wazuh_rule_config = wrc
        if self.validate_wazuh_rule_config():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f"- <wazuh_rule_config> of node {self.get_name()} with id {self.get_id()} has been succesfully set to {wrc}")
        # else: is covered inside of self.validate_wrc_options() already


    # ========================================================================================
    # Out of <wazuh_rule_config>
    # ========================================================================================

    # ============================================
    # Validate All Node Tags
    # ============================================   

    def validate_all(self) -> bool:

        self.validate_node_conjuncted_children_with_error_launch()
                    
        self.validate_node_root_with_error_launch()
                    
        #self.validate_node_type_with_error_launch()
            
        self.validate_path_with_error_launch()
            
        self.validate_id_with_error_launch()
            
        self.validate_name_with_error_launch()
            
        self.validate_wazuh_rule_config()

        # if node is root, it must have path = '/'

        if self.get_root() == "yes" and self.get_path() != '/':
            error_prefix = f"The node {self.get_name()} with id {self.get_id()} failed validation on"
            ExitUtils.exit_with_error(f'{error_prefix} <node root="yes"> and <path> together.\nIf root is set to "yes", the path MUST be / by definition.')
            

    # ============================================
    # General to_string
    # ============================================   

    def to_string(self, tab_times : int = 0) -> str:
        '''
        Method that returns a stringified version of the informations of the node.
        This is what will compose the rule itself.

        Let's be clear: it is just composed of the entries of wazuh_rule_config.
        '''

        return self.get_wazuh_rule_config().to_string(tab_times=tab_times)

    def to_string_raw(self) -> str:
        attributes = "\n".join(f"{key}: {value}" for key, value in vars(self).items() if key != 'wazuh_rule_config')
        attributes += '\nwazuh_rule_config:\n'
        attributes += self.get_wazuh_rule_config().to_string(tab_times=1)
        return f"(\n{attributes}\n)"



