class IncorrectCharacterStateException(Exception):
    """
    Exception raised when an action is taken upon or by a character who is not in the correct state for that action to
    be taken on or by them
    """