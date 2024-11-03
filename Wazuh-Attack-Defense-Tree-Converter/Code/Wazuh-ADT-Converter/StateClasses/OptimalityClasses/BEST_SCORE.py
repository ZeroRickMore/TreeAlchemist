from AbstractOptimality import AbstractOptimality


class BEST_SCORE(AbstractOptimality):
    '''
    Identified by Optimality_Type = BEST_SCORE

    List of properties:
    - score : int = A number indicating the preference for picking the defense. Higher is better.

    '''
    def __init__(self,
                score : int = 50 # Default value is 50
                ):
        self.properties : dict = {}
        self.score = score

    def validate_score(self):
        return isinstance(self.get_property_value('score'), int)

    def validate_all(self):
        # Every validation for the properties.
        # "properties" is a dictionary, and all the methods to
        # use it are inside of the AbstractOptimality class.
        pass