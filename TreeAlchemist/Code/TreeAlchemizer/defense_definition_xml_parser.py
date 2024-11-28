'''
Script di lettura del file defense_definition.xml di input, scritto dall'utente.

L'obbiettivo è ottenere le difese in strutture dati utilizzabili.
'''
import xml.etree.ElementTree as ET
import os
from terminal_UI_utils import PrintUtils, ExitUtils
from typing import List, Union

from DefenseClasses.Defense import Defense
from DefenseClasses.ActiveResponse import ActiveResponse
from DefenseClasses.Command import Command
from DefenseClasses.DefensesTogether import DefensesTogether



def get_all_defenses_from_defense_definition_xml(tree_dir_path : str, adt_name : str = None) -> tuple[List[Union[Defense, DefensesTogether]], dict[int, Union[Defense, DefensesTogether]]]:
    defense_definition_xml_path : str = os.path.join(tree_dir_path, "defense_definition.xml")

    validate_xml_file_and_launch_error(defense_definition_xml_path)

    return generate_all_defenses_from_xml(defense_definition_xml_path, adt_name)


def validate_xml_file_and_launch_error(defense_definition_xml_path : str) -> None:
    if not validate_defense_definition_xml_file(defense_definition_xml_path=defense_definition_xml_path):
        ExitUtils.exit_with_error(f"{defense_definition_xml_path} is not a valid .xml file.")

def validate_defense_definition_xml_file(defense_definition_xml_path : str) -> bool:
    if not (os.path.isfile(defense_definition_xml_path) and defense_definition_xml_path.endswith('.xml') ):
      return False
    tree = ET.parse(defense_definition_xml_path)
    root = tree.getroot()
    return root.tag == 'defenses-definition'




def generate_all_defenses_from_xml(defense_definition_xml_path : str, adt_name : str = '') -> tuple[List[Union[Defense, DefensesTogether]], dict[int, Union[Defense, DefensesTogether]]]:
    '''
    Read the xml and generate the real data structures.
    '''
    all_defenses : List[Defense] = []
    all_defenses_together : List[DefensesTogether] = []
    id_to_defense : dict[int, Union[Defense, DefensesTogether]] = {}

    root = get_xml_root(defense_definition_xml_path)

    for i, defense in enumerate(root.findall("defense")):
        
        exit_error_prefix = f"=== In <defense> tag number [ {i} ] from the beginning of the given xml file. ===\n"

        curr_def = None

        name = get_name(defense=defense, exit_error_prefix=exit_error_prefix)
        id = get_id(defense=defense, exit_error_prefix=exit_error_prefix)
    
        
        # Check if it is a DefenseTogether. If  so, gather it and then continue iterating over <defense> ignoring all other tags.
        defenses_together = defense.findall('defenses-together')
        if len(defenses_together) > 1:
            ExitUtils.exit_with_error(exit_error_prefix+"<defenses-together> must be given exactly once, if given!")
        if len(defenses_together) == 1:
            curr_def = DefensesTogether()
            # Convert to a list of int
            temp = []
            try:
                temp = list(map(int, defenses_together[0].text.split(",")))
            except:
                curr_def.set_defenses_ids(defenses_together[0].text) # Error print is good this way
            
            curr_def.set_defenses_ids(temp)

            curr_def.set_name(name)
            curr_def.set_id(id)
            set_active_response(defense=defense, exit_error_prefix=exit_error_prefix, curr_def=curr_def)
            all_defenses_together.append(curr_def)
            
            # if id is in the dict, then an ID is duplicated and it can NOT happen
            if id in id_to_defense:
                ExitUtils.exit_with_error(f"A duplicated ID in defense_definition.xml was given: {id}.\nIDs MUST be unique.")
            id_to_defense[id] = curr_def

            continue

        # Create Defense object =====================
        curr_def = Defense()
        curr_def.set_name(name)
        curr_def.set_id(id)

        set_command(defense=defense, exit_error_prefix=exit_error_prefix, curr_def=curr_def)

        set_active_response(defense=defense, exit_error_prefix=exit_error_prefix, curr_def=curr_def)

        # if id is in the dict, then an ID is duplicated and it can NOT happen
        if id in id_to_defense:
            ExitUtils.exit_with_error(f"A duplicated ID in defense_definition.xml was given: {id}.\nIDs MUST be unique.")
        id_to_defense[id] = curr_def

        curr_def.generate_extra_values(adt_name=adt_name)

        all_defenses.append(curr_def)

    # Validations =======================================
    validate_defense(all_defenses=all_defenses)

    validate_defenses_together(all_defenses_together=all_defenses_together, id_to_defense=id_to_defense)

    return all_defenses + all_defenses_together , id_to_defense


