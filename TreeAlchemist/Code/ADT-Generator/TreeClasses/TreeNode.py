from TreeClasses.TreeNodeInformations import TreeNodeInformations
from typing import List

# Import scripts from above folder
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from terminal_UI_utils import PrintUtils, ExitUtils

class TreeNode:

    '''
    This class represents a node in the ADT.
    '''
    print_diagnostics = True

    def __init__(self, informations : TreeNodeInformations = None):
        self.informations = informations
        self.children : List['TreeNode'] = []

    def add_child(self, child_node : 'TreeNode'):
        '''
        Add a TreeNode child to a TreeNode.
        
        Exits if the child was already present.
        Of course, you do NOT want duplicates.
        '''
        if self.is_child_present(child_node=child_node):
            ExitUtils.exit_with_error(f"Cannot add child node with name {child_node.get_informations().get_name()} and id {child_node.get_informations().get_id()}\nas it is already present in parent node with name {self.get_informations().get_name()} and id {self.get_informations().get_id()}")
        self.children.append(child_node)

    def is_child_present(self, child_node : 'TreeNode'):
        '''
        Checks if the given child node is already into self.
        '''
        return child_node in self.get_children()

    def get_informations(self) -> TreeNodeInformations:
        return self.informations
    
    def set_informations(self, info : TreeNodeInformations ):
        self.informations = info

        self.get_informations().validate_all()

    def get_children(self) -> List['TreeNode']:
        return self.children
    
    def set_children(self, children):
        ExitUtils.exit_with_error("DO NOT use set_children(). Rather, use add_child().")


    def to_string(self, tab_times : int = 0) -> str:
        '''
        Method that returns a stringified version of the whole node.
        This is what will compose the rule itself.

        Let's be clear: it is just composed of the entries of his node informatons.
        '''

        return self.get_informations().to_string(tab_times=tab_times)
    

    def to_string_minimal(self):
        return f"{self.get_informations().get_name()}___ID={self.get_informations().get_id()}"
    
    def to_string_minimal_children(self):
        n = '\n'
        return f"{n.join(_.to_string_minimal() for _ in self.get_children())}"
    

    def to_string_with_subnodes(self) -> str:
        # Start the string for this node with indentation based on depth
        if self is None:
            return ''
        string = ''
        string += self.to_string(tab_times=1)

        # Recursively add each child's string with increased depth
        for child in self.children:
            string += child.to_string_with_subnodes()
        
        return string