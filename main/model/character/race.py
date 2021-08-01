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
    def _error():
        """
        Raises NotImplementedError
        """

        raise NotImplementedError("This method should be called from one of Race's subclasses.")

    @classmethod
    @abstractmethod
    def get_name(cls) -> str:
        """
        :return: The race's name
        """

        cls._error()

    @classmethod
    @abstractmethod
    def get_strength_bonus(cls) -> int:
        """
        :return: The racial bonus given to a character's strength stat
        """

        cls._error()

    @classmethod
    @abstractmethod
    def get_dexterity_bonus(cls) -> int:
        """
        :return: The racial bonus given to a character's dexterity stat
        """

        cls._error()

    @classmethod
    @abstractmethod
    def get_constitution_bonus(cls) -> int:
        """
        :return: The racial bonus given to a character's constitution stat
        """

        cls._error()

    @classmethod
    @abstractmethod
    def get_intelligence_bonus(cls) -> int:
        """
        :return: The racial bonus given to a character's intelligence stat
        """

        cls._error()

    @classmethod
    @abstractmethod
    def get_wisdom_bonus(cls) -> int:
        """
        :return: The racial bonus given to a character's wisdom stat
        """

        cls._error()

    @classmethod
    @abstractmethod
    def get_charisma_bonus(cls) -> int:
        """
        :return: The racial bonus given to a character's charisma stat
        """

        cls._error()

    @classmethod
    @abstractmethod
    def get_acceptable_alignment_natures(cls) -> List[Alignment.Nature]:
        """
        :return: The alignment natures that a character can have
        """

        cls._error()

    @classmethod
    @abstractmethod
    def get_acceptable_alignment_moralities(cls) -> List[Alignment.Morality]:
        """
        :return: The alignment moralities that a character can have
        """

        cls._error()

    @classmethod
    @abstractmethod
    def get_min_adult_age(cls) -> int:
        """
        :return: The age at which a character of this race becomes an adult
        """

        cls._error()

    @classmethod
    @abstractmethod
    def get_life_expectancy(cls) -> int:
        """
        :return: The age at which a character of this race is expected to die by
        """

        cls._error()

    @classmethod
    @abstractmethod
    def get_size(cls) -> Size:
        """
        :return: The size of a character of this race
        """

        cls._error()

    @classmethod
    @abstractmethod
    def get_speed(cls) -> int:
        """
        :return: The speed of a character of this race
        """

        cls._error()
