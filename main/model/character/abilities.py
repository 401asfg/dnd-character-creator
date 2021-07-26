from typing import Type

from main.model.character.ability import Ability
from main.model.character.class_ import Class
from main.model.character.race import Race
from main.model.inttypes.natural_plus import NaturalPlus

# TODO: test abilities
# TODO: fix not being recognized by autocomplete or typing


def generate_character_abilities(
        strength_dice_roll: Ability,
        dexterity_dice_roll: Ability,
        constitution_dice_roll: Ability,
        intelligence_dice_roll: Ability,
        wisdom_dice_roll: Ability,
        charisma_dice_roll: Ability
) -> Type["Abilities"]:
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

    class Abilities:
        """
        The character's abilities
        """

        class Ability(Ability):
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
                race: Type[Race],
                class_: Type[Class],
                proficiency_bonus: NaturalPlus
        ):
            """
            Initializes this class

            :param race: The race of the character to whom these abilities belong
            :param class_: The class of the character to whom these abilities belong
            :param proficiency_bonus: The proficiency bonus of the character to whom these abilities belong
            """

            self._strength = self.Ability(
                strength_dice_roll,
                NaturalPlus(race.get_strength_bonus()),
                class_.strength_proficiency(),
                proficiency_bonus
            )

            self._dexterity = self.Ability(
                dexterity_dice_roll,
                NaturalPlus(race.get_dexterity_bonus()),
                class_.dexterity_proficiency(),
                proficiency_bonus
            )

            self._constitution = self.Ability(
                constitution_dice_roll,
                NaturalPlus(race.get_constitution_bonus()),
                class_.constitution_proficiency(),
                proficiency_bonus
            )

            self._intelligence = self.Ability(
                intelligence_dice_roll,
                NaturalPlus(race.get_intelligence_bonus()),
                class_.intelligence_proficiency(),
                proficiency_bonus
            )

            self._wisdom = self.Ability(
                wisdom_dice_roll,
                NaturalPlus(race.get_wisdom_bonus()),
                class_.wisdom_proficiency(),
                proficiency_bonus
            )

            self._charisma = self.Ability(
                charisma_dice_roll,
                NaturalPlus(race.get_charisma_bonus()),
                class_.charisma_proficiency(),
                proficiency_bonus
            )

        @property
        def strength(self) -> Ability:
            return self._strength

        @property
        def dexterity(self) -> Ability:
            return self._dexterity

        @property
        def constitution(self) -> Ability:
            return self._constitution

        @property
        def intelligence(self) -> Ability:
            return self._intelligence

        @property
        def wisdom(self) -> Ability:
            return self._wisdom

        @property
        def charisma(self) -> Ability:
            return self._charisma

    return Abilities
