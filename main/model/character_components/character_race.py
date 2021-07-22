from abc import abstractmethod, ABC
from typing import List

from main.model.character_components.character_alignment import CharacterAlignment
from main.model.character_components.character_size import CharacterSize


class CharacterRace(ABC):
    """
    The abstract representation of a character's race; not to be used, only inherited
    """

    # TODO: Add more parameters to account for all aspects of races
    # TODO: Return to dictionary of races?

    _CALL_METHOD_IN_SUBCLASS_MSG = "This method should be called from one of CharacterRace's subclasses."

    @classmethod
    @abstractmethod
    def get_name(cls) -> str:
        """
        :return: The race's name
        """

        raise NotImplementedError(cls._CALL_METHOD_IN_SUBCLASS_MSG)

    @classmethod
    @abstractmethod
    def get_strength_bonus(cls) -> int:
        """
        :return: The racial bonus given to a character's strength stat
        """

        raise NotImplementedError(cls._CALL_METHOD_IN_SUBCLASS_MSG)

    @classmethod
    @abstractmethod
    def get_dexterity_bonus(cls) -> int:
        """
        :return: The racial bonus given to a character's dexterity stat
        """

        raise NotImplementedError(cls._CALL_METHOD_IN_SUBCLASS_MSG)

    @classmethod
    @abstractmethod
    def get_constitution_bonus(cls) -> int:
        """
        :return: The racial bonus given to a character's constitution stat
        """

        raise NotImplementedError(cls._CALL_METHOD_IN_SUBCLASS_MSG)

    @classmethod
    @abstractmethod
    def get_intelligence_bonus(cls) -> int:
        """
        :return: The racial bonus given to a character's intelligence stat
        """

        raise NotImplementedError(cls._CALL_METHOD_IN_SUBCLASS_MSG)

    @classmethod
    @abstractmethod
    def get_wisdom_bonus(cls) -> int:
        """
        :return: The racial bonus given to a character's wisdom stat
        """

        raise NotImplementedError(cls._CALL_METHOD_IN_SUBCLASS_MSG)

    @classmethod
    @abstractmethod
    def get_charisma_bonus(cls) -> int:
        """
        :return: The racial bonus given to a character's charisma stat
        """

        raise NotImplementedError(cls._CALL_METHOD_IN_SUBCLASS_MSG)

    @classmethod
    @abstractmethod
    def get_acceptable_alignment_natures(cls) -> List[CharacterAlignment.Nature]:
        """
        :return: The alignment natures that a character can have
        """

        raise NotImplementedError(cls._CALL_METHOD_IN_SUBCLASS_MSG)

    @classmethod
    @abstractmethod
    def get_acceptable_alignment_moralities(cls) -> List[CharacterAlignment.Morality]:
        """
        :return: The alignment moralities that a character can have
        """

        raise NotImplementedError(cls._CALL_METHOD_IN_SUBCLASS_MSG)

    @classmethod
    @abstractmethod
    def get_min_adult_age(cls) -> int:
        """
        :return: The age at which a character of this race becomes an adult
        """

        raise NotImplementedError(cls._CALL_METHOD_IN_SUBCLASS_MSG)

    @classmethod
    @abstractmethod
    def get_life_expectancy(cls) -> int:
        """
        :return: The age at which a character of this race is expected to die by
        """

        raise NotImplementedError(cls._CALL_METHOD_IN_SUBCLASS_MSG)

    @classmethod
    @abstractmethod
    def get_size(cls) -> CharacterSize:
        """
        :return: The size of a character of this race
        """

        raise NotImplementedError(cls._CALL_METHOD_IN_SUBCLASS_MSG)

    @classmethod
    @abstractmethod
    def get_speed(cls) -> int:
        """
        :return: The speed of a character of this race
        """

        raise NotImplementedError(cls._CALL_METHOD_IN_SUBCLASS_MSG)
