from abc import abstractmethod, ABC
from typing import Tuple

from main.model.character.utility.enumerators.ability_proficiency import AbilityProficiency
from main.model.dice.die import Die


class Class(ABC):
    """
    The abstract representation of a class that a character can be; not to be used, only inherited
    """

    # TODO: test all classes and all their aspects

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

    @classmethod
    def proficient(cls, ability_proficiency: AbilityProficiency) -> bool:
        """
        :param ability_proficiency: The ability proficiency
        :return: True if the given ability_proficiency is in class' ability proficiencies set; otherwise, false
        """

        return ability_proficiency in cls._get_ability_proficiencies()

    @staticmethod
    @abstractmethod
    def _get_ability_proficiencies() -> Tuple[AbilityProficiency, ...]:
        """
        :return: The abilities that a character of this class is proficient in
        """

        _error()


def _error():
    """
    Raises NotImplementedError
    """

    raise NotImplementedError("This method should be called from one of Class' subclasses.")
