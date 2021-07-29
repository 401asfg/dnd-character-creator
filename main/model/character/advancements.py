from math import floor


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


def get_level(exp: int) -> int:
    """
    Gets the level for the given amount of experience points

    :param exp: The amount of experience points
    :return: The level for the given exp
    """

    return _get_exp_index(exp) + 1


def get_min_exp(level: int) -> int:
    """
    Gets the experience points required to attain the given level; raises IndexError if there is no exp amount
    that a character can have that will allow them to attain the given level, as defined by the exp list

    :param level: The level of the character
    :return: The minimum experience points needed for a character to get to the given level
    """

    return _exp_list[level - 1]


def get_proficiency_bonus(level: int) -> int:
    """
    Gets the proficiency bonus for the given level

    :param level: The level of the character
    :return: The proficiency bonus for the given level
    """

    return floor((level - 1) * _RATE_PB_INCR) + _MIN_PB


def _get_exp_index(exp: int) -> int:
    """
    Gets the exp list index for the given experience points

    :param exp: The amount of experience points
    :return: The index of the exp list that holds a value less than or equal to the given exp
    """

    exp_index = 0

    for i in range(len(_exp_list)):
        if exp >= _exp_list[i]:
            exp_index = i
        else:
            break

    return exp_index
