import unittest

from main.model.dice.dice import Dice
from main.model.int_types.posint import Posint


class DiceTest(unittest.TestCase):
    def test_name(self):
        def assert_name(num: int, sides: Dice.Sides, expected_name: str):
            """
            Assert that dice.name produces the expected_name

            :param num: The number of dice in the set
            :param sides: The number of sides each dice has
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
            :param sides: The number of sides each dice has
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
            :param sides: The number of sides each dice has
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

    def test_possible_score(self):
        def assert_possible_score_for_all_sides(num_dice: int):
            """
            Asserts that all the values between the min and max possible scores are possible scores of the dice set, and
            that this holds true for all possible sides the dice for the given num of dice

            :param num_dice: The number of dice in the set
            """

            def assert_possible_score(num: int, sides: Dice.Sides):
                """
                Asserts that all the values between the min and max possible scores are possible scores of the dice set

                :param num: The number of dice in the set
                :param sides: The number of sides of the dice whose possible scores are being checked
                """

                dice = Dice(Posint(num), sides)

                for i in range(dice.min_possible_score, dice.max_possible_score + 1):
                    self.assertTrue(dice.possible_score(i))

            assert_possible_score(num_dice, Dice.Sides.FOUR)
            assert_possible_score(num_dice, Dice.Sides.SIX)
            assert_possible_score(num_dice, Dice.Sides.EIGHT)
            assert_possible_score(num_dice, Dice.Sides.TEN)
            assert_possible_score(num_dice, Dice.Sides.TWELVE)
            assert_possible_score(num_dice, Dice.Sides.TWENTY)

        assert_possible_score_for_all_sides(1)
        assert_possible_score_for_all_sides(2)
        assert_possible_score_for_all_sides(3)
        assert_possible_score_for_all_sides(4)
        assert_possible_score_for_all_sides(5)
        assert_possible_score_for_all_sides(6)
        assert_possible_score_for_all_sides(7)
        assert_possible_score_for_all_sides(8)
        assert_possible_score_for_all_sides(9)
        assert_possible_score_for_all_sides(10)
        assert_possible_score_for_all_sides(11)
        assert_possible_score_for_all_sides(12)
        assert_possible_score_for_all_sides(13)
        assert_possible_score_for_all_sides(14)
        assert_possible_score_for_all_sides(15)
        assert_possible_score_for_all_sides(16)
        assert_possible_score_for_all_sides(17)
        assert_possible_score_for_all_sides(18)
        assert_possible_score_for_all_sides(19)
        assert_possible_score_for_all_sides(20)
        assert_possible_score_for_all_sides(21)
        assert_possible_score_for_all_sides(22)
        assert_possible_score_for_all_sides(23)
        assert_possible_score_for_all_sides(64)
        assert_possible_score_for_all_sides(77)
        assert_possible_score_for_all_sides(525)
        assert_possible_score_for_all_sides(634)
        assert_possible_score_for_all_sides(1345)
        assert_possible_score_for_all_sides(6246)

        def assert_not_possible_score_for_all_sides(num_dice: int):
            """
            Asserts that values less than the min and larger than the max possible scores are not possible scores of the
            dice set, and that this holds for all possible sides the dice for the given num of dice

            :param num_dice: The number of dice in the set
            """

            def assert_not_possible_score(num: int, sides: Dice.Sides):
                """
                Asserts that values less than the min and larger than the max possible scores are not possible scores of
                the dice set

                :param num: The number of dice in the set
                :param sides: The number of sides of the dice whose possible scores are being checked
                """

                dice = Dice(Posint(num), sides)

                MAX = dice.max_possible_score

                self.assertFalse(dice.possible_score(-9345376))
                self.assertFalse(dice.possible_score(-1423))
                self.assertFalse(dice.possible_score(-854))

                for i in range(-100, dice.min_possible_score):
                    self.assertFalse(dice.possible_score(i))

                for i in range(MAX + 1, MAX + 101):
                    self.assertFalse(dice.possible_score(i))

                self.assertFalse(dice.possible_score(MAX + 256))
                self.assertFalse(dice.possible_score(MAX + 3456))
                self.assertFalse(dice.possible_score(MAX + 74563234))

            assert_not_possible_score(num_dice, Dice.Sides.FOUR)
            assert_not_possible_score(num_dice, Dice.Sides.SIX)
            assert_not_possible_score(num_dice, Dice.Sides.EIGHT)
            assert_not_possible_score(num_dice, Dice.Sides.TEN)
            assert_not_possible_score(num_dice, Dice.Sides.TWELVE)
            assert_not_possible_score(num_dice, Dice.Sides.TWENTY)

        assert_not_possible_score_for_all_sides(1)
        assert_not_possible_score_for_all_sides(2)
        assert_not_possible_score_for_all_sides(3)
        assert_not_possible_score_for_all_sides(4)
        assert_not_possible_score_for_all_sides(5)
        assert_not_possible_score_for_all_sides(6)
        assert_not_possible_score_for_all_sides(7)
        assert_not_possible_score_for_all_sides(8)
        assert_not_possible_score_for_all_sides(9)
        assert_not_possible_score_for_all_sides(10)
        assert_not_possible_score_for_all_sides(11)
        assert_not_possible_score_for_all_sides(12)
        assert_not_possible_score_for_all_sides(13)
        assert_not_possible_score_for_all_sides(14)
        assert_not_possible_score_for_all_sides(15)
        assert_not_possible_score_for_all_sides(16)
        assert_not_possible_score_for_all_sides(17)
        assert_not_possible_score_for_all_sides(18)
        assert_not_possible_score_for_all_sides(19)
        assert_not_possible_score_for_all_sides(20)
        assert_not_possible_score_for_all_sides(21)
        assert_not_possible_score_for_all_sides(22)
        assert_not_possible_score_for_all_sides(23)
        assert_not_possible_score_for_all_sides(64)
        assert_not_possible_score_for_all_sides(77)
        assert_not_possible_score_for_all_sides(525)
        assert_not_possible_score_for_all_sides(634)
        assert_not_possible_score_for_all_sides(1345)
        assert_not_possible_score_for_all_sides(6246)
