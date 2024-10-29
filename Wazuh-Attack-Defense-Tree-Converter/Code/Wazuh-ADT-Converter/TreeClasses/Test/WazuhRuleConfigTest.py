# Import scripts from above folder
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from WazuhRuleConfig import *



def test_description():
    w = WazuhRuleConfig(description=1)
    # w.set_wrc_description(1) # It will just exit() straight forward due to implementation. Let's set it in constructor!
    assert(not w.validate_wrc_description())
    w = WazuhRuleConfig(description="Hello!")
    assert(w.validate_wrc_description())


def test_frequency():
    w = WazuhRuleConfig(wrc_frequency="Wrong place for a string")
    # w.set_wrc_frequency("A string again?!")
    assert(not w.validate_wrc_frequency())
    w = WazuhRuleConfig()
    w.set_wrc_frequency(None)
    assert(w.validate_wrc_frequency())
    w = WazuhRuleConfig()
    w.set_wrc_frequency(5)
    assert(w.validate_wrc_frequency())

def test_timeframe():
    w = WazuhRuleConfig(wrc_timeframe="Wrong place")
    assert(not w.validate_wrc_timeframe())
    w.set_wrc_timeframe(5)
    assert(w.validate_wrc_timeframe())
    w.set_wrc_timeframe(None)
    assert(w.validate_wrc_timeframe())

def test_ignore():
    w = WazuhRuleConfig(wrc_ignore_after="Wrong place")
    assert(not w.validate_wrc_ignore())
    w.set_wrc_ignore(5)
    assert(w.validate_wrc_ignore())
    w.set_wrc_ignore(None)
    assert(w.validate_wrc_ignore())

def test_match():
    w = WazuhRuleConfig(match_list="Wrong place")
    assert(not w.validate_wrc_match())
    w.set_wrc_match([Match()])
    assert(w.validate_wrc_match())
    w = WazuhRuleConfig(match_list=["Wrong place", "Not a list of strings"])
    assert(not w.validate_wrc_match())
    # w.set_wrc_match(["Wrong place", "Not a list of strings"]) # Exits
    # assert(not w.validate_wrc_match())
    w.set_wrc_match(None)
    assert(w.validate_wrc_match())

def test_regex():
    w = WazuhRuleConfig(regex_list="Wrong place")
    assert(not w.validate_wrc_regex())
    w.set_wrc_regex([Regex()])
    assert(w.validate_wrc_regex())
    w = WazuhRuleConfig(regex_list=["Wrong place", "Not a list of strings"])
    assert(not w.validate_wrc_regex())
    # w.set_wrc_regex(["Wrong place", "Not a list of strings"]) # Exits
    # assert(not w.validate_wrc_regex())
    w.set_wrc_regex(None)
    assert(w.validate_wrc_regex())

def test_srcip():
    w = WazuhRuleConfig(srcip_list="Wrong place")
    assert(not w.validate_wrc_srcip())
    # w.set_wrc_srcip([Srcip()]) # Exits. Give a valid srcip.
    #assert(w.validate_wrc_srcip())
    w = WazuhRuleConfig(srcip_list=["Wrong place", "Not a list of strings"])
    assert(not w.validate_wrc_srcip())
    # w.set_wrc_srcip(["Wrong place", "Not a list of strings"]) # Exits
    # assert(not w.validate_wrc_srcip())
    w.set_wrc_srcip(None)
    assert(w.validate_wrc_srcip())
    w.set_wrc_srcip([Srcip(srcip='10.0.0.0'), Srcip(srcip='20.0.0.0')]) # Exits. Give a valid srcip.
    assert(w.validate_wrc_srcip())

def test_dstip():
    w = WazuhRuleConfig(dstip_list="Wrong place")
    assert(not w.validate_wrc_dstip())
    # w.set_wrc_dstip([Dstip()]) # Exits. Give a valid dstip.
    #assert(w.validate_wrc_dstip())
    w = WazuhRuleConfig(dstip_list=["Wrong place", "Not a list of strings"])
    assert(not w.validate_wrc_dstip())
    # w.set_wrc_dstip(["Wrong place", "Not a list of strings"]) # Exits
    # assert(not w.validate_wrc_dstip())
    w.set_wrc_dstip(None)
    assert(w.validate_wrc_dstip())
    w.set_wrc_dstip([Dstip(dstip='10.0.0.0'), Dstip(dstip='20.0.0.0')]) # Exits. Give a valid dstip.
    assert(w.validate_wrc_dstip())

