from enum import Enum


class State(Enum):
    """
    The state of the character
    """

    ALIVE = 0
    DOWNED = 1
    DEAD = 2
