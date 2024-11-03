from abc import ABC, abstractmethod
# Import scripts from above folder
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from terminal_UI_utils import PrintUtils, ExitUtils



class AbstractOptimality(ABC):

    @abstractmethod
    def __init__(self):
        ExitUtils.exit_with_error("YOU MUST NOT instanciate a AbstractOptimality object. NEVER.")

    # Getter
    def get_properties(self):
        return self.properties

    # Setter
    def set_properties(self, properties : dict):
        if not isinstance(properties, dict):
            ExitUtils.exit_with_error("Attempting to set 'properties' of a Optimality class to a non-dict element. Aborting.\n")
        self.properties = properties
    
    # Add a property to the properties dict
    def add_property(self, property_key, property_value):
        '''
        This works exactly as a dictionary insertion
        '''
        self.get_properties()[property_key] = property_value

    # Get the value of a property through the dictionary key
    def get_property_value(self, property_key):
        return self.get_properties().get(property_key)
    
    @abstractmethod
    def validate_all(self):
        '''
        Implement all of the validations for the properties here.
        '''
        pass