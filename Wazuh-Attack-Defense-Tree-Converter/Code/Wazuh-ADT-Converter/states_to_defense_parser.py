'''
Script di lettura del file states_to_defense.xml di input, scritto dall'utente.

L'obbiettivo è ottenere le difese in strutture dati utilizzabili.
'''
import xml.etree.ElementTree as ET
import os
from terminal_UI_utils import PrintUtils, ExitUtils

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

    The returned structure is of this form:

    { ( 1, 2, 3 ) : "Def1" }

    With the tuple being the state, each number a node_id
    And the string being the name of a defense
    '''


    state_to_defense : dict[tuple[int], str] = {}


    root = get_xml_root(states_to_defense_xml_path)

    for i, state in enumerate(root.findall("state")):
        
        exit_error_prefix = f"=== In <state> tag number [ {i} ] from the beginning of the given xml file. ===\n"

        curr_state = State()

        description = get_description(state=state, exit_error_prefix=exit_error_prefix)
        curr_stat
        







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

