'''
This script generates the rules that will match for the states.


A state is defined by all the rules that match the very last <if_sid>
So, if I have 3 nodes composing a state, the state will be composed of 3 possible rules,
each having a different <if_sid> and <if_matched_sid> as the remaining two nodes.

To trigger a active-response, I will use <if_sid> listing all the nodes composing it.

What will happen is:
3 rules that will match the whole state, matching also the very last rule triggered (the rule having <if_sid> will act like a trigger for that one one too)
    The rule with that one <if_sid> will be launching the active-response for that single node if present and if it has a better Optimality.
    The active-response mapped to that one <if_sid> will have both the original single node and THIS new rule state separated by a comma.
The active-response mapped to the state [ curr_state.get_state_defense().get_defense() ] in the very fist place will have <if_sid> with these 3 newly defined rules.    
 
So, an implementation idea would be:

for each curr_state in all_states:
    curr_def = curr_state.get_defense()
    for each node_id in curr_state.get_node_ids():
        curr_node = node_id_to_node.get(node_id) # Add check
        if curr_node is None: throw error saying a node id is wrong
'''
from typing import List

from StateClasses.State import State

from TreeClasses.Tree import Tree
from TreeClasses.TreeNode import TreeNode

def generate_state_rules(node_id_to_node : dict[int, TreeNode], 
                        adt : Tree,
                        all_states: List[State]
                        ):


    for curr_state in all_states: # Iterate over each State

        curr_def = curr_state.get_state_defense().get_defense()
        curr_node_ids = curr_state.get_node_ids()

        # Is there just a single node?
        if len(curr_node_ids) == 1:
            node_id = curr_node_ids[0]
            curr_node = node_id_to_node.get(node_id)
            old_rules_id = curr_def.get_rules_id()
            if old_rules_id != '': # Some rules are already set
                if not old_rules_id.endswith(','):
                    new_rules_id = f'{old_rules_id}, '
                    curr_def.set_rules_id(new_rules_id) # Update to add a comma at the end, to append the current rule
                    old_rules_id = new_rules_id # Update for the next set

            curr_def.set_rules_id(f'{old_rules_id}{curr_node.get_informations().get_wazuh_rule_config().get_rule_id()}') # Append the rule id of this single node

            continue


        # TODO: Implement this (hardest part tbh...)
        for node_id in curr_node_ids:
            curr_node = node_id_to_node.get(node_id) # Add check
            if curr_node is None:
                #throw error saying a node id is wrong
                pass
            
