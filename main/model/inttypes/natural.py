class Natural:
    """
    An integer that is not negative
    """

    def __init__(self, value: int):
        """
        Initializes the fields; raises ValueError if value is less than 0

        :param value: The value of the natural number
        """

        if value < 0:
            raise ValueError("A natural cannot be less than 0.")

        self._value = value

    @property
    def value(self) -> int:
        return self._value
