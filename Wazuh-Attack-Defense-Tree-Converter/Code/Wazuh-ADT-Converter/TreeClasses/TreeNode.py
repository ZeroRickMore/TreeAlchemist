from terminal_UI_utils import PrintUtils, ExitUtils
import TreeNodeInformations

class TreeNode:
    '''
    This class represents a node in the ADT.
    '''

    def __init__(self, informations : TreeNodeInformations = TreeNodeInformations()):
        self.informations = informations
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def __repr__(self, level=0):
        # A string representation of the tree for easy visualization
        ret = "  " * level + f"{self.informations.to_string()}\n"
        for child in self.children:
            ret += child.__repr__(level + 1)
        return ret
