'''
Script di lettura del file .xml di input, scritto dall'utente.

L'obbiettivo è ottenere una struttura dati che rappresenti l'albero, personalizzata per
ottenere in modo rapido ed efficiente le rispettive regole.

Di cosa ho bisogno per scrivere le regole Wazuh, e in che ordine?

- Di sicuro, l'ordine è dalle foglie verso la radice, livello per livello.
  Questo perché in Wazuh l'ordine delle regole è importante, e visto che i nodi superiori si attivano col match degli inferiori,
  quelli inferiori vanno sicuramente sotto.
- Dal nodo foglia, mi interessa il singolo ramo, non ho alcuna correlazione con gli altri rami.
  Partendo dalla foglia, potrei quindi salire e 


- La difesa associata a un nodo è una struttura dati a sé, alla quale il nodo fa riferimento tra i suoi attributi

Andando per livelli, propongo di creare l'albero e salvarmi la struttura coi livelli.

'''
import xml.etree.ElementTree as ET
import os
from terminal_UI_utils import PrintUtils, ExitUtils
from typing import List
# TreeClasses imports
from TreeClasses.Tree import Tree
from TreeClasses.TreeNode import TreeNode
from TreeClasses.TreeNodeInformations import TreeNodeInformations
from TreeClasses.WazuhRuleConfig import WazuhRuleConfig
from TreeClasses.Dstip import Dstip
from TreeClasses.Dstport import Dstport
from TreeClasses.Info import Info
from TreeClasses.Match import Match
from TreeClasses.Regex import Regex
from TreeClasses.Srcip import Srcip
from TreeClasses.Srcport import Srcport



def convert_xml_ADT_to_usable_structure(tree_dir_path : str):
    '''
    Function that, taken a valid path to a file containing ADT necessary files, 
    returns the ADT converted to a usable data structure.

    The input path validation MUST be done in advance.
    '''

    xml_tree_path               : str = os.path.join(tree_dir_path, "tree.xml")
    defense_definition_xml_path : str = os.path.join(tree_dir_path, "defense_definition.xml")
    defense_to_nodes_json_path  : str = os.path.join(tree_dir_path, "defense_to_nodes.json")

    tree_with_attack_nodes_only = get_ADT_with_attack_nodes_only(xml_tree_path=xml_tree_path)



    



def get_ADT_with_attack_nodes_only(xml_tree_path : str):
    validate_xml_tree_file_and_launch_error(xml_tree_path=xml_tree_path)

    ADT = generate_ADT_from_xml_file(xml_tree_path)

def validate_xml_tree_file_and_launch_error(xml_tree_path : str):
    if not validate_xml_tree_file(xml_tree_path=xml_tree_path):
        ExitUtils.exit_with_error(f"{xml_tree_path} is not a valid .xml file.")

def validate_xml_tree_file(xml_tree_path : str):
    if not os.path.isfile(xml_tree_path) or not xml_tree_path.endswith('.xml'):
      return False
    tree = ET.parse(xml_tree_path)
    root = tree.getroot()
    return root.tag == 'tree'


