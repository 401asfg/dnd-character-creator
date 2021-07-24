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

    def test_value_setter(self):
        def assert_same_value(x: int):
            """
            Asserts that after ability.score = x, ability.score and x.value are equal
            """

            ability = Ability(NaturalPlus(1))
            ability.score = NaturalPlus(x)
            self.assertEqual(ability.score, x)

        for_each_ability_score_value(assert_same_value)

        def assert_error(x: int):
            """
            Asserts that ability.score = x raises an error
            """

            try:
                ability = Ability(NaturalPlus(1))
                ability.score = NaturalPlus(x)
                self.fail("The greater than 20 value should have caused ability.score to raise an error.")
            except ValueError:
                assert_same_value(1)

        assert_error(21)
        assert_error(22)
        assert_error(23)
        assert_error(43)
        assert_error(32)
        assert_error(93)
        assert_error(234)
        assert_error(654)
        assert_error(754747455)


def for_each_ability_score_value(fn: Callable[[int], None]):
    """
    Call fn for each ability score value

    :param fn: The fn to call
    """

    for i in range(1, Ability.MAX_SCORE + 1):
        fn(i)
