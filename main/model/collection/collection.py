from main.model.collection.collection_item import CollectionItem
from main.model.collection.exceptions.item_in_collection_exception import ItemInCollectionException
from main.model.collection.exceptions.item_not_in_collection_excpetion import ItemNotInCollectionException


class Collection:
    """
    A collection of collection items
    """

    def __init__(self):
        """
        Initializes the class
        """

        self._collection = []
        self._index = 0

    def __iter__(self):
        """
        Implement iter(self).
        """

        return self

    def __next__(self):
        """
        Return len(self).
        """

        if self._index < len(self._collection):
            item = self._collection[self._index]
            self._index += 1
            return item
        raise StopIteration

    def __len__(self):
        """
        Return len(self).
        """

        return len(self._collection)

    def __contains__(self, item):
        """
        Return key in self.
        """

        return item in self._collection

    def add(self, item: CollectionItem):
        """
        Add the given item to the collection; raises ItemInCollectionException if item is already in the collection

        :param item: The item to add
        """

        if item in self._collection:
            raise ItemInCollectionException(
                "Cannot add an item to a collection that already contains that item"
            )

        self._collection.append(item)

    def remove(self, item: CollectionItem):
        """
        Remove the given item from the collection; raises ItemNotInCollectionException if item is not in the collection

        :param item: The item to remove
        """

        if item not in self._collection:
            raise ItemNotInCollectionException(
                "Cannot remove an item from a collection if the item is not in the collection."
            )

        for i in range(len(self._collection)):
            if item == self._collection[i]:
                self._collection.pop(i)
                return

    def get(self, index: int) -> CollectionItem:
        """
        Get the item at the given index; raises IndexError if the given index does not correspond to any item within the
        collection

        :param index: The collection index of the item to get
        :return: The item at the given index
        """

        if index < 0 or index >= len(self._collection):
            raise IndexError("The given index does not correspond to any item within the collection.")

        return self._collection[index]
