# ============================================
# repetitive validate operations for TreeNodeInformations and TagClasses
# ============================================

def is_allowed(allowed_values : list, string : str) -> bool:
    '''
    Check if the given string is one of the ones in allowed_values list
    '''
    for allowed_value in allowed_values:
        if string == allowed_value:
            return True
    return False 

def is_yes_or_no(string : str) -> bool:
    '''
    Check if the given string is one of ["yes", "no"]
    '''
    allowed_values = ["yes", "no"]
    return is_allowed(allowed_values=allowed_values, string=string)

def is_osmatch_osregex_pcre2(string : str) -> bool:
    '''
    Check if the given string is one of ["osmatch", "osregex", "pcre2"]
    '''
    allowed_values = ["osmatch", "osregex", "pcre2"]
    return is_allowed(allowed_values=allowed_values, string=string)


def is_ip_address(string : str) -> bool:
    '''
    Check if the given string is a valid IPv4 or IPv6 address
    '''
    return is_valid_ipv4(ip = string) or is_valid_ipv6(ip = string)

import ipaddress

def is_valid_ipv4(ip : str) -> bool:
    try:
        # Try to create an IPv4 address object
        ip = ipaddress.IPv4Address(ip)
        return True
    except ipaddress.AddressValueError:
        # If an exception is raised, the address is not valid
        return False


def is_valid_ipv6(ip : str) -> bool:
    try:
        # Try to create an IPv6 address object
        ip = ipaddress.IPv6Address(ip)
        return True
    except ipaddress.AddressValueError:
        # If an exception is raised, the address is not valid
        return False


import re
def is_time_interval(string : str) -> bool:

    # Define the list of regex patterns
    patterns = [
        r'\b([0-9]{1,2}:[0-5][0-9])\-([0-9]{1,2}:[0-5][0-9])\b',         # hh:mm-hh:mm
        r'\b([0-9]{1,2}:[0-5][0-9]\s?(?:am|pm))\-([0-9]{1,2}:[0-5][0-9]\s?(?:am|pm))\b',  # hh:mm am-hh:mm pm
        r'\b([0-9]{1,2})\-([0-9]{1,2})\b',                                 # hh-hh
        r'\b([0-9]\s?(?:am|pm))\-([0-9]\s?(?:am|pm))\b',                   # h am-h pm
        r'\b([0-9]:[0-5][0-9])\-([0-9]:[0-5][0-9])\b',                     # h:mm-h:mm
        r'\b([0-9]:[0-5][0-9]\s?(?:am|pm))\-([0-9]:[0-5][0-9]\s?(?:am|pm))\b',  # h:mm am-h:mm pm
        r'\b([0-9])\-([0-9])\b',                                           # h-h
        r'\b([0-9]\s?(?:am|pm))\-([0-9]\s?(?:am|pm))\b'                    # h am-h pm
    ]


    # Check if the string matches any of the patterns
    for pattern in patterns:
        if re.match(pattern, string, re.IGNORECASE):
            return True
    return False




def test_time_interval():
    test_strings = [
        "09:30-10:30",
        "9:00 am-10:00 pm",
        "8-9",
        "7 pm-8 am",
        "2:15-3:45",
        "4:15 am-5:30 pm",
        "5-6",
        "3 am-4 pm",
        "not a time format"
    ]

    # Test each string
    for s in test_strings:
        print(f"{s}: {is_time_interval(s)}")

