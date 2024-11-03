from abc import ABC, abstractmethod
# Import scripts from above folder
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from terminal_UI_utils import PrintUtils, ExitUtils



class AbstractOptimality(ABC):
    '''
    Note that the generation of self.properties should ONLY be done
    through the method generate_properties_dict() inside of states_to_defenses_parser.py

    Any other usage is not directly supported, nor recommended.
    '''

    def __init__(self):
        self.properties : dict = {}

    # Getter
    def get_properties(self) -> dict:
        return self.properties

    # Setter
    def set_properties(self, properties : dict):
        if not isinstance(properties, dict):
            ExitUtils.exit_with_error("Attempting to set 'properties' of a Optimality class to a non-dict element. Aborting.\n")
        self.properties = properties




    def find_key_and_return_value(self, data : dict, needed_key : str) -> dict:
        """
        Recursively searches for a specified key in a nested dictionary.

        :param data: The dictionary to search through. Use self.get_properties() here.
        :param needed_key: The key to find. It is one of your xml tags inside of <defense> and its children.
        :return: the value if it's found, else None
        """
        if not isinstance(data, dict):
            return None

        # Check if the key is in the current dictionary
        if needed_key in data:
            return data[needed_key]

        # Recursively check each value
        for value in data.values():
            if isinstance(value, dict):
                res = self.find_key_and_return_value(value, needed_key)
                if res is not None:
                    return res

        return None


    # Get the value of a property through the dictionary key
    def get_property_value_attribute_no_duplicate_tags_traversed(self, property_key):
        '''
        Useful if and only if the tag you are looking for traverses
        and xpath composed of tags that DO NOT repeat.

        [ UNIQUE TAGS ONLY !!!]

        It is EXTREMELY recommended not to duplicate tags in the xml property section.
        If needed, use the dictionary syntax and not the methods provided.
        '''
        
        value = self.find_key_and_return_value(data=self.get_properties(), needed_key=property_key).get('attribute')

        if value is not None:
            return value
        
        ExitUtils.exit_with_error(f"Attemped to get attribute with key {property_key} in dict :\n\n{self.get_properties()}\n\nbut not found")
    

    
    # Get the text of a property through the dictionary key
    def get_property_value_text(self, property_key):
        '''
        Useful if and only if the tag you are looking for traverses
        and xpath composed of tags that DO NOT repeat.

        [ UNIQUE TAGS ONLY !!!]

        It is EXTREMELY recommended not to duplicate tags in the xml property section.
        If needed, use the dictionary syntax and not the methods provided.
        '''
        
        value = self.find_key_and_return_value(data=self.get_properties(), needed_key=property_key).get('text')

        if value is not None:
            return value
        
        ExitUtils.exit_with_error(f"Attemped to get text with key {property_key} in dict :\n\n{self.get_properties()}\n\nbut not found")
    
    @abstractmethod
    def validate_all(self):
        '''
        Implement all of the validations for the properties here.
        '''
        pass