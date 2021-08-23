from abc import ABC
from typing import Tuple

from main.model.character.alignment import Alignment
from main.model.character.utility.enumerators.size import Size
from test_helper.race_test_helper import RaceTestHelper


class GnomeTestHelper(RaceTestHelper, ABC):
    def _test_gnome_init(
            self,
            expected_name: str,
            expected_min_adult_age: int,
            expected_life_expectancy: int,
            expected_acceptable_alignment_natures: Tuple[Alignment.Nature, ...],
            expected_acceptable_alignment_moralities: Tuple[Alignment.Morality, ...],
            expected_additional_trait_names: Tuple[str, ...],
            expected_additional_other_proficiency_names: Tuple[str, ...]
    ):
        """
        Helper method used to test the init method of the gnome

        :param expected_name: The expected name of the gnome
        :param expected_min_adult_age: The expected min adult age of the gnome
        :param expected_life_expectancy: The expected life expectancy of the gnome
        :param expected_acceptable_alignment_natures: The expected acceptable alignment natures of the gnome
        :param expected_acceptable_alignment_moralities: The expected acceptable alignment moralities of the gnome
        :param expected_additional_trait_names: The expected additional trait names of the gnome
        :param expected_additional_other_proficiency_names: The expected additional other proficiency names of the gnome
        """

        super()._test_init(
            expected_trait_names=(
                "Darkvision",
                "Gnome Cunning"
            ) + expected_additional_trait_names,
            expected_other_proficiency_names=(
                "Common Language",
                "Gnomish Language"
            ) + expected_additional_other_proficiency_names,
            expected_name=expected_name,
            expected_acceptable_alignment_natures=expected_acceptable_alignment_natures,
            expected_acceptable_alignment_moralities=expected_acceptable_alignment_moralities,
            expected_hp_bonus=0,
            expected_size=Size.SMALL,
            expected_speed=25,
            expected_min_adult_age=expected_min_adult_age,
            expected_life_expectancy=expected_life_expectancy
        )

    def _test_gnome_get_ability_bonus(
            self,
            expected_strength_bonus: int,
            expected_dexterity_bonus: int,
            expected_constitution_bonus: int,
            expected_wisdom_bonus: int,
            expected_charisma_bonus: int
    ):
        """
        Helper method used to test the get ability bonus method of the gnome

        :param expected_strength_bonus: The expected strength bonus of the gnome
        :param expected_dexterity_bonus: The expected dexterity bonus of the gnome
        :param expected_constitution_bonus: The expected constitution bonus of the gnome
        :param expected_wisdom_bonus: The expected wisdom bonus of the gnome
        :param expected_charisma_bonus: The expected charisma bonus of the gnome
        """

        self._test_get_ability_bonus(
            expected_strength_bonus=expected_strength_bonus,
            expected_dexterity_bonus=expected_dexterity_bonus,
            expected_constitution_bonus=expected_constitution_bonus,
            expected_intelligence_bonus=2,
            expected_wisdom_bonus=expected_wisdom_bonus,
            expected_charisma_bonus=expected_charisma_bonus
        )

    def _test_gnome_proficient_in_skill(self):
        """
        Helper method used to test the proficient in skill method of the gnome
        """

        self._test_proficient_in_skill(())
