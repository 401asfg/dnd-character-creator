import unittest
from abc import ABC, abstractmethod
from typing import Tuple

from main.model.character.alignment import Alignment
from main.model.character.race import Race
from main.model.character.utility.enumerators.ability import Ability
from main.model.character.utility.enumerators.size import Size
from main.model.character.utility.enumerators.skill import Skill


class RaceTestHelper(unittest.TestCase, ABC):
    race: Race

    @abstractmethod
    def setUp(self) -> None:
        raise NotImplementedError("Should be implemented in child class to set the class' race parameter.")

    def _test_init(
            self,
            expected_trait_names: Tuple[str, ...],
            expected_other_proficiency_names: Tuple[str, ...],
            expected_name: str,
            expected_acceptable_alignment_natures: Tuple[Alignment.Nature, ...],
            expected_acceptable_alignment_moralities: Tuple[Alignment.Morality, ...],
            expected_min_adult_age: int,
            expected_life_expectancy: int,
            expected_size: Size,
            expected_speed: int,
            expected_hp_bonus: int
    ):
        """
        Helper method used to test the init method of the race

        :param expected_trait_names: The expected traits of the race
        :param expected_other_proficiency_names: The expected other proficiencies of the race
        :param expected_name: The expected name of the race
        :param expected_acceptable_alignment_natures: The expected acceptable alignment natures of the race
        :param expected_acceptable_alignment_moralities: The expected acceptable alignment moralities of the race
        :param expected_min_adult_age: The expected min adult age of the race
        :param expected_life_expectancy: The expected life expectancy of the race
        :param expected_size: The expected size of the race
        :param expected_speed: The expected speed of the race
        :param expected_hp_bonus: The expected hit point bonus of the race
        """

        # traits
        self.assertEqual(len(expected_trait_names), len(self.race.traits))

        for i in range(len(expected_trait_names)):
            self.assertEqual(expected_trait_names[i], self.race.traits[i].name)

        # other proficiencies
        self.assertEqual(len(expected_other_proficiency_names), len(self.race.other_proficiencies))

        for i in range(len(expected_other_proficiency_names)):
            self.assertEqual(expected_other_proficiency_names[i], self.race.other_proficiencies[i].name)

        # name
        self.assertEqual(expected_name, self.race.get_name())

        # alignment natures
        self.assertEqual(len(expected_acceptable_alignment_natures), len(self.race.get_acceptable_alignment_natures()))

        natures = (
            Alignment.Nature.LAWFUL,
            Alignment.Nature.NEUTRAL,
            Alignment.Nature.CHAOTIC
        )

        for nature in natures:
            self.assertEqual(
                nature in expected_acceptable_alignment_natures,
                nature in self.race.get_acceptable_alignment_natures()
            )

        # alignment moralities
        self.assertEqual(
            len(expected_acceptable_alignment_moralities),
            len(self.race.get_acceptable_alignment_moralities())
        )

        moralities = (
            Alignment.Morality.GOOD,
            Alignment.Morality.NEUTRAL,
            Alignment.Morality.EVIL
        )

        for morality in moralities:
            self.assertEqual(
                morality in expected_acceptable_alignment_moralities,
                morality in self.race.get_acceptable_alignment_moralities()
            )

        # ages
        self.assertEqual(expected_min_adult_age, self.race.get_min_adult_age())
        self.assertEqual(expected_life_expectancy, self.race.get_life_expectancy())

        # size
        self.assertEqual(expected_size, self.race.get_size())

        # speed
        self.assertEqual(expected_speed, self.race.get_speed())

        # hp bonus
        self.assertEqual(expected_hp_bonus, self.race.get_hit_point_bonus())

    def _test_get_ability_bonus(
            self,
            expected_strength_bonus: int,
            expected_dexterity_bonus: int,
            expected_constitution_bonus: int,
            expected_intelligence_bonus: int,
            expected_wisdom_bonus: int,
            expected_charisma_bonus: int,
    ):
        """
        Helper method used to test the get ability bonus method of the race

        :param expected_strength_bonus: The expected strength bonus of the race
        :param expected_dexterity_bonus: The expected dexterity bonus of the race
        :param expected_constitution_bonus: The expected constitution bonus of the race
        :param expected_intelligence_bonus: The expected intelligence bonus of the race
        :param expected_wisdom_bonus: The expected wisdom bonus of the race
        :param expected_charisma_bonus: The expected charisma bonus of the race
        """

        def assert_get_ability_bonus(expected_bonus: int, ability: Ability):
            """
            Asserts that the expected_bonus is the same as the race's ability bonus for the given ability

            :param expected_bonus: The bonus the race is expected to have for the ability
            :param ability: The ability whose bonus to check against the expected bonus
            """

            self.assertEqual(expected_bonus, self.race.get_ability_bonus(ability))

        assert_get_ability_bonus(expected_strength_bonus, Ability.STRENGTH)
        assert_get_ability_bonus(expected_dexterity_bonus, Ability.DEXTERITY)
        assert_get_ability_bonus(expected_constitution_bonus, Ability.CONSTITUTION)
        assert_get_ability_bonus(expected_intelligence_bonus, Ability.INTELLIGENCE)
        assert_get_ability_bonus(expected_wisdom_bonus, Ability.WISDOM)
        assert_get_ability_bonus(expected_charisma_bonus, Ability.CHARISMA)

    def _test_proficient_in_skill(self, expected_skill_proficiencies: Tuple[Skill, ...]):
        """
        Helper method used to test the proficient in skill method of the race

        :param expected_skill_proficiencies: The expected skill proficiencies of the race
        """

        for skill in Skill:
            self.assertEqual(skill in expected_skill_proficiencies, self.race.proficient_in_skill(skill))
