from main.model.int_types.posint import Posint


class Level:
    """
    The level that a character can have
    """

    MAX_LEVEL = 20

    def __init__(self, value: Posint):
        """
        Initializes the class; raises ValueError if value is greater than MAX_LEVEL

        :param value: The value of the level
        """

        if value.value > self.MAX_LEVEL:
            raise ValueError("A level cannot be greater than " + str(self.MAX_LEVEL) + ".")

        self._value = value.value

    @property
    def value(self) -> int:
        return self._value
