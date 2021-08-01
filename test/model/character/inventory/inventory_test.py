import unittest

from main.model.character.inventory.inventory import Inventory
from main.model.character.inventory.inventory_item import InventoryItem
from main.model.character.inventory.inventory_max_weight_exceeded_exception import InventoryMaxWeightExceededException
from main.model.collection.exceptions.item_in_collection_exception import ItemInCollectionException
from main.model.int_types.natural import Natural


class InventoryTest(unittest.TestCase):
    def setUp(self):
        self.inventory = Inventory(Natural(15))
        self.inventoryB = Inventory(Natural(44))

    def test_init(self):
        self.assertEqual(0, self.inventory.weight)
        self.assertEqual(15, self.inventory.max_weight)

        self.assertEqual(0, self.inventoryB.weight)
        self.assertEqual(44, self.inventoryB.max_weight)

    def test_add(self):
        itemA = InventoryItem(Natural(8), "A")
        itemB = InventoryItem(Natural(2), "B")
        itemC = InventoryItem(Natural(5), "C")
        itemD = InventoryItem(Natural(7), "D")

        self.inventory.add(itemA)
        self.assertEqual(8, self.inventory.weight)
        self.assertEqual(1, len(self.inventory))
        self.assertTrue(itemA in self.inventory)
        self.assertFalse(itemB in self.inventory)
        self.assertFalse(itemC in self.inventory)
        self.assertFalse(itemD in self.inventory)

        self.inventory.add(itemB)
        self.assertEqual(10, self.inventory.weight)
        self.assertEqual(2, len(self.inventory))
        self.assertTrue(itemA in self.inventory)
        self.assertTrue(itemB in self.inventory)
        self.assertFalse(itemC in self.inventory)
        self.assertFalse(itemD in self.inventory)

        self.inventory.add(itemC)
        self.assertEqual(15, self.inventory.weight)
        self.assertEqual(3, len(self.inventory))
        self.assertTrue(itemA in self.inventory)
        self.assertTrue(itemB in self.inventory)
        self.assertTrue(itemC in self.inventory)
        self.assertFalse(itemD in self.inventory)

        try:
            self.inventory.add(itemD)
            self.fail("Shouldn't have been able to add itemD, should exceed weight capacity.")
        except InventoryMaxWeightExceededException:
            pass

        self.assertEqual(15, self.inventory.weight)
        self.assertEqual(3, len(self.inventory))
        self.assertTrue(itemA in self.inventory)
        self.assertTrue(itemB in self.inventory)
        self.assertTrue(itemC in self.inventory)
        self.assertFalse(itemD in self.inventory)

        self.inventoryB.add(itemD)
        self.assertEqual(7, self.inventoryB.weight)

        self.inventoryB.add(itemC)
        self.assertEqual(12, self.inventoryB.weight)

        try:
            self.inventoryB.add(InventoryItem(Natural(37), "Temp Item"))
            self.fail("Shouldn't have been able to add itemA, should exceed weight capacity.")
        except InventoryMaxWeightExceededException:
            pass

        self.assertEqual(12, self.inventoryB.weight)

        inventoryC = Inventory(Natural(17))
        inventoryC.add(itemA)

        try:
            inventoryC.add(itemA)
            self.fail("Shouldn't have been able to add itemA, it should already be in the inventory.")
        except ItemInCollectionException:
            pass
