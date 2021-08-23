from main.model.character.alignment import Alignment
from main.model.character.races.half_orc import HalfOrc
from main.model.character.utility.enumerators.size import Size
from main.model.character.utility.enumerators.skill import Skill
from test_helper.race_test_helper import RaceTestHelper


class HalfOrcTest(RaceTestHelper):
    def setUp(self) -> None:
        self.race = HalfOrc()

    def test_init(self):
        super()._test_init(
            expected_name="Half-Orc",
            expected_size=Size.MEDIUM,
            expected_speed=30,
            expected_hp_bonus=0,
            expected_min_adult_age=14,
            expected_life_expectancy=75,
            expected_acceptable_alignment_natures=(
                Alignment.Nature.NEUTRAL,
                Alignment.Nature.CHAOTIC
            ),
            expected_acceptable_alignment_moralities=(
                Alignment.Morality.NEUTRAL,
                Alignment.Morality.EVIL
            ),
            expected_trait_names=("Darkvision", "Relentless Endurance", "Savage Attacks"),
            expected_other_proficiency_names=("Common Language", "Orc Language")
        )

    def test_get_ability_bonus(self):
        super()._test_get_ability_bonus(
            expected_strength_bonus=2,
            expected_charisma_bonus=0,
            expected_intelligence_bonus=0,
            expected_constitution_bonus=1,
            expected_dexterity_bonus=0,
            expected_wisdom_bonus=0
        )

    def test_proficient_in_skill(self):
        super()._test_proficient_in_skill((Skill.INTIMIDATION,))
