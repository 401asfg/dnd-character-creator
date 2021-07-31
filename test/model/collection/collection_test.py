import unittest

from main.model.collection.collection import Collection
from main.model.collection.collection_item import CollectionItem
from main.model.collection.exceptions.item_in_collection_exception import ItemInCollectionException
from main.model.collection.exceptions.item_not_in_collection_excpetion import ItemNotInCollectionException


class CollectionTest(unittest.TestCase):
    def setUp(self):
        self.collection = Collection()
        self.itemA = CollectionItem("Item A")
        self.itemB = CollectionItem("Item B")
        self.itemC = CollectionItem("Item C")

    def test_init(self):
        self.assertEqual(0, len(self.collection))
        self.assertFalse(self.itemA in self.collection)
        self.assertFalse(self.itemB in self.collection)
        self.assertFalse(self.itemC in self.collection)

    def test_add(self):
        def assert_add_error(item: CollectionItem):
            """
            Asserts that attempting to add the given item to the collection results in an exception

            :param item: An item that's in the collection
            """

            try:
                self.collection.add(item)
                self.fail("The item should have been in the collection")
            except ItemInCollectionException:
                pass

        self.collection.add(self.itemB)
        self.assertEqual(1, len(self.collection))
        self.assertFalse(self.itemA in self.collection)
        self.assertTrue(self.itemB in self.collection)
        self.assertFalse(self.itemC in self.collection)
        assert_add_error(self.itemB)

        self.collection.add(self.itemA)
        self.assertEqual(2, len(self.collection))
        self.assertTrue(self.itemA in self.collection)
        self.assertTrue(self.itemB in self.collection)
        self.assertFalse(self.itemC in self.collection)
        assert_add_error(self.itemB)
        assert_add_error(self.itemA)

        self.collection.add(self.itemC)
        self.assertEqual(3, len(self.collection))
        self.assertTrue(self.itemA in self.collection)
        self.assertTrue(self.itemB in self.collection)
        self.assertTrue(self.itemC in self.collection)
        assert_add_error(self.itemB)
        assert_add_error(self.itemA)
        assert_add_error(self.itemC)

    def test_get(self):
        def assert_get_error(index: int):
            """
            Asserts that attempting to get an item with the given index from the collection results in an exception

            :param index: An index that is outside the collection's bounds
            """

            try:
                self.collection.get(index)
                self.fail("The index should not have corresponded to an item")
            except IndexError:
                pass

        self.collection.add(self.itemC)
        self.assertEqual(self.itemC, self.collection.get(0))
        assert_get_error(-4)
        assert_get_error(-3)
        assert_get_error(-2)
        assert_get_error(-1)
        assert_get_error(1)
        assert_get_error(2)
        assert_get_error(3)
        assert_get_error(4)

        self.collection.add(self.itemA)
        self.assertEqual(self.itemA, self.collection.get(1))
        self.assertEqual(self.itemC, self.collection.get(0))
        assert_get_error(-4)
        assert_get_error(-3)
        assert_get_error(-2)
        assert_get_error(-1)
        assert_get_error(2)
        assert_get_error(3)
        assert_get_error(4)

        self.collection.add(self.itemB)
        self.assertEqual(self.itemA, self.collection.get(1))
        self.assertEqual(self.itemB, self.collection.get(2))
        self.assertEqual(self.itemC, self.collection.get(0))
        assert_get_error(-4)
        assert_get_error(-3)
        assert_get_error(-2)
        assert_get_error(-1)
        assert_get_error(3)
        assert_get_error(4)

    def test_iteration(self):
        for item in self.collection:
            self.fail("The iterator should not have run since collection has no items.")

        self.collection.add(self.itemA)

        item_list = [
            self.itemA,
            self.itemC,
            self.itemB
        ]

        for i in range(len(self.collection)):
            self.assertEqual(item_list[i], self.collection.get(i))

        self.collection.add(self.itemC)

        for i in range(len(self.collection)):
            self.assertEqual(item_list[i], self.collection.get(i))

        self.collection.add(self.itemB)

        for i in range(len(self.collection)):
            self.assertEqual(item_list[i], self.collection.get(i))

        for i in range(len(self.collection)):
            self.assertEqual(item_list[i], self.collection.get(i))

    def test_remove(self):
        def assert_remove_error(item: CollectionItem):
            """
            Asserts that attempting to remove the given item from the collection results in an exception

            :param item: An item that's not in the collection
            """

            try:
                self.collection.remove(item)
                self.fail("The item should not have been in the collection")
            except ItemNotInCollectionException:
                pass

        self.collection.add(self.itemC)
        self.assertEqual(1, len(self.collection))
        self.assertFalse(self.itemA in self.collection)
        self.assertFalse(self.itemB in self.collection)
        self.assertTrue(self.itemC in self.collection)
        self.assertEqual(self.itemC, self.collection.get(0))
        assert_remove_error(self.itemA)
        assert_remove_error(self.itemB)

        self.collection.remove(self.itemC)
        self.assertEqual(0, len(self.collection))
        self.assertFalse(self.itemA in self.collection)
        self.assertFalse(self.itemB in self.collection)
        self.assertFalse(self.itemC in self.collection)
        assert_remove_error(self.itemA)
        assert_remove_error(self.itemB)
        assert_remove_error(self.itemC)

        self.collection.add(self.itemA)
        self.assertEqual(1, len(self.collection))
        self.assertTrue(self.itemA in self.collection)
        self.assertFalse(self.itemB in self.collection)
        self.assertFalse(self.itemC in self.collection)
        self.assertEqual(self.itemA, self.collection.get(0))
        assert_remove_error(self.itemB)
        assert_remove_error(self.itemC)

        self.collection.add(self.itemC)
        self.assertEqual(2, len(self.collection))
        self.assertTrue(self.itemA in self.collection)
        self.assertFalse(self.itemB in self.collection)
        self.assertTrue(self.itemC in self.collection)
        self.assertEqual(self.itemA, self.collection.get(0))
        self.assertEqual(self.itemC, self.collection.get(1))
        assert_remove_error(self.itemB)

        self.collection.remove(self.itemC)
        self.assertEqual(1, len(self.collection))
        self.assertTrue(self.itemA in self.collection)
        self.assertFalse(self.itemB in self.collection)
        self.assertFalse(self.itemC in self.collection)
        self.assertEqual(self.itemA, self.collection.get(0))
        assert_remove_error(self.itemB)
        assert_remove_error(self.itemC)

        self.collection.add(self.itemB)
        self.assertEqual(2, len(self.collection))
        self.assertTrue(self.itemA in self.collection)
        self.assertTrue(self.itemB in self.collection)
        self.assertFalse(self.itemC in self.collection)
        self.assertEqual(self.itemA, self.collection.get(0))
        self.assertEqual(self.itemB, self.collection.get(1))
        assert_remove_error(self.itemC)

        self.collection.add(self.itemC)
        self.assertEqual(3, len(self.collection))
        self.assertTrue(self.itemA in self.collection)
        self.assertTrue(self.itemB in self.collection)
        self.assertTrue(self.itemC in self.collection)
        self.assertEqual(self.itemA, self.collection.get(0))
        self.assertEqual(self.itemB, self.collection.get(1))
        self.assertEqual(self.itemC, self.collection.get(2))

        self.collection.remove(self.itemB)
        self.assertEqual(2, len(self.collection))
        self.assertTrue(self.itemA in self.collection)
        self.assertFalse(self.itemB in self.collection)
        self.assertTrue(self.itemC in self.collection)
        self.assertEqual(self.itemA, self.collection.get(0))
        self.assertEqual(self.itemC, self.collection.get(1))
        assert_remove_error(self.itemB)

        self.collection.remove(self.itemC)
        self.assertEqual(1, len(self.collection))
        self.assertTrue(self.itemA in self.collection)
        self.assertFalse(self.itemB in self.collection)
        self.assertFalse(self.itemC in self.collection)
        self.assertEqual(self.itemA, self.collection.get(0))
        assert_remove_error(self.itemB)
        assert_remove_error(self.itemC)

        self.collection.remove(self.itemA)
        self.assertEqual(0, len(self.collection))
        self.assertFalse(self.itemA in self.collection)
        self.assertFalse(self.itemB in self.collection)
        self.assertFalse(self.itemC in self.collection)
        assert_remove_error(self.itemA)
        assert_remove_error(self.itemB)
        assert_remove_error(self.itemC)
