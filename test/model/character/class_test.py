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
