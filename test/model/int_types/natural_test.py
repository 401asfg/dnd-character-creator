import unittest

from main.model.int_types.natural import Natural


class NaturalTest(unittest.TestCase):
    def test_init(self):
        def assert_same_value(x: int):
            """
            Asserts that x and Natural(x).value are equal
            """

            self.assertEqual(Natural(x).value, x)

        assert_same_value(0)
        assert_same_value(1)
        assert_same_value(2)
        assert_same_value(3)
        assert_same_value(32)
        assert_same_value(93)
        assert_same_value(234)
        assert_same_value(2345234)

        def assert_error(x: int):
            """
            Asserts that Natural(x) raises an error
            """

            try:
                Natural(x)
                self.fail("The non-natural value should have caused Natural to raise an error.")
            except ValueError:
                pass

        assert_error(-1)
        assert_error(-2)
        assert_error(-3)
        assert_error(-34)
        assert_error(-3245236)
