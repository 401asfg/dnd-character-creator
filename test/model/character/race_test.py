import unittest
from collections import Callable

from main.model.character.alignment import Alignment
from main.model.character.race import Race
from main.model.character.races.dragonborn import Dragonborn
from main.model.character.races.dwarf import Dwarf
from main.model.character.races.elf import Elf
from main.model.character.races.gnome import Gnome
from main.model.character.races.human import Human
from main.model.character.enumerators.size import Size


class RaceTest(unittest.TestCase):
    def test_race_base_class(self):
        def assert_raises_not_implemented_error(fn: Callable):
            """
            Assert that calling the given fn raises a NotImplementedError
            """

            try:
                fn()
                self.fail("Race's methods should not be implemented")
            except NotImplementedError:
                pass

        assert_raises_not_implemented_error(Race.get_name)
        assert_raises_not_implemented_error(Race.get_strength_bonus)
        assert_raises_not_implemented_error(Race.get_dexterity_bonus)
        assert_raises_not_implemented_error(Race.get_constitution_bonus)
        assert_raises_not_implemented_error(Race.get_intelligence_bonus)
        assert_raises_not_implemented_error(Race.get_wisdom_bonus)
        assert_raises_not_implemented_error(Race.get_charisma_bonus)
        assert_raises_not_implemented_error(Race.get_acceptable_alignment_natures)
        assert_raises_not_implemented_error(Race.get_acceptable_alignment_moralities)
        assert_raises_not_implemented_error(Race.get_min_adult_age)
        assert_raises_not_implemented_error(Race.get_life_expectancy)
        assert_raises_not_implemented_error(Race.get_size)
        assert_raises_not_implemented_error(Race.get_speed)

    def test_get_name(self):
        self.assertEqual(Dragonborn.get_name(), "Dragonborn")
        self.assertEqual(Human.get_name(), "Human")
        self.assertEqual(Elf.get_name(), "Elf")

    def test_get_strength_bonus(self):
        self.assertEqual(Dwarf.get_strength_bonus(), 0)
        self.assertEqual(Human.get_strength_bonus(), 1)
        self.assertEqual(Gnome.get_strength_bonus(), 0)

    def test_get_dexterity_bonus(self):
        self.assertEqual(Elf.get_dexterity_bonus(), 2)
        self.assertEqual(Dwarf.get_dexterity_bonus(), 0)
        self.assertEqual(Dragonborn.get_dexterity_bonus(), 0)

    def test_get_constitution_bonus(self):
        self.assertEqual(Gnome.get_constitution_bonus(), 0)
        self.assertEqual(Human.get_constitution_bonus(), 1)
        self.assertEqual(Elf.get_constitution_bonus(), 0)

    def test_get_intelligence_bonus(self):
        self.assertEqual(Dwarf.get_intelligence_bonus(), 0)
        self.assertEqual(Elf.get_intelligence_bonus(), 0)
        self.assertEqual(Gnome.get_intelligence_bonus(), 2)

    def test_get_wisdom_bonus(self):
        self.assertEqual(Elf.get_wisdom_bonus(), 0)
        self.assertEqual(Dragonborn.get_wisdom_bonus(), 0)
        self.assertEqual(Human.get_wisdom_bonus(), 1)

    def test_get_charisma_bonus(self):
        self.assertEqual(Gnome.get_charisma_bonus(), 0)
        self.assertEqual(Dragonborn.get_charisma_bonus(), 0)
        self.assertEqual(Dwarf.get_charisma_bonus(), 0)

    def test_get_acceptable_alignment_natures(self):
        self.assertEqual(
            Elf.get_acceptable_alignment_natures(),
            [
                Alignment.Nature.NEUTRAL,
                Alignment.Nature.CHAOTIC
            ]
        )

        self.assertEqual(
            Gnome.get_acceptable_alignment_natures(),
            [
                Alignment.Nature.LAWFUL,
                Alignment.Nature.NEUTRAL,
                Alignment.Nature.CHAOTIC
            ]
        )

        self.assertEqual(
            Dwarf.get_acceptable_alignment_natures(),
            [
                Alignment.Nature.LAWFUL,
                Alignment.Nature.NEUTRAL
            ]
        )

    def test_get_acceptable_alignment_moralities(self):
        self.assertEqual(
            Dragonborn.get_acceptable_alignment_moralities(),
            [
                Alignment.Morality.GOOD,
                Alignment.Morality.EVIL
            ]
        )

        self.assertEqual(
            Gnome.get_acceptable_alignment_moralities(),
            [
                Alignment.Morality.GOOD,
                Alignment.Morality.NEUTRAL
            ]
        )

        self.assertEqual(
            Human.get_acceptable_alignment_moralities(),
            [
                Alignment.Morality.GOOD,
                Alignment.Morality.NEUTRAL,
                Alignment.Morality.EVIL
            ]
        )

    def test_get_min_adult_age(self):
        self.assertEqual(Human.get_min_adult_age(), 18)
        self.assertEqual(Elf.get_min_adult_age(), 100)
        self.assertEqual(Dwarf.get_min_adult_age(), 50)

    def test_get_life_expectancy(self):
        self.assertEqual(Elf.get_life_expectancy(), 750)
        self.assertEqual(Gnome.get_life_expectancy(), 500)
        self.assertEqual(Dragonborn.get_life_expectancy(), 80)

    def test_get_size(self):
        self.assertEqual(Elf.get_size(), Size.MEDIUM)
        self.assertEqual(Human.get_size(), Size.MEDIUM)
        self.assertEqual(Dwarf.get_size(), Size.MEDIUM)

    def test_get_speed(self):
        self.assertEqual(Dragonborn.get_speed(), 30)
        self.assertEqual(Human.get_speed(), 30)
        self.assertEqual(Gnome.get_speed(), 25)
