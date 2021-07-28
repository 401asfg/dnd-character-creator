import unittest

from main.model.character.classes.bard import Bard
from main.model.character.classes.ranger import Ranger
from main.model.character.classes.wizard import Wizard


class ClassTest(unittest.TestCase):
    def test_get_name(self):
        self.assertEqual(Bard.get_name(), "Bard")
        self.assertEqual(Ranger.get_name(), "Ranger")
        self.assertEqual(Wizard.get_name(), "Wizard")

    def test_get_hit_die(self):
        self.assertEqual(Bard.get_hit_points(), 8)
        self.assertEqual(Ranger.get_hit_points(), 10)
        self.assertEqual(Wizard.get_hit_points(), 6)

    def test_get_strength_proficiency(self):
        self.assertEqual(Bard.get_strength_proficiency(), False)
        self.assertEqual(Ranger.get_strength_proficiency(), True)
        self.assertEqual(Wizard.get_strength_proficiency(), False)

    def test_get_dexterity_proficiency(self):
        self.assertEqual(Bard.get_dexterity_proficiency(), True)
        self.assertEqual(Ranger.get_dexterity_proficiency(), True)
        self.assertEqual(Wizard.get_dexterity_proficiency(), False)

    def test_get_constitution_proficiency(self):
        self.assertEqual(Bard.get_constitution_proficiency(), False)
        self.assertEqual(Ranger.get_constitution_proficiency(), False)
        self.assertEqual(Wizard.get_constitution_proficiency(), False)

    def test_get_intelligence_proficiency(self):
        self.assertEqual(Bard.get_intelligence_proficiency(), False)
        self.assertEqual(Ranger.get_intelligence_proficiency(), False)
        self.assertEqual(Wizard.get_intelligence_proficiency(), True)

    def test_get_wisdom_proficiency(self):
        self.assertEqual(Bard.get_wisdom_proficiency(), False)
        self.assertEqual(Ranger.get_wisdom_proficiency(), False)
        self.assertEqual(Wizard.get_wisdom_proficiency(), True)

    def test_get_charisma_proficiency(self):
        self.assertEqual(Bard.get_charisma_proficiency(), True)
        self.assertEqual(Ranger.get_charisma_proficiency(), False)
        self.assertEqual(Wizard.get_charisma_proficiency(), False)
