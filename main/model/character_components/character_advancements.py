from collections import namedtuple
from math import floor


class CharacterAdvancements:
    """
    The database of the levels and proficiency bonuses that correspond with key amounts of experience points
    """

    _MIN_PB = 2
    _RATE_PB_INCR = 1 / 4

    _exp_list = [
        0,
        300,
        900,
        2700,
        6500,
        14000,
        23000,
        34000,
        48000,
        64000,
        85000,
        100000,
        120000,
        140000,
        165000,
        195000,
        225000,
        265000,
        305000,
        355000
    ]

    @classmethod
    def get_experience_points(cls, level: int) -> int:
        """
        Gets the experience points required to attain the given level; raises IndexError if there is no exp amount
        that a character can have that will allow them to attain the given level, as defined by the exp list

        :param level: The level of the character
        :return: The minimum experience points needed for a character to get to the given level
        """

        return cls._exp_list[level - 1]

    @classmethod
    def get_level(cls, exp: int) -> int:
        """
        Gets the level for the given amount of experience points

        :param exp: The amount of experience points
        :return: The level for the given exp
        """

        return cls._get_exp_index(exp) + 1

    @classmethod
    def get_proficiency_bonus(cls, exp: int) -> int:
        """
        Gets the proficiency bonus for the given amount of experience points

        :param exp: The amount of experience points
        :return: The proficiency bonus for the given exp
        """

        return floor(cls._get_exp_index(exp) * cls._RATE_PB_INCR) + cls._MIN_PB

    @classmethod
    def reachable_level(cls, level: int) -> bool:
        """
        Checks that the level can be reached by a character

        :param level: The level to check
        :return: Returns true if the given level is in the advancement database, otherwise returns false
        """

        return 1 <= level <= len(cls._exp_list)

    @classmethod
    def _get_exp_index(cls, exp: int) -> int:
        """
        Gets the exp list index for the given experience points

        :param exp: The amount of experience points
        :return: The index of the exp list that holds a value less than or equal to the given exp
        """

        exp_index = 0

        for i in range(len(cls._exp_list)):
            if exp >= cls._exp_list[i]:
                exp_index = i
            else:
                break

        return exp_index
