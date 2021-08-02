from main.model.character.inventory.inventory_item import InventoryItem
from main.model.character.inventory.inventory_max_weight_exceeded_exception import InventoryMaxWeightExceededException
from main.model.collection.collection import Collection
from main.model.int_types.natural import Natural


class Inventory(Collection):
    """
    A collection of inventory items
    """

    def __init__(self, max_weight: Natural):
        """
        Initializes the class

        :param max_weight: The maximum combined item weight that the inventory can hold
        """

        super().__init__()
        self._max_weight = max_weight.value
        self._weight = 0

    def add(self, item: InventoryItem):
        """
        Add the given item to the collection; raises ItemInCollectionException if item is already in the collection;
        raises InventoryMaxWeightExceededException if adding the given item would put the inventory's weight over its
        max weight

        :param item: The item to add
        """

        if self.weight + item.weight > self.max_weight:
            raise InventoryMaxWeightExceededException

        super().add(item)

    @property
    def weight(self) -> int:
        """
        :return: The combined weight of all the items in the inventory
        """

        weight = 0

        for item in self._collection:
            weight += item.weight

        return weight

    @property
    def max_weight(self) -> int:
        return self._max_weight
