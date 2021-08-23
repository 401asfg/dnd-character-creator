from abc import abstractmethod, ABC
from typing import Tuple, Dict

from main.model.character.alignment import Alignment
from main.model.character.utility.enumerators.ability import Ability
from main.model.character.utility.enumerators.size import Size
from main.model.character.utility.enumerators.skill import Skill
from main.model.collection.collection_item import CollectionItem


class Race(ABC):
    """
    The abstract representation of a character's race; not to be used, only inherited
    """

    # TODO: test all subclasses independently

    # TODO: refactor this and class into subclasses of new type

    # TODO: Add more parameters to account for all aspects of races
    # TODO: Return to dictionary of races?
    # TODO: test all races and all of their aspects

    @property
    @abstractmethod
    def traits(self) -> Tuple[CollectionItem, ...]:
        """
        :return: The traits of a character of this race
        """

        _error()

    @property
    @abstractmethod
    def other_proficiencies(self) -> Tuple[CollectionItem, ...]:
        """
        :return: The other proficiencies of this race
        """

        _error()

    def get_ability_bonus(self, ability: Ability) -> int:
        """
        :param ability: The ability to get the racial bonus of
        :return: The bonus, for the given ability, that a character of this race gets; 0 if this race has no bonus for
        the given ability
        """

        ability_bonuses = self._get_ability_bonuses()

        if ability not in ability_bonuses:
            return 0

        return ability_bonuses[ability]

    def proficient_in_skill(self, skill: Skill) -> bool:
        """
        :param skill: The skill proficiency to check
        :return: True if the given skill is in class' skill proficiencies set; otherwise, false
        """

        return skill in self._get_skill_proficiencies()

    @staticmethod
    @abstractmethod
    def get_name() -> str:
        """
        :return: The race's name
        """

        _error()

    @staticmethod
    @abstractmethod
    def get_acceptable_alignment_natures() -> Tuple[Alignment.Nature, ...]:
        """
        :return: The alignment natures that a character can have
        """

        _error()

    @staticmethod
    @abstractmethod
    def get_acceptable_alignment_moralities() -> Tuple[Alignment.Morality, ...]:
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

    @staticmethod
    @abstractmethod
    def get_hit_point_bonus() -> int:
        """
        :return: The max hit point increase that a character of this race has
        """

        _error()

    @abstractmethod
    def _get_ability_bonuses(self) -> Dict[Ability, int]:
        """
        :return: The ability bonuses that a character of this race has; doesn't contain entries for abilities that
        won't provide a bonus
        """

        _error()

    @abstractmethod
    def _get_skill_proficiencies(self) -> Tuple[Skill, ...]:
        """
        :return: The skills that a character of this race is proficient in
        """

        _error()

    @staticmethod
    def _get_appended_ability_bonuses(
            ability_bonuses: Dict[Ability, int],
            ability: Ability,
            bonus: int
    ) -> Dict[Ability, int]:
        """
        Get the given ability_bonuses set with the given ability bonus appended to it

        :param ability_bonuses: The original ability_bonuses set, which has the given ability bonus appended to it
        :param ability: The key, that corresponds to the bonus value, to append to the ability_bonuses set
        :param bonus: The value, that corresponds to the ability key, to append to the ability_bonuses set
        :return: The given ability_bonuses set with the given ability bonus appended to it
        """

        ability_bonuses[ability] = bonus
        return ability_bonuses


def _error():
    """
    Raises NotImplementedError
    """

    raise NotImplementedError("This method should be called from one of Race's subclasses.")
