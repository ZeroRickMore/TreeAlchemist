from  StateClasses.StateDefense import StateDefense


class State:
    '''
    This class represents a state, which is a list of node IDs
    linked to a specific "Defense" object.
    '''

    print_diagnostics = True



    def __init__(self,
                description : str = None, # <description>
                nodes : tuple[int] = None, # <nodes>
                state_defense : StateDefense = None, # <defense>
                ):
        
        self.description = description
        self.nodes = nodes

        self.state_defense = state_defense

    

