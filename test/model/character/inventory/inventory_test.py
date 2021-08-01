import unittest

from main.model.character.inventory.inventory import Inventory
from main.model.character.inventory.inventory_item import InventoryItem
from main.model.character.inventory.inventory_max_weight_exceeded_exception import InventoryMaxWeightExceededException
from main.model.collection.exceptions.item_in_collection_exception import ItemInCollectionException
from main.model.int_types.natural import Natural


class InventoryTest(unittest.TestCase):
    def setUp(self):
        self.inventory = Inventory(Natural(15))
        self.inventory_b = Inventory(Natural(44))

    def test_init(self):
        self.assertEqual(0, self.inventory.weight)
        self.assertEqual(15, self.inventory.max_weight)

        self.assertEqual(0, self.inventory_b.weight)
        self.assertEqual(44, self.inventory_b.max_weight)

    def test_add(self):
        item_a = InventoryItem(Natural(8), "A")
        item_b = InventoryItem(Natural(2), "B")
        item_c = InventoryItem(Natural(5), "C")
        item_d = InventoryItem(Natural(7), "D")

        self.inventory.add(item_a)
        self.assertEqual(8, self.inventory.weight)
        self.assertEqual(1, len(self.inventory))
        self.assertTrue(item_a in self.inventory)
        self.assertFalse(item_b in self.inventory)
        self.assertFalse(item_c in self.inventory)
        self.assertFalse(item_d in self.inventory)

        self.inventory.add(item_b)
        self.assertEqual(10, self.inventory.weight)
        self.assertEqual(2, len(self.inventory))
        self.assertTrue(item_a in self.inventory)
        self.assertTrue(item_b in self.inventory)
        self.assertFalse(item_c in self.inventory)
        self.assertFalse(item_d in self.inventory)

        self.inventory.add(item_c)
        self.assertEqual(15, self.inventory.weight)
        self.assertEqual(3, len(self.inventory))
        self.assertTrue(item_a in self.inventory)
        self.assertTrue(item_b in self.inventory)
        self.assertTrue(item_c in self.inventory)
        self.assertFalse(item_d in self.inventory)

        try:
            self.inventory.add(item_d)
            self.fail("Shouldn't have been able to add itemD, should exceed weight capacity.")
        except InventoryMaxWeightExceededException:
            pass

        self.assertEqual(15, self.inventory.weight)
        self.assertEqual(3, len(self.inventory))
        self.assertTrue(item_a in self.inventory)
        self.assertTrue(item_b in self.inventory)
        self.assertTrue(item_c in self.inventory)
        self.assertFalse(item_d in self.inventory)

        self.inventory_b.add(item_d)
        self.assertEqual(7, self.inventory_b.weight)

        self.inventory_b.add(item_c)
        self.assertEqual(12, self.inventory_b.weight)

        try:
            self.inventory_b.add(InventoryItem(Natural(37), "Temp Item"))
            self.fail("Shouldn't have been able to add itemA, should exceed weight capacity.")
        except InventoryMaxWeightExceededException:
            pass

        self.assertEqual(12, self.inventory_b.weight)

        inventory_c = Inventory(Natural(17))
        inventory_c.add(item_a)

        try:
            inventory_c.add(item_a)
            self.fail("Shouldn't have been able to add itemA, it should already be in the inventory.")
        except ItemInCollectionException:
            pass
