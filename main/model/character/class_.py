from abc import abstractmethod, ABC
from main.model.dice.die import Die


class Class(ABC):
    """
    The abstract representation of a class that a character can be; not to be used, only inherited
    """

    # TODO: refactor this and race into subclasses of new type

    # TODO: create tests

    @staticmethod
    def _error():
        """
        Raises NotImplementedError
        """

        raise NotImplementedError("This method should be called from one of Class' subclasses.")

    @classmethod
    @abstractmethod
    def get_name(cls) -> str:
        """
        :return: The class' name
        """

        cls._error()

    @classmethod
    @abstractmethod
    def get_hit_die(cls) -> Die:
        """
        :return: The hit die that this class gives to a character
        """

        cls._error()

    @classmethod
    @abstractmethod
    def get_strength_proficiency(cls) -> bool:
        """
        :return: True if class is proficient in strength; otherwise, false
        """

        cls._error()

    @classmethod
    @abstractmethod
    def get_dexterity_proficiency(cls) -> bool:
        """
        :return: True if class is proficient in dexterity; otherwise, false
        """

        cls._error()

    @classmethod
    @abstractmethod
    def get_constitution_proficiency(cls) -> bool:
        """
        :return: True if class is proficient in constitution; otherwise, false
        """

        cls._error()

    @classmethod
    @abstractmethod
    def get_intelligence_proficiency(cls) -> bool:
        """
        :return: True if class is proficient in intelligence; otherwise, false
        """

        cls._error()

    @classmethod
    @abstractmethod
    def get_wisdom_proficiency(cls) -> bool:
        """
        :return: True if class is proficient in wisdom; otherwise, false
        """

        cls._error()

    @classmethod
    @abstractmethod
    def get_charisma_proficiency(cls) -> bool:
        """
        :return: True if class is proficient in charisma; otherwise, false
        """

        cls._error()
