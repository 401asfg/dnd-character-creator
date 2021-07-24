from math import floor

from main.model.inttypes.natural_plus import NaturalPlus


class Ability:
    """
    One of the character's main stats (STR, DEX, CON, INT, WIS, CHA)
    """

    MAX_SCORE = 20

    def __init__(self, score: NaturalPlus):
        """
        Initializes the class; if score is greater than MAX_SCORE, raises ValueError

        :param score: The ability's score
        """

        self.score = score

    @property
    def score(self) -> int:
        return self._score.value

    @score.setter
    def score(self, x: NaturalPlus):
        """
        Sets ability score; if x is greater than MAX_SCORE, raises ValueError

        :param x: The value of the ability score
        """

        if x.value > self.MAX_SCORE:
            raise ValueError("An ability score cannot be above MAX_SCORE")

        self._score = x

    @property
    def modifier(self) -> int:
        """
        :return: The ability modifier for the current ability score
        """

        return floor((self.score - 10) / 2)
