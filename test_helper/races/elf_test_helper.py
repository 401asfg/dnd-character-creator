from abc import ABC
from typing import Tuple

from main.model.character.alignment import Alignment
from main.model.character.utility.enumerators.size import Size
from main.model.character.utility.enumerators.skill import Skill
from test_helper.race_test_helper import RaceTestHelper


class ElfTestHelper(RaceTestHelper, ABC):
    def _test_elf_init(
            self,
            expected_additional_trait_names: Tuple[str, ...],
            expected_additional_other_proficiency_names: Tuple[str, ...],
            expected_name: str,
            expected_speed: int
    ):
        """
        Helper method used to test the init method of the elf

        :param expected_additional_trait_names: The expected traits of the elf
        :param expected_additional_other_proficiency_names: The expected other proficiencies of the elf
        :param expected_name: The expected name of the elf
        :param expected_speed: The expected speed of the elf
        """

        self._test_init(
            expected_trait_names=(
                "Darkvision",
                "Fey Ancestry",
                "Trance"
            ) + expected_additional_trait_names,
            expected_other_proficiency_names=(
                "Common Language",
                "Elvish Language",
                "Elf Weapon Training"
            ) + expected_additional_other_proficiency_names,
            expected_name=expected_name,
            expected_acceptable_alignment_natures=(
                Alignment.Nature.NEUTRAL,
                Alignment.Nature.CHAOTIC
            ),
            expected_acceptable_alignment_moralities=(
                Alignment.Morality.GOOD,
                Alignment.Morality.NEUTRAL
            ),
            expected_hp_bonus=0,
            expected_size=Size.MEDIUM,
            expected_speed=expected_speed,
            expected_min_adult_age=100,
            expected_life_expectancy=750
        )

    def _test_elf_get_ability_bonus(
            self,
            expected_strength_bonus: int,
            expected_constitution_bonus: int,
            expected_intelligence_bonus: int,
            expected_wisdom_bonus: int,
            expected_charisma_bonus: int
    ):
        """
        Helper method used to test the get ability bonus method of the elf

        :param expected_strength_bonus: The expected strength bonus of the elf
        :param expected_constitution_bonus: The expected constitution bonus of the elf
        :param expected_intelligence_bonus: The expected intelligence bonus of the elf
        :param expected_wisdom_bonus: The expected wisdom bonus of the elf
        :param expected_charisma_bonus: The expected charisma bonus of the elf
        """

        self._test_get_ability_bonus(
            expected_strength_bonus=expected_strength_bonus,
            expected_dexterity_bonus=2,
            expected_constitution_bonus=expected_constitution_bonus,
            expected_intelligence_bonus=expected_intelligence_bonus,
            expected_wisdom_bonus=expected_wisdom_bonus,
            expected_charisma_bonus=expected_charisma_bonus
        )

    def _test_elf_proficient_in_skill(self):
        """
        Helper method used to test the proficient in skill method of the elf
        """

        self._test_proficient_in_skill((Skill.PERCEPTION,))
