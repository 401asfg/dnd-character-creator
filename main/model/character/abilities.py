from typing import Type

from main.model.character.ability import Ability
from main.model.character.character import Character
from main.model.inttypes.natural_plus import NaturalPlus

# TODO: test


def get_character_abilities(
        strength_dice_roll: Ability,
        dexterity_dice_roll: Ability,
        constitution_dice_roll: Ability,
        intelligence_dice_roll: Ability,
        wisdom_dice_roll: Ability,
        charisma_dice_roll: Ability
) -> Type["_Abilities"]:
    """
    Get the abilities for a character

    :param strength_dice_roll: The character's strength ability with its score taken directly from the dice roll
    :param dexterity_dice_roll: The character's dexterity ability with its score taken directly from the dice roll
    :param constitution_dice_roll: The character's constitution ability with its score taken directly from the dice roll
    :param intelligence_dice_roll: The character's intelligence ability with its score taken directly from the dice roll
    :param wisdom_dice_roll: The character's wisdom ability with its score taken directly from the dice roll
    :param charisma_dice_roll: The character's charisma ability with its score taken directly from the dice roll
    :return: The abilities of a character
    """

    class _Abilities:
        """
        The character's abilities
        """

        class _Ability(Ability):
            """
            An ability in the context of it belonging to the character
            """

            def __init__(
                    self,
                    dice_roll_ability: Ability,
                    racial_ability_bonus: NaturalPlus,
                    class_proficient: bool,
                    proficiency_bonus: NaturalPlus
            ):
                """
                Initializes the class; sets the ability score to the dice roll score plus the racial bonus for this
                ability

                :param dice_roll_ability: An ability with its score taken directly from the dice roll
                :param racial_ability_bonus: The racial bonus to add to the ability's score
                :param class_proficient: Whether or not the character's class is proficient in this ability
                :param proficiency_bonus: The character's proficiency bonus
                """

                super().__init__(NaturalPlus(dice_roll_ability.score + racial_ability_bonus.value))
                self._proficiency = class_proficient
                self._proficiency_bonus = proficiency_bonus

            @property
            def saving_throw(self) -> int:
                """
                :return: The saving throw modifier: ability modifier, plus proficiency_bonus if class is proficient in
                this ability
                """

                return self.modifier + self._proficiency * self._proficiency_bonus.value

        def __init__(
                self,
                character: Character
        ):
            """
            Initializes this class

            :param character: The character to whom these abilities belong
            """

            race = character._race
            class_ = character._class
            pb = NaturalPlus(character.proficiency_bonus)

            self._strength = self._Ability(
                strength_dice_roll,
                NaturalPlus(race.get_strength_bonus()),
                class_.strength_proficiency(),
                pb
            )

            self._dexterity = self._Ability(
                dexterity_dice_roll,
                NaturalPlus(race.get_dexterity_bonus()),
                class_.dexterity_proficiency(),
                pb
            )

            self._constitution = self._Ability(
                constitution_dice_roll,
                NaturalPlus(race.get_constitution_bonus()),
                class_.constitution_proficiency(),
                pb
            )

            self._intelligence = self._Ability(
                intelligence_dice_roll,
                NaturalPlus(race.get_intelligence_bonus()),
                class_.intelligence_proficiency(),
                pb
            )

            self._wisdom = self._Ability(
                wisdom_dice_roll,
                NaturalPlus(race.get_wisdom_bonus()),
                class_.wisdom_proficiency(),
                pb
            )

            self._charisma = self._Ability(
                charisma_dice_roll,
                NaturalPlus(race.get_charisma_bonus()),
                class_.charisma_proficiency(),
                pb
            )

        @property
        def strength(self) -> _Ability:
            return self._strength

        @property
        def dexterity(self) -> _Ability:
            return self._dexterity

        @property
        def constitution(self) -> _Ability:
            return self._constitution

        @property
        def intelligence(self) -> _Ability:
            return self._intelligence

        @property
        def wisdom(self) -> _Ability:
            return self._wisdom

        @property
        def charisma(self) -> _Ability:
            return self._charisma

    return _Abilities
