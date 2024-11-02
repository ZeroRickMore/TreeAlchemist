'''
Script di lettura del file defense_definition.xml di input, scritto dall'utente.

L'obbiettivo è ottenere le difese in strutture dati utilizzabili.
'''
import xml.etree.ElementTree as ET
import os
from terminal_UI_utils import PrintUtils, ExitUtils

def get_all_defenses(tree_dir_path : str):
    defense_definition_xml_path : str = os.path.join(tree_dir_path, "defense_definition.xml")

    validate_xml_tree_file_and_launch_error(defense_definition_xml_path)




def validate_xml_tree_file_and_launch_error(defense_definition_xml_path : str):
    if not validate_defense_definition_xml_file(defense_definition_xml_path=defense_definition_xml_path):
        ExitUtils.exit_with_error(f"{defense_definition_xml_path} is not a valid .xml file.")

def validate_defense_definition_xml_file(defense_definition_xml_path : str) -> bool:
    if not (os.path.isfile(defense_definition_xml_path) and defense_definition_xml_path.endswith('.xml') ):
      return False
    tree = ET.parse(defense_definition_xml_path)
    root = tree.getroot()
    return root.tag == 'defenses-definition'