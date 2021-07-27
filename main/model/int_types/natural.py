from main.model.int_types.posint import Posint


class Natural(Posint):
    """
    An integer that is not negative
    """

    def __init__(self, value: int):
        """
        Initializes the fields; raises ValueError if value is less than 0

        :param value: The value of the natural number
        """

        self._min_value = 0
        super().__init__(value)
