import unittest

from main.model.character.inventory.inventory_item import InventoryItem
from main.model.int_types.natural import Natural


class InventoryItemTest(unittest.TestCase):
    def test_init(self):
        item_a = InventoryItem(Natural(5), "A", "Item A's description.")
        self.assertEqual(5, item_a.weight)
        self.assertEqual("A", item_a.name)
        self.assertEqual("Item A's description.", item_a.info)

        item_b = InventoryItem(Natural(38), "Item B", "B's description.")
        self.assertEqual(38, item_b.weight)
        self.assertEqual("Item B", item_b.name)
        self.assertEqual("B's description.", item_b.info)
