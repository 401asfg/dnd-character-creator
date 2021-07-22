from main.exceptions.incorrect_character_state_exception import IncorrectCharacterStateException
from main.model.character_components.advancements import Advancements
from main.model.character_components.alignment import Alignment
from main.model.character_components.class_ import Class
from typing import Type
from enum import Enum

from main.model.character_components.race import Race


class Character:
    """
    A 5th edition D&D character, with stats, skills, and info
    """

    class State(Enum):
        """
        The state of the character
        """

        ALIVE = 0
        DOWNED = 1
        DEAD = 2

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

        self._state = self.State.ALIVE

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
        self._failed_death_saves = 0

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

    # TODO: Use property instead of function for death_save?

    def death_save(self, success: bool):
        """
        Make a death save; increments the successful or failed death save counter depending on success; if the success
        counter reaches MAX_SUCCESSFUL_DEATH_SAVES, character's state is changed to ALIVE; if the fail counter reaches
        MAX_FAILED_DEATH_SAVES, character's state is changed to DEAD; if either max is reached, reverts death saves;
        raises IncorrectCharacterState if the character is not downed

        :param success: Whether or not the death save was successful; if true increments the successful death save
        counter; otherwise, increments the failed death save counter
        """

        if self._state != self.State.DOWNED:
            raise IncorrectCharacterStateException("Tried to make a death save while the character was not downed")

        def death_save_of_type(count: int, count_max: int, outcome_state: Character.State) -> int:
            """
            Make either a successful or failed death save

            :param count: The value of a death save counter
            :param count_max: The max value the death save counter, represented by count, should go to; if count_max
            equals count + 1, sets character's state to outcome_state and reverts death saves
            :param outcome_state: The character's state is changed to this if count + 1 equals count_max
            :return: count + 1 or 0 if count equals count_max
            """

            count += 1

            if count == count_max:
                self._state = outcome_state
                self._reset_death_saves()
                return 0

            return count

        if success:
            self._successful_death_saves = death_save_of_type(
                self._successful_death_saves,
                self.MAX_SUCCESSFUL_DEATH_SAVES,
                self.State.ALIVE
            )
        else:
            self._failed_death_saves = death_save_of_type(
                self._failed_death_saves,
                self.MAX_FAILED_DEATH_SAVES,
                self.State.DEAD
            )

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

    def _reset_death_saves(self):
        """
        Resets both death save counts to 0
        """

        self._successful_death_saves = 0
        self._failed_death_saves = 0
