import argparse
import os
from terminal_UI_utils import PrintUtils, ExitUtils

def get_valid_tree_path() -> str:
    # ===========================================================================
    # Argument Parser
    # ===========================================================================

    parser = argparse.ArgumentParser(description="Script to transfor a given Attack Defense Tree to implemented Wazuh rules.")

    # -tp and --treepath are used for the user to specify which Tree to use
    parser.add_argument("-tdp", "--treedirpath", type=str, required=True, help="The directory containins all the files useful for the script, according to the documentation.\nThe path can be absolute or relative. For relative paths, use the standard notation with the dot.\nTo use current working directory, type '.'\nFirst, absolute is checked, then current working directory is prepended to you input.\nBe careful about naming the containing files correctly.\nFear not, if the file names are incorrect, you will obtain adequate hints on how to fix.")

    args = parser.parse_args()

    # ====================================================
    # Access to the arguments and checks 
    # ====================================================

    # ==================================
    # Validate the input path:
    # Check if it is an existing directory using Absolute or Relative path
    # ==================================

    tree_dir_path : str = args.treedirpath

    PrintUtils.print_phase_start(f"Validating the given directory:\n\t[ {tree_dir_path} ]")

    # Check user wanting to use cwd
    if tree_dir_path.startswith('.'):
        tree_dir_path = os.path.join(os.getcwd(), tree_dir_path[2:])

    # Validate path existence
    elif not (os.path.isdir(tree_dir_path)):
        given_path = tree_dir_path
        tree_dir_path = os.path.join(os.getcwd(), tree_dir_path) # Prepend and treat as relative path to cwd
        if not (os.path.isdir(tree_dir_path)):
            ExitUtils.exit_with_error(f"PLEASE PROVIDE A VALID DIRECTORY!\n\nBoth absolute path:\n\t[ {given_path} ]\n\nand relative path:\n\t[ {tree_dir_path} ]\n\nare NOT on your system.")
        else:
            PrintUtils.print_in_green(f"Relative path to directory found. Using:\n\t[ {tree_dir_path} ]")
    
    # Check if the required files are present
    NECESSARY_FILES = ["tree.xml", "defense_definition.xml", "defense_to_nodes.json"]
    
    files_in_directory = os.listdir(tree_dir_path)
    missing_files = []
    for needed in NECESSARY_FILES:
        if needed not in files_in_directory:
            missing_files.append(needed)
            
    if missing_files:
        ExitUtils.exit_with_error(f"The given directory:\n\t[ {tree_dir_path} ]\n\nDoes NOT contain all the necessary files.\n\nPlease include:\n\n\t- {'\n\t- '.join([_ for _ in missing_files])}")

    PrintUtils.print_in_green(f"- You have provided a valid directory. I will use:\n  {tree_dir_path}")



    PrintUtils.print_phase_end(f"Finished validating the given directory: {tree_dir_path}")

    return tree_dir_path