def generate_ADT_from_xml_file(xml_tree_path : str):
    '''
    Read the xml and generate the real data structure.
    '''
    node_conjunctions : List[tuple] = []
    node_path_to_node : dict        = {}   # str -> TreeNode
    try:
      t = ET.parse(xml_tree_path)
    except ET.ParseError as e:
        if "duplicate attribute" in str(e):
            ExitUtils.exit_with_error("Duplicate attribute found in XML.")
        else:
            ExitUtils.exit_with_error(f"XML Parse Error: {e}")
        
    root = t.getroot()

    ADT = Tree()

    for node in root.findall("node"):
        
        curr_infos = TreeNodeInformations()
        # Set <node> attributes ============================
        # conjuncted_children
        conj_children = node.get('conjuncted_children')
        if conj_children is not None: 
            curr_infos.set_conjuncted_children(conj_children) 

        # root
        root = node.get('root')
        if root is not None:
            curr_infos.set_root(root)

        '''
        # type
        type = node.get('type')
        if type is not None:
            curr_infos.set_type(type)
        '''

        # Set <tags> outside of wazuh_rule_config ============================
        # <path>
        path = node.findall('path')
        if len(path) != 1:
            ExitUtils.exit_with_error("<path> must be given exactly once!\nIf you are using path with both names and IDs, just keep one.")
        curr_infos.set_path(path[0].text)

        # <id>
        id = node.findall('id')
        if len(id) != 1:
            ExitUtils.exit_with_error("<id> must be given exactly once!")
        try:
            id = int(id[0].text)
        except:
            curr_infos.set_id(id[0].text) # Listen... This gives the perfect error output string...
        curr_infos.set_id(id)

        # <name>
        name = node.findall('name')
        if len(name) != 1:
            ExitUtils.exit_with_error("<name> must be given exactly once!")
        curr_infos.set_name(name[0].text)

        # <wazuh_rule_config> ================================================
        curr_wrc = WazuhRuleConfig(relative_node_name=curr_infos.get_name())
        wrc_tag = node.findall('wazuh_rule_config')
        if len(wrc_tag) != 1:
            ExitUtils.exit_with_error("<wazuh_rule_config> must be given exactly once!")
        wrc_tag = wrc_tag[0]

        # <frequency>
        frequency = wrc_tag.findall('frequency')
        # if it is present, must be only once
        if len(frequency) != 1 and len(frequency) != 0:
            ExitUtils.exit_with_error("<frequency> must be given exactly once, if given!")
        # if given, process it
        if len(frequency) == 1: 
            try:
              frequency = int(frequency[0].text)
            except:
              curr_wrc.set_wrc_frequency(frequency[0].text) # Listen... This gives the perfect error output string...
            curr_wrc.set_wrc_frequency(frequency)

        # <timeframe>
        timeframe = wrc_tag.findall('timeframe')
        # if it is present, must be only once
        if len(timeframe) != 1 and len(timeframe) != 0:
            ExitUtils.exit_with_error("<timeframe> must be given exactly once, if given!")
        # if given, process it
        if len(timeframe) == 1: 
            try:
              timeframe = int(timeframe[0].text)
            except:
              curr_wrc.set_wrc_timeframe(timeframe[0].text) # Listen... This gives the perfect error output string...
            curr_wrc.set_wrc_timeframe(timeframe)

        # <ignore_after>
        ignore_after = wrc_tag.findall('ignore_after')
        # if it is present, must be only once
        if len(ignore_after) != 1 and len(ignore_after) != 0:
            ExitUtils.exit_with_error("<ignore_after> must be given exactly once, if given!")
        # if given, process it
        if len(ignore_after) == 1: 
            try:
              ignore_after = int(ignore_after[0].text)
            except:
              curr_wrc.set_wrc_ignore(ignore_after[0].text) # Listen... This gives the perfect error output string...
            curr_wrc.set_wrc_ignore(ignore_after)


        # <already_existing_Id>
        already_existing_id = wrc_tag.findall('already_existing_id')
        # if it is present, must be only once
        if len(already_existing_id) != 1 and len(already_existing_id) != 0:
            ExitUtils.exit_with_error("<already_existing_id> must be given exactly once, if given!")
        # if given, process it
        if len(already_existing_id) == 1: 
            try:
              already_existing_id = int(already_existing_id[0].text)
            except:
              curr_wrc.set_wrc_already_existing_id(already_existing_id[0].text) # Listen... This gives the perfect error output string...
            curr_wrc.set_wrc_already_existing_id(already_existing_id)

        # <match>
        match = wrc_tag.findall('match')
        # if given, process it
        if len(match) >= 1:
            curr_match : List[Match] = []
            for m in match:
                match_object = Match(relative_node_name=curr_infos.get_name())
                # negate=""
                match_negate = m.get('negate')
                if match_negate is not None:
                    match_object.set_wrc_match_negate(match_negate)
                # type=""
                match_type = m.get('type')
                if match_type is not None:
                    match_object.set_wrc_match_type(match_type)
                # content
                match_object.set_wrc_match_match(m.text)
                curr_match.append(match_object)
            curr_wrc.set_wrc_match(curr_match)
            
        # <regex>
        regex = wrc_tag.findall('regex')
        # if given, process it
        if len(regex) >= 1:
            curr_regex : List[Regex] = []
            for m in regex:
                regex_object = Regex(relative_node_name=curr_infos.get_name())
                # negate=""
                regex_negate = m.get('negate')
                if regex_negate is not None:
                    regex_object.set_wrc_regex_negate(regex_negate)
                # type=""
                regex_type = m.get('type')
                if regex_type is not None:
                    regex_object.set_wrc_regex_type(regex_type)
                # content
                regex_object.set_wrc_regex_regex(m.text)
                curr_regex.append(regex_object)
            curr_wrc.set_wrc_regex(curr_regex)
            

        curr_infos.wazuh_rule_config = curr_wrc # Do NOT use this to access the variables. Use setters, to obtain a validation every time! This is for printing purposes!

        print(curr_infos.to_string_raw())
        curr_node = TreeNode()


# Oh no! My extremely secret path has been leaked on Github...
generate_ADT_from_xml_file(r"Z:\GitHub\TreeAlchemist\Wazuh-Attack-Defense-Tree-Converter\Code\Wazuh-ADT-Converter\TreeClasses\Test\test-tree-functional.xml")
#generate_ADT_from_xml_file(r"Z:\GitHub\TreeAlchemist\Wazuh-Attack-Defense-Tree-Converter\Code\Wazuh-ADT-Converter\TreeClasses\Test\test-tree-wrong-alr-exist-id.xml")
