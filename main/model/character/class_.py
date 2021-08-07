from abc import abstractmethod, ABC
from main.model.dice.die import Die


class Class(ABC):
    """
    The abstract representation of a class that a character can be; not to be used, only inherited
    """

    # TODO: refactor this and race into subclasses of new type

    # TODO: create tests

    @staticmethod
    @abstractmethod
    def get_name() -> str:
        """
        :return: The class' name
        """

        _error()

    @staticmethod
    @abstractmethod
    def get_hit_die() -> Die:
        """
        :return: The hit die that this class gives to a character
        """

        _error()

    @staticmethod
    @abstractmethod
    def get_strength_proficiency() -> bool:
        """
        :return: True if class is proficient in strength; otherwise, false
        """

        _error()

    @staticmethod
    @abstractmethod
    def get_dexterity_proficiency() -> bool:
        """
        :return: True if class is proficient in dexterity; otherwise, false
        """

        _error()

    @staticmethod
    @abstractmethod
    def get_constitution_proficiency() -> bool:
        """
        :return: True if class is proficient in constitution; otherwise, false
        """

        _error()

    @staticmethod
    @abstractmethod
    def get_intelligence_proficiency() -> bool:
        """
        :return: True if class is proficient in intelligence; otherwise, false
        """

        _error()

    @staticmethod
    @abstractmethod
    def get_wisdom_proficiency() -> bool:
        """
        :return: True if class is proficient in wisdom; otherwise, false
        """

        _error()

    @staticmethod
    @abstractmethod
    def get_charisma_proficiency() -> bool:
        """
        :return: True if class is proficient in charisma; otherwise, false
        """

        _error()


def _error():
    """
    Raises NotImplementedError
    """

    raise NotImplementedError("This method should be called from one of Class' subclasses.")
