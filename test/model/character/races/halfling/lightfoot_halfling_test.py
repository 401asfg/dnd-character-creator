from main.model.character.races.halflings.lightfoot_halfling import LightfootHalfling
from test_helper.races.halfling_test_helper import HalflingTestHelper


class LightfootHalflingTest(HalflingTestHelper):
    def setUp(self) -> None:
        self.race = LightfootHalfling()

    def test_halfling_init(self):
        super()._test_halfling_init(
            expected_additional_trait_names=("Naturally Stealthy",),
            expected_name="Lightfoot Halfling"
        )

    def test_halfling_get_ability_bonus(self):
        super()._test_halfling_get_ability_bonus(
            expected_strength_bonus=0,
            expected_charisma_bonus=1,
            expected_constitution_bonus=0,
            expected_wisdom_bonus=0,
            expected_intelligence_bonus=0
        )

    def test_halfling_proficient_in_skill(self):
        super()._test_halfing_proficient_in_skill()
