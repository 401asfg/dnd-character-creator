from main.model.character.alignment import Alignment
from main.model.character.races.gnomes.rock_gnome import RockGnome
from test_helper.races.gnome_test_helper import GnomeTestHelper


class RockGnomeTest(GnomeTestHelper):
    def setUp(self) -> None:
        self.race = RockGnome()

    def test_gnome_init(self):
        super()._test_gnome_init(
            expected_additional_trait_names=(
                "Artificer's Lore",
            ),
            expected_additional_other_proficiency_names=("Tinker",),
            expected_name="Rock Gnome",
            expected_acceptable_alignment_natures=(
                Alignment.Nature.LAWFUL,
                Alignment.Nature.NEUTRAL,
                Alignment.Nature.CHAOTIC
            ),
            expected_acceptable_alignment_moralities=(
                Alignment.Morality.GOOD,
                Alignment.Morality.NEUTRAL
            ),
            expected_min_adult_age=40,
            expected_life_expectancy=500
        )

    def test_gnome_get_ability_bonus(self):
        super()._test_gnome_get_ability_bonus(
            expected_strength_bonus=0,
            expected_dexterity_bonus=0,
            expected_constitution_bonus=1,
            expected_wisdom_bonus=0,
            expected_charisma_bonus=0
        )

    def test_gnome_proficient_in_skill(self):
        super()._test_gnome_proficient_in_skill()
