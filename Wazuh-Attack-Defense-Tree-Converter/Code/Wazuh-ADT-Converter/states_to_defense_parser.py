'''
Script di lettura del file states_to_defense.xml di input, scritto dall'utente.

L'obbiettivo è ottenere le difese in strutture dati utilizzabili.
'''
import xml.etree.ElementTree as ET
import os
from terminal_UI_utils import PrintUtils, ExitUtils
import importlib # Used to dynamically generate OptimalityType objects

from StateClasses.State import State
from StateClasses.StateDefense import StateDefense
from StateClasses.OptimalityClasses.AbstractOptimality import AbstractOptimality


def get_all_states_to_defense(tree_dir_path : str) -> dict[tuple[int], str]:
    states_to_defense_xml_path : str = os.path.join(tree_dir_path, "states_to_defense.xml")

    validate_xml_file_and_launch_error(states_to_defense_xml_path)

    return generate_states_to_defense_from_xml(states_to_defense_xml_path)


def validate_xml_file_and_launch_error(states_to_defense_xml_path : str) -> None:
    if not validate_states_to_defense_xml_file(states_to_defense_xml_path=states_to_defense_xml_path):
        ExitUtils.exit_with_error(f"{states_to_defense_xml_path} is not a valid .xml file.")

def validate_states_to_defense_xml_file(states_to_defense_xml_path : str) -> bool:
    if not (os.path.isfile(states_to_defense_xml_path) and states_to_defense_xml_path.endswith('.xml') ):
      return False
    tree = ET.parse(states_to_defense_xml_path)
    root = tree.getroot()
    return root.tag == 'states'



def generate_states_to_defense_from_xml(states_to_defense_xml_path : str) -> dict[tuple[int], str]:
    '''
    Read the xml and generate the real data structures.
    '''


    state_to_defense : dict[tuple[int], str] = {}


    root = get_xml_root(states_to_defense_xml_path)

    for i, state in enumerate(root.findall("state")):
        
        exit_error_prefix = f"=== In <state> tag number [ {i} ] from the beginning of the given xml file. ===\n"

        curr_state = State()

        description = get_description(state=state, exit_error_prefix=exit_error_prefix)
        curr_state.set_description(description)

        node_ids = get_node_ids(state=state, exit_error_prefix=exit_error_prefix)

        # Try to convert nodes to a tuple of int
        try:
            node_ids = tuple(map(int, node_ids.split(',')))
        except:
            curr_state.set_node_ids(node_ids) # The given error suits well for diagnostics
        
        curr_state.set_node_ids(node_ids)

        state_defense = generate_state_defense(state=state, exit_error_prefix=exit_error_prefix)
        







# ==================================================================================
#   METHODS TO NAVIGATE AND PROCESS THE XML FILE PROVIDED
# ==================================================================================

def get_xml_root(states_to_defense_xml_path) -> ET.Element:
    try:
        t = ET.parse(states_to_defense_xml_path)
    except ET.ParseError as e:
        if "duplicate attribute" in str(e):
            ExitUtils.exit_with_error("Duplicate attribute found in XML.")
        else:
            ExitUtils.exit_with_error(f"XML Parse Error: {e}")
    return t.getroot()


def get_description(state : ET.Element, exit_error_prefix : str) -> str:
    description = state.findall('description')
    if len(description) > 1 or len(description) == 0:
        ExitUtils.exit_with_error(exit_error_prefix+"<description> must be given exactly once!")
    
    return description[0].text


def get_node_ids(state : ET.Element, exit_error_prefix : str) -> str:
    node_ids = state.findall('nodes')
    if len(node_ids) > 1 or len(node_ids) == 0:
        ExitUtils.exit_with_error(exit_error_prefix+"<nodes> must be given exactly once!")
    
    return node_ids[0].text 

def generate_state_defense(state : ET.Element, exit_error_prefix : str) -> StateDefense:
    state_defense = state.findall('defense')
    if len(state_defense) > 1 or len(state_defense) == 0:
        ExitUtils.exit_with_error(exit_error_prefix+"<defense> must be given exactly once!")
    
    state_defense = state_defense[0] # Get the first tag, which is the only one
    id = get_id(state=state, exit_error_prefix=exit_error_prefix)
    
    curr_state_def = StateDefense()
    curr_state_def.set_id(id)

    optimality = generate_optimality(state_defense=state_defense, exit_error_prefix=exit_error_prefix)




def get_id(state : ET.Element, exit_error_prefix : str) -> int:
    # get id=""
    id = state.get('id')
    if id is None: 
        ExitUtils.exit_with_error(exit_error_prefix+'id="" must be given!')
    try:
        id = int(id)
    except:
        ExitUtils.exit_with_error(exit_error_prefix+'id="" must be an int!')
    return id



def generate_optimality(state_defense : ET.Element, exit_error_prefix : str) -> AbstractOptimality:
    opt_type = get_optimality_type(state_defense=state_defense, exit_error_prefix=exit_error_prefix)
    # Let's use introspection to generate this object dynamically
    curr_opt : AbstractOptimality = None

    try:
        # Import the module where the class resides
        module = importlib.import_module(f"StateClasses.OptimalityClasses.{opt_type}")
        
        # Retrieve the class by name
        OptClass = getattr(module, opt_type)
        
        # Instantiate the class
        curr_opt = OptClass()

    except ModuleNotFoundError as e:
        ExitUtils.exit_with_error("The defined optimality-type is not supported, specifically:\n\nModule not found:", e)
    except AttributeError as e:
        ExitUtils.exit_with_error("The defined optimality-type is not supported, specifically:\n\nClass not found in module:", e)
    except Exception as e:
        ExitUtils.exit_with_error("The defined optimality-type is not supported, specifically:\n\nAn error occurred:", e)

    curr_opt.set_properties(generate_properties_dict(state_defense, exit_error_prefix))


