from AbstractOptimality import AbstractOptimality


class BEST_SCORE(AbstractOptimality):
    '''
    Identified by Optimality_Type = BEST_SCORE

    List of properties:
    - score : int = A number indicating the preference for picking the defense. Higher is better.

    '''

    def validate_score(self):
        return isinstance(self.get_property_value('score'), int)
    
    def validate_score_with_error_launch(self):
        if not self.validate_score():
            error_prefix = f"BEST_SCORE with score {self.get_score()} failed validation on"
            error_suffix = f"was given instead."
            ExitUtils.exit_with_error(f'{error_prefix} <defense id="">. {Defense.get_id_allow_criteria()} {self.get_id()} of type {type(self.get_id())} {error_suffix}')


    def validate_all(self):
        # Every validation for the properties.
        # "properties" is a dictionary, and all the methods to
        # use it are inside of the AbstractOptimality class.
        self.validate_score_with_error_launch()