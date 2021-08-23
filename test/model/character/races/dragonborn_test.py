from main.model.character.alignment import Alignment
from main.model.character.races.dragonborn import Dragonborn, DraconicAncestry
from main.model.character.utility.enumerators.size import Size
from test_helper.race_test_helper import RaceTestHelper


class DragonbornTest(RaceTestHelper):
    def setUp(self) -> None:
        self.race = Dragonborn(DraconicAncestry.BRONZE)

    def test_init(self):
        super()._test_init(
            expected_trait_names=(
                "Bronze",
                "Breath Weapon",
                "Damage Resistance"
            ),
            expected_other_proficiency_names=(
                "Common Language",
                "Draconic Language"
            ),
            expected_name="Dragonborn",
            expected_size=Size.MEDIUM,
            expected_speed=30,
            expected_min_adult_age=15,
            expected_life_expectancy=80,
            expected_hp_bonus=0,
            expected_acceptable_alignment_natures=(
                Alignment.Nature.LAWFUL,
                Alignment.Nature.NEUTRAL,
                Alignment.Nature.CHAOTIC
            ),
            expected_acceptable_alignment_moralities=(
                Alignment.Morality.GOOD,
                Alignment.Morality.EVIL
            )
        )

        def assert_ancestry(draconic_ancestry: DraconicAncestry, expected_ancestry_trait_name: str):
            """
            Asserts that creating a dragonborn with the given draconic_ancestry gives the dragonborn a trait with the
            expected_ancestry_trait_name

            :param draconic_ancestry: The ancestry to create the dragonborn with
            :param expected_ancestry_trait_name: The trait name to check for
            """

            dragonborn = Dragonborn(draconic_ancestry)
            self.assertEqual(expected_ancestry_trait_name, dragonborn.traits[0].name)

        assert_ancestry(DraconicAncestry.BLACK, "Black")
        assert_ancestry(DraconicAncestry.BLUE, "Blue")
        assert_ancestry(DraconicAncestry.BRASS, "Brass")
        assert_ancestry(DraconicAncestry.BRONZE, "Bronze")
        assert_ancestry(DraconicAncestry.COPPER, "Copper")
        assert_ancestry(DraconicAncestry.GOLD, "Gold")
        assert_ancestry(DraconicAncestry.GREEN, "Green")
        assert_ancestry(DraconicAncestry.RED, "Red")
        assert_ancestry(DraconicAncestry.SILVER, "Silver")
        assert_ancestry(DraconicAncestry.WHITE, "White")

    def test_get_ability_bonus(self):
        super()._test_get_ability_bonus(
            expected_strength_bonus=2,
            expected_charisma_bonus=1,
            expected_intelligence_bonus=0,
            expected_constitution_bonus=0,
            expected_wisdom_bonus=0,
            expected_dexterity_bonus=0
        )

    def test_proficient_in_skill(self):
        super()._test_proficient_in_skill(())