import unittest

from main.model.character.classes.bard import Bard
from main.model.character.classes.ranger import Ranger
from main.model.character.classes.wizard import Wizard
from main.model.character.utility.enumerators.ability_proficiency import AbilityProficiency


class ClassTest(unittest.TestCase):
    def test_get_name(self):
        self.assertEqual(Bard.get_name(), "Bard")
        self.assertEqual(Ranger.get_name(), "Ranger")
        self.assertEqual(Wizard.get_name(), "Wizard")

    def test_get_hit_die(self):
        self.assertEqual(Bard.get_hit_die().name, "1d8")
        self.assertEqual(Ranger.get_hit_die().name, "1d10")
        self.assertEqual(Wizard.get_hit_die().name, "1d6")

    def test_proficient_in_strength(self):
        self.assertEqual(Bard.proficient(AbilityProficiency.STRENGTH), False)
        self.assertEqual(Ranger.proficient(AbilityProficiency.STRENGTH), True)
        self.assertEqual(Wizard.proficient(AbilityProficiency.STRENGTH), False)

    def test_proficient_in_dexterity(self):
        self.assertEqual(Bard.proficient(AbilityProficiency.DEXTERITY), True)
        self.assertEqual(Ranger.proficient(AbilityProficiency.DEXTERITY), True)
        self.assertEqual(Wizard.proficient(AbilityProficiency.DEXTERITY), False)

    def test_proficient_in_constitution(self):
        self.assertEqual(Bard.proficient(AbilityProficiency.CONSTITUTION), False)
        self.assertEqual(Ranger.proficient(AbilityProficiency.CONSTITUTION), False)
        self.assertEqual(Wizard.proficient(AbilityProficiency.CONSTITUTION), False)

    def test_proficient_in_intelligence(self):
        self.assertEqual(Bard.proficient(AbilityProficiency.INTELLIGENCE), False)
        self.assertEqual(Ranger.proficient(AbilityProficiency.INTELLIGENCE), False)
        self.assertEqual(Wizard.proficient(AbilityProficiency.INTELLIGENCE), True)

    def test_proficient_in_wisdom(self):
        self.assertEqual(Bard.proficient(AbilityProficiency.WISDOM), False)
        self.assertEqual(Ranger.proficient(AbilityProficiency.WISDOM), False)
        self.assertEqual(Wizard.proficient(AbilityProficiency.WISDOM), True)

    def test_proficient_in_charisma(self):
        self.assertEqual(Bard.proficient(AbilityProficiency.CHARISMA), True)
        self.assertEqual(Ranger.proficient(AbilityProficiency.CHARISMA), False)
        self.assertEqual(Wizard.proficient(AbilityProficiency.CHARISMA), False)
