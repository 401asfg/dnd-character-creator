import unittest

from main.model.dice.die import Die


class DieTest(unittest.TestCase):
    def test_name(self):
        def assert_name(sides: Die.Sides, expected_name: str):
            """
            Assert that die.name produces the expected_name

            :param sides: The number of sides each die has
            :param expected_name: The expected name
            """
            self.assertEqual(expected_name, Die(sides).name)

        assert_name(Die.Sides.FOUR, "1d4")
        assert_name(Die.Sides.SIX, "1d6")
        assert_name(Die.Sides.EIGHT, "1d8")
        assert_name(Die.Sides.TEN, "1d10")
        assert_name(Die.Sides.TWELVE, "1d12")
        assert_name(Die.Sides.TWENTY, "1d20")

    def test_min_possible_score(self):
        def assert_min_possible_score(sides: Die.Sides, expected_score: int):
            """
            Assert that die.min_possible_score produces the expected_name

            :param sides: The number of sides each die has
            :param expected_score: The expected score
            """
            self.assertEqual(expected_score, Die(sides).min_possible_score)

        assert_min_possible_score(Die.Sides.FOUR, 1)
        assert_min_possible_score(Die.Sides.SIX, 1)
        assert_min_possible_score(Die.Sides.EIGHT, 1)
        assert_min_possible_score(Die.Sides.TEN, 1)
        assert_min_possible_score(Die.Sides.TWELVE, 1)
        assert_min_possible_score(Die.Sides.TWENTY, 1)

    def test_max_possible_score(self):
        def assert_max_possible_score(sides: Die.Sides, expected_score: int):
            """
            Assert that die.max_possible_score produces the expected_name

            :param sides: The number of sides each die has
            :param expected_score: The expected score
            """
            self.assertEqual(expected_score, Die(sides).max_possible_score)

        assert_max_possible_score(Die.Sides.FOUR, 4)
        assert_max_possible_score(Die.Sides.SIX, 6)
        assert_max_possible_score(Die.Sides.EIGHT, 8)
        assert_max_possible_score(Die.Sides.TEN, 10)
        assert_max_possible_score(Die.Sides.TWELVE, 12)
        assert_max_possible_score(Die.Sides.TWENTY, 20)

    def test_possible_score(self):
        def assert_possible_score(sides: Die.Sides):
            """
            Asserts that all the values between the min and max possible scores are possible scores of the die

            :param sides: The number of sides of the die whose possible scores are being checked
            """

            die = Die(sides)

            for i in range(die.min_possible_score, die.max_possible_score + 1):
                self.assertTrue(die.possible_score(i))

        assert_possible_score(Die.Sides.FOUR)
        assert_possible_score(Die.Sides.SIX)
        assert_possible_score(Die.Sides.EIGHT)
        assert_possible_score(Die.Sides.TEN)
        assert_possible_score(Die.Sides.TWELVE)
        assert_possible_score(Die.Sides.TWENTY)

        def assert_not_possible_score(sides: Die.Sides):
            """
            Asserts that values less than the min and larger than the max possible scores are not possible scores of the
            die

            :param sides: The number of sides of the die whose possible scores are being checked
            """

            die = Die(sides)

            MAX = die.max_possible_score

            self.assertFalse(die.possible_score(-9345376))
            self.assertFalse(die.possible_score(-1423))
            self.assertFalse(die.possible_score(-854))

            for i in range(-100, die.min_possible_score):
                self.assertFalse(die.possible_score(i))

            for i in range(MAX + 1, MAX + 101):
                self.assertFalse(die.possible_score(i))

            self.assertFalse(die.possible_score(MAX + 256))
            self.assertFalse(die.possible_score(MAX + 3456))
            self.assertFalse(die.possible_score(MAX + 74563234))

        assert_not_possible_score(Die.Sides.FOUR)
        assert_not_possible_score(Die.Sides.SIX)
        assert_not_possible_score(Die.Sides.EIGHT)
        assert_not_possible_score(Die.Sides.TEN)
        assert_not_possible_score(Die.Sides.TWELVE)
        assert_not_possible_score(Die.Sides.TWENTY)
