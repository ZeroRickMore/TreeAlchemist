# Import scripts from above folder
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from WazuhRuleConfig import *



def test_description():
    w = WazuhRuleConfig()
    w.set_wrc_description(1)



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
    assert(wrc.validate_wrc_already_existing_id())      # This needs to work here

    # Assign frequency
    wrc.set_wrc_frequency(2)
    assert(not wrc.validate_wrc_already_existing_id())  # This should not work
    wrc.set_wrc_frequency(None) # Set back to normal

    # Assign timeframe
    wrc.set_wrc_timeframe(2)
    assert(not wrc.validate_wrc_already_existing_id())  # This should not work
    wrc.set_wrc_timeframe(None) # Set back to normal

    # Assign ignore
    wrc.set_wrc_ignore(7)
    assert(not wrc.validate_wrc_already_existing_id())  # This should not work
    wrc.set_wrc_ignore(None)    # Set back to normal

    # Assign match
    wrc.set_wrc_match([Match()])
    assert(not wrc.validate_wrc_already_existing_id())  # This should not work
    wrc.set_wrc_match(None)     # Set back to normal

    # Assign regex
    wrc.set_wrc_regex([Regex()])
    assert(not wrc.validate_wrc_already_existing_id())  # This should not work
    wrc.set_wrc_regex(None)     # Set back to normal

    # Assign srcip
    wrc.set_wrc_srcip([Srcip(srcip='0.0.0.0')])
    assert(not wrc.validate_wrc_already_existing_id())  # This should not work
    wrc.set_wrc_srcip(None)     # Set back to normal

    # Assign dstip
    wrc.set_wrc_dstip([Dstip(dstip='0.0.0.0')])
    assert(not wrc.validate_wrc_already_existing_id())  # This should not work
    wrc.set_wrc_dstip(None)     # Set back to normal

    # Assign srcport
    wrc.set_wrc_srcport([Srcport()])
    assert(not wrc.validate_wrc_already_existing_id())  # This should not work
    wrc.set_wrc_srcport(None)   # Set back to normal

    # Assign dstport
    wrc.set_wrc_dstport([Dstport()])
    assert(not wrc.validate_wrc_already_existing_id())  # This should not work
    wrc.set_wrc_dstport(None)   # Set back to normal

    # Assign time
    wrc.set_wrc_time('6-8')
    assert(not wrc.validate_wrc_already_existing_id())  # This should not work
    wrc.set_wrc_time(None)      # Set back to normal

    # Assign weekday
    wrc.set_wrc_weekday('weekdays')
    assert(not wrc.validate_wrc_already_existing_id())  # This should not work
    wrc.set_wrc_weekday(None)   # Set back to normal

    # Assign same_srcip
    wrc.set_wrc_same_srcip(True)
    assert(not wrc.validate_wrc_already_existing_id())  # This should not work
    wrc.set_wrc_same_srcip(False)    # Set back to normal

    # Assign different_srcip
    wrc.set_wrc_different_srcip(True)
    assert(not wrc.validate_wrc_already_existing_id())  # This should not work
    wrc.set_wrc_different_srcip(False) # Set back to normal

    # Assign same_srcport
    wrc.set_wrc_same_srcport(True)
    assert(not wrc.validate_wrc_already_existing_id())  # This should not work
    wrc.set_wrc_same_srcport(False)     # Set back to normal

    # Assign different_srcport
    wrc.set_wrc_different_srcport(True)
    assert(not wrc.validate_wrc_already_existing_id())  # This should not work
    wrc.set_wrc_different_srcport(False)    # Set back to normal

    # Assign same_dstport
    wrc.set_wrc_same_dstport(True)
    assert(not wrc.validate_wrc_already_existing_id())  # This should not work
    wrc.set_wrc_same_dstport(False)         # Set back to normal

    # Assign different_dstport
    wrc.set_wrc_different_dstport(True)
    assert(not wrc.validate_wrc_already_existing_id())  # This should not work
    wrc.set_wrc_different_dstport(False)    # Set back to normal

    # Assign same_location
    wrc.set_wrc_same_location(True)
    assert(not wrc.validate_wrc_already_existing_id())  # This should not work
    wrc.set_wrc_same_location(False)        # Set back to normal  

    # Assign same_srcuser
    wrc.set_wrc_same_srcuser(True)
    assert(not wrc.validate_wrc_already_existing_id())  # This should not work
    wrc.set_wrc_same_srcuser(False)         # Set back to normal

    # Assign different_srcuser
    wrc.set_wrc_different_srcuser(True)
    assert(not wrc.validate_wrc_already_existing_id())  # This should not work
    wrc.set_wrc_different_srcuser(False)    # Set back to normal

    # Assign info
    wrc.set_wrc_info([Info()])
    assert(not wrc.validate_wrc_already_existing_id())  # This should not work
    wrc.set_wrc_info(None)                  # Set back to normal

    # Assign options
    wrc.set_wrc_options(['no_log'])
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
    #test_already_existing_id_working()
    #test_already_existing_id_errors()
    test_description()

if __name__ == '__main__':
    test()