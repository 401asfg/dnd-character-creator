from enum import Enum


class CharacterAlignment:
    """
    The alignment of a character
    """

    # TODO: add dicts for moralities, natures, and alignments

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

    def __init__(self, nature: Nature, morality: Morality):
        """
        Initializes the alignment's fields

        :param nature: How lawful or chaotic the character is
        :param morality: How good or evil the character is
        """

        self._nature = nature
        self._morality = morality

    def name(self) -> str:
        """
        Gets the name of the alignment

        :return: The name of the alignment; typically is of the form "<nature name> <morality name>"; if both nature
        and morality are NEUTRAL, the name is "TRUE NEUTRAL"
        """

        if self._nature == self.Nature.NEUTRAL and self._morality == self.Morality.NEUTRAL:
            return "TRUE NEUTRAL"

        return self._nature.name + " " + self._morality.name
