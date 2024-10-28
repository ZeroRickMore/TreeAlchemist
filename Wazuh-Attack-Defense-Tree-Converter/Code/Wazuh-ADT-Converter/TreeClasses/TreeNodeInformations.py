import validations
from typing import List

# Support classes import
from Match import Match
from Regex import Regex
from FreqSrcip import FreqSrcip
from FreqDstip import FreqDstip
from FreqSrcport import FreqSrcport
from FreqDstport import FreqDstport

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
                node_conjuncted_children: str = "no", 
                node_root               : str = "no", 
                node_type               : str = "atk",
                path                    : str = "",
                id                      : int = -1,
                name                    : str = "N/A",
                wrc_frequency           : int = None, #Set this to None by default because it is not mandatory and can be omitted
                wrc_timeframe           : int = None, #Set this to None by default because it is not mandatory and can be omitted
                wrc_ignore_after        : int = None, #Set this to None by default because it is not mandatory and can be omitted
                wrc_already_existing_id : int = None, #Set this to None by default because it is not mandatory and can be omitted
                match_list              : List[Match] = None, #Set this to None by default because it is not mandatory and can be omitted
                regex_list              : List[Regex] = None, #Set this to None by default because it is not mandatory and can be omitted
                freq_srcip              : List[FreqSrcip] = None, #Set this to None by default because it is not mandatory and can be omitted
                freq_dstip              : List[FreqDstip] = None, #Set this to None by default because it is not mandatory and can be omitted
                freq_srcport            : List[FreqSrcport] = None, #Set this to None by default because it is not mandatory and can be omitted
                freq_dstport            : List[FreqDstport] = None, #Set this to None by default because it is not mandatory and can be omitted
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
        self.wazuh_rule_config = {
            "frequency"             :   wrc_frequency,
            "timeframe"             :   wrc_timeframe,
            "ignore"                :   wrc_ignore_after,
            "already_existing_id"   :   wrc_already_existing_id,
            "match"                 :   match_list,
            "regex"                 :   regex_list,
            "srcip"                 :   freq_srcip,
            "dstip"                 :   freq_dstip,
            "srcport"               :   freq_srcport,
            "dstport"               :   freq_dstport,
        }

        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def __repr__(self, level=0):
        # A string representation of the tree for easy visualization
        ret = "  " * level + f"{self.value}\n"
        for child in self.children:
            ret += child.__repr__(level + 1)
        return ret
    


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
        return validations.is_yes_or_no(self.node_tag_attributes["conjuncted_children"])
    
    @staticmethod
    def get_conjuncted_children_allow_criteria() -> str:
        return "It must be 'yes' or 'no'."

    def set_conjuncted_children(self, conjuncted_children : str):
        self.node_tag_attributes["conjuncted_children"] = conjuncted_children
        if self.validate_node_conjuncted_children():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f"- conjuncted_children of node {self.name} has been succesfully set to {conjuncted_children}")
        else:
            ExitUtils.exit_with_error(f"You cannot set conjuncted_children of node {self.name} with id {self.id} to {conjuncted_children}  of type {type(conjuncted_children)}. {TreeNodeInformations.get_conjuncted_children_allow_criteria()}")

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
                PrintUtils.print_in_green(f"- root of node {self.name} has been succesfully set to {root}")
        else:
            ExitUtils.exit_with_error(f'You cannot set <node root=""> of node {self.name} with id {self.id} to {root} of type {type(root)}. {TreeNodeInformations.get_root_allow_criteria()}')
    

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
        return validations.is_allowed(allowed_values=allowed_values, string=self.node_tag_attributes["type"])

    @staticmethod
    def get_type_allow_criteria() -> str:
        return "It must be 'atk' or 'def'."

    def set_type(self, type_ : str):
        self.node_tag_attributes["type"] = type_
        if self.validate_node_type():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f"- type of node {self.name} has been succesfully set to {type_}")
        else:
            ExitUtils.exit_with_error(f'You cannot set <node type="" of node {self.name} with id {self.id} to {type_} of type {type(type_)}. {TreeNodeInformations.get_type_allow_criteria()}')



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
        return self.path.endswith(r"/")

    @staticmethod
    def get_path_allow_criteria() -> str:
        return "It must end with a / ."

    def set_path(self, path : str):
        self.path = path
        if self.validate_path():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f"- <path> of node {self.name} has been succesfully set to {path}")
        else:
            ExitUtils.exit_with_error(f"You cannot set <path> of node {self.name} with id {self.id} to {path} of type {type(path)}. {TreeNodeInformations.get_path_allow_criteria()}")


    # ============================================
    # <id> operations
    # ============================================

    def get_id(self) -> int:
        return self.id

    def validate_id(self) -> bool:
        return isinstance(self.id, int) and self.id >= 0

    @staticmethod
    def get_id_allow_criteria() -> str:
        return "It must be a positive integer."

    def set_id(self, id : int):
        self.id = id
        if self.validate_id():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f"- <id> of node {self.name} has been succesfully set to {id}")
        else:
            ExitUtils.exit_with_error(f"You cannot set <id> of node {self.name} with id {self.id} to {id} of type {type(id)}. {TreeNodeInformations.get_id_allow_criteria()}")


    # ============================================
    # <name> operations
    # ============================================

    def get_name(self) -> str:
        return self.name

    def validate_name(self) -> bool:
        # Type check
        return isinstance(self.name, str)

    @staticmethod
    def get_name_allow_criteria() -> str:
        return "It must be a string."

    def set_name(self, name : str):
        self.name = name
        if self.validate_name():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f"- <name> of node {self.name} has been succesfully set to {name}")
        else:
            ExitUtils.exit_with_error(f"You cannot set <name> of node {self.name} with id {self.id} to {name} of type {type(name)}. {TreeNodeInformations.get_name_allow_criteria()}")



    # ========================================================================================
    # Inside of <wazuh_rule_config>
    # ========================================================================================


    # ============================================
    # <frequency> operations
    # ============================================

    def get_wrc_frequency(self) -> int:
        return self.wazuh_rule_config["frequency"]

    def validate_wrc_frequency(self) -> bool:
        return self.wazuh_rule_config["frequency"] is None or ( isinstance(self.wazuh_rule_config["frequency"], int) and ( self.wazuh_rule_config["frequency"] in range(2, 10000) ) )

    @staticmethod
    def get_wrc_frequency_allow_criteria() -> str:
        return "It must be an integer from 2 to 9999 ."

    def set_wrc_frequency(self, frequency : int):
        self.wazuh_rule_config["frequency"] = frequency
        if self.validate_wrc_frequency():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, <frequency> of node {self.name} has been succesfully set to {frequency}")
        else:
            ExitUtils.exit_with_error(f"You cannot set <frequency> of node {self.name} with id {self.id} to {frequency} of type {type(frequency)}. {TreeNodeInformations.get_wrc_frequency_allow_criteria()}")


    # ============================================
    # <timeframe> operations
    # ============================================
    
    def get_wrc_timeframe(self) -> int:
        return self.wazuh_rule_config["timeframe"]

    def validate_wrc_timeframe(self) -> bool:
        return self.wazuh_rule_config["timeframe"] is None or ( isinstance(self.wazuh_rule_config["timeframe"], int) and ( self.wazuh_rule_config["timeframe"] in range(1, 100000) ) )

    @staticmethod
    def get_wrc_timeframe_allow_criteria() -> str:
        return "It must be an integer from 1 to 99999 ."

    def set_wrc_timeframe(self, timeframe : int):
        self.wazuh_rule_config["timeframe"] = timeframe
        if self.validate_wrc_timeframe():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, <timeframe> of node {self.name} has been succesfully set to {timeframe}")
        else:
            ExitUtils.exit_with_error(f"You cannot set <timeframe> of node {self.name} with id {self.id} to {timeframe} of type {type(timeframe)}. {TreeNodeInformations.get_wrc_timeframe_allow_criteria()}")


    # ============================================
    # <ignore> operations | NOTE: In the xml syntax it is <ignore_after>
    # ============================================
    
    def get_wrc_ignore(self) -> int:
        return self.wazuh_rule_config["ignore"]

    def validate_wrc_ignore(self) -> bool:
        return self.wazuh_rule_config["ignore"] is None or ( isinstance(self.wazuh_rule_config["ignore"], int) and ( self.wazuh_rule_config["ignore"] in range(1, 1000000) ) )

    @staticmethod
    def get_wrc_ignore_allow_criteria() -> str:
        return "It must be an integer from 1 to 999999 ."

    def set_wrc_ignore(self, ignore : int):
        self.wazuh_rule_config["ignore"] = ignore
        if self.validate_wrc_ignore():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, <ignore> of node {self.name} has been succesfully set to {ignore}")
        else:
            ExitUtils.exit_with_error(f"You cannot set <ignore> of node {self.name} with id {self.id} to {ignore} of type {type(ignore)}. {TreeNodeInformations.get_wrc_ignore_allow_criteria()}")


    # ============================================
    # <already_existing_id> operations
    # ============================================
    
    def get_wrc_already_existing_id(self) -> int:
        return self.wazuh_rule_config["already_existing_id"]

    def validate_wrc_already_existing_id(self) -> bool:
        # Type check
        if not (self.wazuh_rule_config["already_existing_id"] is None or isinstance(self.wazuh_rule_config["already_existing_id"], int) ):
            return False
        # This needs to be used on pre-existing rules, so no other tag needs to be present
        for wrc_tag in self.wazuh_rule_config:
            if self.wazuh_rule_config[wrc_tag] == "already_existing_id":
                continue
            if self.wazuh_rule_config[wrc_tag] is not None:
                return False
        return True          

    @staticmethod
    def get_wrc_already_existing_id_allow_criteria() -> str:
        return "It must be an integer, and every other tag inside of <wazuh_rules_config> MUST not be present."

    def set_wrc_already_existing_id(self, already_existing_id : int):
        self.wazuh_rule_config["already_existing_id"] = already_existing_id
        if self.validate_wrc_already_existing_id():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, <already_existing_id> of node {self.name} has been succesfully set to {already_existing_id}")
        else:
            ExitUtils.exit_with_error(f"You cannot set <already_existing_id> of node {self.name} with id {self.id} to {already_existing_id} of type {type(already_existing_id)}. {TreeNodeInformations.get_wrc_already_existing_id_allow_criteria()}")


    # ============================================
    # <match> operations
    # ============================================
    
    def get_wrc_match(self) -> int:
        return self.wazuh_rule_config["match"]

    def validate_wrc_match(self) -> bool:
        # Type check
        if not self.wazuh_rule_config["match"] is None:
            for match in self.wazuh_rule_config["match"]:
                if not isinstance(match, Match):
                    return False
                match.validate_all()     
        return True      

    def set_wrc_match(self, all_match : List[Match]):
        self.wazuh_rule_config["match"] = all_match
        if self.validate_wrc_match():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, all <match> entries of node {self.name} have been succesfully set to: {[_.to_string() for _ in all_match]}")
        # else: is covered inside of match.validate_all() already


    # ============================================
    # <regex> operations
    # ============================================
    
    def get_wrc_regex(self) -> int:
        return self.wazuh_rule_config["regex"]

    def validate_wrc_regex(self) -> bool:
        # Type check
        if not self.wazuh_rule_config["regex"] is None:
            for regex in self.wazuh_rule_config["regex"]:
                if not isinstance(regex, Regex):
                    return False
                regex.validate_all()     
        return True      

    def set_wrc_regex(self, all_regex : List[Regex]):
        self.wazuh_rule_config["regex"] = all_regex
        if self.validate_wrc_regex():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, all <regex> entries of node {self.name} have been succesfully set to: {[_.to_string() for _ in all_regex]}")
        # else: is covered inside of match.validate_all() already


    # ============================================
    # <srcip> operations | NOTE: sull'xml è <freq_srcip>
    # ============================================
    
    def get_wrc_srcip(self) -> int:
        return self.wazuh_rule_config["srcip"]

    def validate_wrc_srcip(self) -> bool:
        # Type check
        if not self.wazuh_rule_config["srcip"] is None:
            for srcip in self.wazuh_rule_config["srcip"]:
                if not isinstance(srcip, FreqSrcip):
                    return False
                srcip.validate_all()
        return True           

    def set_wrc_srcip(self, all_srcip : List[FreqSrcip]):
        self.wazuh_rule_config["srcip"] = all_srcip
        if self.validate_wrc_srcip():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, all <freq_srcip> entries of node {self.name} have been succesfully set to: {[_.to_string() for _ in all_srcip]}")
        # else: is covered inside of match.validate_all() already


    # ============================================
    # <dstip> operations | NOTE: sull'xml è <freq_dstip>
    # ============================================
    
    def get_wrc_dstip(self) -> int:
        return self.wazuh_rule_config["dstip"]

    def validate_wrc_dstip(self) -> bool:
        # Type check
        if not self.wazuh_rule_config["dstip"] is None:
            for dstip in self.wazuh_rule_config["dstip"]:
                if not isinstance(dstip, FreqDstip):
                    return False
                dstip.validate_all()    
        return True       

    def set_wrc_dstip(self, all_dstip : List[FreqDstip]):
        self.wazuh_rule_config["dstip"] = all_dstip
        if self.validate_wrc_dstip():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, all <freq_dstip> entries of node {self.name} have been succesfully set to: {[_.to_string() for _ in all_dstip]}")
        # else: is covered inside of match.validate_all() already


    # ============================================
    # <srcport> operations | NOTE: sull'xml è <freq_srcport>
    # ============================================
    
    def get_wrc_srcport(self) -> int:
        return self.wazuh_rule_config["srcport"]

    def validate_wrc_srcport(self) -> bool:
        # Type check
        if not self.wazuh_rule_config["srcport"] is None:
            for srcport in self.wazuh_rule_config["srcport"]:
                if not isinstance(srcport, FreqSrcport):
                    return False
                srcport.validate_all()        
        return True   

    def set_wrc_srcport(self, all_srcport : List[FreqSrcport]):
        self.wazuh_rule_config["srcport"] = all_srcport
        if self.validate_wrc_srcport():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, all <freq_srcport> entries of node {self.name} have been succesfully set to: {[_.to_string() for _ in all_srcport]}")
        # else: is covered inside of match.validate_all() already



    # ============================================
    # <dstport> operations | NOTE: sull'xml è <freq_dstport>
    # ============================================

    def get_wrc_dstport(self) -> int:
        return self.wazuh_rule_config["dstport"]

    def validate_wrc_dstport(self) -> bool:
        # Type check
        if not self.wazuh_rule_config["dstport"] is None:
            for dstport in self.wazuh_rule_config["dstport"]:
                if not isinstance(dstport, FreqDstport):
                    return False
                dstport.validate_all()
        return True       

    def set_wrc_dstport(self, all_dstport : List[FreqDstport]):
        self.wazuh_rule_config["dstport"] = all_dstport
        if self.validate_wrc_dstport():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, all <freq_dstport> entries of node {self.name} have been succesfully set to: {[_.to_string() for _ in all_dstport]}")
        # else: is covered inside of match.validate_all() already



    # ========================================================================================
    # Out of <wazuh_rule_config>
    # ========================================================================================

    # ============================================
    # Validate All Node Tags
    # ============================================   

    def validate_all(self) -> bool:
        error_prefix = f"The node {self.name} with id {self.id} failed validation on"
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


    # ============================================
    # General to_string
    # ============================================   

    def to_string(self):
        '''
        Method that returns a stringified version of the whole node.
        This is what will compose the rule itself.
        '''

        to_string = ''


def test():
    # Normal node with all default entries
    t = TreeNodeInformations()
    t.set_path("/")
    t.set_id(1)
    t.validate_all()


if __name__ == '__main__':
    test()