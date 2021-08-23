from main.model.character.races.dwarves.dwarf import ToolProficiency
from main.model.character.races.dwarves.hill_dwarf import HillDwarf
from test_helper.races.dwarf_test_helper import DwarfTestHelper


class HillDwarfTest(DwarfTestHelper):
    def setUp(self) -> None:
        self.race = HillDwarf(ToolProficiency.SMITHS_TOOLS)

    def test_dwarf_init(self):
        self._test_dwarf_init(
            expected_additional_trait_names=("Dwarven Toughness",),
            expected_additional_other_proficiency_names=(),
            expected_name="Hill Dwarf",
            expected_hp_bonus=1
        )

        self.assertEqual("Brewer's Supplies", HillDwarf(ToolProficiency.BREWERS_SUPPLIES).other_proficiencies[1].name)
        self.assertEqual("Mason's Tools", HillDwarf(ToolProficiency.MASONS_TOOLS).other_proficiencies[1].name)

    def test_dwarf_get_ability_bonus(self):
        self._test_dwarf_get_ability_bonus(
            expected_strength_bonus=0,
            expected_dexterity_bonus=0,
            expected_intelligence_bonus=0,
            expected_wisdom_bonus=1,
            expected_charisma_bonus=0
        )

    def test_dwarf_proficient_in_skill(self):
        self._test_dwarf_proficient_in_skill()
