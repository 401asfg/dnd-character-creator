class CollectionItem:
    """
    An item that can be added to a collection
    """

    def __init__(self, name: str, description: str = None):
        """
        Initializes the class

        :param name: The item's name
        :param description: The item's description
        """

        self._name = name
        self._description = description

    @property
    def name(self) -> str:
        return self._name

    @property
    def description(self) -> str:
        return self._description
