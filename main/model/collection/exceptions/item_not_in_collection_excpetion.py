class ItemNotInCollectionException(Exception):
    """
    Exception raised when a collection makes a request of an item that it does not contain
    """