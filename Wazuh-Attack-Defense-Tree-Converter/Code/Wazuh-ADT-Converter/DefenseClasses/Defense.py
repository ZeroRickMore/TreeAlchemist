from typing import List

# Import scripts from above folder
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from terminal_UI_utils import PrintUtils, ExitUtils
import validations
from DefenseClasses.Command import Command
from DefenseClasses.ActiveResponse import ActiveResponse


class Defense:
    '''
    This class represents the whole defense, so it is mapped to one or more states
    and has a Command and Active response.
    '''

    def __init__(self, 
                 #mapped_states : List[int] = None, # The states the defense is mapped to, inside of states_to_defense.xml
                 

                ):
        pass