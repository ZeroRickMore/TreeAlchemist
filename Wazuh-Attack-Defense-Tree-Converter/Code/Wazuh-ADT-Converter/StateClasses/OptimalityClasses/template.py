'''
DO NOT import this class.
If imported, it will throw a fat error saying you should not use this.

This is merely a template to quickly write OptimalityClasses
'''
# Import scripts from above folder
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from terminal_UI_utils import PrintUtils, ExitUtils

ExitUtils.exit_with_error("YOU MUST NOT IMPORT ANYTHING FROM template.py.\nThis is merely a template class.\n")




# ============================================================================
#               TEMPLATE FROM HERE
# ============================================================================


from AbstractOptimality import AbstractOptimality

# modify class name to what you are introducing
class OPTIMALITY_NAME(AbstractOptimality):
    '''
    Identified by Optimality_Type = OPTIMALITY_NAME

    List of properties:
    - PROPERTY_NAME : PROPERTY_TYPE = PROPERTY_DESCRIPTION
    
    '''

    def __init__(self,
                 # properties here
                 ):
        self.properties = {}
        # Initialize every property here

    def validate_PROPERTYKEY(self):
        # Insert the validation for a key of "properties" dict
        return True

    def validate_all(self):
        # Every validation for the properties.
        # "properties" is a dictionary, and all the methods to
        # use it are inside of the AbstractOptimality class.
        pass
    
