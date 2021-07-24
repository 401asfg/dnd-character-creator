from main.model.inttypes.natural import Natural


class NaturalPlus(Natural):
    """
    An integer that is not negative or zero
    """

    def __init__(self, value: int):
        """
        Initializes the fields; raises ValueError if value is less than 1

        :param value: The value of the natural+ number
        """

        if value == 0:
            raise ValueError("A natural+ cannot be equal to 0.")

        super().__init__(value)
