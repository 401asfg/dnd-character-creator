from main.model.character.alignment import Alignment
from main.model.character.races.tiefling import Tiefling
from main.model.character.utility.enumerators.size import Size
from test_helper.race_test_helper import RaceTestHelper


class TieflingTest(RaceTestHelper):
    def setUp(self) -> None:
        self.race = Tiefling()

    def test_init(self):
        super()._test_init(
            expected_name="Tiefling",
            expected_speed=30,
            expected_size=Size.MEDIUM,
            expected_hp_bonus=0,
            expected_min_adult_age=18,
            expected_life_expectancy=99,
            expected_acceptable_alignment_natures=(
                Alignment.Nature.NEUTRAL,
                Alignment.Nature.CHAOTIC
            ),
            expected_acceptable_alignment_moralities=(
                Alignment.Morality.NEUTRAL,
                Alignment.Morality.EVIL
            ),
            expected_trait_names=(
                "Darkvision",
                "Hellish Resistance"
            ),
            expected_other_proficiency_names=(
                "Common Language",
                "Infernal Language"
            )
        )

    def test_get_ability_bonus(self):
        super()._test_get_ability_bonus(
            expected_intelligence_bonus=1,
            expected_wisdom_bonus=0,
            expected_constitution_bonus=0,
            expected_charisma_bonus=2,
            expected_dexterity_bonus=0,
            expected_strength_bonus=0
        )

    def test_proficient_in_skill(self):
        super()._test_proficient_in_skill(())
