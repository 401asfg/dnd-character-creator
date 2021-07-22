from main.model.character_components.advancements import Advancements
from main.model.character_components.alignment import Alignment
from main.model.character_components.class_ import Class
from typing import Type

from main.model.character_components.race import Race


class Character:
    """
    A 5th edition D&D character, with stats, skills, and info
    """

    MAX_SUCCESSFUL_DEATH_SAVES = 3
    MAX_FAILED_DEATH_SAVES = 3

    # TODO: add rest of parameters
    # TODO: add rest of functions
    # TODO: add exceptions to ctor (note all exceptions)

    def __init__(
            self,
            name: str,
            player_name: str,
            class_: Type[Class],
            race: Type[Race],
            level: int,
            background: str,
            alignment: Alignment
    ):
        """
        Builds the character in its initial state; raises ValueError if the given level is unreachable

        :param name: Name of the character
        :param player_name: Name of the player playing the character
        :param class_: The character's class
        :param race: The character's race
        :param level: Character's starting level
        :param background: Background of the character
        :param alignment: Alignment of the character
        """

        # TODO: set new variables based on the character class and character race's static methods

        self.name = name
        self._player_name = player_name

        # TODO: add class variables
        # TODO: add race variables

        self._background = background
        self._alignment = alignment

        if Advancements.reachable_level(level):
            self._level = level
        else:
            raise ValueError("The given level is not reachable by a character")

        self._successful_death_saves = 0
        self.failed_death_saves = 0

        self._exp = Advancements.get_experience_points(self._level)
        self._proficiency_bonus = Advancements.get_proficiency_bonus(self._exp)

    def gain_exp(self, points: int):
        """
        Give the character experience points; adjust the character's level and proficiency bonus to those which
        correspond with the new exp amount, as defined in the CharacterAdvancements class

        :param points: The amount of experience points to give the character
        """

        self._exp += points
        self._level = Advancements.get_level(self._exp)
        self._proficiency_bonus = Advancements.get_proficiency_bonus(self._exp)

    def pass_death_save(self):
        """
        Succeed in a death save; increment successful death saves; if successful death saves is equal to the maximum
        successful death saves, the character is revived
        """

        self._successful_death_saves += 1

        if self._successful_death_saves >= self.MAX_SUCCESSFUL_DEATH_SAVES:
            self._successful_death_saves = 0

        # TODO: add downed and revive mechanics

    def fail_death_save(self):
        """
        Fail in a death save; increment failed death saves; if failed death saves is equal to the maximum failed death
        saves, the character is killed
        """

        self.failed_death_saves += 1

        # TODO: add downed and death mechanics

    @property
    def name(self) -> str:
        return self.name

    @property
    def player_name(self) -> str:
        return self._player_name

    # TODO: Add properties for dictionary derived values

    @property
    def level(self) -> int:
        return self._level

    @property
    def background(self) -> str:
        return self._background

    @property
    def successful_death_saves(self) -> int:
        return self._successful_death_saves

    @property
    def failed_death_saves(self) -> int:
        return self.failed_death_saves

    @property
    def alignment(self) -> Alignment:
        return self._alignment

    @property
    def experience_points(self) -> int:
        return self._exp
