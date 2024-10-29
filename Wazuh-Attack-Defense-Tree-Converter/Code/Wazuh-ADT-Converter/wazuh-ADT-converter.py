'''
Launcher for the whole script to convert an ADT written in an xml file, that is given as input through -path,
and obtain the Wazuh implementation of it.

'''

import argparse
import os
from terminal_UI_utils import PrintUtils, ExitUtils
import ADT_xml_parser

def main():
    # ===========================================================================
    # Argument Parser
    # ===========================================================================

    parser = argparse.ArgumentParser(description="Script to obtain the implementation of an Attack Defense Tree inside of Wazuh.")

    # -path is used for the user to specify which Tree to use
    parser.add_argument("-path", type=str, required=True, help="The path to the xml file containing the Attack Defense Tree to convert.")

    args = parser.parse_args()

    # ====================================================
    # Access to the arguments and checks 
    # ====================================================

    # ==================================
    # Validate the input path: Check if the path exists and is a file, and ends with ".xml"
    # ==================================

    input_path = args.path

    ADESSO NON PRENDO PIù UN SINGOLO FILE MA L INTERA CARTELLA CHE CONTIENE:
        - tree_name.xml (stesso nome della cartella)
        - defense_definition.xml
        - defense_to_nodes.json


    PrintUtils.print_phase_start("Validating user input")

    if not (os.path.isfile(input_path) and input_path.endswith(".xml")):
        ExitUtils.exit_with_error("Please provide a valid xml file!")
    else:
        PrintUtils.print_in_green(f"- You have provided a valid xml file. I will use:\n  {input_path}")

    PrintUtils.print_phase_end("Finished validating user input")

    usable_ADT_structure = ADT_xml_parser.convert_xml_ADT_to_usable_structure(path_to_xml_ADT = input_path)

    
















if __name__ == '__main__':
    main()