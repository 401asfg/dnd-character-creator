from abc import abstractmethod, ABC
from typing import List

from main.model.character.alignment import Alignment
from main.model.character.utility.enumerators.size import Size


class Race(ABC):
    """
    The abstract representation of a character's race; not to be used, only inherited
    """

    # TODO: refactor this and class into subclasses of new type

    # TODO: Add more parameters to account for all aspects of races
    # TODO: Return to dictionary of races?

    @staticmethod
    @abstractmethod
    def get_name() -> str:
        """
        :return: The race's name
        """

        _error()

    @staticmethod
    @abstractmethod
    def get_strength_bonus() -> int:
        """
        :return: The racial bonus given to a character's strength stat
        """

        _error()

    @staticmethod
    @abstractmethod
    def get_dexterity_bonus() -> int:
        """
        :return: The racial bonus given to a character's dexterity stat
        """

        _error()

    @staticmethod
    @abstractmethod
    def get_constitution_bonus() -> int:
        """
        :return: The racial bonus given to a character's constitution stat
        """

        _error()

    @staticmethod
    @abstractmethod
    def get_intelligence_bonus() -> int:
        """
        :return: The racial bonus given to a character's intelligence stat
        """

        _error()

    @staticmethod
    @abstractmethod
    def get_wisdom_bonus() -> int:
        """
        :return: The racial bonus given to a character's wisdom stat
        """

        _error()

    @staticmethod
    @abstractmethod
    def get_charisma_bonus() -> int:
        """
        :return: The racial bonus given to a character's charisma stat
        """

        _error()

    @staticmethod
    @abstractmethod
    def get_additional_ability_bonus() -> int:
        """
        :return: The racial bonus given to one of the character's ability stats, chosen by the player
        """

        _error()

    @staticmethod
    @abstractmethod
    def get_acceptable_alignment_natures() -> List[Alignment.Nature]:
        """
        :return: The alignment natures that a character can have
        """

        _error()

    @staticmethod
    @abstractmethod
    def get_acceptable_alignment_moralities() -> List[Alignment.Morality]:
        """
        :return: The alignment moralities that a character can have
        """

        _error()

    @staticmethod
    @abstractmethod
    def get_min_adult_age() -> int:
        """
        :return: The age at which a character of this race becomes an adult
        """

        _error()

    @staticmethod
    @abstractmethod
    def get_life_expectancy() -> int:
        """
        :return: The age at which a character of this race is expected to die by
        """

        _error()

    @staticmethod
    @abstractmethod
    def get_size() -> Size:
        """
        :return: The size of a character of this race
        """

        _error()

    @staticmethod
    @abstractmethod
    def get_speed() -> int:
        """
        :return: The speed of a character of this race
        """

        _error()


def _error():
    """
    Raises NotImplementedError
    """

    raise NotImplementedError("This method should be called from one of Race's subclasses.")
