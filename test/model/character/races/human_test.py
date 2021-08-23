from main.model.character.alignment import Alignment
from main.model.character.races.human import Human
from main.model.character.utility.enumerators.language import Language
from main.model.character.utility.enumerators.size import Size
from main.model.character.utility.helper_modules.common_race_collection_items import get_language
from test_helper.race_test_helper import RaceTestHelper


class HumanTest(RaceTestHelper):
    def setUp(self) -> None:
        self.race = Human(Language.ELVISH)

    def test_init(self):
        super()._test_init(
            expected_name="Human",
            expected_size=Size.MEDIUM,
            expected_speed=30,
            expected_hp_bonus=0,
            expected_min_adult_age=18,
            expected_life_expectancy=99,
            expected_acceptable_alignment_natures=(
                Alignment.Nature.LAWFUL,
                Alignment.Nature.NEUTRAL,
                Alignment.Nature.CHAOTIC
            ),
            expected_acceptable_alignment_moralities=(
                Alignment.Morality.GOOD,
                Alignment.Morality.NEUTRAL,
                Alignment.Morality.EVIL
            ),
            expected_trait_names=(),
            expected_other_proficiency_names=(
                "Common Language",
                "Elvish Language"
            )
        )

    def test_init_language(self):
        def assert_language_pass(language: Language):
            """
            Asserts that giving a human the given language doesn't raise an error and gives the human a proficiency
            in that language

            :param language: A language that doesn't raise an error when given to a human
            """

            try:
                human = Human(language)
                self.assertEqual(get_language(language).name, human.other_proficiencies[1].name)
            except ValueError:
                self.fail("The given language shouldn't have caused the human to raise an error.")

        for lang in Language:
            if lang != Language.COMMON:
                assert_language_pass(lang)

    def test_init_language_error(self):
        try:
            Human(Language.COMMON)
            self.fail("The COMMON language should have caused the human to raise an error.")
        except ValueError:
            pass

    def test_get_ability_bonus(self):
        super()._test_get_ability_bonus(
            expected_strength_bonus=1,
            expected_charisma_bonus=1,
            expected_dexterity_bonus=1,
            expected_constitution_bonus=1,
            expected_intelligence_bonus=1,
            expected_wisdom_bonus=1
        )

    def test_proficient_in_skill(self):
        super()._test_proficient_in_skill(())
