import validations
from typing import List

# Support classes import
from TreeClasses.Match import Match
from TreeClasses.Regex import Regex
from TreeClasses.Srcip import Srcip
from TreeClasses.Dstip import Dstip
from TreeClasses.Srcport import Srcport
from TreeClasses.Dstport import Dstport
from TreeClasses.Info import Info

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
                srcip_list              : List[Srcip] = None, #Set this to None by default because it is not mandatory and can be omitted
                dstip_list              : List[Dstip] = None, #Set this to None by default because it is not mandatory and can be omitted
                srcport_list            : List[Srcport] = None, #Set this to None by default because it is not mandatory and can be omitted
                dstport_list            : List[Dstport] = None, #Set this to None by default because it is not mandatory and can be omitted
                time                    : str  = None, #Set this to None by default because it is not mandatory and can be omitted
                weekday                 : str  = None, #Set this to None by default because it is not mandatory and can be omitted
                freq_same_srcip         : bool = False, #Set this to False by default because it is not mandatory and can be omitted
                freq_different_srcip    : bool = False, #Set this to False by default because it is not mandatory and can be omitted
                freq_same_srcport       : bool = False, #Set this to False by default because it is not mandatory and can be omitted
                freq_different_srcport  : bool = False, #Set this to False by default because it is not mandatory and can be omitted
                freq_same_dstport       : bool = False, #Set this to False by default because it is not mandatory and can be omitted
                freq_different_dstport  : bool = False, #Set this to False by default because it is not mandatory and can be omitted
                freq_same_location      : bool = False, #Set this to False by default because it is not mandatory and can be omitted     
                freq_same_srcuser       : bool = False, #Set this to False by default because it is not mandatory and can be omitted            
                freq_different_srcuser  : bool = False, #Set this to False by default because it is not mandatory and can be omitted 
                description             : str  = None, #Set this to False by default because it is not mandatory and can be omitted 
                info_list               : List[Info] = None, #Set this to False by default because it is not mandatory and can be omitted 
                options_list            : List[str]  = None, #Set this to False by default because it is not mandatory and can be omitted 
                ):
            
            self.relative_node_name =   relative_node_name
            self.frequency          =   wrc_frequency
            self.timeframe          =   wrc_timeframe
            self.ignore             =   wrc_ignore_after
            self.already_existing_id=   wrc_already_existing_id
            self.match              =   match_list
            self.regex              =   regex_list
            self.srcip              =   srcip_list
            self.dstip              =   dstip_list
            self.srcport            =   srcport_list
            self.dstport            =   dstport_list
            self.time               =   time
            self.weekday            =   weekday
            self.same_srcip         =   freq_same_srcip
            self.different_srcip    =   freq_different_srcip
            self.same_srcport       =   freq_same_srcport
            self.different_srcport  =   freq_different_srcport
            self.same_dstport       =   freq_same_dstport
            self.different_dstport  =   freq_different_dstport
            self.same_location      =   freq_same_location
            self.same_srcuser       =   freq_same_srcuser
            self.different_srcuser  =   freq_different_srcuser
            self.description        =   description
            self.info               =   info_list
            self.options            =   options_list

            
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

    def validate_wrc_frequency_with_error_launch(self):
        if not self.validate_wrc_frequency():
            error_prefix = f"The node {self.relative_node_name} failed validation on"
            error_suffix = f"was given instead."
            ExitUtils.exit_with_error(f"{error_prefix} <frequency> in <wazuh_rule_config>. {WazuhRuleConfig.get_wrc_frequency_allow_criteria()} {self.get_wrc_frequency()} of type {type(self.get_wrc_frequency())} {error_suffix}")
 

    @staticmethod
    def get_wrc_frequency_allow_criteria() -> str:
        return "It must be an integer from 2 to 9999 ."

    def set_wrc_frequency(self, frequency : int):
        self.frequency = frequency

        self.validate_wrc_frequency_with_error_launch()
        
        if self.print_diagnostics:
            PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, <frequency> of node {self.relative_node_name} has been succesfully set to {frequency}")
    
    #def to_string_wrc_frequency(self) -> str:
    #    return f"<frequency>{self.get_wrc_frequency()}</frequency>"


    # ============================================
    # <timeframe> operations
    # ============================================
    
    def get_wrc_timeframe(self) -> int:
        return self.timeframe

    def validate_wrc_timeframe(self) -> bool:
        return self.get_wrc_timeframe() is None or ( isinstance(self.get_wrc_timeframe(), int) and ( self.get_wrc_timeframe() in range(1, 100000) ) )

    def validate_wrc_timeframe_with_error_launch(self):
        if not self.validate_wrc_timeframe():
            error_prefix = f"The node {self.relative_node_name} failed validation on"
            error_suffix = f"was given instead."
            ExitUtils.exit_with_error(f"{error_prefix} <timeframe> in <wazuh_rule_config>. {WazuhRuleConfig.get_wrc_timeframe_allow_criteria()} {self.get_wrc_timeframe()} of type {type(self.get_wrc_timeframe())} {error_suffix}")


    @staticmethod
    def get_wrc_timeframe_allow_criteria() -> str:
        return "It must be an integer from 1 to 99999 ."

    def set_wrc_timeframe(self, timeframe : int):
        self.timeframe = timeframe

        self.validate_wrc_timeframe_with_error_launch()

        if self.print_diagnostics:
            PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, <timeframe> of node {self.relative_node_name} has been succesfully set to {timeframe}")

    #def to_string_wrc_timeframe(self) -> str:
    #    return f"<timeframe>{self.get_wrc_timeframe()}</timeframe>"


    # ============================================
    # <ignore> operations | NOTE: In the xml syntax it is <ignore_after>
    # ============================================
    
    def get_wrc_ignore(self) -> int:
        return self.ignore

    def validate_wrc_ignore(self) -> bool:
        return self.get_wrc_ignore() is None or ( isinstance(self.get_wrc_ignore(), int) and ( self.get_wrc_ignore() in range(1, 1000000) ) )

    def validate_wrc_ignore_with_error_launch(self):
        if not self.validate_wrc_ignore():
            error_prefix = f"The node {self.relative_node_name} failed validation on"
            error_suffix = f"was given instead."
            ExitUtils.exit_with_error(f"{error_prefix} <ignore_after> in <wazuh_rule_config>. {WazuhRuleConfig.get_wrc_ignore_allow_criteria()} {self.get_wrc_ignore()} of type {type(self.get_wrc_ignore())} {error_suffix}")

    @staticmethod
    def get_wrc_ignore_allow_criteria() -> str:
        return "It must be an integer from 1 to 999999 ."

    def set_wrc_ignore(self, ignore : int):
        self.ignore = ignore

        self.validate_wrc_ignore_with_error_launch()

        if self.print_diagnostics:
            PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, <ignore> of node {self.relative_node_name} has been succesfully set to {ignore}")
       
    #def to_string_wrc_ignore(self) -> str:
    #    return f"<ignore>{self.get_wrc_ignore()}</ignore>"


    # ============================================
    # <already_existing_id> operations
    # It blantly translates to an <if_sid> considering it needs to be triggered over a pre-existing rule as soon as it is launched.
    # ============================================
    
    def get_wrc_already_existing_id(self) -> int:
        return self.already_existing_id

    def validate_wrc_already_existing_id(self) -> bool:
        # Type check
        if self.get_wrc_already_existing_id() is None:
            return True
        if not isinstance(self.get_wrc_already_existing_id(), int):
            return False
        # This needs to be used on pre-existing rules, so no other tag needs to be present
        for wrc_tag in self.__dict__.keys():
            # These are allowed to be given with already_existing_id
            if wrc_tag == "already_existing_id" or wrc_tag == "relative_node_name" or wrc_tag == 'description':
                continue
            if self.__dict__[wrc_tag] is None or (isinstance(self.__dict__[wrc_tag], bool) and self.__dict__[wrc_tag] == False):
                continue
            else:
                if self.print_diagnostics:
                    PrintUtils.print_in_red(f"- ERROR: <already_existing_id> is present, but another tag is given: <{wrc_tag}> with value {self.__dict__[wrc_tag]}.")
                return False
        return True

    def validate_wrc_already_existing_id_with_error_launch(self):
        if not self.validate_wrc_already_existing_id():
            error_prefix = f"The node {self.relative_node_name} failed validation on"
            error_suffix = f"was given instead."
            ExitUtils.exit_with_error(f"{error_prefix} <already_existing_id> in <wazuh_rule_config>. {WazuhRuleConfig.get_wrc_already_existing_id_allow_criteria()} {self.get_wrc_already_existing_id()} of type {type(self.get_wrc_already_existing_id())} {error_suffix}")
        
    @staticmethod
    def get_wrc_already_existing_id_allow_criteria() -> str:
        return "It must be an integer, and every other tag inside of <wazuh_rules_config> MUST NOT be present."

    def set_wrc_already_existing_id(self, already_existing_id : int):
        self.already_existing_id = already_existing_id

        self.validate_wrc_already_existing_id_with_error_launch()

        self.set_wrc_description(f"{self.get_wrc_description()+('.' if not self.get_wrc_description().endswith('.') else '') if self.get_wrc_description() is not None else ''} A rule to simply trigger consequent to the rule with id = {self.get_wrc_already_existing_id()}")
        if self.print_diagnostics:
            PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, <already_existing_id> of node {self.relative_node_name} has been succesfully set to {already_existing_id}")
       
    def to_string_wrc_already_existing_id(self) -> str:
        return f"<if_sid>{self.get_wrc_already_existing_id()}</if_sid>"


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

    def validate_wrc_match_with_error_launch(self) -> bool:
        if not self.validate_wrc_match():
            error_prefix = f"The node {self.relative_node_name} failed validation on"
            ExitUtils.exit_with_error(f"{error_prefix}: This does not need to be fancy, it is a back end issue. Do NOT initialize match as a list of non-Match objects.")


    def set_wrc_match(self, all_match : List[Match]):
        self.match = all_match

        self.validate_wrc_match_with_error_launch()

        if self.print_diagnostics:
            PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, all <match> entries of node {self.relative_node_name} have been succesfully set to: {([_.to_string() for _ in all_match]) if all_match is not None else None}")
        # else: is covered inside of match.validate_all() already

    def to_string_wrc_match(self, tab_times : int = 0) -> str:
        return f"{"\n".join([f"{'\t'*tab_times}{match.to_string()}" for match in self.get_wrc_match()])}"


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

    def validate_wrc_regex_with_error_launch(self) -> bool:
        if not self.validate_wrc_regex():
            error_prefix = f"The node {self.relative_node_name} failed validation on"
            ExitUtils.exit_with_error(f"{error_prefix}: This does not need to be fancy, it is a back end issue. Do NOT initialize regex as a list of non-Regex objects.")


    def set_wrc_regex(self, all_regex : List[Regex]):
        self.regex = all_regex

        self.validate_wrc_regex_with_error_launch()

        if self.print_diagnostics:
            PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, all <regex> entries of node {self.relative_node_name} have been succesfully set to: {([_.to_string() for _ in all_regex]) if all_regex is not None else None}")
        # else: is covered inside of regex.validate_all() already

    def to_string_wrc_regex(self, tab_times : int = 0) -> str:
        return f"{"\n".join([f"{'\t'*tab_times}{regex.to_string()}" for regex in self.get_wrc_regex()])}"


    # ============================================
    # <srcip> operations
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

    def validate_wrc_srcip_with_error_launch(self) -> bool:
        if not self.validate_wrc_srcip():
            error_prefix = f"The node {self.relative_node_name} failed validation on"
            ExitUtils.exit_with_error(f"{error_prefix}: This does not need to be fancy, it is a back end issue. Do NOT initialize srcip as a list of non-Srcip objects.")


    def set_wrc_srcip(self, all_srcip : List[Srcip]):
        self.srcip = all_srcip

        self.validate_wrc_srcip_with_error_launch()

        if self.print_diagnostics:
            PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, all <srcip> entries of node {self.relative_node_name} have been succesfully set to: {([_.to_string() for _ in all_srcip]) if all_srcip is not None else None}")
        # else: is covered inside of freqsrcip.validate_all() already

    def to_string_wrc_srcip(self) -> str:
        return f"{"\n".join([f"<{srcip}>" for srcip in self.get_wrc_srcip()])}"


    # ============================================
    # <dstip> operations
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

    def validate_wrc_dstip_with_error_launch(self) -> bool:
        if not self.validate_wrc_dstip():
            error_prefix = f"The node {self.relative_node_name} failed validation on"
            ExitUtils.exit_with_error(f"{error_prefix}: This does not need to be fancy, it is a back end issue. Do NOT initialize dstip as a list of non-Dstip objects.")


    def set_wrc_dstip(self, all_dstip : List[Dstip]):
        self.dstip = all_dstip

        self.validate_wrc_dstip_with_error_launch()

        if self.print_diagnostics:
            PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, all <dstip> entries of node {self.relative_node_name} have been succesfully set to: {([_.to_string() for _ in all_dstip]) if all_dstip is not None else None}")
        # else: is covered inside of freqdstip.validate_all() already

    def to_string_wrc_dstip(self) -> str:
        return f"{"\n".join([f"<{dstip}>" for dstip in self.get_wrc_dstip()])}"


    # ============================================
    # <srcport> operations
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

    def validate_wrc_srcport_with_error_launch(self) -> bool:
        if not self.validate_wrc_srcport():
            error_prefix = f"The node {self.relative_node_name} failed validation on"
            ExitUtils.exit_with_error(f"{error_prefix}: This does not need to be fancy, it is a back end issue. Do NOT initialize srcport as a list of non-Srcport objects.")


    def set_wrc_srcport(self, all_srcport : List[Srcport]):
        self.srcport = all_srcport

        self.validate_wrc_srcport_with_error_launch()

        if self.print_diagnostics:
            PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, all <srcport> entries of node {self.relative_node_name} have been succesfully set to: {([_.to_string() for _ in all_srcport]) if all_srcport is not None else None}")
        # else: is covered inside of freqsrcport.validate_all() already

    def to_string_wrc_srcport(self) -> str:
        return f"{"\n".join([f"<{srcport}>" for srcport in self.get_wrc_srcport()])}"


    # ============================================
    # <dstport> operations
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

    def validate_wrc_dstport_with_error_launch(self) -> bool:
        if not self.validate_wrc_dstport():
            error_prefix = f"The node {self.relative_node_name} failed validation on"
            ExitUtils.exit_with_error(f"{error_prefix}: This does not need to be fancy, it is a back end issue. Do NOT initialize dstport as a list of non-Dstport objects.")



    def set_wrc_dstport(self, all_dstport : List[Dstport]):
        self.dstport = all_dstport

        self.validate_wrc_dstport_with_error_launch()

        if self.print_diagnostics:
            PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, all <dstport> entries of node {self.relative_node_name} have been succesfully set to: {([_.to_string() for _ in all_dstport]) if all_dstport is not None else None}")
        # else: is covered inside of freqdstport.validate_all() already

    def to_string_wrc_dstport(self) -> str:
        return f"{"\n".join([f"<{dstport}>" for dstport in self.get_wrc_dstport()])}"


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

    def validate_wrc_time_with_error_launch(self):
        if not self.validate_wrc_time():
            error_prefix = f"The node {self.relative_node_name} failed validation on"
            error_suffix = f"was given instead."
            ExitUtils.exit_with_error(f"{error_prefix} <time> in <wazuh_rule_config>. {WazuhRuleConfig.get_wrc_time_allow_criteria()} {self.get_wrc_time()} of type {type(self.get_wrc_time())} {error_suffix}")


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

        self.validate_wrc_time_with_error_launch()

        if self.print_diagnostics:
            PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, <time> of node {self.relative_node_name} has been succesfully set to {time}")


    def to_string_wrc_time(self) -> str:
        return f"<time>{self.get_wrc_time()}</time>"


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

    def validate_wrc_weekday_with_error_launch(self):
        if not self.validate_wrc_weekday():
            error_prefix = f"The node {self.relative_node_name} failed validation on"
            error_suffix = f"was given instead."
            ExitUtils.exit_with_error(f"{error_prefix} <weekday> in <wazuh_rule_config>. {WazuhRuleConfig.get_wrc_weekday_allow_criteria()} {self.get_wrc_weekday()} of type {type(self.get_wrc_weekday())} {error_suffix}")


    @staticmethod
    def get_wrc_weekday_allow_criteria() -> str:

        return '''\n
It must be either "weekdays", "weekends", or match the "weekday - weekday" string,
where weekday is any day of the week in lowercase, such as "monday - sunday".\n
        '''

    def set_wrc_weekday(self, weekday : str):
        self.weekday = weekday

        self.validate_wrc_weekday_with_error_launch()

        if self.print_diagnostics:
            PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, <weekday> of node {self.relative_node_name} has been succesfully set to {weekday}")

    def to_string_wrc_weekday(self) -> str:
        return f"<weekday>{self.get_wrc_weekday()}</weekday>"


    # ============================================
    # <same_srcip> operations
    # ============================================
    
    def get_wrc_same_srcip(self) -> bool:
        return self.same_srcip

    def validate_wrc_same_srcip(self) -> bool:
        return isinstance(self.get_wrc_same_srcip(), bool)

    def validate_wrc_same_srcip_with_error_launch(self):
        if not self.validate_wrc_same_srcip():
            error_prefix = f"The node {self.relative_node_name} failed validation on"
            error_suffix = f"was given instead."
            ExitUtils.exit_with_error(f"{error_prefix} <freq_same_srcip> in <wazuh_rule_config>. {WazuhRuleConfig.get_wrc_same_srcip_allow_criteria()} {self.get_wrc_same_srcip()} of type {type(self.get_wrc_same_srcip())} {error_suffix}")
  

    @staticmethod
    def get_wrc_same_srcip_allow_criteria() -> str:
        return "Must just be <freq_same_srcip /> tag."

    def set_wrc_same_srcip(self, same_srcip : bool):
        self.same_srcip = same_srcip

        self.validate_wrc_same_srcip_with_error_launch()

        if self.print_diagnostics:
            PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, <freq_same_srcip> of node {self.relative_node_name} has been succesfully set to {same_srcip}")

    def to_string_wrc_same_srcip(self) -> str:
        return "<same_srcip />"


    # ============================================
    # <different_srcip> operations
    # ============================================
    
    def get_wrc_different_srcip(self) -> bool:
        return self.different_srcip

    def validate_wrc_different_srcip(self) -> bool:
        return isinstance(self.get_wrc_different_srcip(), bool)

    def validate_wrc_different_srcip_with_error_launch(self):
        if not self.validate_wrc_different_srcip():
            error_prefix = f"The node {self.relative_node_name} failed validation on"
            error_suffix = f"was given instead."
            ExitUtils.exit_with_error(f"{error_prefix} <freq_different_srcip> in <wazuh_rule_config>. {WazuhRuleConfig.get_wrc_different_srcip_allow_criteria()} {self.get_wrc_different_srcip()} of type {type(self.get_wrc_different_srcip())} {error_suffix}")

    @staticmethod
    def get_wrc_different_srcip_allow_criteria() -> str:
        return "Must just be <freq_different_srcip /> tag."

    def set_wrc_different_srcip(self, different_srcip : bool):
        self.different_srcip = different_srcip

        self.validate_wrc_different_srcip_with_error_launch()
        
        if self.print_diagnostics:
            PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, <freq_different_srcip> of node {self.relative_node_name} has been succesfully set to {different_srcip}")

    def to_string_wrc_different_srcip(self) -> str:
        return "<different_srcip />"


    # ============================================
    # <same_srcport> operations
    # ============================================

    def get_wrc_same_srcport(self) -> bool:
        return self.same_srcport

    def validate_wrc_same_srcport(self) -> bool:
        return isinstance(self.get_wrc_same_srcport(), bool)

    def validate_wrc_same_srcport_with_error_launch(self):
        if not self.validate_wrc_same_srcport():
            error_prefix = f"The node {self.relative_node_name} failed validation on"
            error_suffix = f"was given instead."
            ExitUtils.exit_with_error(f"{error_prefix} <freq_same_srcport> in <wazuh_rule_config>. {WazuhRuleConfig.get_wrc_same_srcport_allow_criteria()} {self.get_wrc_same_srcport()} of type {type(self.get_wrc_same_srcport())} {error_suffix}")

    @staticmethod
    def get_wrc_same_srcport_allow_criteria() -> str:
        return "Must just be <freq_same_srcport /> tag."

    def set_wrc_same_srcport(self, same_srcport : bool):
        self.same_srcport = same_srcport

        self.validate_wrc_same_srcport_with_error_launch()

        if self.print_diagnostics:
            PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, <freq_same_srcport> of node {self.relative_node_name} has been succesfully set to {same_srcport}")

    def to_string_wrc_same_srcport(self) -> str:
        return "<same_srcport />"


    # ============================================
    # <different_srcport> operations
    # ============================================

    def get_wrc_different_srcport(self) -> bool:
        return self.different_srcport

    def validate_wrc_different_srcport(self) -> bool:
        return isinstance(self.get_wrc_different_srcport(), bool)

    def validate_wrc_different_srcport_with_error_launch(self):
        if not self.validate_wrc_different_srcport():
            error_prefix = f"The node {self.relative_node_name} failed validation on"
            error_suffix = f"was given instead."
            ExitUtils.exit_with_error(f"{error_prefix} <freq_different_srcport> in <wazuh_rule_config>. {WazuhRuleConfig.get_wrc_different_srcport_allow_criteria()} {self.get_wrc_different_srcport()} of type {type(self.get_wrc_different_srcport())} {error_suffix}")
   

    @staticmethod
    def get_wrc_different_srcport_allow_criteria() -> str:
        return "Must just be <freq_different_srcport /> tag."

    def set_wrc_different_srcport(self, different_srcport : bool):
        self.different_srcport = different_srcport

        self.validate_wrc_different_srcport_with_error_launch()

        if self.print_diagnostics:
            PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, <freq_different_srcport> of node {self.relative_node_name} has been succesfully set to {different_srcport}")

    def to_string_wrc_different_srcport(self) -> str:
        return "<different_srcport />"


    # ============================================
    # <same_dstport> operations
    # ============================================

    def get_wrc_same_dstport(self) -> bool:
        return self.same_dstport

    def validate_wrc_same_dstport(self) -> bool:
        return isinstance(self.get_wrc_same_dstport(), bool)

    def validate_wrc_same_dstport_with_error_launch(self):
        if not self.validate_wrc_same_dstport():
            error_prefix = f"The node {self.relative_node_name} failed validation on"
            error_suffix = f"was given instead."
            ExitUtils.exit_with_error(f"{error_prefix} <freq_same_dstport> in <wazuh_rule_config>. {WazuhRuleConfig.get_wrc_same_dstport_allow_criteria()} {self.get_wrc_same_dstport()} of type {type(self.get_wrc_same_dstport())} {error_suffix}")


    @staticmethod
    def get_wrc_same_dstport_allow_criteria() -> str:
        return "Must just be <freq_same_dstport /> tag."

    def set_wrc_same_dstport(self, same_dstport : bool):
        self.same_dstport = same_dstport

        self.validate_wrc_same_dstport_with_error_launch()

        if self.print_diagnostics:
            PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, <freq_same_dstport> of node {self.relative_node_name} has been succesfully set to {same_dstport}")
        
    def to_string_wrc_same_dstport(self) -> str:
        return "<same_dstport />"
    

    # ============================================
    # <different_dstport> operations
    # ============================================

    def get_wrc_different_dstport(self) -> bool:
        return self.different_dstport

    def validate_wrc_different_dstport(self) -> bool:
        return isinstance(self.get_wrc_different_dstport(), bool)

    def validate_wrc_different_dstport_with_error_launch(self):
        if not self.validate_wrc_different_dstport():
            error_prefix = f"The node {self.relative_node_name} failed validation on"
            error_suffix = f"was given instead."
            ExitUtils.exit_with_error(f"{error_prefix} <freq_different_dstport> in <wazuh_rule_config>. {WazuhRuleConfig.get_wrc_different_dstport_allow_criteria()} {self.get_wrc_different_dstport()} of type {type(self.get_wrc_different_dstport())} {error_suffix}")


    @staticmethod
    def get_wrc_different_dstport_allow_criteria() -> str:
        return "Must just be <freq_different_dstport /> tag."

    def set_wrc_different_dstport(self, different_dstport : bool):
        self.different_dstport = different_dstport

        self.validate_wrc_different_dstport_with_error_launch()

        if self.print_diagnostics:
            PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, <freq_different_dstport> of node {self.relative_node_name} has been succesfully set to {different_dstport}")
        
    def to_string_wrc_different_dstport(self) -> str:
        return "<different_dstport />"


    # ============================================
    # <same_location> operations
    # ============================================

    def get_wrc_same_location(self) -> bool:
        return self.same_location

    def validate_wrc_same_location(self) -> bool:
        return isinstance(self.get_wrc_same_location(), bool)

    def validate_wrc_same_location_with_error_launch(self):
        if not self.validate_wrc_same_location():
            error_prefix = f"The node {self.relative_node_name} failed validation on"
            error_suffix = f"was given instead."
            ExitUtils.exit_with_error(f"{error_prefix} <freq_same_location> in <wazuh_rule_config>. {WazuhRuleConfig.get_wrc_same_location_allow_criteria()} {self.get_wrc_same_location()} of type {type(self.get_wrc_same_location())} {error_suffix}")


    @staticmethod
    def get_wrc_same_location_allow_criteria() -> str:
        return "Must just be <freq_same_location /> tag."

    def set_wrc_same_location(self, same_location : bool):
        self.same_location = same_location

        self.validate_wrc_same_location_with_error_launch()

        if self.print_diagnostics:
            PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, <freq_same_location> of node {self.relative_node_name} has been succesfully set to {same_location}")

    def to_string_wrc_same_location(self) -> str:
        return "<same_location />"

    # ============================================
    # <same_srcuser> operations
    # ============================================

    def get_wrc_same_srcuser(self) -> bool:
        return self.same_srcuser

    def validate_wrc_same_srcuser(self) -> bool:
        return isinstance(self.get_wrc_same_srcuser(), bool)

    def validate_wrc_same_srcuser_with_error_launch(self):
        if not self.validate_wrc_same_srcuser():
            error_prefix = f"The node {self.relative_node_name} failed validation on"
            error_suffix = f"was given instead."
            ExitUtils.exit_with_error(f"{error_prefix} <freq_same_srcuser> in <wazuh_rule_config>. {WazuhRuleConfig.get_wrc_same_srcuser_allow_criteria()} {self.get_wrc_same_srcuser()} of type {type(self.get_wrc_same_srcuser())} {error_suffix}")


    @staticmethod
    def get_wrc_same_srcuser_allow_criteria() -> str:
        return "Must just be <freq_same_srcuser /> tag."

    def set_wrc_same_srcuser(self, same_srcuser : bool):
        self.same_srcuser = same_srcuser

        self.validate_wrc_same_srcuser_with_error_launch()

        if self.print_diagnostics:
            PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, <freq_same_srcuser> of node {self.relative_node_name} has been succesfully set to {same_srcuser}")
        
    def to_string_wrc_same_srcuser(self) -> str:
        return "<same_srcuser />"
    

    # ============================================
    # <different_srcuser> operations
    # ============================================

    def get_wrc_different_srcuser(self) -> bool:
        return self.different_srcuser

    def validate_wrc_different_srcuser(self) -> bool:
        return isinstance(self.get_wrc_different_srcuser(), bool)

    def validate_wrc_different_srcuser_with_error_launch(self):
        if not self.validate_wrc_different_srcuser():
            error_prefix = f"The node {self.relative_node_name} failed validation on"
            error_suffix = f"was given instead."
            ExitUtils.exit_with_error(f"{error_prefix} <freq_different_srcuser> in <wazuh_rule_config>. {WazuhRuleConfig.get_wrc_different_srcuser_allow_criteria()} {self.get_wrc_different_srcuser()} of type {type(self.get_wrc_different_srcuser())} {error_suffix}")

    @staticmethod
    def get_wrc_different_srcuser_allow_criteria() -> str:
        return "Must just be <freq_different_srcuser /> tag."

    def set_wrc_different_srcuser(self, different_srcuser : bool):
        self.different_srcuser = different_srcuser

        self.validate_wrc_different_srcuser_with_error_launch()
        
        if self.print_diagnostics:
            PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, <freq_different_srcuser> of node {self.relative_node_name} has been succesfully set to {different_srcuser}")

    def to_string_wrc_different_srcuser(self) -> str:
        return "<different_srcuser />"

    # ============================================
    # <description> operations
    # ============================================

    def get_wrc_description(self) -> str:
        return self.description

    def validate_wrc_description(self) -> bool:
        return isinstance(self.get_wrc_description(), str)

    def validate_wrc_description_with_error_launch(self):
        if not self.validate_wrc_description():
            error_prefix = f"The node {self.relative_node_name} failed validation on"
            error_suffix = f"was given instead."
            ExitUtils.exit_with_error(f"{error_prefix} <description> in <wazuh_rule_config>. {WazuhRuleConfig.get_wrc_description_allow_criteria()} {self.get_wrc_description()} of type {type(self.get_wrc_description())} {error_suffix}")
   

    @staticmethod
    def get_wrc_description_allow_criteria() -> str:
        return "You must provide a description as a string! This is what will be seen in Wazuh Dashboard!"

    def set_wrc_description(self, description : str):
        self.description = description

        self.validate_wrc_description_with_error_launch()

        if self.print_diagnostics:
            PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, <description> of node {self.relative_node_name} has been succesfully set to {description}")
       
    def to_string_wrc_description(self) -> str:
        return f"<description>{self.get_wrc_description()}{'.' if not self.get_wrc_description().endswith('.') else ''}</description>"


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

    def validate_wrc_info_with_error_launch(self) -> bool:
        if not self.validate_wrc_info():
            error_prefix = f"The node {self.relative_node_name} failed validation on"
            ExitUtils.exit_with_error(f"{error_prefix}: This does not need to be fancy, it is a back end issue. Do NOT initialize info as a list of non-Info objects.")


    def set_wrc_info(self, all_info : List[Info]):
        self.info = all_info

        self.validate_wrc_info_with_error_launch()

        if self.print_diagnostics:
            PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, all <info> entries of node {self.relative_node_name} have been succesfully set to: {([_.to_string() for _ in all_info]) if all_info is not None else None}")
        # else: is covered inside of info.validate_all() already

    def to_string_wrc_info(self) -> str:
        return f"{"\n".join([f"<{info}>" for info in self.get_wrc_info()])}"


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
                    return False
                    #ExitUtils.exit_with_error(f"You cannot set <options> of node {self.relative_node_name} to {options} of type {type(options)}. {WazuhRuleConfig.get_wrc_options_allow_criteria()}")
        return True    
        
    def validate_wrc_options_with_error_launch(self) -> bool:
        if not self.validate_wrc_options():
            error_prefix = f"The node {self.relative_node_name} failed validation on"
            ExitUtils.exit_with_error(f"{error_prefix}: This does not need to be fancy, it is a back end issue. Do NOT initialize options as a list of non-String objects.")



    @staticmethod
    def get_wrc_options_allow_criteria() -> str:
        return 'Every <options> tag must contain one of the following strings: "alert_by_email", "no_email_alert", "no_log", "no_full_log", "no_counter".'

    def set_wrc_options(self, options : List[str]):
        self.options = options
        if self.validate_wrc_options():
            if self.print_diagnostics:
                PrintUtils.print_in_green(f"- Inside <wazuh_rule_config>, <options> of node {self.relative_node_name} has been succesfully set to {options}")
        # else: is covered inside of self.validate_wrc_options() already

    def to_string_wrc_options(self) -> str:
        return f"{"\n".join([f"<{options}>" for options in self.get_wrc_options()])}"

    # ========================================================================================
    # Out of <wazuh_rule_config>
    # ========================================================================================


    # ============================================
    # Validate All Node Tags
    # ============================================   


    def validate_all(self) -> bool:

        self.validate_wrc_frequency_with_error_launch()
                  
        self.validate_wrc_timeframe_with_error_launch()
           
        self.validate_wrc_ignore_with_error_launch()
        
        self.validate_wrc_already_existing_id_with_error_launch()
            
        self.validate_wrc_match()

        self.validate_wrc_regex()

        self.validate_wrc_srcip()

        self.validate_wrc_dstip()

        self.validate_wrc_srcport()

        self.validate_wrc_dstport()

        self.validate_wrc_time_with_error_launch()
            
        self.validate_wrc_weekday_with_error_launch()
            
        self.validate_wrc_same_srcip_with_error_launch()
            
        self.validate_wrc_different_srcip_with_error_launch()
            
        self.validate_wrc_same_srcport_with_error_launch()
            
        self.validate_wrc_different_srcport_with_error_launch()

        self.validate_wrc_same_dstport_with_error_launch()

        self.validate_wrc_different_dstport_with_error_launch()
            
        self.validate_wrc_same_location_with_error_launch()
            
        self.validate_wrc_same_srcuser_with_error_launch()
            
        self.validate_wrc_different_srcuser_with_error_launch()
            
        self.validate_wrc_description_with_error_launch()
            
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
            
            error_prefix = f"The node {self.relative_node_name} failed validation on"
            ExitUtils.exit_with_error(f"{error_prefix} 'at least one identifying tag must be given'.\n{allow_criteria_for_error_print}")           

        validate_at_least_one_identificator_present(self)




    # ============================================
    # General to_string
    # ============================================   

    def to_string(self, tab_times : int = 0):
        '''
        Method that returns a stringified version of the wazuh_rule_config part of the node.
        This is what will compose the rule itself.

        To populate id and level, replace
        PLACEHOLDER_ID with the id
        PLACEHOLDER_LEVEL with the level
        '''
        string   =   '\t'*tab_times + '<rule id="PLACEHOLDER_ID" level="PLACEHOLDER_LEVEL"'

        # Insert frequency=""
        if self.get_wrc_frequency() is not None:
            string  +=    f' frequency="{self.get_wrc_frequency()}"' # Optional
        # Insert timeframe=""
        if self.get_wrc_timeframe() is not None:
            string  +=   f' timeframe="{self.get_wrc_timeframe()}"' # Optional
        # Insert ignore=""
        if self.get_wrc_ignore() is not None:
            string  +=    f' ignore="{self.get_wrc_ignore()}"' # Optional

        string += '>\n' # Close the <rule> tag
        # Insert <description>
        if self.get_wrc_description() is not None:
            string      +=   '\t'*tab_times +  '\t'+self.to_string_wrc_description()+'\n'  # Mandatory


        # Insert <info>
        if self.get_wrc_info() is not None:
            string  +=    '\t'*tab_times + '\t'+self.to_string_wrc_info()+'\n' # Optional

        # Insert <if_sid> - Guard to save some processing time
        if self.get_wrc_already_existing_id() is not None:
            string  +=    '\t'*tab_times + '\t'+self.to_string_wrc_already_existing_id()+'\n' # Optional
            return string # Already done! No more to check, as this is a standalone tag.  


        # Insert <match>
        if self.get_wrc_match() is not None:
            string  +=    self.to_string_wrc_match(tab_times=tab_times+1)+'\n' # Optional    
        # Insert <regex>
        if self.get_wrc_regex() is not None:
            string  +=    self.to_string_wrc_regex(tab_times=tab_times+1)+'\n' # Optional    
        # Insert <srcip>
        if self.get_wrc_srcip() is not None:
            string  +=    '\t'*tab_times + '\t'+self.to_string_wrc_srcip()+'\n' # Optional   
        # Insert <dstip>
        if self.get_wrc_dstip() is not None:
            string  +=    '\t'*tab_times + '\t'+self.to_string_wrc_dstip()+'\n' # Optional   
        # Insert <srcport>
        if self.get_wrc_srcport() is not None:
            string  +=    '\t'*tab_times + '\t'+self.to_string_wrc_srcport()+'\n' # Optional   
        # Insert <dstport>
        if self.get_wrc_dstport() is not None:
            string  +=    '\t'*tab_times + '\t'+self.to_string_wrc_dstport()+'\n' # Optional   
        # Insert <time>
        if self.get_wrc_time() is not None:
            string  +=    '\t'*tab_times + '\t'+self.to_string_wrc_time()+'\n' # Optional   
        # Insert <weekday>
        if self.get_wrc_weekday() is not None:
            string  +=    '\t'*tab_times + '\t'+self.to_string_wrc_weekday()+'\n' # Optional   
        # Insert <same_srcip>
        if self.get_wrc_same_srcip():
            string  +=    '\t'*tab_times + '\t'+self.to_string_wrc_same_srcip()+'\n' # Optional 
        # Insert <different_srcip>
        if self.get_wrc_different_srcip():
            string  +=    '\t'*tab_times + '\t'+self.to_string_wrc_different_srcip()+'\n' # Optional 
        # Insert <same_srcport>
        if self.get_wrc_same_srcport():
            string  +=    '\t'*tab_times + '\t'+self.to_string_wrc_same_srcport()+'\n' # Optional   
        # Insert <different_srcport>
        if self.get_wrc_different_srcport():
            string  +=    '\t'*tab_times + '\t'+self.to_string_wrc_different_srcport()+'\n' # Optional         
        # Insert <same_dstport>
        if self.get_wrc_same_dstport():
            string  +=    '\t'*tab_times + '\t'+self.to_string_wrc_same_dstport()+'\n' # Optional    
        # Insert <different_dstport>
        if self.get_wrc_different_dstport():
            string  +=    '\t'*tab_times + '\t'+self.to_string_wrc_different_dstport()+'\n' # Optional 
        # Insert <same_location>
        if self.get_wrc_same_location():
            string  +=    '\t'*tab_times + '\t'+self.to_string_wrc_same_location()+'\n' # Optional
        # Insert <same_srcuser>
        if self.get_wrc_same_srcuser():
            string  +=    '\t'*tab_times + '\t'+self.to_string_wrc_same_srcuser()+'\n' # Optional 
        # Insert <different_srcuser>
        if self.get_wrc_different_srcuser():
            string  +=    '\t'*tab_times + '\t'+self.to_string_wrc_different_srcuser()+'\n' # Optional 
        # Insert <options>
        if self.get_wrc_options() is not None:
            string  +=    '\t'*tab_times + '\t'+self.to_string_wrc_options()+'\n' # Optional   

        string +=  '\t'*tab_times + '</rule>'
        return string


def test():
    w = WazuhRuleConfig()
    w.set_wrc_description("Very useful desc!")
    w.set_wrc_frequency(5)
    w.set_wrc_timeframe(10)
    w.set_wrc_time("9-19")
    w.validate_all()
    print(w.to_string())

if __name__ == '__main__':
    test()