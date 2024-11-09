'''
Script di lettura del file tree.xml, scritto dall'utente.

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



def get_ADT_from_tree_xml(tree_dir_path : str) -> tuple[Tree, dict[int, TreeNode]]:
    '''
    Function that, taken a valid path to a file containing ADT necessary files, 
    returns the ADT converted to a usable data structure.

    The input path validation MUST be done in advance.
    '''

    xml_tree_path = os.path.join(tree_dir_path, "tree.xml")

    # Read the xml file, validate it, and create a validates Tree structure from it
    tree_with_attack_nodes_only, id_to_node = get_ADT_with_attack_nodes_only(xml_tree_path=xml_tree_path)

    # Assing the values that do not get assigned from user
    tree_with_attack_nodes_only.assign_system_required_values_to_nodes()

    return tree_with_attack_nodes_only, id_to_node



    



def get_ADT_with_attack_nodes_only(xml_tree_path : str) -> tuple[Tree, dict[int, TreeNode]]:
    validate_xml_tree_file_and_launch_error(xml_tree_path=xml_tree_path)

    adt, id_to_node = generate_ADT_from_xml_file(xml_tree_path)
    return adt, id_to_node

def validate_xml_tree_file_and_launch_error(xml_tree_path : str):
    if not validate_xml_tree_file(xml_tree_path=xml_tree_path):
        ExitUtils.exit_with_error(f"{xml_tree_path} is not a valid .xml file.")

def validate_xml_tree_file(xml_tree_path : str) -> bool:
    if not (os.path.isfile(xml_tree_path) and xml_tree_path.endswith('.xml') ):
      return False
    tree = ET.parse(xml_tree_path)
    root = tree.getroot()
    return root.tag == 'tree'


def generate_ADT_from_xml_file(xml_tree_path : str) -> tuple[Tree, dict[int, TreeNode]]:
    '''
    Read the xml and generate the real data structure.
    '''
    #node_conjunctions : List[tuple]     = []

    # These dictionaries allow a quick lookup for the nodes rather than a tree visit later on.
    node_path_to_nodes : dict           = {}   # str -> List[TreeNode]
    node_id_to_node    : dict           = {}   
    node_name_to_id    : dict           = {}

    try:
        t = ET.parse(xml_tree_path)
    except ET.ParseError as e:
        if "duplicate attribute" in str(e):
            ExitUtils.exit_with_error("Duplicate attribute found in XML.")
        else:
            ExitUtils.exit_with_error(f"XML Parse Error: {e}")
        
    root = t.getroot()

    for i, node in enumerate(root.findall("node")):
        
        exit_error_prefix = f"=== In <node> tag number [ {i} ] from the beginning of the given xml file. ===\n"

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
            ExitUtils.exit_with_error(exit_error_prefix+"<path> must be given exactly once!\nIf you are using path with both names and IDs, just keep one.")
        curr_infos.set_path(path[0].text)

        # <id>
        id = node.findall('id')
        if len(id) != 1:
            ExitUtils.exit_with_error(exit_error_prefix+"<id> must be given exactly once!")
        try:
            id = int(id[0].text)
        except:
            curr_infos.set_id(id[0].text) # Listen... This gives the perfect error output string...
        curr_infos.set_id(id)

        # <name>
        name = node.findall('name')
        if len(name) != 1:
            ExitUtils.exit_with_error(exit_error_prefix+"<name> must be given exactly once!")
        curr_infos.set_name(name[0].text)

        # <wazuh_rule_config> ================================================
        curr_wrc = WazuhRuleConfig(relative_node_name=curr_infos.get_name())
        wrc_tag = node.findall('wazuh_rule_config')
        if len(wrc_tag) != 1:
            ExitUtils.exit_with_error(exit_error_prefix+"<wazuh_rule_config> must be given exactly once!")
        wrc_tag = wrc_tag[0]




        # <description>
        description = wrc_tag.findall('description')
        # if it is present, must be only once
        if len(description) != 1 and len(description) != 0:
            ExitUtils.exit_with_error(exit_error_prefix+"<description> must be given exactly once, if given! If you gave more than one, just collapse them into a sigle string.\nIt will not go in a new line on Wazuh Dashboard, anyway.")
        # if given, process it
        if len(description) == 1:
            curr_wrc.set_wrc_description(description[0].text)


        # <rule_id>
        rule_id = wrc_tag.findall('rule_id')
        # if it is present, must be only once
        if len(rule_id) != 1:
            ExitUtils.exit_with_error(exit_error_prefix+"<rule_id> must be given exactly once! Friendly reminder: Do NOT use sytem-wide duplicate IDs, else Wazuh itself won't start.")
        try:
            rule_id = int(rule_id[0].text)
        except:
            curr_wrc.set_rule_id(rule_id[0].text) # Listen... This gives the perfect error output string...
        
        curr_wrc.set_rule_id(rule_id)


        # <info>
        info = wrc_tag.findall('info')
        # if given, process it
        if len(info) >= 1:
            curr_info : List[Info] = []
            for m in info:
                info_object = Info(relative_node_name=curr_infos.get_name())
                # type=""
                info_type = m.get('type')
                if info_type is not None:
                    info_object.set_wrc_info_type(info_type)
                # content
                info_object.set_wrc_info_info(m.text)
                curr_info.append(info_object)
            curr_wrc.set_wrc_info(curr_info)

        # <options>
        options = wrc_tag.findall('options')
        # if given, process it
        if len(options) >= 1:
            curr_options : List[str] = []
            for m in options:
                option = m.text
                curr_options.append(option)
            curr_wrc.set_wrc_options(curr_options)


        # <frequency>
        frequency = wrc_tag.findall('frequency')
        # if it is present, must be only once
        if len(frequency) != 1 and len(frequency) != 0:
            ExitUtils.exit_with_error(exit_error_prefix+"<frequency> must be given exactly once, if given!")
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
            ExitUtils.exit_with_error(exit_error_prefix+"<timeframe> must be given exactly once, if given!")
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
            ExitUtils.exit_with_error(exit_error_prefix+"<ignore_after> must be given exactly once, if given!")
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
            ExitUtils.exit_with_error(exit_error_prefix+"<already_existing_id> must be given exactly once, if given!")
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

        # <srcip>
        srcip = wrc_tag.findall('srcip')
        # if given, process it
        if len(srcip) >= 1:
            curr_srcip : List[Srcip] = []
            for m in srcip:
                srcip_object = Srcip(relative_node_name=curr_infos.get_name())
                # negate=""
                srcip_negate = m.get('negate')
                if srcip_negate is not None:
                    srcip_object.set_wrc_srcip_negate(srcip_negate)
                # content
                srcip_object.set_wrc_srcip_srcip(m.text)
                curr_srcip.append(srcip_object)
            curr_wrc.set_wrc_srcip(curr_srcip)


        # <dstip>
        dstip = wrc_tag.findall('dstip')
        # if given, process it
        if len(dstip) >= 1:
            curr_dstip : List[Dstip] = []
            for m in dstip:
                dstip_object = Dstip(relative_node_name=curr_infos.get_name())
                # negate=""
                dstip_negate = m.get('negate')
                if dstip_negate is not None:
                    dstip_object.set_wrc_dstip_negate(dstip_negate)
                # content
                dstip_object.set_wrc_dstip_dstip(m.text)
                curr_dstip.append(dstip_object)
            curr_wrc.set_wrc_dstip(curr_dstip)

        # <srcport>
        srcport = wrc_tag.findall('srcport')
        # if given, process it
        if len(srcport) >= 1:
            curr_srcport : List[Srcport] = []
            for m in srcport:
                srcport_object = Srcport(relative_node_name=curr_infos.get_name())
                # negate=""
                srcport_negate = m.get('negate')
                if srcport_negate is not None:
                    srcport_object.set_wrc_srcport_negate(srcport_negate)
                # type=""
                srcport_type = m.get('type')
                if srcport_type is not None:
                    srcport_object.set_wrc_srcport_type(srcport_type)
                # content
                srcport_object.set_wrc_srcport_srcport(m.text)
                curr_srcport.append(srcport_object)
            curr_wrc.set_wrc_srcport(curr_srcport)


        # <dstport>
        dstport = wrc_tag.findall('dstport')
        # if given, process it
        if len(dstport) >= 1:
            curr_dstport : List[Dstport] = []
            for m in dstport:
                dstport_object = Dstport(relative_node_name=curr_infos.get_name())
                # negate=""
                dstport_negate = m.get('negate')
                if dstport_negate is not None:
                    dstport_object.set_wrc_dstport_negate(dstport_negate)
                # type=""
                dstport_type = m.get('type')
                if dstport_type is not None:
                    dstport_object.set_wrc_dstport_type(dstport_type)
                # content
                dstport_object.set_wrc_dstport_dstport(m.text)
                curr_dstport.append(dstport_object)
            curr_wrc.set_wrc_dstport(curr_dstport)

        # <time>
        time = wrc_tag.findall('time')
        # if it is present, must be only once
        if len(time) != 1 and len(time) != 0:
            ExitUtils.exit_with_error(exit_error_prefix+"<time> must be given exactly once, if given!")
        # if given, process it
        if len(time) == 1:
            curr_wrc.set_wrc_time(time[0].text)
        
        # <weekday>
        weekday = wrc_tag.findall('weekday')
        # if it is present, must be only once
        if len(weekday) != 1 and len(weekday) != 0:
            ExitUtils.exit_with_error(exit_error_prefix+"<weekday> must be given exactly once, if given!")
        # if given, process it
        if len(weekday) == 1:
            curr_wrc.set_wrc_weekday(weekday[0].text) 


        # BOOLEAN TAGS =====================================================================

        # <freq_same_srcip />
        freq_same_srcip = wrc_tag.findall('freq_same_srcip')
        # if it is present, must be only once
        if len(freq_same_srcip) != 1 and len(freq_same_srcip) != 0:
            ExitUtils.exit_with_error(exit_error_prefix+"<freq_same_srcip> must be given exactly once, if given!")
        # if given, process it
        if len(freq_same_srcip) == 1:
            curr_wrc.set_wrc_same_srcip(True) 


        # <freq_different_srcip />
        freq_different_srcip = wrc_tag.findall('freq_different_srcip')
        # if it is present, must be only once
        if len(freq_different_srcip) != 1 and len(freq_different_srcip) != 0:
            ExitUtils.exit_with_error(exit_error_prefix+"<freq_different_srcip> must be given exactly once, if given!")
        # if given, process it
        if len(freq_different_srcip) == 1:
            curr_wrc.set_wrc_different_srcip(True) 


        # <freq_same_srcport />
        freq_same_srcport = wrc_tag.findall('freq_same_srcport')
        # if it is present, must be only once
        if len(freq_same_srcport) != 1 and len(freq_same_srcport) != 0:
            ExitUtils.exit_with_error(exit_error_prefix+"<freq_same_srcport> must be given exactly once, if given!")
        # if given, process it
        if len(freq_same_srcport) == 1:
            curr_wrc.set_wrc_same_srcport(True) 

        # <freq_different_srcport />
        freq_different_srcport = wrc_tag.findall('freq_different_srcport')
        # if it is present, must be only once
        if len(freq_different_srcport) != 1 and len(freq_different_srcport) != 0:
            ExitUtils.exit_with_error(exit_error_prefix+"<freq_different_srcport> must be given exactly once, if given!")
        # if given, process it
        if len(freq_different_srcport) == 1:
            curr_wrc.set_wrc_different_srcport(True) 
        
        # <freq_same_dstport />
        freq_same_dstport = wrc_tag.findall('freq_same_dstport')
        # if it is present, must be only once
        if len(freq_same_dstport) != 1 and len(freq_same_dstport) != 0:
            ExitUtils.exit_with_error(exit_error_prefix+"<freq_same_dstport> must be given exactly once, if given!")
        # if given, process it
        if len(freq_same_dstport) == 1:
            curr_wrc.set_wrc_same_dstport(True) 

        # <freq_different_dstport />
        freq_different_dstport = wrc_tag.findall('freq_different_dstport')
        # if it is present, must be only once
        if len(freq_different_dstport) != 1 and len(freq_different_dstport) != 0:
            ExitUtils.exit_with_error(exit_error_prefix+"<freq_different_dstport> must be given exactly once, if given!")
        # if given, process it
        if len(freq_different_dstport) == 1:
            curr_wrc.set_wrc_different_dstport(True) 

        # <freq_same_location />
        freq_same_location = wrc_tag.findall('freq_same_location')
        # if it is present, must be only once
        if len(freq_same_location) != 1 and len(freq_same_location) != 0:
            ExitUtils.exit_with_error(exit_error_prefix+"<freq_same_location> must be given exactly once, if given!")
        # if given, process it
        if len(freq_same_location) == 1:
            curr_wrc.set_wrc_same_location(True) 

        # <freq_same_srcuser />
        freq_same_srcuser = wrc_tag.findall('freq_same_srcuser')
        # if it is present, must be only once
        if len(freq_same_srcuser) != 1 and len(freq_same_srcuser) != 0:
            ExitUtils.exit_with_error(exit_error_prefix+"<freq_same_srcuser> must be given exactly once, if given!")
        # if given, process it
        if len(freq_same_srcuser) == 1:
            curr_wrc.set_wrc_same_srcuser(True) 

        # <freq_different_srcuser />
        freq_different_srcuser = wrc_tag.findall('freq_different_srcuser')
        # if it is present, must be only once
        if len(freq_different_srcuser) != 1 and len(freq_different_srcuser) != 0:
            ExitUtils.exit_with_error(exit_error_prefix+"<freq_different_srcuser> must be given exactly once, if given!")
        # if given, process it
        if len(freq_different_srcuser) == 1:
            curr_wrc.set_wrc_different_srcuser(True) 

        curr_infos.set_wazuh_rule_config(curr_wrc)

        #print(curr_infos.to_string_raw())
        curr_node = TreeNode(curr_infos)

        curr_node.get_informations().validate_all() # A very last total validate

        # Insert into the dicts
        curr_path = curr_node.get_informations().get_path() # Extra sureness by getting the path directly from the newly created node
        if curr_path in node_path_to_nodes:
            node_path_to_nodes[curr_path].append(curr_node)
        else:
            node_path_to_nodes[curr_path] = [curr_node]

        curr_id = curr_node.get_informations().get_id()
        if curr_id in node_id_to_node:
            ExitUtils.exit_with_error(exit_error_prefix+f"The <id> [ {curr_id} ] is duplicated! You MUST use different <id> for each node.")
        node_id_to_node[curr_id] = curr_node    
    
        curr_name = curr_node.get_informations().get_name()
        if curr_name in node_name_to_id:
            ExitUtils.exit_with_error(exit_error_prefix+f"The <name> [ {curr_name} ] is duplicated! You MUST use different <name> for each node.")
        node_name_to_id[curr_name] = curr_id 
    # End of the single node computation


    # Very human syntax to print the dict
    #print("\nnode_path_to_nodes ==================================\n\n"+"\n".join(f'{path} : { [f"{node.get_informations().get_name()} --- {node.get_informations().get_id()}" for node in nodelist] }' for path, nodelist in node_path_to_nodes.items()))
    #print("\nnode_id_to_node    ==================================\n\n"+"\n".join(f'{id} : {node.get_informations().get_name()} --- {node.get_informations().get_id()}' for id, node in node_id_to_node.items()))
    #print("\nnode_name_to_id    ==================================\n\n"+"\n".join(f'{name} : {id}' for name, id in node_name_to_id.items()))


    # After the processing stage, check if all of the elements in every single path lead to a real node
    for path in node_path_to_nodes:
        path = str(path)
        if path == '/': # This path is only theoretical and identifies the root node
            continue
        
        node_names_or_ids = path.split("/")
        node_names_or_ids = [n for n in node_names_or_ids if n != ''] # No empty string, thanks.

        for node_name_or_id in node_names_or_ids:
            try:
                if node_name_or_id.isdigit(): # it is an id
                    node_id_to_node[node_name_or_id]
                else: # It is a name
                    node_id_to_node[node_name_to_id[node_name_or_id]]
            except: # This is a value error if not found in the dict, hence it does not exist and is not identified as a valid existing node
                ExitUtils.exit_with_error(f"The path:\n\n\t[{path}]\n\ncontains an invalid node name or id : \n\n\t[{node_name_or_id}] .\n\nFix it before trying again.")



    # NOW THE ACTUAL TREE NODES CONNECTIONS
    '''
    Sample tree structure:

    /: ['Root --- 0']
    /Root/: ['Child1 Conj --- 1', 'Child2 Conj --- 2', 'Child3 --- 3', 'Child4 --- 4']
    /Root/Child1 Conj/: ['Child1_1 --- 5', 'Child1_2 --- 6']
    /Root/Child4/: ['Child4_1 --- 7']
    
    '''



    adt = Tree()

    # Try to assign the root and see if it's present
    try:
        adt.set_root(node_path_to_nodes['/'][0])
    except:
        ExitUtils.exit_with_error('You MUST provide a <node> as root="yes".\nElse, the tree would have no root...')

    # Check if one and only one "root" is given
    if len(node_path_to_nodes['/']) > 1:
        ExitUtils.exit_with_error('You MUST provide a SINGLE <node> as root="yes".\nElse, the tree would have more than one root...')


    #print(ADT.get_root().get_informations().get_name())

    for path in node_path_to_nodes:
        parent_node : TreeNode
        parent_name_or_id = None
        is_id = None

        path = str(path)
        # Check if I am on root (handling is a little different)
        if path == '/':
            continue # This entry is not a map to the children.

        else:
            parent_name_or_id = path.split("/")[-2] # The second to last entry of the path is the parent name or id. Why? /Root/ -> ['', 'Root', '']
            #print(f"PATH IS -> [{path}] - NAME OR ID IS -> [{parent_name_or_id}]")
            is_id = bool(parent_name_or_id.isdigit())
            if is_id:
                parent_node = node_id_to_node[parent_name_or_id]
            else:
                parent_node = node_id_to_node[node_name_to_id[parent_name_or_id]] # Why not map name to node directly? It seems memory-intensive on big trees...
                

        # Append children
        for child in node_path_to_nodes[path]:
            #print(f"PATH -> {path}, CHILD -> {child.get_informations().get_name()}")
            parent_node.add_child(child)

        # This is not a human syntax but I somehow like it...
        #print(f"[{parent_name_or_id if parent_name_or_id is not None else ''}] is a [{("digit" if is_id else "name") if is_id is not None else ''}] mapped to [{parent_node.get_informations().get_name()}]. His children are: {[_.get_informations().get_name() for _ in parent_node.get_children() ]}")
    
    return adt, node_id_to_node



def test():
    # Oh no! My extremely secret path has been leaked on Github...
    path_append = os.getcwd()
    #adt, _ = generate_ADT_from_xml_file(os.path.join(path_append, r"TreeAlchemist\Code\ADT-Generator\Input-Files\Test\test-tree-functional.xml")
    #generate_ADT_from_xml_file(os.path.join(path_append, r"TreeAlchemist\Code\ADT-Generator\Input-Files\Test\test-tree-wrong-alr-exist-id.xml"))
    #generate_ADT_from_xml_file(os.path.join(path_append, r"TreeAlchemist\Code\ADT-Generator\Input-Files\Test\test-tree-wrong-alr-exist-id.xml"))
    #adt = generate_ADT_from_xml_file(os.path.join(path_append, r"TreeAlchemist\Code\ADT-Generator\Input-Files\Test\test-tree-wrong-rule-id.xml"))
    adt, _  = generate_ADT_from_xml_file(os.path.join(path_append, r"TreeAlchemist\Code\ADT-Generator\Input-Files\Test\test-tree-multinode-functional.xml"))
    #generate_ADT_from_xml_file(os.path.join(path_append, r"TreeAlchemist\Code\ADT-Generator\Input-Files\Test\test-tree-mismatched-root-path.xml")
    #generate_ADT_from_xml_file(os.path.join(path_append, r"TreeAlchemist\Code\ADT-Generator\Input-Files\Test\test-tree-too-many-roots.xml")
    #generate_ADT_from_xml_file(os.path.join(path_append, r"TreeAlchemist\Code\ADT-Generator\Input-Files\Test\test-tree-duplicate-name.xml")
    #generate_ADT_from_xml_file(os.path.join(path_append, r"TreeAlchemist\Code\ADT-Generator\Input-Files\Test\test-tree-duplicate-id.xml")
    #adt = generate_ADT_from_xml_file(os.path.join(path_append, r"TreeAlchemist\Code\ADT-Generator\Input-Files\Test\test-tree-invalid-path.xml")

    adt.assign_system_required_values_to_nodes()
    adt.print_tree_for_debug_with_explicit_nodes()

    #print(adt.get_root().to_string_minimal())
    #print(adt.get_root().to_string_minimal_children())

if __name__ == '__main__':
    test()