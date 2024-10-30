# Import scripts from above folder
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from TreeNodeInformations import *


def test():
    # Normal node with all default entries
    t = TreeNodeInformations()
    t.set_path("/")
    t.set_id(0)
    t.get_wazuh_rule_config().set_wrc_description("A good description!")
    t.get_wazuh_rule_config().set_wrc_time("8-9")
    t.validate_all()




if __name__ == '__main__':
    test()