# ==================================================================================
#   METHODS TO NAVIGATE AND PROCESS THE XML FILE PROVIDED
# ==================================================================================

def get_xml_root(defense_definition_xml_path) -> ET.Element:
    try:
        t = ET.parse(defense_definition_xml_path)
    except ET.ParseError as e:
        if "duplicate attribute" in str(e):
            ExitUtils.exit_with_error("Duplicate attribute found in XML.")
        else:
            ExitUtils.exit_with_error(f"XML Parse Error: {e}")
    return t.getroot()


def get_name(defense : ET.Element, exit_error_prefix : str) -> str:
    # get name=""
    name = defense.get('name')
    if name is None: 
        ExitUtils.exit_with_error(exit_error_prefix+'name="" must be given!')
    return name

def get_id(defense : ET.Element, exit_error_prefix : str) -> int:
    # get id=""
    id = defense.get('id')
    if id is None: 
        ExitUtils.exit_with_error(exit_error_prefix+'id="" must be given!')
    try:
        id = int(id)
    except:
        ExitUtils.exit_with_error(exit_error_prefix+'id="" must be an int!')
    return id


def set_command(defense : ET.Element, exit_error_prefix : str, curr_def : Union[Defense, DefensesTogether]) -> None:
    '''
    defense: the tag taken from the xml through ET
    exit_error_prefix: the prefix for error printing
    curr_def: a Defense or DefensesTogether object

    Gathers the <command> infos and sets them in the object
    '''
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
    # END OF Check Command ===========



def set_active_response(defense : ET.Element, exit_error_prefix : str, curr_def : Union[Defense, DefensesTogether]) -> None:
    '''
    defense: the tag taken from the xml through ET
    exit_error_prefix: the prefix for error printing
    curr_def: a Defense or DefensesTogether object

    Gathers the <active-response> infos and sets them in the object
    '''
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

        # print(curr_def.to_string_active_response())
    # END OF Check active_response ===========

    
def validate_defense(all_defenses : List[Defense]) -> None:
    for defense in all_defenses:
        # This is a Defense object
        defense.validate_all()

def validate_defenses_together(all_defenses_together : List[DefensesTogether], id_to_defense : dict) -> None:
    for defense_together in all_defenses_together:
        # This is a DefensesTogether object
        def_ids_needed = defense_together.get_defenses_ids()

        for id in def_ids_needed:
            if id == defense_together.get_id():
                ExitUtils.exit_with_error(f"The <defenses-together> on defense id {defense_together.get_id()} contains itself within the given IDs, with defense id: {id}.\nDo not repeat it.")
            if id not in id_to_defense:
                ExitUtils.exit_with_error(f"The <defenses-together> on defense id {defense_together.get_id()} contains a non-existent defense id: {id}.")
            defense_together.add_defense(id_to_defense[id])
        defense_together.validate_all()



# TEST ========================
def test():
    defs = get_all_defenses_from_defense_definition_xml(r'Z:\GitHub\TreeAlchemizer\TreeAlchemist\Code\TreeAlchemizer\Input-Files\test-tree')
    import wazuh_ready_printer
    print(wazuh_ready_printer.to_string_all_defenses_wazuh_ready(tree_name='BEST ADT', all_defenses=defs, tab_times=0))

if __name__ == '__main__':
    test()