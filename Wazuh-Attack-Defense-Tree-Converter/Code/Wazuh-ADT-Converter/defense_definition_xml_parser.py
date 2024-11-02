'''
Script di lettura del file defense_definition.xml di input, scritto dall'utente.

L'obbiettivo è ottenere le difese in strutture dati utilizzabili.
'''
import xml.etree.ElementTree as ET
import os
from terminal_UI_utils import PrintUtils, ExitUtils
from typing import List

from DefenseClasses.Defense import Defense
from DefenseClasses.ActiveResponse import ActiveResponse
from DefenseClasses.Command import Command
from DefenseClasses.DefensesTogether import DefensesTogether



def get_all_defenses_from_xml(tree_dir_path : str):
    defense_definition_xml_path : str = os.path.join(tree_dir_path, "defense_definition.xml")

    validate_xml_tree_file_and_launch_error(defense_definition_xml_path)

    return generate_all_defenses_from_xml(defense_definition_xml_path)




def validate_xml_tree_file_and_launch_error(defense_definition_xml_path : str):
    if not validate_defense_definition_xml_file(defense_definition_xml_path=defense_definition_xml_path):
        ExitUtils.exit_with_error(f"{defense_definition_xml_path} is not a valid .xml file.")

def validate_defense_definition_xml_file(defense_definition_xml_path : str) -> bool:
    if not (os.path.isfile(defense_definition_xml_path) and defense_definition_xml_path.endswith('.xml') ):
      return False
    tree = ET.parse(defense_definition_xml_path)
    root = tree.getroot()
    return root.tag == 'defenses-definition'




def generate_all_defenses_from_xml(defense_definition_xml_path : str):
    '''
    Read the xml and generate the real data structure.
    '''
    all_defenses = []

    try:
        t = ET.parse(defense_definition_xml_path)
    except ET.ParseError as e:
        if "duplicate attribute" in str(e):
            ExitUtils.exit_with_error("Duplicate attribute found in XML.")
        else:
            ExitUtils.exit_with_error(f"XML Parse Error: {e}")
    
    root = t.getroot()

    for i, defense in enumerate(root.findall("defense")):
        
        exit_error_prefix = f"=== In <defense> tag number [ {i} ] from the beginning of the given xml file. ===\n"

        curr_def = None

        # get name=""
        name = defense.get('name')
        if name is None: 
            ExitUtils.exit_with_error(exit_error_prefix+'name="" must be given!')

        # get id=""
        id = defense.get('id')
        if id is None: 
            ExitUtils.exit_with_error(exit_error_prefix+'id="" must be given!')
        try:
            id = int(id)
        except:
            ExitUtils.exit_with_error(exit_error_prefix+'id="" must be an int!')     
    
        
        # Check if it is a DefenseTogether. If  so, gather it and then continue iterating over <defense> ignoring all other tags.
        defenses_together = defense.findall('defenses_together')
        if len(defenses_together) > 1:
            ExitUtils.exit_with_error(exit_error_prefix+"<defenses_together> must be given exactly once, if given!")
        if len(defenses_together) == 1:
            curr_def = DefensesTogether()
            curr_def.set_defenses_together_ids(defenses_together[0].text)
            curr_def.set_name(name)
            curr_def.set_id(id)
            all_defenses.append(curr_def)
            continue

        # Create Defense object =====================
        curr_def = Defense()
        curr_def.set_name(name)
        curr_def.set_id(id)

        # Check Command ===========
        command = defense.findall('command')
        if len(command) > 1:
            ExitUtils.exit_with_error(exit_error_prefix+"<command> must be given exactly once, if given!")
        if len(command) == 1:
            # Create Command
            command_obj = Command()
            command = command[0]
            
            # Get extra_args
            extra_args = command.findall('extra_args')
            if len(extra_args) > 1:
                ExitUtils.exit_with_error(exit_error_prefix+"<extra_args> must be given exactly once, if given!")
            if len(extra_args == 1):
                try:
                    extra_args = int(extra_args)
                except:
                    command_obj.set_extra_args(extra_args[0])
                command_obj.set_extra_args(extra_args)
            
            # Get timeout_allowed
            timeout_allowed = command.findall('timeout_allowed')
            if len(timeout_allowed) > 1:
                ExitUtils.exit_with_error(exit_error_prefix+"<timeout_allowed> must be given exactly once, if given!")
            if len(timeout_allowed == 1):
                command_obj.set_timeout_allowed(timeout_allowed[0])
            curr_def.set_command(command_obj)

        # Check active_response ===========
        active_response = defense.findall('active-response')
        if len(active_response) > 1:
            ExitUtils.exit_with_error(exit_error_prefix+"<active-response> must be given exactly once, if given!")
        if len(active_response) == 1:
            # Create Command
            activeres_obj = ActiveResponse()
            active_response = active_response[0]
            
            # Get location
            location = active_response.findall('location')
            if len(location) > 1:
                ExitUtils.exit_with_error(exit_error_prefix+"<location> must be given exactly once, if given!")
            if len(location == 1):
                activeres_obj.set_location(location)
            
            # Get agent_id
            agent_id = active_response.findall('agent_id')
            if len(agent_id) > 1:
                ExitUtils.exit_with_error(exit_error_prefix+"<agent_id> must be given exactly once, if given!")
            if len(agent_id == 1):
                activeres_obj.set_agent_id(agent_id[0]) 

            # Get timeout
            timeout = active_response.findall('timeout')
            if len(timeout) > 1:
                ExitUtils.exit_with_error(exit_error_prefix+"<timeout> must be given exactly once, if given!")
            if len(timeout == 1):
                try:
                    timeout = int(timeout)
                except:
                    activeres_obj.set_timeout(timeout[0])
                activeres_obj.set_timeout(timeout)
            curr_def.set_active_response(activeres_obj)

        curr_def.generate_extra_values()
        
        all_defenses.append(curr_def)

    # print debug
    for deff in all_defenses:
        if isinstance(deff, Defense):
            print(deff.to_string_total())
        else:
            print(deff)
        







get_all_defenses_from_xml(r'Z:\GitHub\TreeAlchemist\Wazuh-Attack-Defense-Tree-Converter\Code\Wazuh-ADT-Converter\Input-Files\test-tree')