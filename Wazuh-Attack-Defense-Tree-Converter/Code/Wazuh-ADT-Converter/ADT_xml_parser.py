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




def convert_xml_ADT_to_usable_structure(path_to_xml_ADT : str):
    '''
    Function that, taken a valid path to an xml ADT file, returns the ADT
    converted to a usable data structure.

    The input validation MUST be done in advance.
    '''
    tree = ET.parse(path_to_xml_ADT)
    root = tree.getroot()


    print(root.tag)

if __name__ == '__main__':
    convert_xml_ADT_to_usable_structure("extremely-simple-ADT-toy.xml")