def get_optimality_type(state_defense : ET.Element, exit_error_prefix : str) -> str:
    optimality_type = state_defense.findall('optimality-type')
    if len(optimality_type) > 1 or len(optimality_type) == 0:
        ExitUtils.exit_with_error(exit_error_prefix+"<optimality-type> must be given exactly once!")
    
    return optimality_type[0].text


def generate_properties_dict(element : ET.Element, exit_error_prefix : str) -> dict:
    '''
    To access an element of the dictionary, follow this syntax:

    <tag> is a tag in the xml, and it will be a key in the dictionary.
    Each <tag> is mapped to a list, containing a dict element for each time the tag
    is repeated, with three entries:
        attributes -> the attributes of the tag
        text -> the text inside of the tag
        children -> a dictionary containing all the child tags

    Basically, to access an element you follow this syntax:

    let's say I want to reach element <score> of the second <state> in this structure here:
    <states>
        <state>
                <description>Very cool state 1 desc</description>
                <nodes>1</nodes>
                <defense id="1"> <!-- This is Def1 -->
                        <optimality-type>BEST_SCORE</optimality-type>
                        <score>1</score> <!-- Very low -->
                </defense>
        </state>

        <state>
                <description>Very cool state 2 desc</description>
                <nodes>2</nodes>
                <defense id="2"> <!-- This is Def2 -->
                        <optimality-type>BEST_SCORE</optimality-type>
                        <score>2</score> <!-- Very low -->
                </defense>
        </state>
    </states>
    
    We must start from the very root, in this case <states>

    1) access the dict of the children of "states" tag.
    In this case, it contains <state>
    root_children_dict = properties_dict['states']['children']
    2) access the <state> tag in the position we need. Of course, list indexes start from 0
    so if we need the second, we take the one in position 1
    second_state_tag_dict = root_children_dict['state'][1]
    3) access the first <defense> tag inside of it 
    defense_tag_dict = second_state_tag_dict['children']['defense'][0]
    4) access the first <score> tag inside of it
    score_tag_dict = defense_tag_dict['children']['score'][0]
    5) access the 'text' of the finally found tag
    score = score_tag_dict['text']

    All in one line:
    score = result_dict['states']['children']['state'][1]['children']['defense'][0]['children']['score'][0]['text']

    In the end:
    1) find the xpath towards the tag you need
    2) get the root_children_dict. This is done by accessing ['{ROOT_NAME}']['children']
    3) for each tag you pass, access the tag dict of it by ['TAG_NAME'][NEEDED_INDEX],
    where TAG_NAME is the next tag in the xpath, and NEEDED_INDEX is the number you need counting
    from the top, starting from 0.
    4) when the needed tag is reached, access one of its values by accessing
    its dict with the keys: 'attributes' or 'text'
    
    '''
    
    
    # Create a dictionary to store the nested structure
    result = {}

    # Get the tag name
    tag_name = element.tag

    # Initialize the current dictionary for the tag
    text = element.text.strip() if element.text else None
    if text == '':
        text = None
    current_dict = {
        'attributes': element.attrib if element.attrib else None,  # Always include attributes
        'text' : text,
        'children' : None,
    }

    # Initialize a dictionary to hold child elements
    children = {}

    # Process child elements
    for child in element:
        child_dict = generate_properties_dict(child, exit_error_prefix)  # Recursive call for each child
        
        # Append child dict to the appropriate list in the children dictionary
        child_tag = child.tag
        if child_tag not in children:
            children[child_tag] = []  # Create a new list if this tag hasn't been added yet
        children[child_tag].append(child_dict[child_tag])  # Append the child dictionary

    # If there are child elements, add them to the current dict
    if children:
        current_dict['children'] = children  # Add a 'children' key with the children dict

    # Add the current dictionary to the result under the tag name
    if tag_name in result:
        # If we already have this tag, we should store multiple entries
        if isinstance(result[tag_name], list):
            result[tag_name].append(current_dict)
        else:
            result[tag_name] = [result[tag_name], current_dict]
    else:
        result[tag_name] = current_dict  # Set current_dict if no children

    return result

# Helper function to understand the dictionary.
def properties_dict_pretty_print(data, indent=0):
    """Recursively print the dictionary in a structured format with values next to keys."""
    for key, value in data.items():
        # Print the current key with indentation
        print('    ' * indent + f"{key}: ", end='')
        
        if isinstance(value, dict):
            print("{")  # Open the dictionary
            properties_dict_pretty_print(value, indent + 1)
            print('    ' * indent + "}")  # Close the dictionary
        elif isinstance(value, list):
            print("[")  # Open the list
            for item in value:
                if isinstance(item, dict):
                    properties_dict_pretty_print(item, indent + 1)
                else:
                    print('    ' * (indent + 1) + str(item))
            print('    ' * indent + "]")  # Close the list
        else:
            # Print the value if it's neither a dict nor a list
            print(str(value))  # Print value next to the key


def test_properties_dict():
    # Load the XML file
    tree = ET.parse(r'Z:\GitHub\TreeAlchemist\Wazuh-Attack-Defense-Tree-Converter\Code\Wazuh-ADT-Converter\Input-Files\test-tree\states_to_defense.xml')
    root = tree.getroot()

    # Get the dictionary representation
    result_dict = generate_properties_dict(root, exit_error_prefix='Sta andando tutto male! ')

    # Print the result
    properties_dict_pretty_print(result_dict)
    # Access <score> of the second <state>

    print("The score should be 2 ->", result_dict['states']['children']['state'][1]['children']['defense'][0]['children']['score'][0]['text'])


if __name__ == '__main__':
    test_properties_dict()