import unittest

from main.model.dice.dice import Dice
from main.model.int_types.posint import Posint


class DiceTest(unittest.TestCase):
    def test_name(self):
        def assert_name(num: int, sides: Dice.Sides, expected_name: str):
            """
            Assert that dice.name produces the expected_name

            :param num: The number of dice in the set
            :param sides: The number of sides each die has
            :param expected_name: The expected name
            """
            self.assertEqual(expected_name, Dice(Posint(num), sides).name)

        assert_name(1, Dice.Sides.FOUR, "1d4")
        assert_name(1, Dice.Sides.SIX, "1d6")
        assert_name(1, Dice.Sides.EIGHT, "1d8")
        assert_name(1, Dice.Sides.TEN, "1d10")
        assert_name(1, Dice.Sides.TWELVE, "1d12")
        assert_name(1, Dice.Sides.TWENTY, "1d20")

        assert_name(4, Dice.Sides.FOUR, "4d4")
        assert_name(4, Dice.Sides.SIX, "4d6")
        assert_name(4, Dice.Sides.EIGHT, "4d8")
        assert_name(4, Dice.Sides.TEN, "4d10")
        assert_name(4, Dice.Sides.TWELVE, "4d12")
        assert_name(4, Dice.Sides.TWENTY, "4d20")

        assert_name(27, Dice.Sides.FOUR, "27d4")
        assert_name(27, Dice.Sides.SIX, "27d6")
        assert_name(27, Dice.Sides.EIGHT, "27d8")
        assert_name(27, Dice.Sides.TEN, "27d10")
        assert_name(27, Dice.Sides.TWELVE, "27d12")
        assert_name(27, Dice.Sides.TWENTY, "27d20")

    def test_min_possible_score(self):
        def assert_min_possible_score(num: int, sides: Dice.Sides, expected_score: int):
            """
            Assert that dice.min_possible_score produces the expected_name

            :param num: The number of dice in the set
            :param sides: The number of sides each die has
            :param expected_score: The expected score
            """
            self.assertEqual(expected_score, Dice(Posint(num), sides).min_possible_score)

        assert_min_possible_score(1, Dice.Sides.FOUR, 1)
        assert_min_possible_score(1, Dice.Sides.SIX, 1)
        assert_min_possible_score(1, Dice.Sides.EIGHT, 1)
        assert_min_possible_score(1, Dice.Sides.TEN, 1)
        assert_min_possible_score(1, Dice.Sides.TWELVE, 1)
        assert_min_possible_score(1, Dice.Sides.TWENTY, 1)

        assert_min_possible_score(4, Dice.Sides.FOUR, 4)
        assert_min_possible_score(4, Dice.Sides.SIX, 4)
        assert_min_possible_score(4, Dice.Sides.EIGHT, 4)
        assert_min_possible_score(4, Dice.Sides.TEN, 4)
        assert_min_possible_score(4, Dice.Sides.TWELVE, 4)
        assert_min_possible_score(4, Dice.Sides.TWENTY, 4)

        assert_min_possible_score(27, Dice.Sides.FOUR, 27)
        assert_min_possible_score(27, Dice.Sides.SIX, 27)
        assert_min_possible_score(27, Dice.Sides.EIGHT, 27)
        assert_min_possible_score(27, Dice.Sides.TEN, 27)
        assert_min_possible_score(27, Dice.Sides.TWELVE, 27)
        assert_min_possible_score(27, Dice.Sides.TWENTY, 27)

    def test_max_possible_score(self):
        def assert_max_possible_score(num: int, sides: Dice.Sides, expected_score: int):
            """
            Assert that dice.max_possible_score produces the expected_name

            :param num: The number of dice in the set
            :param sides: The number of sides each die has
            :param expected_score: The expected score
            """
            self.assertEqual(expected_score, Dice(Posint(num), sides).max_possible_score)

        assert_max_possible_score(1, Dice.Sides.FOUR, 4)
        assert_max_possible_score(1, Dice.Sides.SIX, 6)
        assert_max_possible_score(1, Dice.Sides.EIGHT, 8)
        assert_max_possible_score(1, Dice.Sides.TEN, 10)
        assert_max_possible_score(1, Dice.Sides.TWELVE, 12)
        assert_max_possible_score(1, Dice.Sides.TWENTY, 20)

        assert_max_possible_score(4, Dice.Sides.FOUR, 16)
        assert_max_possible_score(4, Dice.Sides.SIX, 24)
        assert_max_possible_score(4, Dice.Sides.EIGHT, 32)
        assert_max_possible_score(4, Dice.Sides.TEN, 40)
        assert_max_possible_score(4, Dice.Sides.TWELVE, 48)
        assert_max_possible_score(4, Dice.Sides.TWENTY, 80)

        assert_max_possible_score(27, Dice.Sides.FOUR, 108)
        assert_max_possible_score(27, Dice.Sides.SIX, 162)
        assert_max_possible_score(27, Dice.Sides.EIGHT, 216)
        assert_max_possible_score(27, Dice.Sides.TEN, 270)
        assert_max_possible_score(27, Dice.Sides.TWELVE, 324)
        assert_max_possible_score(27, Dice.Sides.TWENTY, 540)
