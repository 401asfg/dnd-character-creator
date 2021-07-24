from enum import Enum


class Alignment:
    """
    The alignment of a character
    """

    class Nature(Enum):
        """
        How lawful or chaotic a character is
        """

        LAWFUL = 0
        NEUTRAL = 1
        CHAOTIC = 2

    class Morality(Enum):
        """
        How good or evil a character is
        """

        GOOD = 0
        NEUTRAL = 1
        EVIL = 2

    _nature_names = {
        Nature.LAWFUL: "Lawful",
        Nature.NEUTRAL: "Neutral",
        Nature.CHAOTIC: "Chaotic"
    }

    _morality_names = {
        Morality.GOOD: "Good",
        Morality.NEUTRAL: "Neutral",
        Morality.EVIL: "Evil"
    }

    def __init__(self, nature: Nature, morality: Morality):
        """
        Initializes the alignment's fields

        :param nature: How lawful or chaotic the character is
        :param morality: How good or evil the character is
        """

        self._nature = nature
        self._morality = morality

    @property
    def name(self) -> str:
        """
        Get the name of the alignment

        :return: The name of the alignment; typically is of the form "<nature name> <morality name>"; if both nature
        and morality are NEUTRAL, the name is "True Neutral"
        """

        if self._nature == self.Nature.NEUTRAL and self._morality == self.Morality.NEUTRAL:
            return "True Neutral"

        return self._nature_names[self._nature] + " " + self._morality_names[self._morality]

    @property
    def nature(self) -> Nature:
        return self._nature

    @property
    def morality(self) -> Morality:
        return self._morality
