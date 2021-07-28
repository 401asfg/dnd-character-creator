from abc import ABC, abstractmethod
from math import floor
from typing import Type

from main.model.character.ability_score import AbilityScore
from main.model.character.class_ import Class
from main.model.character.race import Race
from main.model.int_types.natural import Natural
from main.model.int_types.posint import Posint

# TODO: test abilities
# TODO: fix not being recognized by autocomplete or typing

_NOT_IMPLEMENTED_MSG = 'Method implemented in subclass, call "generate_character_abilities" to access.'


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

            raise NotImplementedError(_NOT_IMPLEMENTED_MSG)

        @property
        @abstractmethod
        def score(self) -> int:
            raise NotImplementedError(_NOT_IMPLEMENTED_MSG)

        @property
        @abstractmethod
        def modifier(self) -> int:
            """
            :return: The ability modifier for the current ability score
            """

            raise NotImplementedError(_NOT_IMPLEMENTED_MSG)

        @property
        @abstractmethod
        def saving_throw(self) -> int:
            """
            :return: The saving throw modifier: ability modifier, plus proficiency_bonus if class is proficient in
            this ability
            """

            raise NotImplementedError(_NOT_IMPLEMENTED_MSG)

    @abstractmethod
    def __init__(
            self,
            race: Type[Race],
            class_: Type[Class],
            proficiency_bonus: Posint
    ):
        """
        Initializes this class

        :param race: The race of the character to whom these abilities belong
        :param class_: The class of the character to whom these abilities belong
        :param proficiency_bonus: The proficiency bonus of the character to whom these abilities belong
        """

        raise NotImplementedError(_NOT_IMPLEMENTED_MSG)

    @property
    @abstractmethod
    def strength(self) -> Ability:
        raise NotImplementedError(_NOT_IMPLEMENTED_MSG)

    @property
    @abstractmethod
    def dexterity(self) -> Ability:
        raise NotImplementedError(_NOT_IMPLEMENTED_MSG)

    @property
    @abstractmethod
    def constitution(self) -> Ability:
        raise NotImplementedError(_NOT_IMPLEMENTED_MSG)

    @property
    @abstractmethod
    def intelligence(self) -> Ability:
        raise NotImplementedError(_NOT_IMPLEMENTED_MSG)

    @property
    @abstractmethod
    def wisdom(self) -> Ability:
        raise NotImplementedError(_NOT_IMPLEMENTED_MSG)

    @property
    @abstractmethod
    def charisma(self) -> Ability:
        raise NotImplementedError(_NOT_IMPLEMENTED_MSG)


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
                race: Type[Race],
                class_: Type[Class],
                proficiency_bonus: Posint
        ):
            self._strength = self._Ability(
                strength,
                Natural(race.get_strength_bonus()),
                class_.get_strength_proficiency(),
                proficiency_bonus
            )

            self._dexterity = self._Ability(
                dexterity,
                Natural(race.get_dexterity_bonus()),
                class_.get_dexterity_proficiency(),
                proficiency_bonus
            )

            self._constitution = self._Ability(
                constitution,
                Natural(race.get_constitution_bonus()),
                class_.get_constitution_proficiency(),
                proficiency_bonus
            )

            self._intelligence = self._Ability(
                intelligence,
                Natural(race.get_intelligence_bonus()),
                class_.get_intelligence_proficiency(),
                proficiency_bonus
            )

            self._wisdom = self._Ability(
                wisdom,
                Natural(race.get_wisdom_bonus()),
                class_.get_wisdom_proficiency(),
                proficiency_bonus
            )

            self._charisma = self._Ability(
                charisma,
                Natural(race.get_charisma_bonus()),
                class_.get_charisma_proficiency(),
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