def test_srcport():
    w = WazuhRuleConfig(srcport_list="Wrong place")
    assert(not w.validate_wrc_srcport())
    w.set_wrc_srcport([Srcport()])
    assert(w.validate_wrc_srcport())
    w.set_wrc_srcport([Srcport(srcport="Ciao")])
    assert(w.validate_wrc_srcport())
    w = WazuhRuleConfig(srcport_list=["Wrong place", "Not a list of strings"])
    assert(not w.validate_wrc_srcport())
    # w.set_wrc_srcport(["Wrong place", "Not a list of strings"]) # Exits
    # assert(not w.validate_wrc_srcport())
    w.set_wrc_srcport(None)
    assert(w.validate_wrc_srcport())

def test_dstport():
    w = WazuhRuleConfig(dstport_list="Wrong place")
    assert(not w.validate_wrc_dstport())
    w.set_wrc_dstport([Dstport()])
    assert(w.validate_wrc_dstport())
    w.set_wrc_dstport([Dstport(dstport="Ciao")])
    assert(w.validate_wrc_dstport())
    w = WazuhRuleConfig(dstport_list=["Wrong place", "Not a list of strings"])
    assert(not w.validate_wrc_dstport())
    # w.set_wrc_dstport(["Wrong place", "Not a list of strings"]) # Exits
    # assert(not w.validate_wrc_dstport())
    w.set_wrc_dstport(None)
    assert(w.validate_wrc_dstport())


