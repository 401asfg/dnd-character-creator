import unittest

from main.model.character.level import Level
from main.model.int_types.posint import Posint


class LevelTest(unittest.TestCase):
    def test_init(self):
        for i in range(1, Level.MAX_LEVEL + 1):
            self.assertEqual(i, Level(Posint(i)).value)

        def assert_error(value: int):
            """
            Asserts that giving level the value produces an error

            :param value: The value to give to the level's constructor
            """

            try:
                Level(Posint(value))
                self.fail("The value should have produced an error when given to level.")
            except ValueError:
                pass

        for i in range(Level.MAX_LEVEL + 1, 400):
            assert_error(i)
