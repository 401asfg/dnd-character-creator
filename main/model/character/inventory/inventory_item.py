from main.model.collection.collection_item import CollectionItem
from main.model.int_types.natural import Natural


class InventoryItem(CollectionItem):
    """
    An item that can be added to an inventory
    """

    def __init__(self, weight: Natural, name: str, info: str = None):
        """
        Initializes the class

        :param weight: The item's weight
        :param name: The item's name
        :param info: The item's info
        """

        self._weight = weight.value
        super().__init__(name, info)

    @property
    def weight(self) -> int:
        return self._weight
