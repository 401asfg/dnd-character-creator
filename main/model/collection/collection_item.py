class CollectionItem:
    """
    An item that can be added to a collection
    """

    def __init__(self, name: str, info: str = None):
        """
        Initializes the class

        :param name: The item's name
        :param info: The item's info
        """

        self._name = name
        self._description = info

    @property
    def name(self) -> str:
        return self._name

    @property
    def info(self) -> str:
        return self._description
