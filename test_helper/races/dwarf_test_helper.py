from abc import ABC
from typing import Tuple

from main.model.character.alignment import Alignment
from main.model.character.utility.enumerators.size import Size
from test_helper.race_test_helper import RaceTestHelper


class DwarfTestHelper(RaceTestHelper, ABC):

    def _test_dwarf_init(
            self,
            expected_additional_trait_names: Tuple[str, ...],
            expected_additional_other_proficiency_names: Tuple[str, ...],
            expected_name: str,
            expected_hp_bonus: int
    ):
        """
        Helper method used to test the init method of the dwarf

        :param expected_additional_trait_names: The expected traits of the dwarf
        :param expected_additional_other_proficiency_names: The expected other proficiencies of the dwarf
        :param expected_name: The expected name of the dwarf
        :param expected_hp_bonus: The expected hit point bonus of the dwarf
        """

        super()._test_init(
            expected_trait_names=(
                "Darkvision",
                "Dwarven Resilience"
            ) + expected_additional_trait_names,
            expected_other_proficiency_names=(
                "Dwarven Combat Training",
                "Smith's Tools",
                "Stonecunning",
                "Common Language",
                "Dwarvish Language"
            ) + expected_additional_other_proficiency_names,
            expected_name=expected_name,
            expected_acceptable_alignment_natures=(
                Alignment.Nature.LAWFUL,
                Alignment.Nature.NEUTRAL
            ),
            expected_acceptable_alignment_moralities=(
                Alignment.Morality.GOOD,
                Alignment.Morality.NEUTRAL
            ),
            expected_min_adult_age=50,
            expected_life_expectancy=350,
            expected_size=Size.MEDIUM,
            expected_speed=30,
            expected_hp_bonus=expected_hp_bonus
        )

    def _test_dwarf_get_ability_bonus(
            self,
            expected_strength_bonus: int,
            expected_dexterity_bonus: int,
            expected_intelligence_bonus: int,
            expected_wisdom_bonus: int,
            expected_charisma_bonus: int
    ):
        """
        Helper method used to test the get ability bonus method of the dwarf

        :param expected_strength_bonus: The expected strength bonus of the dwarf
        :param expected_dexterity_bonus: The expected dexterity bonus of the dwarf
        :param expected_intelligence_bonus: The expected intelligence bonus of the dwarf
        :param expected_wisdom_bonus: The expected wisdom bonus of the dwarf
        :param expected_charisma_bonus: The expected charisma bonus of the dwarf
        """

        self._test_get_ability_bonus(
            expected_strength_bonus=expected_strength_bonus,
            expected_dexterity_bonus=expected_dexterity_bonus,
            expected_constitution_bonus=2,
            expected_intelligence_bonus=expected_intelligence_bonus,
            expected_wisdom_bonus=expected_wisdom_bonus,
            expected_charisma_bonus=expected_charisma_bonus
        )

    def _test_dwarf_proficient_in_skill(self):
        """
        Helper method used to test the proficient in skill method of the dwarf
        """

        self._test_proficient_in_skill(())
