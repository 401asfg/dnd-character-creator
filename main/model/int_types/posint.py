class Posint:
    """
    A positive integer (cannot be zero or negative)
    """

    _min_value = 1

    def __init__(self, value: int):
        """
        Initializes the fields; raises ValueError if value is less than 1

        :param value: The value of the positive integer
        """

        if value < self._min_value:
            raise ValueError("A " + self.__class__.__name__ + " cannot be less than " + str(self._min_value) + ".")

        self._value = value

    @property
    def value(self) -> int:
        return self._value
