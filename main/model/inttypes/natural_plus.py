class NaturalPlus:
    """
    An integer that is not negative or zero
    """

    def __init__(self, value: int):
        """
        Initializes the fields; raises ValueError if value is less than 1

        :param value: The value of the natural+ number
        """

        if value < 1:
            raise ValueError("A natural+ cannot be equal to 0.")

        self._value = value

    @property
    def value(self) -> int:
        return self._value
