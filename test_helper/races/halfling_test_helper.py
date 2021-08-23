from abc import ABC
from typing import Tuple

from main.model.character.alignment import Alignment
from main.model.character.utility.enumerators.size import Size
from test_helper.race_test_helper import RaceTestHelper


class HalflingTestHelper(RaceTestHelper, ABC):
    def _test_halfling_init(
            self,
            expected_additional_trait_names: Tuple[str, ...],
            expected_name: str
    ):
        """
        Helper method used to test the init method of the halfling

        :param expected_additional_trait_names: The expected traits of the halfling
        :param expected_name: The expected name of the halfling
        """

        self._test_init(
            expected_trait_names=(
                "Lucky",
                "Brave",
                "Halfling Nimbleness"
            ) + expected_additional_trait_names,
            expected_other_proficiency_names=(
                "Common Language",
                "Halfling Language"
            ),
            expected_name=expected_name,
            expected_acceptable_alignment_natures=(
                Alignment.Nature.LAWFUL,
                Alignment.Nature.NEUTRAL
            ),
            expected_acceptable_alignment_moralities=(
                Alignment.Morality.GOOD,
                Alignment.Morality.NEUTRAL
            ),
            expected_hp_bonus=0,
            expected_size=Size.SMALL,
            expected_speed=25,
            expected_min_adult_age=20,
            expected_life_expectancy=150
        )

    def _test_halfling_get_ability_bonus(
            self,
            expected_strength_bonus: int,
            expected_constitution_bonus: int,
            expected_intelligence_bonus: int,
            expected_wisdom_bonus: int,
            expected_charisma_bonus: int
    ):
        """
        Helper method used to test the get ability bonus method of the halfling

        :param expected_strength_bonus: The expected strength bonus of the halfling
        :param expected_constitution_bonus: The expected constitution bonus of the halfling
        :param expected_intelligence_bonus: The expected intelligence bonus of the halfling
        :param expected_wisdom_bonus: The expected wisdom bonus of the halfling
        :param expected_charisma_bonus: The expected charisma bonus of the halfling
        """

        self._test_get_ability_bonus(
            expected_strength_bonus=expected_strength_bonus,
            expected_dexterity_bonus=2,
            expected_constitution_bonus=expected_constitution_bonus,
            expected_intelligence_bonus=expected_intelligence_bonus,
            expected_wisdom_bonus=expected_wisdom_bonus,
            expected_charisma_bonus=expected_charisma_bonus
        )

    def _test_halfing_proficient_in_skill(self):
        """
        Helper method used to test the proficient in skill method of the halfing
        """

        self._test_proficient_in_skill(())
