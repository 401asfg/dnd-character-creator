import unittest

from main.model.character.purse import Purse
from main.model.int_types.natural import Natural


class PurseTest(unittest.TestCase):
    def setUp(self):
        self.purse = Purse()

    def test_init(self):
        self.assertEqual(0, self.purse.copper_coins)
        self.assertEqual(0, self.purse.silver_coins)
        self.assertEqual(0, self.purse.electrum_coins)
        self.assertEqual(0, self.purse.gold_coins)
        self.assertEqual(0, self.purse.platinum_coins)

    def test_copper_coins_setter(self):
        self.purse.copper_coins = 45
        self.assertEqual(45, self.purse.copper_coins)
        self.purse.copper_coins += 11
        self.assertEqual(56, self.purse.copper_coins)
        self.purse.copper_coins -= 40
        self.assertEqual(16, self.purse.copper_coins)
        self.purse.copper_coins = 0
        self.assertEqual(0, self.purse.copper_coins)
        self.purse.copper_coins += 71
        self.assertEqual(71, self.purse.copper_coins)
        self.purse.copper_coins -= 100
        self.assertEqual(0, self.purse.copper_coins)
        self.purse.copper_coins = 34
        self.assertEqual(34, self.purse.copper_coins)
        self.purse.copper_coins = -11
        self.assertEqual(0, self.purse.copper_coins)

    def test_silver_coins_setter(self):
        self.purse.silver_coins = 23
        self.assertEqual(23, self.purse.silver_coins)
        self.purse.silver_coins += 4
        self.assertEqual(27, self.purse.silver_coins)
        self.purse.silver_coins -= 8
        self.assertEqual(19, self.purse.silver_coins)
        self.purse.silver_coins = 0
        self.assertEqual(0, self.purse.silver_coins)
        self.purse.silver_coins += 6
        self.assertEqual(6, self.purse.silver_coins)
        self.purse.silver_coins -= 100
        self.assertEqual(0, self.purse.silver_coins)
        self.purse.silver_coins = 1
        self.assertEqual(1, self.purse.silver_coins)
        self.purse.silver_coins = -11
        self.assertEqual(0, self.purse.silver_coins)

    def test_electrum_coins_setter(self):
        self.purse.electrum_coins = 7
        self.assertEqual(7, self.purse.electrum_coins)
        self.purse.electrum_coins += 22
        self.assertEqual(29, self.purse.electrum_coins)
        self.purse.electrum_coins -= 11
        self.assertEqual(18, self.purse.electrum_coins)
        self.purse.electrum_coins = 0
        self.assertEqual(0, self.purse.electrum_coins)
        self.purse.electrum_coins += 165
        self.assertEqual(165, self.purse.electrum_coins)
        self.purse.electrum_coins -= 200
        self.assertEqual(0, self.purse.electrum_coins)
        self.purse.electrum_coins = 2
        self.assertEqual(2, self.purse.electrum_coins)
        self.purse.electrum_coins = -19
        self.assertEqual(0, self.purse.electrum_coins)

    def test_gold_coins_setter(self):
        self.purse.gold_coins = 1
        self.assertEqual(1, self.purse.gold_coins)
        self.purse.gold_coins += 3
        self.assertEqual(4, self.purse.gold_coins)
        self.purse.gold_coins -= 2
        self.assertEqual(2, self.purse.gold_coins)
        self.purse.gold_coins = 0
        self.assertEqual(0, self.purse.gold_coins)
        self.purse.gold_coins += 8
        self.assertEqual(8, self.purse.gold_coins)
        self.purse.gold_coins -= 20
        self.assertEqual(0, self.purse.gold_coins)
        self.purse.gold_coins = 3
        self.assertEqual(3, self.purse.gold_coins)
        self.purse.gold_coins = -7
        self.assertEqual(0, self.purse.gold_coins)

    def test_platinum_coins_setter(self):
        self.purse.platinum_coins = 0
        self.assertEqual(0, self.purse.platinum_coins)
        self.purse.platinum_coins += 28
        self.assertEqual(28, self.purse.platinum_coins)
        self.purse.platinum_coins -= 7
        self.assertEqual(21, self.purse.platinum_coins)
        self.purse.platinum_coins = 0
        self.assertEqual(0, self.purse.platinum_coins)
        self.purse.platinum_coins += 88
        self.assertEqual(88, self.purse.platinum_coins)
        self.purse.platinum_coins -= 15
        self.assertEqual(73, self.purse.platinum_coins)
        self.purse.platinum_coins = 66
        self.assertEqual(66, self.purse.platinum_coins)
        self.purse.platinum_coins = -7
        self.assertEqual(0, self.purse.platinum_coins)
