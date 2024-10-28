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

