import validations
from typing import List

# Support classes import
from Match import Match
from Regex import Regex
from Srcip import Srcip
from Dstip import Dstip
from Srcport import Srcport
from Dstport import Dstport
from Info import Info

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


class WazuhRuleConfig:
    '''
    This class represents all the informations that are relevant to Wazuh.
    Practically: the xml tags of it.
    '''
    print_diagnostics = True
    # This has way too many arguments...
    def __init__(self,
                relative_node_name      : str = "unspecified", #Useful for prints
                wrc_frequency           : int = None, #Set this to None by default because it is not mandatory and can be omitted
                wrc_timeframe           : int = None, #Set this to None by default because it is not mandatory and can be omitted
                wrc_ignore_after        : int = None, #Set this to None by default because it is not mandatory and can be omitted
                wrc_already_existing_id : int = None, #Set this to None by default because it is not mandatory and can be omitted
                match_list              : List[Match] = None, #Set this to None by default because it is not mandatory and can be omitted
                regex_list              : List[Regex] = None, #Set this to None by default because it is not mandatory and can be omitted
                srcip                   : List[Srcip] = None, #Set this to None by default because it is not mandatory and can be omitted
                dstip                   : List[Dstip] = None, #Set this to None by default because it is not mandatory and can be omitted
                srcport                 : List[Srcport] = None, #Set this to None by default because it is not mandatory and can be omitted
                dstport                 : List[Dstport] = None, #Set this to None by default because it is not mandatory and can be omitted
                time                    : str  = None, #Set this to None by default because it is not mandatory and can be omitted
                weekday                 : str  = None, #Set this to None by default because it is not mandatory and can be omitted
                freq_same_srcip         : bool = False, #Set this to False by default because it is not mandatory and can be omitted
                freq_different_srcip    : bool = False, #Set this to False by default because it is not mandatory and can be omitted
                freq_same_srcport       : bool = False, #Set this to False by default because it is not mandatory and can be omitted
                freq_different_srcport  : bool = False, #Set this to False by default because it is not mandatory and can be omitted
                freq_same_location      : bool = False, #Set this to False by default because it is not mandatory and can be omitted     
                freq_same_srcuser       : bool = False, #Set this to False by default because it is not mandatory and can be omitted            
                freq_different_srcuser  : bool = False, #Set this to False by default because it is not mandatory and can be omitted 
                description             : str  = None, #Set this to False by default because it is not mandatory and can be omitted 
                info                    : List[Info] = None, #Set this to False by default because it is not mandatory and can be omitted 
                options                 : List[str]  = None, #Set this to False by default because it is not mandatory and can be omitted 
                ):
            
            self.relative_node_name =   relative_node_name
            self.frequency          =   wrc_frequency
            self.timeframe          =   wrc_timeframe
            self.ignore             =   wrc_ignore_after
            self.already_existing_id=   wrc_already_existing_id
            self.match              =   match_list
            self.regex              =   regex_list
            self.srcip              =   srcip
            self.dstip              =   dstip
            self.srcport            =   srcport
            self.dstport            =   dstport
            self.time               =   time
            self.weekday            =   weekday
            self.same_srcip         =   freq_same_srcip
            self.different_srcip    =   freq_different_srcip
            self.same_srcport       =   freq_same_srcport
            self.different_srcport  =   freq_different_srcport
            self.same_location      =   freq_same_location
            self.same_srcuser       =   freq_same_srcuser
            self.different_srcuser  =   freq_different_srcuser
            self.description        =   description
            self.info               =   info
            self.options            =   options

            
    # ========================================================================================
    # Inside of <wazuh_rule_config>
    # ========================================================================================


    # ============================================
    # <frequency> operations
    # ============================================

    def get_wrc_frequency(self) -> int:
        return self.frequency

    def validate_wrc_frequency(self) -> bool:
        return self.get_wrc_frequency() is None or ( isinstance(self.get_wrc_frequency(), int) and ( self.get_wrc_frequency() in range(2, 10000) ) )

    @staticmethod
    def get_wrc_frequency_allow_criteria() -> str:
        return "It must be an integer from 2 to 9999 ."

    def set_wrc_frequency(self, frequency : int):
        self.frequency = frequency
        if self.validate_wrc_frequency():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, <frequency> of node {self.relative_node_name} has been succesfully set to {frequency}")
        else:
            ExitUtils.exit_with_error(f"You cannot set <frequency> of node {self.relative_node_name} to {frequency} of type {type(frequency)}. {WazuhRuleConfig.get_wrc_frequency_allow_criteria()}")


    # ============================================
    # <timeframe> operations
    # ============================================
    
    def get_wrc_timeframe(self) -> int:
        return self.timeframe

    def validate_wrc_timeframe(self) -> bool:
        return self.get_wrc_timeframe() is None or ( isinstance(self.get_wrc_timeframe(), int) and ( self.get_wrc_timeframe() in range(1, 100000) ) )

    @staticmethod
    def get_wrc_timeframe_allow_criteria() -> str:
        return "It must be an integer from 1 to 99999 ."

    def set_wrc_timeframe(self, timeframe : int):
        self.timeframe = timeframe
        if self.validate_wrc_timeframe():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, <timeframe> of node {self.relative_node_name} has been succesfully set to {timeframe}")
        else:
            ExitUtils.exit_with_error(f"You cannot set <timeframe> of node {self.relative_node_name} to {timeframe} of type {type(timeframe)}. {WazuhRuleConfig.get_wrc_timeframe_allow_criteria()}")


    # ============================================
    # <ignore> operations | NOTE: In the xml syntax it is <ignore_after>
    # ============================================
    
    def get_wrc_ignore(self) -> int:
        return self.ignore

    def validate_wrc_ignore(self) -> bool:
        return self.get_wrc_ignore() is None or ( isinstance(self.get_wrc_ignore(), int) and ( self.get_wrc_ignore() in range(1, 1000000) ) )

    @staticmethod
    def get_wrc_ignore_allow_criteria() -> str:
        return "It must be an integer from 1 to 999999 ."

    def set_wrc_ignore(self, ignore : int):
        self.ignore = ignore
        if self.validate_wrc_ignore():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, <ignore> of node {self.relative_node_name} has been succesfully set to {ignore}")
        else:
            ExitUtils.exit_with_error(f"You cannot set <ignore> of node {self.relative_node_name} to {ignore} of type {type(ignore)}. {WazuhRuleConfig.get_wrc_ignore_allow_criteria()}")


    # ============================================
    # <already_existing_id> operations
    # ============================================
    
    def get_wrc_already_existing_id(self) -> int:
        return self.already_existing_id

    def validate_wrc_already_existing_id(self) -> bool:
        # Type check
        if not (self.get_wrc_already_existing_id() is None or isinstance(self.get_wrc_already_existing_id(), int) ):
            return False
        # This needs to be used on pre-existing rules, so no other tag needs to be present
        for wrc_tag in self.__dict__.keys():
            if self.__dict__[wrc_tag] == "already_existing_id":
                continue
            if self.__dict__[wrc_tag] is not None and (isinstance(self.__dict__[wrc_tag], bool) and self.__dict__[wrc_tag] == True):
                PrintUtils.print_in_red(f"- ERROR: <already_existing_id> is present, but another tag is given: <{wrc_tag}>vwith value {self.__dict__[wrc_tag]}.")
                return False
        return True          

    @staticmethod
    def get_wrc_already_existing_id_allow_criteria() -> str:
        return "It must be an integer, and every other tag inside of <wazuh_rules_config> MUST NOT be present."

    def set_wrc_already_existing_id(self, already_existing_id : int):
        self.already_existing_id = already_existing_id
        if self.validate_wrc_already_existing_id():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, <already_existing_id> of node {self.relative_node_name} has been succesfully set to {already_existing_id}")
        else:
            ExitUtils.exit_with_error(f"You cannot set <already_existing_id> of node {self.relative_node_name} to {already_existing_id} of type {type(already_existing_id)}. {WazuhRuleConfig.get_wrc_already_existing_id_allow_criteria()}")


    # ============================================
    # <match> operations
    # ============================================
    
    def get_wrc_match(self) -> List[Match]:
        return self.match

    def validate_wrc_match(self) -> bool:
        # Type check
        if not self.get_wrc_match() is None:
            for match in self.get_wrc_match():
                if not isinstance(match, Match):
                    return False
                match.validate_all()     
        return True      

    def set_wrc_match(self, all_match : List[Match]):
        self.match = all_match
        if self.validate_wrc_match():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, all <match> entries of node {self.relative_node_name} have been succesfully set to: {[_.to_string() for _ in all_match]}")
        # else: is covered inside of match.validate_all() already


    # ============================================
    # <regex> operations
    # ============================================
    
    def get_wrc_regex(self) -> List[Regex]:
        return self.regex

    def validate_wrc_regex(self) -> bool:
        # Type check
        if not self.get_wrc_regex() is None:
            for regex in self.get_wrc_regex():
                if not isinstance(regex, Regex):
                    return False
                regex.validate_all()     
        return True      

    def set_wrc_regex(self, all_regex : List[Regex]):
        self.regex = all_regex
        if self.validate_wrc_regex():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, all <regex> entries of node {self.relative_node_name} have been succesfully set to: {[_.to_string() for _ in all_regex]}")
        # else: is covered inside of regex.validate_all() already


    # ============================================
    # <srcip> operations | NOTE: sull'xml è <srcip>
    # ============================================
    
    def get_wrc_srcip(self) -> List[Srcip]:
        return self.srcip

    def validate_wrc_srcip(self) -> bool:
        # Type check
        if not self.get_wrc_srcip() is None:
            for srcip in self.get_wrc_srcip():
                if not isinstance(srcip, Srcip):
                    return False
                srcip.validate_all()
        return True           

    def set_wrc_srcip(self, all_srcip : List[Srcip]):
        self.srcip = all_srcip
        if self.validate_wrc_srcip():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, all <srcip> entries of node {self.relative_node_name} have been succesfully set to: {[_.to_string() for _ in all_srcip]}")
        # else: is covered inside of freqsrcip.validate_all() already


    # ============================================
    # <dstip> operations | NOTE: sull'xml è <dstip>
    # ============================================
    
    def get_wrc_dstip(self) -> List[Dstip]:
        return self.dstip

    def validate_wrc_dstip(self) -> bool:
        # Type check
        if not self.get_wrc_dstip() is None:
            for dstip in self.get_wrc_dstip():
                if not isinstance(dstip, Dstip):
                    return False
                dstip.validate_all()    
        return True       

    def set_wrc_dstip(self, all_dstip : List[Dstip]):
        self.dstip = all_dstip
        if self.validate_wrc_dstip():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, all <dstip> entries of node {self.relative_node_name} have been succesfully set to: {[_.to_string() for _ in all_dstip]}")
        # else: is covered inside of freqdstip.validate_all() already


    # ============================================
    # <srcport> operations | NOTE: sull'xml è <srcport>
    # ============================================
    
    def get_wrc_srcport(self) -> List[Srcport]:
        return self.srcport

    def validate_wrc_srcport(self) -> bool:
        # Type check
        if not self.get_wrc_srcport() is None:
            for srcport in self.get_wrc_srcport():
                if not isinstance(srcport, Srcport):
                    return False
                srcport.validate_all()        
        return True   

    def set_wrc_srcport(self, all_srcport : List[Srcport]):
        self.srcport = all_srcport
        if self.validate_wrc_srcport():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, all <srcport> entries of node {self.relative_node_name} have been succesfully set to: {[_.to_string() for _ in all_srcport]}")
        # else: is covered inside of freqsrcport.validate_all() already



    # ============================================
    # <dstport> operations | NOTE: sull'xml è <dstport>
    # ============================================

    def get_wrc_dstport(self) -> List[Dstport]:
        return self.dstport

    def validate_wrc_dstport(self) -> bool:
        # Type check
        if not self.get_wrc_dstport() is None:
            for dstport in self.get_wrc_dstport():
                if not isinstance(dstport, Dstport):
                    return False
                dstport.validate_all()
        return True       

    def set_wrc_dstport(self, all_dstport : List[Dstport]):
        self.dstport = all_dstport
        if self.validate_wrc_dstport():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, all <dstport> entries of node {self.relative_node_name} have been succesfully set to: {[_.to_string() for _ in all_dstport]}")
        # else: is covered inside of freqdstport.validate_all() already



    # ============================================
    # <time> operations
    # ============================================
    
    def get_wrc_time(self) -> str:
        return self.time

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
        self.time = time
        if self.validate_wrc_time():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, <time> of node {self.relative_node_name} has been succesfully set to {time}")
        else:
            ExitUtils.exit_with_error(f"You cannot set <time> of node {self.relative_node_name} to {time} of type {type(time)}. {WazuhRuleConfig.get_wrc_time_allow_criteria()}")




    # ============================================
    # <weekday> operations
    # ============================================
    
    def get_wrc_weekday(self) -> str:
        return self.weekday

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
        self.weekday = weekday
        if self.validate_wrc_weekday():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, <weekday> of node {self.relative_node_name} has been succesfully set to {weekday}")
        else:
            ExitUtils.exit_with_error(f"You cannot set <weekday> of node {self.relative_node_name} to {weekday} of type {type(weekday)}. {WazuhRuleConfig.get_wrc_weekday_allow_criteria()}")


    # ============================================
    # <same_srcip> operations
    # ============================================
    
    def get_wrc_same_srcip(self) -> bool:
        return self.same_srcip

    def validate_wrc_same_srcip(self) -> bool:
        return isinstance(self.get_wrc_same_srcip(), bool)

    @staticmethod
    def get_wrc_same_srcip_allow_criteria() -> str:
        return "Must just be <freq_same_srcip /> tag."

    def set_wrc_same_srcip(self, same_srcip : bool):
        self.same_srcip = same_srcip
        if self.validate_wrc_same_srcip():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, <freq_same_srcip> of node {self.relative_node_name} has been succesfully set to {same_srcip}")
        else:
            ExitUtils.exit_with_error(f"You cannot set <freq_same_srcip> of node {self.relative_node_name} to {same_srcip} of type {type(same_srcip)}. {WazuhRuleConfig.get_wrc_same_srcip_allow_criteria()}")


    # ============================================
    # <different_srcip> operations
    # ============================================
    
    def get_wrc_different_srcip(self) -> bool:
        return self.different_srcip

    def validate_wrc_different_srcip(self) -> bool:
        return isinstance(self.get_wrc_different_srcip(), bool)

    @staticmethod
    def get_wrc_different_srcip_allow_criteria() -> str:
        return "Must just be <freq_different_srcip /> tag."

    def set_wrc_different_srcip(self, different_srcip : bool):
        self.different_srcip = different_srcip
        if self.validate_wrc_different_srcip():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, <freq_different_srcip> of node {self.relative_node_name} has been succesfully set to {different_srcip}")
        else:
            ExitUtils.exit_with_error(f"You cannot set <freq_different_srcip> of node {self.relative_node_name} to {different_srcip} of type {type(different_srcip)}. {WazuhRuleConfig.get_wrc_different_srcip_allow_criteria()}")



    # ============================================
    # <same_srcport> operations
    # ============================================

    def get_wrc_same_srcport(self) -> bool:
        return self.same_srcport

    def validate_wrc_same_srcport(self) -> bool:
        return isinstance(self.get_wrc_same_srcport(), bool)

    @staticmethod
    def get_wrc_same_srcport_allow_criteria() -> str:
        return "Must just be <freq_same_srcport /> tag."

    def set_wrc_same_srcport(self, same_srcport : bool):
        self.same_srcport = same_srcport
        if self.validate_wrc_same_srcport():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, <freq_same_srcport> of node {self.relative_node_name} has been succesfully set to {same_srcport}")
        else:
            ExitUtils.exit_with_error(f"You cannot set <freq_same_srcport> of node {self.relative_node_name} to {same_srcport} of type {type(same_srcport)}. {WazuhRuleConfig.get_wrc_same_srcport_allow_criteria()}")




    # ============================================
    # <different_srcport> operations
    # ============================================

    def get_wrc_different_srcport(self) -> bool:
        return self.different_srcport

    def validate_wrc_different_srcport(self) -> bool:
        return isinstance(self.get_wrc_different_srcport(), bool)

    @staticmethod
    def get_wrc_different_srcport_allow_criteria() -> str:
        return "Must just be <freq_different_srcport /> tag."

    def set_wrc_different_srcport(self, different_srcport : bool):
        self.different_srcport = different_srcport
        if self.validate_wrc_different_srcport():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, <freq_different_srcport> of node {self.relative_node_name} has been succesfully set to {different_srcport}")
        else:
            ExitUtils.exit_with_error(f"You cannot set <freq_different_srcport> of node {self.relative_node_name} to {different_srcport} of type {type(different_srcport)}. {WazuhRuleConfig.get_wrc_different_srcport_allow_criteria()}")



    # ============================================
    # <same_location> operations
    # ============================================

    def get_wrc_same_location(self) -> bool:
        return self.same_location

    def validate_wrc_same_location(self) -> bool:
        return isinstance(self.get_wrc_same_location(), bool)

    @staticmethod
    def get_wrc_same_location_allow_criteria() -> str:
        return "Must just be <freq_same_location /> tag."

    def set_wrc_same_location(self, same_location : bool):
        self.same_location = same_location
        if self.validate_wrc_same_location():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, <freq_same_location> of node {self.relative_node_name} has been succesfully set to {same_location}")
        else:
            ExitUtils.exit_with_error(f"You cannot set <freq_same_location> of node {self.relative_node_name} to {same_location} of type {type(same_location)}. {WazuhRuleConfig.get_wrc_same_location_allow_criteria()}")


    # ============================================
    # <same_srcuser> operations
    # ============================================

    def get_wrc_same_srcuser(self) -> bool:
        return self.same_srcuser

    def validate_wrc_same_srcuser(self) -> bool:
        return isinstance(self.get_wrc_same_srcuser(), bool)

    @staticmethod
    def get_wrc_same_srcuser_allow_criteria() -> str:
        return "Must just be <freq_same_srcuser /> tag."

    def set_wrc_same_srcuser(self, same_srcuser : bool):
        self.same_srcuser = same_srcuser
        if self.validate_wrc_same_srcuser():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, <freq_same_srcuser> of node {self.relative_node_name} has been succesfully set to {same_srcuser}")
        else:
            ExitUtils.exit_with_error(f"You cannot set <freq_same_srcuser> of node {self.relative_node_name} to {same_srcuser} of type {type(same_srcuser)}. {WazuhRuleConfig.get_wrc_same_srcuser_allow_criteria()}")


    # ============================================
    # <different_srcuser> operations
    # ============================================

    def get_wrc_different_srcuser(self) -> bool:
        return self.different_srcuser

    def validate_wrc_different_srcuser(self) -> bool:
        return isinstance(self.get_wrc_different_srcuser(), bool)

    @staticmethod
    def get_wrc_different_srcuser_allow_criteria() -> str:
        return "Must just be <freq_different_srcuser /> tag."

    def set_wrc_different_srcuser(self, different_srcuser : bool):
        self.different_srcuser = different_srcuser
        if self.validate_wrc_different_srcuser():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, <freq_different_srcuser> of node {self.relative_node_name} has been succesfully set to {different_srcuser}")
        else:
            ExitUtils.exit_with_error(f"You cannot set <freq_different_srcuser> of node {self.relative_node_name} to {different_srcuser} of type {type(different_srcuser)}. {WazuhRuleConfig.get_wrc_different_srcuser_allow_criteria()}")



    # ============================================
    # <description> operations
    # ============================================

    def get_wrc_description(self) -> str:
        return self.description

    def validate_wrc_description(self) -> bool:
        return isinstance(self.get_wrc_description(), str)

    @staticmethod
    def get_wrc_description_allow_criteria() -> str:
        return "You must provide a description! This is what will be seen in Wazuh Dashboard!"

    def set_wrc_description(self, description : str):
        self.description = description
        if self.validate_wrc_description():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, <description> of node {self.relative_node_name} has been succesfully set to {description}")
        else:
            ExitUtils.exit_with_error(f"You cannot set <description> of node {self.relative_node_name} to {description} of type {type(description)}. {WazuhRuleConfig.get_wrc_description_allow_criteria()}")


    # ============================================
    # <info> operations
    # ============================================
    
    def get_wrc_info(self) -> List[Info]:
        return self.info

    def validate_wrc_info(self) -> bool:
        # Type check
        if not self.get_wrc_info() is None:
            for info in self.get_wrc_info():
                if not isinstance(info, Info):
                    return False
                info.validate_all()     
        return True      

    def set_wrc_info(self, all_info : List[Info]):
        self.info = all_info
        if self.validate_wrc_info():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, all <info> entries of node {self.relative_node_name} have been succesfully set to: {[_.to_string() for _ in all_info]}")
        # else: is covered inside of info.validate_all() already


    # ============================================
    # <options> operations
    # ============================================

    def get_wrc_options(self) -> List[str]:
        return self.options

    def validate_wrc_options(self) -> bool:
        # Type check
        if not self.get_wrc_options() is None:
            for options in self.get_wrc_options():
                if not isinstance(options, str):
                    return False
                if not validations.is_allowed(allowed_values=["alert_by_email", "no_email_alert", "no_log", "no_full_log", "no_counter"], string=options):
                    ExitUtils.exit_with_error(f"You cannot set <options> of node {self.relative_node_name} to {options} of type {type(options)}. {WazuhRuleConfig.get_wrc_options_allow_criteria()}")
        return True    

    @staticmethod
    def get_wrc_options_allow_criteria() -> str:
        return 'Every <options> tag must contain one of the following strings: "alert_by_email", "no_email_alert", "no_log", "no_full_log", "no_counter".'

    def set_wrc_options(self, options : str):
        self.options = options
        if self.validate_wrc_options():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, <options> of node {self.relative_node_name} has been succesfully set to {options}")
        # else: is covered inside of self.validate_wrc_options() already


    # ========================================================================================
    # Out of <wazuh_rule_config>
    # ========================================================================================


    # ============================================
    # Validate All Node Tags
    # ============================================   


    def validate_all(self) -> bool:
        error_prefix = f"The node {self.relative_node_name} failed validation on"
        error_suffix = f"was given instead."

        if not self.validate_wrc_frequency():
            ExitUtils.exit_with_error(f"{error_prefix} <frequency> in <wazuh_rule_config>. {WazuhRuleConfig.get_wrc_frequency_allow_criteria()} {self.get_wrc_frequency()} of type {type(self.get_wrc_frequency())} {error_suffix}")
        
        if not self.validate_wrc_timeframe():
            ExitUtils.exit_with_error(f"{error_prefix} <timeframe> in <wazuh_rule_config>. {WazuhRuleConfig.get_wrc_timeframe_allow_criteria()} {self.get_wrc_timeframe()} of type {type(self.get_wrc_timeframe())} {error_suffix}")
        
        if not self.validate_wrc_ignore():
        
            ExitUtils.exit_with_error(f"{error_prefix} <ignore_after> in <wazuh_rule_config>. {WazuhRuleConfig.get_wrc_ignore_allow_criteria()} {self.get_wrc_ignore()} of type {type(self.get_wrc_ignore())} {error_suffix}")
        
        if not self.validate_wrc_already_existing_id():
            ExitUtils.exit_with_error(f"{error_prefix} <already_existing_id> in <wazuh_rule_config>. {WazuhRuleConfig.get_wrc_already_existing_id_allow_criteria()} {self.get_wrc_already_existing_id()} of type {type(self.get_wrc_already_existing_id())} {error_suffix}")
        
        self.validate_wrc_match()

        self.validate_wrc_regex()

        self.validate_wrc_srcip()

        self.validate_wrc_dstip()

        self.validate_wrc_srcport()

        self.validate_wrc_dstport()

        if not self.validate_wrc_time():
            ExitUtils.exit_with_error(f"{error_prefix} <time> in <wazuh_rule_config>. {WazuhRuleConfig.get_wrc_time_allow_criteria()} {self.get_wrc_time()} of type {type(self.get_wrc_time())} {error_suffix}")

        if not self.validate_wrc_weekday():
            ExitUtils.exit_with_error(f"{error_prefix} <weekday> in <wazuh_rule_config>. {WazuhRuleConfig.get_wrc_weekday_allow_criteria()} {self.get_wrc_weekday()} of type {type(self.get_wrc_weekday())} {error_suffix}")

        if not self.validate_wrc_same_srcip():
            ExitUtils.exit_with_error(f"{error_prefix} <freq_same_srcip> in <wazuh_rule_config>. {WazuhRuleConfig.get_wrc_same_srcip_allow_criteria()} {self.get_wrc_same_srcip()} of type {type(self.get_wrc_same_srcip())} {error_suffix}")
  
        if not self.validate_wrc_different_srcip():
            ExitUtils.exit_with_error(f"{error_prefix} <freq_different_srcip> in <wazuh_rule_config>. {WazuhRuleConfig.get_wrc_different_srcip_allow_criteria()} {self.get_wrc_different_srcip()} of type {type(self.get_wrc_different_srcip())} {error_suffix}")

        if not self.validate_wrc_same_srcport():
            ExitUtils.exit_with_error(f"{error_prefix} <freq_same_srcport> in <wazuh_rule_config>. {WazuhRuleConfig.get_wrc_same_srcport_allow_criteria()} {self.get_wrc_same_srcport()} of type {type(self.get_wrc_same_srcport())} {error_suffix}")
    
        if not self.validate_wrc_different_srcport():
            ExitUtils.exit_with_error(f"{error_prefix} <freq_different_srcport> in <wazuh_rule_config>. {WazuhRuleConfig.get_wrc_different_srcport_allow_criteria()} {self.get_wrc_different_srcport()} of type {type(self.get_wrc_different_srcport())} {error_suffix}")
   
        if not self.validate_wrc_same_location():
            ExitUtils.exit_with_error(f"{error_prefix} <freq_same_location> in <wazuh_rule_config>. {WazuhRuleConfig.get_wrc_same_location_allow_criteria()} {self.get_wrc_same_location()} of type {type(self.get_wrc_same_location())} {error_suffix}")
   
        if not self.validate_wrc_same_srcuser():
            ExitUtils.exit_with_error(f"{error_prefix} <freq_same_srcuser> in <wazuh_rule_config>. {WazuhRuleConfig.get_wrc_same_srcuser_allow_criteria()} {self.get_wrc_same_srcuser()} of type {type(self.get_wrc_same_srcuser())} {error_suffix}")
   
        if not self.validate_wrc_different_srcuser():
            ExitUtils.exit_with_error(f"{error_prefix} <freq_different_srcuser> in <wazuh_rule_config>. {WazuhRuleConfig.get_wrc_different_srcuser_allow_criteria()} {self.get_wrc_different_srcuser()} of type {type(self.get_wrc_different_srcuser())} {error_suffix}")
   
        if not self.validate_wrc_description():
            ExitUtils.exit_with_error(f"{error_prefix} <description> in <wazuh_rule_config>. {WazuhRuleConfig.get_wrc_description_allow_criteria()} {self.get_wrc_description()} of type {type(self.get_wrc_description())} {error_suffix}")
   
        self.validate_wrc_info()

        self.validate_wrc_options()

        # MULTIPLE TAGS CHECK
        def validate_at_least_one_identificator_present(self : WazuhRuleConfig):
            '''
            Method that checks if a valid identifier for the node is given.
            The meaning is: A valid Wazuh rule that will trigger the node.
            After all, creating a node, so a Wazuh rule, that cannot be triggered,
            is rather useless.
            '''
            need_one_at_least_list = ["already_existing_id", "match", "regex", "srcip", "dstip", "srcport", "dstport", "time", "weekday" ]

            allow_criteria_for_error_print = f"One of the following tags must be present in order to identify the\nway to trigger the Wazuh rule related to it, inside of <wazuh_rule_config>:\n\n{"\n".join([f"<{item}>" for item in need_one_at_least_list])}"

            # NOTE: Careful that "need_one_at_least_list" contains names that are the exact name of one of the attributes of the class WazuhRuleConfig.
            # Reflection is used to access them, this is why! Else, the dict will not match and throw an exception.
            # NOTE: The default value is "None" for all. Careful to keep it this way, else this validation will always return True.

            curr_class_attributes = self.__dict__
            for tag in need_one_at_least_list:
                if curr_class_attributes[tag] is not None:
                    return True
                    
            ExitUtils.exit_with_error(f"{error_prefix} 'at least one identifying tag must be given'.\n{allow_criteria_for_error_print}")           

        validate_at_least_one_identificator_present(self)




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
    wrc = WazuhRuleConfig()
    wrc.set_wrc_description("Hello!")
    wrc.validate_all()


if __name__ == '__main__':
    test()