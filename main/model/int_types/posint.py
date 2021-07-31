from main.model.int_types.natural import Natural


class Posint(Natural):
    """
    A positive integer (cannot be zero or negative)
    """

    def __init__(self, value: int):
        """
        Initializes the fields; raises ValueError if value is less than 1

        :param value: The value of the positive integer
        """

        if value == 0:
            raise ValueError("A posint cannot be less than 1.")

        super().__init__(value)
