class Purse:
    """
    The purse of a character
    """

    def __init__(self):
        """
        Initializes the class; purse doesn't contain any coins
        """

        self.copper_coins = 0
        self.silver_coins = 0
        self.electrum_coins = 0
        self.gold_coins = 0
        self.platinum_coins = 0

    @property
    def copper_coins(self) -> int:
        return self._copper_coins

    @copper_coins.setter
    def copper_coins(self, num: int):
        """
        Set the number of copper coins to num; if num < 0, copper coins is set to 0

        :param num: The number of copper coins
        """

        if num < 0:
            self._copper_coins = 0
        else:
            self._copper_coins = num

    @property
    def silver_coins(self) -> int:
        return self._silver_coins

    @silver_coins.setter
    def silver_coins(self, num: int):
        """
        Set the number of silver coins to num; if num < 0, silver coins is set to 0

        :param num: The number of silver coins
        """

        if num < 0:
            self._silver_coins = 0
        else:
            self._silver_coins = num

    @property
    def electrum_coins(self) -> int:
        return self._electrum_coins

    @electrum_coins.setter
    def electrum_coins(self, num: int):
        """
        Set the number of electrum coins to num; if num < 0, electrum coins is set to 0

        :param num: The number of electrum coins
        """

        if num < 0:
            self._electrum_coins = 0
        else:
            self._electrum_coins = num

    @property
    def gold_coins(self) -> int:
        return self._gold_coins

    @gold_coins.setter
    def gold_coins(self, num: int):
        """
        Set the number of gold coins to num; if num < 0, gold coins is set to 0

        :param num: The number of gold coins
        """

        if num < 0:
            self._gold_coins = 0
        else:
            self._gold_coins = num

    @property
    def platinum_coins(self) -> int:
        return self._platinum_coins

    @platinum_coins.setter
    def platinum_coins(self, num: int):
        """
        Set the number of platinum coins to num; if num < 0, platinum coins is set to 0

        :param num: The number of platinum coins
        """

        if num < 0:
            self._platinum_coins = 0
        else:
            self._platinum_coins = num
