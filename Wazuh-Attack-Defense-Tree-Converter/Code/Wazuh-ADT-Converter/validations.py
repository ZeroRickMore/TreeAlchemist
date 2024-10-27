# ============================================
# repetitive validate operations for TreeNodeInformations and TagClasses
# ============================================

def is_allowed(allowed_values : list, string : str) -> bool:
    for allowed_value in allowed_values:
        if string == allowed_value:
            return True
    return False 

def is_yes_or_no(string : str) -> bool:
    allowed_values = ["yes", "no"]
    return is_allowed(allowed_values=allowed_values, string=string)

def is_osmatch_osregex_pcre2(string : str) -> bool:
    allowed_values = ["osmatch", "osregex", "pcre2"]
    return is_allowed(allowed_values=allowed_values, string=string)