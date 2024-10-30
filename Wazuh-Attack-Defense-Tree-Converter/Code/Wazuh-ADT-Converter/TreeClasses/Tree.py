from TreeNode import *

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


