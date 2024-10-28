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
                time                    : str = None, #Set this to None by default because it is not mandatory and can be omitted
                weekday                 : str = None, #Set this to None by default because it is not mandatory and can be omitted
                freq_same_srcip              : bool = False, #Set this to False by default because it is not mandatory and can be omitted
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
            "time"                  :   time,
            "weekday"               :   weekday,
            "same_srcip"            :   freq_same_srcip,
        }

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



    # ========================================================================================
    # Inside of <wazuh_rule_config>
    # ========================================================================================


    # ============================================
    # <frequency> operations
    # ============================================

    def get_wrc_frequency(self) -> int:
        return self.wazuh_rule_config["frequency"]

    def validate_wrc_frequency(self) -> bool:
        return self.get_wrc_frequency() is None or ( isinstance(self.get_wrc_frequency(), int) and ( self.get_wrc_frequency() in range(2, 10000) ) )

    @staticmethod
    def get_wrc_frequency_allow_criteria() -> str:
        return "It must be an integer from 2 to 9999 ."

    def set_wrc_frequency(self, frequency : int):
        self.wazuh_rule_config["frequency"] = frequency
        if self.validate_wrc_frequency():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, <frequency> of node {self.get_name()} with id {self.get_id()} has been succesfully set to {frequency}")
        else:
            ExitUtils.exit_with_error(f"You cannot set <frequency> of node {self.get_name()} with id {self.get_id()} to {frequency} of type {type(frequency)}. {TreeNodeInformations.get_wrc_frequency_allow_criteria()}")


    # ============================================
    # <timeframe> operations
    # ============================================
    
    def get_wrc_timeframe(self) -> int:
        return self.wazuh_rule_config["timeframe"]

    def validate_wrc_timeframe(self) -> bool:
        return self.get_wrc_timeframe() is None or ( isinstance(self.get_wrc_timeframe(), int) and ( self.get_wrc_timeframe() in range(1, 100000) ) )

    @staticmethod
    def get_wrc_timeframe_allow_criteria() -> str:
        return "It must be an integer from 1 to 99999 ."

    def set_wrc_timeframe(self, timeframe : int):
        self.wazuh_rule_config["timeframe"] = timeframe
        if self.validate_wrc_timeframe():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, <timeframe> of node {self.get_name()} with id {self.get_id()} has been succesfully set to {timeframe}")
        else:
            ExitUtils.exit_with_error(f"You cannot set <timeframe> of node {self.get_name()} with id {self.get_id()} to {timeframe} of type {type(timeframe)}. {TreeNodeInformations.get_wrc_timeframe_allow_criteria()}")


    # ============================================
    # <ignore> operations | NOTE: In the xml syntax it is <ignore_after>
    # ============================================
    
    def get_wrc_ignore(self) -> int:
        return self.wazuh_rule_config["ignore"]

    def validate_wrc_ignore(self) -> bool:
        return self.get_wrc_ignore() is None or ( isinstance(self.get_wrc_ignore(), int) and ( self.get_wrc_ignore() in range(1, 1000000) ) )

    @staticmethod
    def get_wrc_ignore_allow_criteria() -> str:
        return "It must be an integer from 1 to 999999 ."

    def set_wrc_ignore(self, ignore : int):
        self.wazuh_rule_config["ignore"] = ignore
        if self.validate_wrc_ignore():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, <ignore> of node {self.get_name()} with id {self.get_id()} has been succesfully set to {ignore}")
        else:
            ExitUtils.exit_with_error(f"You cannot set <ignore> of node {self.get_name()} with id {self.get_id()} to {ignore} of type {type(ignore)}. {TreeNodeInformations.get_wrc_ignore_allow_criteria()}")


    # ============================================
    # <already_existing_id> operations
    # ============================================
    
    def get_wrc_already_existing_id(self) -> int:
        return self.wazuh_rule_config["already_existing_id"]

    def validate_wrc_already_existing_id(self) -> bool:
        # Type check
        if not (self.get_wrc_already_existing_id() is None or isinstance(self.get_wrc_already_existing_id(), int) ):
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
                PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, <already_existing_id> of node {self.get_name()} with id {self.get_id()} has been succesfully set to {already_existing_id}")
        else:
            ExitUtils.exit_with_error(f"You cannot set <already_existing_id> of node {self.get_name()} with id {self.get_id()} to {already_existing_id} of type {type(already_existing_id)}. {TreeNodeInformations.get_wrc_already_existing_id_allow_criteria()}")


    # ============================================
    # <match> operations
    # ============================================
    
    def get_wrc_match(self) -> List[Match]:
        return self.wazuh_rule_config["match"]

    def validate_wrc_match(self) -> bool:
        # Type check
        if not self.get_wrc_match() is None:
            for match in self.get_wrc_match():
                if not isinstance(match, Match):
                    return False
                match.validate_all()     
        return True      

    def set_wrc_match(self, all_match : List[Match]):
        self.wazuh_rule_config["match"] = all_match
        if self.validate_wrc_match():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, all <match> entries of node {self.get_name()} with id {self.get_id()} have been succesfully set to: {[_.to_string() for _ in all_match]}")
        # else: is covered inside of match.validate_all() already


    # ============================================
    # <regex> operations
    # ============================================
    
    def get_wrc_regex(self) -> List[Regex]:
        return self.wazuh_rule_config["regex"]

    def validate_wrc_regex(self) -> bool:
        # Type check
        if not self.get_wrc_regex() is None:
            for regex in self.get_wrc_regex():
                if not isinstance(regex, Regex):
                    return False
                regex.validate_all()     
        return True      

    def set_wrc_regex(self, all_regex : List[Regex]):
        self.wazuh_rule_config["regex"] = all_regex
        if self.validate_wrc_regex():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, all <regex> entries of node {self.get_name()} with id {self.get_id()} have been succesfully set to: {[_.to_string() for _ in all_regex]}")
        # else: is covered inside of match.validate_all() already


    # ============================================
    # <srcip> operations | NOTE: sull'xml è <freq_srcip>
    # ============================================
    
    def get_wrc_srcip(self) -> List[FreqSrcip]:
        return self.wazuh_rule_config["srcip"]

    def validate_wrc_srcip(self) -> bool:
        # Type check
        if not self.get_wrc_srcip() is None:
            for srcip in self.get_wrc_srcip():
                if not isinstance(srcip, FreqSrcip):
                    return False
                srcip.validate_all()
        return True           

    def set_wrc_srcip(self, all_srcip : List[FreqSrcip]):
        self.wazuh_rule_config["srcip"] = all_srcip
        if self.validate_wrc_srcip():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, all <freq_srcip> entries of node {self.get_name()} with id {self.get_id()} have been succesfully set to: {[_.to_string() for _ in all_srcip]}")
        # else: is covered inside of match.validate_all() already


    # ============================================
    # <dstip> operations | NOTE: sull'xml è <freq_dstip>
    # ============================================
    
    def get_wrc_dstip(self) -> List[FreqDstip]:
        return self.wazuh_rule_config["dstip"]

    def validate_wrc_dstip(self) -> bool:
        # Type check
        if not self.get_wrc_dstip() is None:
            for dstip in self.get_wrc_dstip():
                if not isinstance(dstip, FreqDstip):
                    return False
                dstip.validate_all()    
        return True       

    def set_wrc_dstip(self, all_dstip : List[FreqDstip]):
        self.wazuh_rule_config["dstip"] = all_dstip
        if self.validate_wrc_dstip():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, all <freq_dstip> entries of node {self.get_name()} with id {self.get_id()} have been succesfully set to: {[_.to_string() for _ in all_dstip]}")
        # else: is covered inside of match.validate_all() already


    # ============================================
    # <srcport> operations | NOTE: sull'xml è <freq_srcport>
    # ============================================
    
    def get_wrc_srcport(self) -> List[FreqSrcport]:
        return self.wazuh_rule_config["srcport"]

    def validate_wrc_srcport(self) -> bool:
        # Type check
        if not self.get_wrc_srcport() is None:
            for srcport in self.get_wrc_srcport():
                if not isinstance(srcport, FreqSrcport):
                    return False
                srcport.validate_all()        
        return True   

    def set_wrc_srcport(self, all_srcport : List[FreqSrcport]):
        self.wazuh_rule_config["srcport"] = all_srcport
        if self.validate_wrc_srcport():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, all <freq_srcport> entries of node {self.get_name()} with id {self.get_id()} have been succesfully set to: {[_.to_string() for _ in all_srcport]}")
        # else: is covered inside of match.validate_all() already



    # ============================================
    # <dstport> operations | NOTE: sull'xml è <freq_dstport>
    # ============================================

    def get_wrc_dstport(self) -> List[FreqDstport]:
        return self.wazuh_rule_config["dstport"]

    def validate_wrc_dstport(self) -> bool:
        # Type check
        if not self.get_wrc_dstport() is None:
            for dstport in self.get_wrc_dstport():
                if not isinstance(dstport, FreqDstport):
                    return False
                dstport.validate_all()
        return True       

    def set_wrc_dstport(self, all_dstport : List[FreqDstport]):
        self.wazuh_rule_config["dstport"] = all_dstport
        if self.validate_wrc_dstport():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, all <freq_dstport> entries of node {self.get_name()} with id {self.get_id()} have been succesfully set to: {[_.to_string() for _ in all_dstport]}")
        # else: is covered inside of match.validate_all() already



    # ============================================
    # <time> operations
    # ============================================
    
    def get_wrc_time(self) -> str:
        return self.wazuh_rule_config["time"]

    def validate_wrc_time(self) -> bool:
        return (
            self.get_wrc_time() is None 
            or 
            ( isinstance(self.get_wrc_time(), str) and ( validations.is_time_interval(self.get_wrc_time()) ) )
        )

    @staticmethod
    def get_wrc_time_allow_criteria() -> str:

        return '''\n
It must be a time interval matching one of these formats:
hh:mm-hh:mm
hh:mm am-hh:mm pm
hh-hh
h am-h pm
h:mm-h:mm
h:mm am-h:mm pm
h-h
h am-h pm.\n
        '''

    def set_wrc_time(self, time : str):
        self.wazuh_rule_config["time"] = time
        if self.validate_wrc_time():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, <time> of node {self.get_name()} with id {self.get_id()} has been succesfully set to {time}")
        else:
            ExitUtils.exit_with_error(f"You cannot set <time> of node {self.get_name()} with id {self.get_id()} to {time} of type {type(time)}. {TreeNodeInformations.get_wrc_time_allow_criteria()}")




    # ============================================
    # <weekday> operations
    # ============================================
    
    def get_wrc_weekday(self) -> str:
        return self.wazuh_rule_config["weekday"]

    def validate_wrc_weekday(self) -> bool:
        allowed_values = ["weekdays", "weekends"]
        return (
            self.get_wrc_weekday() is None 
            or 
            ( isinstance(self.get_wrc_weekday(), str) and ( validations.is_allowed(allowed_values=allowed_values, string=self.get_wrc_weekday()) or validations.is_weekday_range(s = self.get_wrc_weekday()) ) )
        )

    @staticmethod
    def get_wrc_weekday_allow_criteria() -> str:

        return '''\n
It must be either "weekdays", "weekends", or match the "weekday - weekday" string,
where weekday is any day of the week in lowercase, such as "monday - sunday".\n
        '''

    def set_wrc_weekday(self, weekday : str):
        self.wazuh_rule_config["weekday"] = weekday
        if self.validate_wrc_weekday():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, <weekday> of node {self.get_name()} with id {self.get_id()} has been succesfully set to {weekday}")
        else:
            ExitUtils.exit_with_error(f"You cannot set <weekday> of node {self.get_name()} with id {self.get_id()} to {weekday} of type {type(weekday)}. {TreeNodeInformations.get_wrc_weekday_allow_criteria()}")


    # ============================================
    # <same_srcip> operations
    # ============================================
    
    def get_wrc_same_srcip(self) -> str:
        return self.wazuh_rule_config["same_srcip"]

    def validate_wrc_same_srcip(self) -> bool:
        return isinstance(self.get_wrc_same_srcip(), bool)

    @staticmethod
    def get_wrc_same_srcip_allow_criteria() -> str:
        return "Must just be <freq_same_srcip /> tag."

    def set_wrc_same_srcip(self, same_srcip : str):
        self.wazuh_rule_config["same_srcip"] = same_srcip
        if self.validate_wrc_same_srcip():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, <freq_same_srcip> of node {self.get_name()} with id {self.get_id()} has been succesfully set to {same_srcip}")
        else:
            ExitUtils.exit_with_error(f"You cannot set <weekday> of node {self.get_name()} with id {self.get_id()} to {same_srcip} of type {type(same_srcip)}. {TreeNodeInformations.get_wrc_weekday_allow_criteria()}")




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