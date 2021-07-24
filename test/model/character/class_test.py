import unittest

from main.model.character.classes.bard import Bard
from main.model.character.classes.ranger import Ranger
from main.model.character.classes.wizard import Wizard


class ClassTest(unittest.TestCase):
    def test_get_name(self):
        self.assertEqual(Bard.get_name(), "Bard")
        self.assertEqual(Ranger.get_name(), "Ranger")
        self.assertEqual(Wizard.get_name(), "Wizard")

    def test_get_hit_points(self):
        self.assertEqual(Bard.get_hit_points(), 8)
        self.assertEqual(Ranger.get_hit_points(), 10)
        self.assertEqual(Wizard.get_hit_points(), 6)

    def test_strength_proficiency(self):
        self.assertEqual(Bard.strength_proficiency(), False)
        self.assertEqual(Ranger.strength_proficiency(), True)
        self.assertEqual(Wizard.strength_proficiency(), False)

    def test_dexterity_proficiency(self):
        self.assertEqual(Bard.dexterity_proficiency(), True)
        self.assertEqual(Ranger.dexterity_proficiency(), True)
        self.assertEqual(Wizard.dexterity_proficiency(), False)

    def test_constitution_proficiency(self):
        self.assertEqual(Bard.constitution_proficiency(), False)
        self.assertEqual(Ranger.constitution_proficiency(), False)
        self.assertEqual(Wizard.constitution_proficiency(), False)

    def test_intelligence_proficiency(self):
        self.assertEqual(Bard.intelligence_proficiency(), False)
        self.assertEqual(Ranger.intelligence_proficiency(), False)
        self.assertEqual(Wizard.intelligence_proficiency(), True)

    def test_wisdom_proficiency(self):
        self.assertEqual(Bard.wisdom_proficiency(), False)
        self.assertEqual(Ranger.wisdom_proficiency(), False)
        self.assertEqual(Wizard.wisdom_proficiency(), True)

    def test_charisma_proficiency(self):
        self.assertEqual(Bard.charisma_proficiency(), True)
        self.assertEqual(Ranger.charisma_proficiency(), False)
        self.assertEqual(Wizard.charisma_proficiency(), False)