def test_already_existing_id_errors():
    wrc = WazuhRuleConfig()
    '''
    self.description        =   description
    self.already_existing_id=   wrc_already_existing_id
    self.relative_node_name =   relative_node_name
    self.frequency          =   wrc_frequency
    self.timeframe          =   wrc_timeframe
    self.ignore             =   wrc_ignore_after
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
    self.same_dstport       =   freq_same_dstport
    self.different_dstport  =   freq_different_dstport
    self.same_location      =   freq_same_location
    self.same_srcuser       =   freq_same_srcuser
    self.different_srcuser  =   freq_different_srcuser
    self.info               =   info
    self.options            =   options
    '''

    # Assign description and already_existing_id
    wrc.set_wrc_description("Error maximus") # This is prepended to the final desc
    wrc.set_wrc_already_existing_id(5401)
    assert(wrc.validate_wrc_already_existing_id())      # This needs to work here

    # Assign relative_node_name
    wrc.relative_node_name = 'Pippo'
    if wrc.print_diagnostics:
        print("Error expected:")
    assert(wrc.validate_wrc_already_existing_id())      # This needs to work here

    # Assign frequency
    wrc.set_wrc_frequency(2)
    if wrc.print_diagnostics:
        print("Error expected:")
    assert(not wrc.validate_wrc_already_existing_id())  # This should not work
    wrc.set_wrc_frequency(None) # Set back to normal

    # Assign timeframe
    wrc.set_wrc_timeframe(2)
    if wrc.print_diagnostics:
        print("Error expected:")
    assert(not wrc.validate_wrc_already_existing_id())  # This should not work
    wrc.set_wrc_timeframe(None) # Set back to normal

    # Assign ignore
    wrc.set_wrc_ignore(7)
    if wrc.print_diagnostics:
        print("Error expected:")
    assert(not wrc.validate_wrc_already_existing_id())  # This should not work
    wrc.set_wrc_ignore(None)    # Set back to normal

    # Assign match
    wrc.set_wrc_match([Match()])
    if wrc.print_diagnostics:
        print("Error expected:")
    assert(not wrc.validate_wrc_already_existing_id())  # This should not work
    wrc.set_wrc_match(None)     # Set back to normal

    # Assign regex
    wrc.set_wrc_regex([Regex()])
    if wrc.print_diagnostics:
        print("Error expected:")
    assert(not wrc.validate_wrc_already_existing_id())  # This should not work
    wrc.set_wrc_regex(None)     # Set back to normal

    # Assign srcip
    wrc.set_wrc_srcip([Srcip(srcip='0.0.0.0')])
    if wrc.print_diagnostics:
        print("Error expected:")
    assert(not wrc.validate_wrc_already_existing_id())  # This should not work
    wrc.set_wrc_srcip(None)     # Set back to normal

    # Assign dstip
    wrc.set_wrc_dstip([Dstip(dstip='0.0.0.0')])
    if wrc.print_diagnostics:
        print("Error expected:")
    assert(not wrc.validate_wrc_already_existing_id())  # This should not work
    wrc.set_wrc_dstip(None)     # Set back to normal

    # Assign srcport
    wrc.set_wrc_srcport([Srcport()])
    if wrc.print_diagnostics:
        print("Error expected:")
    assert(not wrc.validate_wrc_already_existing_id())  # This should not work
    wrc.set_wrc_srcport(None)   # Set back to normal

    # Assign dstport
    wrc.set_wrc_dstport([Dstport()])
    if wrc.print_diagnostics:
        print("Error expected:")
    assert(not wrc.validate_wrc_already_existing_id())  # This should not work
    wrc.set_wrc_dstport(None)   # Set back to normal

    # Assign time
    wrc.set_wrc_time('6-8')
    if wrc.print_diagnostics:
        print("Error expected:")
    assert(not wrc.validate_wrc_already_existing_id())  # This should not work
    wrc.set_wrc_time(None)      # Set back to normal

    # Assign weekday
    wrc.set_wrc_weekday('weekdays')
    if wrc.print_diagnostics:
        print("Error expected:")
    assert(not wrc.validate_wrc_already_existing_id())  # This should not work
    wrc.set_wrc_weekday(None)   # Set back to normal

    # Assign same_srcip
    wrc.set_wrc_same_srcip(True)
    if wrc.print_diagnostics:
        print("Error expected:")
    assert(not wrc.validate_wrc_already_existing_id())  # This should not work
    wrc.set_wrc_same_srcip(False)    # Set back to normal

    # Assign different_srcip
    wrc.set_wrc_different_srcip(True)
    if wrc.print_diagnostics:
        print("Error expected:")
    assert(not wrc.validate_wrc_already_existing_id())  # This should not work
    wrc.set_wrc_different_srcip(False) # Set back to normal

    # Assign same_srcport
    wrc.set_wrc_same_srcport(True)
    if wrc.print_diagnostics:
        print("Error expected:")
    assert(not wrc.validate_wrc_already_existing_id())  # This should not work
    wrc.set_wrc_same_srcport(False)     # Set back to normal

    # Assign different_srcport
    wrc.set_wrc_different_srcport(True)
    if wrc.print_diagnostics:
        print("Error expected:")
    assert(not wrc.validate_wrc_already_existing_id())  # This should not work
    wrc.set_wrc_different_srcport(False)    # Set back to normal

    # Assign same_dstport
    wrc.set_wrc_same_dstport(True)
    if wrc.print_diagnostics:
        print("Error expected:")
    assert(not wrc.validate_wrc_already_existing_id())  # This should not work
    wrc.set_wrc_same_dstport(False)         # Set back to normal

    # Assign different_dstport
    wrc.set_wrc_different_dstport(True)
    if wrc.print_diagnostics:
        print("Error expected:")
    assert(not wrc.validate_wrc_already_existing_id())  # This should not work
    wrc.set_wrc_different_dstport(False)    # Set back to normal

    # Assign same_location
    wrc.set_wrc_same_location(True)
    if wrc.print_diagnostics:
        print("Error expected:")
    assert(not wrc.validate_wrc_already_existing_id())  # This should not work
    wrc.set_wrc_same_location(False)        # Set back to normal  

    # Assign same_srcuser
    wrc.set_wrc_same_srcuser(True)
    if wrc.print_diagnostics:
        print("Error expected:")
    assert(not wrc.validate_wrc_already_existing_id())  # This should not work
    wrc.set_wrc_same_srcuser(False)         # Set back to normal

    # Assign different_srcuser
    wrc.set_wrc_different_srcuser(True)
    if wrc.print_diagnostics:
        print("Error expected:")
    assert(not wrc.validate_wrc_already_existing_id())  # This should not work
    wrc.set_wrc_different_srcuser(False)    # Set back to normal

    # Assign info
    wrc.set_wrc_info([Info()])
    if wrc.print_diagnostics:
        print("Error expected:")
    assert(not wrc.validate_wrc_already_existing_id())  # This should not work
    wrc.set_wrc_info(None)                  # Set back to normal

    # Assign options
    wrc.set_wrc_options(['no_log'])
    if wrc.print_diagnostics:
        print("Error expected:")
    assert(not wrc.validate_wrc_already_existing_id())  # This should not work
    wrc.set_wrc_options(None)               # Set back to normal


def test_already_existing_id_working():
    '''
    This prints:

    <description>Hello!. A rule to simply trigger consequent to the rule with id = 5401.</description>
    <if_sid>5401</if_sid>

    As expected.
    '''
    wrc = WazuhRuleConfig()
    wrc.set_wrc_description("Hello!") # This is prepended to the final desc
    wrc.set_wrc_already_existing_id(5401)
    wrc.validate_wrc_already_existing_id() # This needs to work
    #print(wrc.to_string())


def test():
    test_already_existing_id_working()
    test_already_existing_id_errors()
    test_description()
    test_frequency()
    test_timeframe()
    test_ignore()
    test_match()
    test_regex()
    test_srcip()
    test_dstip()
    test_srcport()
    test_dstport()
    # This is getting repetitive. The rest are all the same...

if __name__ == '__main__':
    test()
    pass

