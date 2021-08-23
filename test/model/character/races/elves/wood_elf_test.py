from main.model.character.races.elves.wood_elf import WoodElf
from test_helper.races.elf_test_helper import ElfTestHelper


class WoodElfTest(ElfTestHelper):
    def setUp(self) -> None:
        self.race = WoodElf()

    def test_elf_init(self):
        self._test_elf_init(
            expected_additional_trait_names=("Mask of the Wild",),
            expected_additional_other_proficiency_names=(),
            expected_name="Wood Elf",
            expected_speed=35
        )

    def test_elf_get_ability_bonus(self):
        self._test_elf_get_ability_bonus(
            expected_strength_bonus=0,
            expected_constitution_bonus=0,
            expected_intelligence_bonus=0,
            expected_wisdom_bonus=1,
            expected_charisma_bonus=0
        )

    def test_elf_proficient_in_skill(self):
        self._test_elf_proficient_in_skill()
