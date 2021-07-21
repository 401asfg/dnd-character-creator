from enum import Enum


class CharacterAlignment:
    """
    The alignment of a character
    """

    def __init__(self, morality, nature):
        """
        Initializes the alignment's fields

        :param morality: (Morality) How good or evil the character is
        :param nature: (Nature) How lawful or chaotic the character is
        """

        self._morality = morality
        self._nature = nature

    class Morality(Enum):
        """
        How good or evil a character is
        """

        GOOD = 0
        NEUTRAL = 1
        EVIL = 2

    class Nature(Enum):
        """
        How lawful or chaotic a character is
        """

        LAWFUL = 0
        NEUTRAL = 1
        CHAOTIC = 2
