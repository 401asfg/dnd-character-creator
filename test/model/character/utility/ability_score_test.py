import unittest

from main.model.character.utility.ability_score import AbilityScore


class AbilityScoreTest(unittest.TestCase):
    def test_init(self):
        def assert_same_value(x: int):
            """
            Asserts that x and AbilityScore(x).value are equal
            """

            self.assertEqual(AbilityScore(x).value, x)

        for i in range(AbilityScore.MIN_SCORE, AbilityScore.MAX_SCORE + 1):
            assert_same_value(i)

        def assert_error(x: int):
            """
            Asserts that AbilityScore(x) raises an error
            """

            try:
                AbilityScore(x)
                self.fail("An out of bounds value should have caused AbilityScore to raise an error.")
            except ValueError:
                pass

        assert_error(-10)
        assert_error(-7)
        assert_error(-3)
        assert_error(-2)
        assert_error(-1)
        assert_error(0)
        assert_error(1)
        assert_error(2)
        assert_error(19)
        assert_error(20)
        assert_error(21)
        assert_error(22)
        assert_error(42)
        assert_error(542)
        assert_error(2135235234)
