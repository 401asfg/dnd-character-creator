import unittest

from main.model.character.advancements import get_level, get_min_exp, get_proficiency_bonus


class AdvancementsTest(unittest.TestCase):
    def test_get_level(self):
        # TODO: test every level?

        # Level 1
        self.assertEqual(get_level(0), 1)
        self.assertEqual(get_level(200), 1)
        self.assertEqual(get_level(299), 1)

        # Level 2
        self.assertEqual(get_level(300), 2)
        self.assertEqual(get_level(432), 2)
        self.assertEqual(get_level(899), 2)

        # Level 7
        self.assertEqual(get_level(23000), 7)
        self.assertEqual(get_level(26000), 7)
        self.assertEqual(get_level(33999), 7)

        # Level 15
        self.assertEqual(get_level(165000), 15)
        self.assertEqual(get_level(165001), 15)
        self.assertEqual(get_level(170370), 15)
        self.assertEqual(get_level(190000), 15)
        self.assertEqual(get_level(194999), 15)

        # Level 20
        self.assertEqual(get_level(355000), 20)
        self.assertEqual(get_level(355001), 20)
        self.assertEqual(get_level(400000), 20)
        self.assertEqual(get_level(999999), 20)
        self.assertEqual(get_level(45235345564565), 20)

    def test_get_min_exp(self):
        self.assertEqual(get_min_exp(1), 0)
        self.assertEqual(get_min_exp(4), 2700)
        self.assertEqual(get_min_exp(14), 140000)

    def test_get_proficiency_bonus(self):
        # PB 2
        self.assertEqual(get_proficiency_bonus(1), 2)
        self.assertEqual(get_proficiency_bonus(2), 2)
        self.assertEqual(get_proficiency_bonus(3), 2)
        self.assertEqual(get_proficiency_bonus(4), 2)

        # PB 3
        self.assertEqual(get_proficiency_bonus(5), 3)
        self.assertEqual(get_proficiency_bonus(6), 3)
        self.assertEqual(get_proficiency_bonus(7), 3)
        self.assertEqual(get_proficiency_bonus(8), 3)

        # PB 4
        self.assertEqual(get_proficiency_bonus(9), 4)
        self.assertEqual(get_proficiency_bonus(10), 4)
        self.assertEqual(get_proficiency_bonus(11), 4)
        self.assertEqual(get_proficiency_bonus(12), 4)

        # PB 5
        self.assertEqual(get_proficiency_bonus(13), 5)
        self.assertEqual(get_proficiency_bonus(14), 5)
        self.assertEqual(get_proficiency_bonus(15), 5)
        self.assertEqual(get_proficiency_bonus(16), 5)

        # PB 6
        self.assertEqual(get_proficiency_bonus(17), 6)
        self.assertEqual(get_proficiency_bonus(18), 6)
        self.assertEqual(get_proficiency_bonus(19), 6)
        self.assertEqual(get_proficiency_bonus(20), 6)
