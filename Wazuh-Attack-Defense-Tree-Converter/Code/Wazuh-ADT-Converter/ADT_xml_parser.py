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

    t = ET.parse(xml_tree_path)
    root = t.getroot()


    ADT = Tree()

    for node in root.findall("node"):
        curr_node = TreeNode()
        curr_infos = TreeNodeInformations()
        curr_infos.set_conjuncted_children(node.get('conjuncted_children'))
        curr_infos.set_root(node.get('root'))
        curr_infos.set_type(node.get('type'))
        
        

    

