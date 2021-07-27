class AbilityScore:
    """
    An unmodified score to give to one of the character's main stats (STR, DEX, CON, INT, WIS, CHA)
    """

    MIN_SCORE = 3
    MAX_SCORE = 18

    def __init__(self, value: int):
        """
        Initializes the class; if value is less than MIN_SCORE or is greater than MAX_SCORE, raises ValueError

        :param value: The value of the ability score
        """

        if value < self.MIN_SCORE or value > self.MAX_SCORE:
            raise ValueError("An unmodified ability score cannot have the value " + str(value) + ".")

        self._value = value

    @property
    def value(self) -> int:
        return self._value
