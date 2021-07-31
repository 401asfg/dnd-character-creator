import unittest

from main.model.collection.collection_item import CollectionItem


class CollectionItemTest(unittest.TestCase):
    def test_init(self):
        itemA = CollectionItem("Item A", "The description of item A.")
        self.assertEqual("Item A", itemA.name)
        self.assertEqual("The description of item A.", itemA.description)

        itemB = CollectionItem("B", "Does something.")
        self.assertEqual("B", itemB.name)
        self.assertEqual("Does something.", itemB.description)

        itemC = CollectionItem("Item C")
        self.assertEqual("Item C", itemC.name)
        self.assertEqual(None, itemC.description)
