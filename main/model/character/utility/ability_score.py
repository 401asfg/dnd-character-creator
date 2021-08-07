from main.model.dice.dice import Dice
from main.model.int_types.posint import Posint


class AbilityScore(Posint):
    """
    An unmodified score to give to one of the character's main stats (STR, DEX, CON, INT, WIS, CHA)
    """

    _dice = Dice(Posint(3), Dice.Sides.SIX)
    MIN_SCORE = _dice.min_possible_score
    MAX_SCORE = _dice.max_possible_score

    def __init__(self, value: int):
        """
        Initializes the class; if value is less than MIN_SCORE or is greater than MAX_SCORE, raises ValueError

        :param value: The value of the ability score
        """

        if value < self.MIN_SCORE or value > self.MAX_SCORE:
            raise ValueError("An unmodified ability score cannot have the value " + str(value) + ".")

        super().__init__(value)
