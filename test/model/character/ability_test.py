import unittest

from main.model.character.ability import Ability
from main.model.inttypes.natural_plus import NaturalPlus
from typing import Callable


class AbilityTest(unittest.TestCase):
    def test_init(self):
        def assert_same_value(x: int):
            """
            Asserts that x and Ability(x).score are equal
            """

            self.assertEqual(Ability(NaturalPlus(x)).score, x)

        for i in range(1, Ability.MAX_SCORE + 1):
            assert_same_value(i)

        for_each_ability_score_value(assert_same_value)

        def assert_error(x: int):
            """
            Asserts that Ability(x) raises an error
            """

            try:
                Ability(NaturalPlus(x))
                self.fail("The greater than 20 value should have caused Ability to raise an error.")
            except ValueError:
                pass

        assert_error(21)
        assert_error(22)
        assert_error(42)
        assert_error(542)
        assert_error(2135235234)

    def test_modifier(self):
        self.assertEqual(Ability(NaturalPlus(1)).modifier, -5)
        self.assertEqual(Ability(NaturalPlus(2)).modifier, -4)
        self.assertEqual(Ability(NaturalPlus(3)).modifier, -4)
        self.assertEqual(Ability(NaturalPlus(4)).modifier, -3)
        self.assertEqual(Ability(NaturalPlus(5)).modifier, -3)
        self.assertEqual(Ability(NaturalPlus(6)).modifier, -2)
        self.assertEqual(Ability(NaturalPlus(7)).modifier, -2)
        self.assertEqual(Ability(NaturalPlus(8)).modifier, -1)
        self.assertEqual(Ability(NaturalPlus(9)).modifier, -1)
        self.assertEqual(Ability(NaturalPlus(10)).modifier, 0)
        self.assertEqual(Ability(NaturalPlus(11)).modifier, 0)
        self.assertEqual(Ability(NaturalPlus(12)).modifier, 1)
        self.assertEqual(Ability(NaturalPlus(13)).modifier, 1)
        self.assertEqual(Ability(NaturalPlus(14)).modifier, 2)
        self.assertEqual(Ability(NaturalPlus(15)).modifier, 2)
        self.assertEqual(Ability(NaturalPlus(16)).modifier, 3)
        self.assertEqual(Ability(NaturalPlus(17)).modifier, 3)
        self.assertEqual(Ability(NaturalPlus(18)).modifier, 4)
        self.assertEqual(Ability(NaturalPlus(19)).modifier, 4)
        self.assertEqual(Ability(NaturalPlus(20)).modifier, 5)


def for_each_ability_score_value(fn: Callable[[int], None]):
    """
    Call fn for each ability score value

    :param fn: The fn to call
    """

    for i in range(1, Ability.MAX_SCORE + 1):
        fn(i)
