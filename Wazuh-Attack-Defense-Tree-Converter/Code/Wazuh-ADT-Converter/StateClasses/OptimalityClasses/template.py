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

# Import scripts from above folder
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from terminal_UI_utils import PrintUtils, ExitUtils
from StateClasses.OptimalityClasses.AbstractOptimality import AbstractOptimality

# modify class name to what you are introducing
class OPTIMALITY_NAME(AbstractOptimality):
    '''
    Identified by Optimality_Type = OPTIMALITY_NAME

    List of properties:
    - PROPERTY_NAME : PROPERTY_TYPE = PROPERTY_DESCRIPTION
    
    '''

    def validate_all(self):
        # Every validation for the properties.
        # "properties" is a dictionary, and all the methods to
        # use it are inside of the AbstractOptimality class.
        # self.set_instance_variables_from_properties() # Only if implementing the later explained method
        pass


    # OPTIONAL ==========================================

    # OPTIONAL validate_all() support methods
    def validate_PROPERTYKEY(self):
        # Insert the validation for a key of "properties" dict
        # NOTE: The type of everything will be "str" as it's taken from the xml as-is.
        # For better validation, I STRONGLY recommend using instance variables set through a method 
        # that you may call "set_instance_variables_from_properties(self)"
        # as explained later
        
        return True
    
    
    # OPTIONAL set instance variables so that validation and interrogation is way easier
    def set_instance_variables_from_properties(self):
        VARIABLE_NAME = self.get_property_value_text_no_duplicate_tags_traversed(property_key='VARIABLE_NAME')
        self.VARIABLE_NAME = int(VARIABLE_NAME) # "int" is just an example of setting the type to whatever you need
        # This way, you can set the type and have easier access to it, not going through the verbose dict interrogation.
        pass
    
    # OPTIONAL getters (NOT SETTERS). well, setters are strongly not recommended, you should use the xml for this.
    def get_PROPERTYKEY_PROPERTYATTRIBUTE(self):
        # You either used self.set_instance_variables_from_properties() so you can access the variables normally (return self.variable_name)
        # or you can interrogate the properties:
        # self.get_property_value_text_no_duplicate_tags_traversed(property_key='PROPERTYKEY') for content like this: <tag>content</tag>
        # self.get_property_value_attribute_no_duplicate_tags_traversed(property_key='PROPERTYKEY', property_attribute='PROPERTYATTRIBUTE') for content like this: <tag any_attribute="content"></tag>
        # Full example:
        # def get_defense_id(self):
        #       return self.get_property_value_attribute_no_duplicate_tags_traversed(property_key='defense', property_attribute='id')
        
        pass