from main.model.character.races.elves.high_elf import HighElf
from main.model.character.utility.enumerators.language import Language
from test_helper.races.elf_test_helper import ElfTestHelper


class HighElfTest(ElfTestHelper):
    def setUp(self) -> None:
        self.race = HighElf(Language.ORC)

    def test_elf_init(self):
        self._test_elf_init(
            expected_additional_trait_names=(),
            expected_additional_other_proficiency_names=("Orc Language",),
            expected_speed=30,
            expected_name="High Elf"
        )

    def test_init_error(self):
        def assert_init_error(language: Language):
            """
            Asserts that creating a half elf with the given language raises an error

            :param language: The language that raises an error
            """

            try:
                HighElf(language)
                self.fail("A High elf should raise a ValueError if the same language was given to it twice.")
            except ValueError:
                pass

        assert_init_error(Language.COMMON)
        assert_init_error(Language.ELVISH)

    def test_elf_get_ability_bonus(self):
        self._test_elf_get_ability_bonus(
            expected_strength_bonus=0,
            expected_charisma_bonus=0,
            expected_wisdom_bonus=0,
            expected_intelligence_bonus=1,
            expected_constitution_bonus=0
        )

    def test_elf_proficient_in_skill(self):
        self._test_elf_proficient_in_skill()
