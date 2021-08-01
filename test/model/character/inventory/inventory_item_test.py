import unittest

from main.model.character.inventory.inventory_item import InventoryItem
from main.model.int_types.natural import Natural


class InventoryItemTest(unittest.TestCase):
    def test_init(self):
        itemA = InventoryItem(Natural(5), "A", "Item A's description.")
        self.assertEqual(5, itemA.weight)
        self.assertEqual("A", itemA.name)
        self.assertEqual("Item A's description.", itemA.info)

        itemB = InventoryItem(Natural(38), "Item B", "B's description.")
        self.assertEqual(38, itemB.weight)
        self.assertEqual("Item B", itemB.name)
        self.assertEqual("B's description.", itemB.info)
