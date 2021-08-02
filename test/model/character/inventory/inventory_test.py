import unittest

from main.model.character.inventory.inventory import Inventory
from main.model.character.inventory.inventory_item import InventoryItem
from main.model.character.inventory.inventory_max_weight_exceeded_exception import InventoryMaxWeightExceededException
from main.model.collection.exceptions.item_in_collection_exception import ItemInCollectionException
from main.model.collection.exceptions.item_not_in_collection_excpetion import ItemNotInCollectionException
from main.model.int_types.natural import Natural


class InventoryTest(unittest.TestCase):
    def setUp(self):
        self.inventory = Inventory(Natural(15))
        self.inventory_b = Inventory(Natural(44))

        self.item_a = InventoryItem(Natural(8), "A")
        self.item_b = InventoryItem(Natural(2), "B")
        self.item_c = InventoryItem(Natural(5), "C")
        self.item_d = InventoryItem(Natural(7), "D")

    def test_init(self):
        self.assertEqual(0, self.inventory.weight)
        self.assertEqual(15, self.inventory.max_weight)

        self.assertEqual(0, self.inventory_b.weight)
        self.assertEqual(44, self.inventory_b.max_weight)

    def test_add(self):

        self.inventory.add(self.item_a)
        self.assertEqual(8, self.inventory.weight)
        self.assertEqual(1, len(self.inventory))
        self.assertTrue(self.item_a in self.inventory)
        self.assertFalse(self.item_b in self.inventory)
        self.assertFalse(self.item_c in self.inventory)
        self.assertFalse(self.item_d in self.inventory)

        self.inventory.add(self.item_b)
        self.assertEqual(10, self.inventory.weight)
        self.assertEqual(2, len(self.inventory))
        self.assertTrue(self.item_a in self.inventory)
        self.assertTrue(self.item_b in self.inventory)
        self.assertFalse(self.item_c in self.inventory)
        self.assertFalse(self.item_d in self.inventory)

        self.inventory.add(self.item_c)
        self.assertEqual(15, self.inventory.weight)
        self.assertEqual(3, len(self.inventory))
        self.assertTrue(self.item_a in self.inventory)
        self.assertTrue(self.item_b in self.inventory)
        self.assertTrue(self.item_c in self.inventory)
        self.assertFalse(self.item_d in self.inventory)

        try:
            self.inventory.add(self.item_d)
            self.fail("Shouldn't have been able to add itemD, should exceed weight capacity.")
        except InventoryMaxWeightExceededException:
            pass

        self.assertEqual(15, self.inventory.weight)
        self.assertEqual(3, len(self.inventory))
        self.assertTrue(self.item_a in self.inventory)
        self.assertTrue(self.item_b in self.inventory)
        self.assertTrue(self.item_c in self.inventory)
        self.assertFalse(self.item_d in self.inventory)

        self.inventory_b.add(self.item_d)
        self.assertEqual(7, self.inventory_b.weight)

        self.inventory_b.add(self.item_c)
        self.assertEqual(12, self.inventory_b.weight)

        try:
            self.inventory_b.add(InventoryItem(Natural(37), "Temp Item"))
            self.fail("Shouldn't have been able to add itemA, should exceed weight capacity.")
        except InventoryMaxWeightExceededException:
            pass

        self.assertEqual(12, self.inventory_b.weight)

        inventory_c = Inventory(Natural(17))
        inventory_c.add(self.item_a)

        try:
            inventory_c.add(self.item_a)
            self.fail("Shouldn't have been able to add itemA, it should already be in the inventory.")
        except ItemInCollectionException:
            pass

    def test_get(self):
        def assert_get_error(index: int):
            """
            Asserts that calling get with the given index results in an error

            :param index: An index that will cause get to raise an error
            """

            try:
                self.inventory.get(index)
                self.fail("Calling get with the given index should have resulted in an error")
            except IndexError:
                pass

        self.inventory.add(self.item_a)
        self.assertEqual(self.item_a, self.inventory.get(0))

        assert_get_error(-23)
        assert_get_error(-5)
        assert_get_error(-2)
        assert_get_error(-1)
        assert_get_error(1)
        assert_get_error(2)
        assert_get_error(3)
        assert_get_error(4)
        assert_get_error(5)

        self.inventory.add(self.item_b)
        self.assertEqual(self.item_a, self.inventory.get(0))
        self.assertEqual(self.item_b, self.inventory.get(1))

        assert_get_error(-23)
        assert_get_error(-5)
        assert_get_error(-2)
        assert_get_error(-1)
        assert_get_error(2)
        assert_get_error(3)
        assert_get_error(4)
        assert_get_error(5)

        self.inventory.remove(self.item_a)
        self.assertEqual(self.item_b, self.inventory.get(0))

        assert_get_error(-23)
        assert_get_error(-5)
        assert_get_error(-2)
        assert_get_error(-1)
        assert_get_error(1)
        assert_get_error(2)
        assert_get_error(3)
        assert_get_error(4)
        assert_get_error(5)

        self.inventory.add(self.item_a)
        self.inventory.add(self.item_c)
        self.assertEqual(self.item_b, self.inventory.get(0))
        self.assertEqual(self.item_a, self.inventory.get(1))
        self.assertEqual(self.item_c, self.inventory.get(2))

        assert_get_error(-23)
        assert_get_error(-5)
        assert_get_error(-2)
        assert_get_error(-1)
        assert_get_error(3)
        assert_get_error(4)
        assert_get_error(5)

    def test_remove(self):
        self.inventory.add(self.item_a)
        self.assertEqual(8, self.inventory.weight)
        self.assertEqual(1, len(self.inventory))
        self.assertTrue(self.item_a in self.inventory)
        self.assertFalse(self.item_b in self.inventory)
        self.assertFalse(self.item_d in self.inventory)

        self.inventory.remove(self.item_a)
        self.assertEqual(0, self.inventory.weight)
        self.assertEqual(0, len(self.inventory))
        self.assertFalse(self.item_a in self.inventory)
        self.assertFalse(self.item_b in self.inventory)
        self.assertFalse(self.item_d in self.inventory)

        self.inventory.add(self.item_a)
        self.inventory.add(self.item_b)
        self.assertEqual(10, self.inventory.weight)
        self.assertEqual(2, len(self.inventory))
        self.assertTrue(self.item_a in self.inventory)
        self.assertTrue(self.item_b in self.inventory)
        self.assertFalse(self.item_d in self.inventory)

        self.inventory.remove(self.item_a)
        self.assertEqual(2, self.inventory.weight)
        self.assertEqual(1, len(self.inventory))
        self.assertFalse(self.item_a in self.inventory)
        self.assertTrue(self.item_b in self.inventory)
        self.assertFalse(self.item_d in self.inventory)

        self.inventory.add(self.item_d)
        self.assertEqual(9, self.inventory.weight)
        self.assertEqual(2, len(self.inventory))
        self.assertFalse(self.item_a in self.inventory)
        self.assertTrue(self.item_b in self.inventory)
        self.assertTrue(self.item_d in self.inventory)

        try:
            self.inventory.remove(self.item_a)
            self.fail("Item A shouldn't have been in the inventory.")
        except ItemNotInCollectionException:
            pass
