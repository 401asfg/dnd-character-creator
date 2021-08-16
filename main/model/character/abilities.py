from abc import ABC, abstractmethod
from math import floor
from typing import Type

from main.model.character.utility.ability_score import AbilityScore
from main.model.character.class_ import Class
from main.model.character.race import Race
from main.model.character.utility.enumerators.ability import Ability
from main.model.int_types.natural import Natural
from main.model.int_types.posint import Posint

# TODO: test abilities
# TODO: fix not being recognized by autocomplete or typing


def _error():
    """
    Raises a NotImplementedError
    """

    raise NotImplementedError('Method implemented in subclass, call "generate_character_abilities" to access.')


class Abilities(ABC):
    """
    The character's abilities
    """

    class Ability(ABC):
        """
        An ability in the context of it belonging to the character
        """

        @abstractmethod
        def __init__(
                self,
                ability_score: AbilityScore,
                racial_ability_bonus: Natural,
                class_proficient: bool,
                proficiency_bonus: Posint
        ):
            """
            Initializes the class; sets the ability score to the dice roll score plus the racial bonus for this
            ability

            :param ability_score: An ability with its score taken directly from the dice roll
            :param racial_ability_bonus: The racial bonus to add to the ability's score
            :param class_proficient: Whether or not the character's class is proficient in this ability
            :param proficiency_bonus: The character's proficiency bonus
            """

            _error()

        @property
        @abstractmethod
        def score(self) -> int:
            _error()

        @property
        @abstractmethod
        def modifier(self) -> int:
            """
            :return: The ability modifier for the current ability score
            """

            _error()

        @property
        @abstractmethod
        def saving_throw(self) -> int:
            """
            :return: The saving throw modifier: ability modifier, plus proficiency_bonus if class is proficient in
            this ability
            """

            _error()

    @abstractmethod
    def __init__(
            self,
            race: Race,
            class_: Type[Class],
            proficiency_bonus: Posint
    ):
        """
        Initializes this class

        :param race: The race of the character to whom these abilities belong
        :param class_: The class of the character to whom these abilities belong
        :param proficiency_bonus: The proficiency bonus of the character to whom these abilities belong
        """

        _error()

    @property
    @abstractmethod
    def strength(self) -> Ability:
        _error()

    @property
    @abstractmethod
    def dexterity(self) -> Ability:
        _error()

    @property
    @abstractmethod
    def constitution(self) -> Ability:
        _error()

    @property
    @abstractmethod
    def intelligence(self) -> Ability:
        _error()

    @property
    @abstractmethod
    def wisdom(self) -> Ability:
        _error()

    @property
    @abstractmethod
    def charisma(self) -> Ability:
        _error()


def generate_character_abilities(
        strength: AbilityScore,
        dexterity: AbilityScore,
        constitution: AbilityScore,
        intelligence: AbilityScore,
        wisdom: AbilityScore,
        charisma: AbilityScore
) -> Type[Abilities]:
    """
    Get the abilities for a character

    :param strength: The character's strength ability with its score taken directly from the dice roll
    :param dexterity: The character's dexterity ability with its score taken directly from the dice roll
    :param constitution: The character's constitution ability with its score taken directly from the dice roll
    :param intelligence: The character's intelligence ability with its score taken directly from the dice roll
    :param wisdom: The character's wisdom ability with its score taken directly from the dice roll
    :param charisma: The character's charisma ability with its score taken directly from the dice roll
    :return: The abilities of a character
    """

    class _Abilities(Abilities):
        class _Ability(Abilities.Ability):
            def __init__(
                    self,
                    ability_score: AbilityScore,
                    racial_ability_bonus: Natural,
                    class_proficient: bool,
                    proficiency_bonus: Posint
            ):
                self._score = ability_score.value + racial_ability_bonus.value
                self._proficiency = class_proficient
                self._proficiency_bonus = proficiency_bonus

            @property
            def score(self) -> int:
                return self._score

            @property
            def modifier(self) -> int:
                return floor((self.score - 10) / 2)

            @property
            def saving_throw(self) -> int:
                return self.modifier + self._proficiency * self._proficiency_bonus.value

        def __init__(
                self,
                race: Race,
                class_: Type[Class],
                proficiency_bonus: Posint
        ):
            self._strength = self._Ability(
                strength,
                Natural(race.get_ability_bonus(Ability.STRENGTH)),
                class_.proficient_in_ability(Ability.STRENGTH),
                proficiency_bonus
            )

            self._dexterity = self._Ability(
                dexterity,
                Natural(race.get_ability_bonus(Ability.DEXTERITY)),
                class_.proficient_in_ability(Ability.DEXTERITY),
                proficiency_bonus
            )

            self._constitution = self._Ability(
                constitution,
                Natural(race.get_ability_bonus(Ability.CONSTITUTION)),
                class_.proficient_in_ability(Ability.CONSTITUTION),
                proficiency_bonus
            )

            self._intelligence = self._Ability(
                intelligence,
                Natural(race.get_ability_bonus(Ability.INTELLIGENCE)),
                class_.proficient_in_ability(Ability.INTELLIGENCE),
                proficiency_bonus
            )

            self._wisdom = self._Ability(
                wisdom,
                Natural(race.get_ability_bonus(Ability.WISDOM)),
                class_.proficient_in_ability(Ability.WISDOM),
                proficiency_bonus
            )

            self._charisma = self._Ability(
                charisma,
                Natural(race.get_ability_bonus(Ability.CHARISMA)),
                class_.proficient_in_ability(Ability.CHARISMA),
                proficiency_bonus
            )

        @property
        def strength(self) -> Abilities.Ability:
            return self._strength

        @property
        def dexterity(self) -> Abilities.Ability:
            return self._dexterity

        @property
        def constitution(self) -> Abilities.Ability:
            return self._constitution

        @property
        def intelligence(self) -> Abilities.Ability:
            return self._intelligence

        @property
        def wisdom(self) -> Abilities.Ability:
            return self._wisdom

        @property
        def charisma(self) -> Abilities.Ability:
            return self._charisma

    return _Abilities
