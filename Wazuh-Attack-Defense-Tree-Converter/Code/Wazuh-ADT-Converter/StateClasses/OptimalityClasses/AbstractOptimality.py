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

    print_diagnostics = True

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


    def find_key_and_return_value(self, dictionary: dict, needed_key: str) -> dict:
        """
        Recursively searches for a specified key in a nested dictionary or list.

        :param dictionary: The dictionary to search through. Use self.get_properties() here.
        :param needed_key: The key to find. It is one of your XML tags inside of <defense> and its children.
        :return: The value if it's found, else None.
        """
        if not isinstance(dictionary, (dict, list)):
            return None

        # If the current element is a dictionary
        if isinstance(dictionary, dict):
            # Check if the key is in the current dictionary
            if needed_key in dictionary:
                return dictionary[needed_key]

            # Recursively check each value in the dictionary
            for value in dictionary.values():
                res = self.find_key_and_return_value(value, needed_key)
                if res is not None:
                    return res

        # If the current element is a list
        elif isinstance(dictionary, list):
            # Recursively check each item in the list
            for item in dictionary:
                res = self.find_key_and_return_value(item, needed_key)
                if res is not None:
                    return res

        return None


    # Get the value of a property through the dictionary key
    def get_property_value_attribute_no_duplicate_tags_traversed(self, property_key, property_attribute):
        '''
        Useful if and only if the tag you are looking for traverses
        and xpath composed of tags that DO NOT repeat.

        If they do repeat, the first occurence is taken, but this hasn't been throughly tested so don't play with it too much...

        [ UNIQUE TAGS ONLY !!!]

        It is EXTREMELY recommended not to duplicate tags in the xml property section.
        If needed, use the dictionary syntax and not the methods provided.
        '''
        
        # Note that we use [0] to access the first occurrence of the tag.
        # This is EXACTLY why this method is UNIQUE TAGS ONLY, because first occurrence in this case is also the only one.
        value = self.find_key_and_return_value(dictionary=self.get_properties(), needed_key=property_key)[0].get('attributes').get(property_attribute)
        
        return value
        
        #ExitUtils.exit_with_error(f"Attemped to get attribute with key {property_key} in dict :\n\n{self.get_properties()}\n\nbut not found")
    


    # Get the text of a property through the dictionary key
    def get_property_value_text_no_duplicate_tags_traversed(self, property_key):
        '''
        Useful if and only if the tag you are looking for traverses
        and xpath composed of tags that DO NOT repeat.

        If they do repeat, the first occurence is taken, but this hasn't been throughly tested so don't play with it too much...

        [ UNIQUE TAGS ONLY !!!]

        It is EXTREMELY recommended not to duplicate tags in the xml property section.
        If needed, use the dictionary syntax and not the methods provided.
        '''

        # Note that we use [0] to access the first occurrence of the tag.
        # This is EXACTLY why this method is UNIQUE TAGS ONLY, because first occurrence in this case is also the only one.
        value = self.find_key_and_return_value(dictionary=self.get_properties(), needed_key=property_key)[0].get('text')

        if value is not None:
            return value
        
        ExitUtils.exit_with_error(f"Attemped to get text with key {property_key} in dict :\n\n{self.get_properties()}\n\nbut not found")
    
    @abstractmethod
    def validate_all(self):
        '''
        Implement all of the validations for the properties here.
        '''
        pass

    def to_string(self, tab_times : int = 0):
        give_tabs = '\t'*tab_times
        return f"{give_tabs}Optimality ======================\n{give_tabs}\tClass: {type(self)}\n{give_tabs}\tVariables: { {k: v for k, v in vars(self).items() if k != 'properties' }}\n{give_tabs}\tProperties: {self.get_properties()}"
    
