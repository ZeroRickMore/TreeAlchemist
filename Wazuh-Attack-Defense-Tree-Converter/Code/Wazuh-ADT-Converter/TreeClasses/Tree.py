# Annoying way to make the import always work
import sys
import os
# Get the directory where the current file is located
current_directory = os.path.dirname(os.path.abspath(__file__))
# Append the current directory to sys.path
sys.path.append(current_directory)
from TreeClasses.TreeNode import TreeNode
from terminal_UI_utils import PrintUtils

class Tree:
    '''
    The actual ADT.
    '''

    def __init__(self, root_node: TreeNode = None):
        # Initialize the tree with a root node
        self.root = root_node

    def find_node_by_id(self, id_to_check : int):
        '''
        Starts looking for a node through his ID starting from root going downwards.
        '''
        return self.find_node_by_id_rec(current_node=self.get_root(), id_to_check=id_to_check)

    def find_node_by_id_rec(self, current_node: TreeNode, id_to_check: int):
        '''
        Starts looking for a node through his ID starting from current_node going downwards.
        '''
        # Check the current node's ID and traverse its children
        if current_node.get_informations().get_id() == id_to_check:
            return current_node
        for child in current_node.children:
            res = self.find_node_by_id(child, id_to_check)
            if res is not None:
                return res
        return None

    def get_root(self) -> TreeNode:
        return self.root
    
    def set_root(self, root_node : TreeNode):
        self.root = root_node

        root_node.get_informations().validate_all()


    def get_rule_group(self) -> str:
        '''
        The role groups are 'ADT' and the name of the root node.
        '''
        return self.get_root().get_informations().get_name() + ', ADTCVT, '
 


    def to_string(self) -> str:
        
        tab_times = 0

        string = ''
        # Insert group name tag
        string += f'<group name="{self.get_rule_group()}">\n'

        tab_times += 1

        # TODO

    
    def print_tree_for_debug(self):
        # Helper function to recursively print the tree
        def print_subtree(node : TreeNode, depth=0):
            if node is None:
                return
            
            # Indentation and structure for current node
            prefix = "\t" * depth + ("└── " if depth > 0 else "")
            PrintUtils.print_in_sky_blue(f"{prefix}{node.get_informations().get_name()}", end="")

            # Recursively print each child
            for child in node.children:
                print_subtree(child, depth + 1)

        print_subtree(self.root)


    def print_tree_for_debug_with_explicit_nodes(self):
        # Helper function to recursively print the tree
        def print_subtree(node : TreeNode, depth=0):
            if node is None:
                return
            
            # Indentation and structure for current node
            
            prefix = "\t\t" * depth + ("└─────  " if depth > 0 else "")
            rules_tab_depth = depth + 2
            give_tabs_to_rules =  "\t" * rules_tab_depth
            prefix = f"{prefix}{node.to_string_minimal()}\n\n{give_tabs_to_rules}==================\n"
            to_print = f"{node.get_informations().to_string_raw(tab_times=rules_tab_depth)}\n"
            suffix = f"{give_tabs_to_rules}==================\n"

            print(prefix)
            PrintUtils.print_on_a_number_chosen_color(text=to_print, end="", num=depth)
            print(suffix)

            # Recursively print each child
            for child in node.children:
                print_subtree(child, depth + 1)

        print_subtree(self.root)

