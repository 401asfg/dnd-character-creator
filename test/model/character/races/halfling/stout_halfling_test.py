from main.model.character.races.halflings.stout_halfling import StoutHalfling
from test_helper.races.halfling_test_helper import HalflingTestHelper


class StoutHalflingTest(HalflingTestHelper):
    def setUp(self) -> None:
        self.race = StoutHalfling()

    def test_halfling_init(self):
        super()._test_halfling_init(
            expected_additional_trait_names=("Stout Resilience",),
            expected_name="Stout Halfling"
        )

    def test_halfling_get_ability_bonus(self):
        super()._test_halfling_get_ability_bonus(
            expected_strength_bonus=0,
            expected_charisma_bonus=0,
            expected_constitution_bonus=1,
            expected_wisdom_bonus=0,
            expected_intelligence_bonus=0
        )

    def test_halfling_proficient_in_skill(self):
        super()._test_halfing_proficient_in_skill()
