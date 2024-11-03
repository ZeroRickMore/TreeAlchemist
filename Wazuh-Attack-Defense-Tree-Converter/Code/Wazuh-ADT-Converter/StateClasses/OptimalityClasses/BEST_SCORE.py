# Import scripts from above folder
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from terminal_UI_utils import PrintUtils, ExitUtils
from StateClasses.OptimalityClasses.AbstractOptimality import AbstractOptimality

class BEST_SCORE(AbstractOptimality):
    '''
    Identified by Optimality_Type = BEST_SCORE

    List of properties:
    - score : int = A number indicating the preference for picking the defense. Higher is better.

    '''

    def validate_score(self):
        return isinstance(self.get_score(), int)
    
    def validate_score_with_error_launch(self):
        if not self.validate_score():
            score = self.get_score()
            error_prefix = f"BEST_SCORE with score {score} failed validation on"
            error_suffix = f"was given instead."
            ExitUtils.exit_with_error(f'{error_prefix} <score>. It should be and int, but {score} of type {type(score)} {error_suffix}')

    def set_instance_variables_from_properties(self):
        score = self.get_property_value_text_no_duplicate_tags_traversed(property_key='score')
        try:
            self.score = int(score)
        except: # The score is not a int number
            ExitUtils.exit_with_error(f"The given score inside of <score> is {score} and it MUST be a int number.")

    def get_score(self):
        return self.score

    def validate_all(self):
        self.set_instance_variables_from_properties()
        # Every validation for the properties.
        # "properties" is a dictionary, and all the methods to
        # use it are inside of the AbstractOptimality class.
        self.validate_score_with_error_launch()