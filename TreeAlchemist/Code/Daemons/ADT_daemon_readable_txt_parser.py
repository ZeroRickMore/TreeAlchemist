import os
from terminal_UI_utils import ExitUtils, PrintUtils
from pprint import pprint
from typing import Union, Any


def parse_daemon_readable_txt_file(path_to_daemon_file : str, tree_name_to_structure_dict : dict[str, dict[str, Union[tuple, dict[tuple, list[str]]]]]):
    '''
    Works in-place with a dictionary like this:

        {'Root': {
                'states_to_defenses': {('100011',): ['Launch_TA_Root_Def1.sh0'],
                                        ('100012',): ['Launch_TA_Root_Def2.sh0'],
                                        ('100013',): ['Launch_TA_Root_Def3.sh0'],
                                        ('100015',): ['Launch_TA_Root_Def1_1.sh0'],
                                        ('100016', '100013', '100014'): ['Launch_TA_Root_Def1_1.sh0',
                                                                        'Launch_TA_Root_Def3.sh0']},
                'tree_nodes_list': ('100010',
                                    '100011',
                                    '100015',
                                    '100016',
                                    '100012',
                                    '100013',
                                    '100014',
                                    '100017')}} 

    '''
    if not is_valid_txt_file(path_to_daemon_file):
        ExitUtils.exit_with_error(f"The given daemon file {path_to_daemon_file} does not exist or is not a txt file.")

    text = ''
    with open(path_to_daemon_file, 'r', encoding='utf-8') as file:
        text = file.read()

    text : list[str] = text.strip().splitlines()

    current_tree_name = None


    is_parsing = False
    for line in text:
        # Start parsing only if ===START OF ADT===
        if line=='===START OF ADT===':
            is_parsing = True
            continue
        # End parsing  if ===END OF ADT===
        elif line == '===END OF ADT===':
            current_tree_name = None
            is_parsing = False
            continue
        # Parsing if and only if it is supposed to, so we are inside a ===START OF ADT=== and ===END OF ADT=== block
        elif not is_parsing:
            continue

        line = line.split(" :: ")
        
        if not (line[0].startswith('[') and line[0].endswith(']')): # I am looking at the name of the ADT
            tree_name = line[0]
            current_tree_name = tree_name
            tree_nodes = tuple(line[1].replace("[", "").replace("]", "").split(","))
            if tree_name in tree_name_to_structure_dict.keys():
                ExitUtils.exit_with_error(f"Duplicated tree name: {tree_name}.\nThis cannot happen!\nYou most likely generated the same ADT twice, and it is not possibe.\nYou can just change the name of one of the two in the _daemon_readable.txt file,\nbut if you generated them with ADT-Generator, it most likely means\nthat you messed up tree creations.\nIt is strongly recommended to check them out, specifically on Wazuh, to make sure the alerts work correctly.\n")
            
            tree_name_to_structure_dict[tree_name] = {
                'tree_nodes_list' : tree_nodes, 
                'states_to_defenses' : {},
            }

            continue

        state = line[0].replace("[", "").replace("]", "").split(",")
        defenses = line[1].replace("[", "").replace("]", "").split(",")

        tree_name_to_structure_dict[current_tree_name]['states_to_defenses'][tuple(state)] = defenses


        
def parse_all_daemon_readable_files(folder_to_daemon_txt_files : str) -> dict[str, dict[str, Union[tuple, dict[tuple, list[str]]]]]:
    '''
    Returns a structure like this:

        {'Root': {
                'states_to_defenses': {('100011',): ['Launch_TA_Root_Def1.sh0'],
                                        ('100012',): ['Launch_TA_Root_Def2.sh0'],
                                        ('100013',): ['Launch_TA_Root_Def3.sh0'],
                                        ('100015',): ['Launch_TA_Root_Def1_1.sh0'],
                                        ('100016', '100013', '100014'): ['Launch_TA_Root_Def1_1.sh0',
                                                                        'Launch_TA_Root_Def3.sh0']},
                'tree_nodes_list': ('100010',
                                    '100011',
                                    '100015',
                                    '100016',
                                    '100012',
                                    '100013',
                                    '100014',
                                    '100017')}}
    
    '''
    
    if not os.path.isdir(folder_to_daemon_txt_files):
        ExitUtils.exit_with_error(f"The given daemon folder {folder_to_daemon_txt_files} does not exist.")

    txt_files = [os.path.join(folder_to_daemon_txt_files, file) for file in os.listdir(folder_to_daemon_txt_files) if file.endswith('.txt')]

    tree_name_to_structure_dict : dict[str, dict[str, Union[tuple, dict[tuple, list[str]]]]] = {}

    for daemon_txt_path in txt_files:
        parse_daemon_readable_txt_file(path_to_daemon_file=daemon_txt_path, tree_name_to_structure_dict=tree_name_to_structure_dict)

    #pprint(tree_name_to_structure_dict)
    return tree_name_to_structure_dict
            






def is_valid_txt_file(filepath : str):
    # Check if the file exists and has a .txt extension
    return os.path.isfile(filepath) and filepath.lower().endswith('.txt')


