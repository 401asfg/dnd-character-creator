class Personality:
    """
    A personality that a character can have
    """

    def __init__(self, trait_one: str, trait_two: str, ideal: str, bond: str, flaw: str):
        """
        Initializes the class

        :param trait_one: One of the character's personality traits
        :param trait_two: One of the character's personality traits
        :param ideal: The character's ideal
        :param bond: The character's bond
        :param flaw: The character's flaw
        """

        self._trait_one = trait_one
        self._trait_two = trait_two
        self._ideal = ideal
        self._bond = bond
        self._flaw = flaw

    @property
    def trait_one(self) -> str:
        return self._trait_one

    @property
    def trait_two(self) -> str:
        return self._trait_two

    @property
    def ideal(self) -> str:
        return self._ideal

    @property
    def bond(self) -> str:
        return self._bond

    @property
    def flaw(self) -> str:
        return self._flaw
