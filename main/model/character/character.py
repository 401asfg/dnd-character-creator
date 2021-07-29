from main.model.character.advancements import get_level, get_proficiency_bonus, get_min_exp
from main.model.character.enumerators.size import Size
from main.model.character.exceptions.incorrect_character_state_exception import IncorrectCharacterStateException
from typing import Type, Callable, Any

from main.model.character.alignment import Alignment
from main.model.character.level import Level
from main.model.character.race import Race
from main.model.character.class_ import Class
from main.model.character.enumerators.state import State
from main.model.int_types.natural import Natural
from main.model.int_types.posint import Posint
from main.model.character.abilities import Abilities
from main.model.character.skills import Skills


class Character:
    """
    A 5th edition D&D character, with stats, skills, and info
    """

    # TODO: all tests have actual and expected backwards?

    MAX_SUCCESSFUL_DEATH_SAVES = 3
    MAX_FAILED_DEATH_SAVES = 3
    _BASE_PASSIVE_WISDOM = 10

    # TODO: add rest of parameters
    # TODO: add rest of functions
    # TODO: add exceptions to ctor (note all exceptions)

    def __init__(
            self,
            name: str,
            player_name: str,
            class_: Type[Class],
            race: Type[Race],
            level: Level,
            abilities: Type[Abilities],
            skills: Type[Skills],
            background: str,
            alignment: Alignment,
            age: Natural
    ):
        """
        Builds the character in its initial state; raises ValueError if the given level is unreachable or the given
        alignment is inappropriate for a character of the given race

        :param name: The character's name
        :param player_name: Name of the player playing the character
        :param class_: The character's class
        :param race: The character's race
        :param level: The character's starting level
        :param abilities: The character's abilities
        :param skills: The character's skills
        :param background: The character's background
        :param alignment: The character's alignment
        :param age: The character's age
        """

        # TODO: set new variables based on the character class and character race's static methods

        # TODO: modify tests with ability scores

        self._initialize_core_fields(name, player_name, class_, race, level, background, age)
        self._initialize_exception_raising_fields(alignment)
        self._abilities = abilities(self._race, self._class, Posint(self.proficiency_bonus))

        self._skills = skills(
            strength=self.abilities.strength,
            dexterity=self.abilities.dexterity,
            intelligence=self.abilities.intelligence,
            wisdom=self.abilities.wisdom,
            charisma=self.abilities.charisma,
            proficiency_bonus=Posint(self.proficiency_bonus)
        )

        self._initialize_hit_points()

    def gain_exp(self, points: int):
        """
        Give the character experience points

        :param points: The amount of experience points to give the character
        """

        self._exp += points

    def death_save(self, success: bool):
        """
        Make a death save; increments the successful or failed death save counter depending on success; if the success
        counter reaches MAX_SUCCESSFUL_DEATH_SAVES, character's state is changed to ALIVE and the character gains 1
        hit_point; if the fail counter reaches MAX_FAILED_DEATH_SAVES, character's state is changed to DEAD; if either
        max is reached, resets death saves; raises IncorrectCharacterState if the character is not downed

        :param success: Whether or not the death save was successful; if true increments the successful death save
        counter; otherwise, increments the failed death save counter
        """

        if self._state != State.DOWNED:
            raise IncorrectCharacterStateException("Tried to make a death save while the character was not downed")

        def death_save_of_type(count: int, count_max: int, outcome_state: State) -> int:
            """
            Make either a successful or failed death save

            :param count: The value of a death save counter
            :param count_max: The max value the death save counter, represented by count, should go to; if count_max
            equals count + 1, sets character's state to outcome_state and resets death saves
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
                State.ALIVE
            )
        else:
            self._failed_death_saves = death_save_of_type(
                self._failed_death_saves,
                self.MAX_FAILED_DEATH_SAVES,
                State.DEAD
            )

        if self.state == State.ALIVE:
            self.hit_points = 1

    def gain_inspiration(self):
        """
        Increment the character's inspiration by 1
        """

        self._add_inspiration(1)

    def spend_inspiration(self):
        """
        Decrement the character's inspiration by 1; raises ValueError if spending an inspiration point would make
        inspiration negative
        """

        self._add_inspiration(-1)

    @property
    def name(self) -> str:
        return self._name

    @property
    def player_name(self) -> str:
        return self._player_name

    @property
    def class_name(self) -> str:
        return self._class.get_name()

    @property
    def race_name(self) -> str:
        return self._race.get_name()

    @property
    def abilities(self) -> Abilities:
        return self._abilities

    @property
    def skills(self) -> Skills:
        return self._skills

    # TODO: Add properties for dictionary derived values

    @property
    def background(self) -> str:
        return self._background

    @property
    def state(self) -> State:
        return self._state

    @property
    def hit_points(self) -> int:
        """
        Get the character's hit_points

        :return: The character's hit_points
        """

        return self._hit_points

    @hit_points.setter
    def hit_points(self, value: int):
        """
        Set the character's hit_points

        :param value: The amount of hit_points the character has; if value > max_hit_points, hit_points =
        max_hit_points; if value <= 0, hit_points = 0 and the character state is changed to DOWNED; if character state
        is DOWNED or DEAD, raises IncorrectCharacterStateException
        """

        if self._state == State.DOWNED or self._state == State.DEAD:
            raise IncorrectCharacterStateException(
                "Character's hit_points cannot be changed when not in the ALIVE state."
            )

        if value <= 0:
            self._hit_points = 0
            self._state = State.DOWNED
        elif value > self._max_hit_points:
            self._hit_points = self._max_hit_points
        else:
            self._hit_points = value

    @property
    def max_hit_points(self) -> int:
        return self._max_hit_points

    @property
    def successful_death_saves(self) -> int:
        return self._successful_death_saves

    @property
    def failed_death_saves(self) -> int:
        return self._failed_death_saves

    @property
    def alignment(self) -> Alignment:
        return self._alignment

    @property
    def experience_points(self) -> int:
        return self._exp

    @property
    def level(self) -> int:
        """
        :return: The character's level for the given amount of experience points the character has
        """

        return get_level(self._exp)

    @property
    def passive_wisdom(self) -> int:
        """
        :return: The character's passive wisdom
        """

        return self._BASE_PASSIVE_WISDOM + self.skills.perception.modifier

    @property
    def inspiration(self) -> int:
        return self._inspiration.value

    @property
    def proficiency_bonus(self) -> int:
        """
        :return: The character's proficiency bonus for the given level of the character
        """

        return get_proficiency_bonus(self.level)

    @property
    def age(self) -> int:
        return self._age.value

    @property
    def size(self) -> Size:
        """
        :return: The character's size, determined by the character's race
        """

        return self._race.get_size()

    @property
    def speed(self) -> int:
        """
        :return: The character's speed, determined by the character's race
        """

        return self._race.get_speed()

    def _initialize_core_fields(
            self,
            name: str,
            player_name: str,
            class_: Type[Class],
            race: Type[Race],
            level: Level,
            background: str,
            age: Natural
    ):
        """
        Initializes the fields of the character that are not derived from any other values

        :param name: The character's name
        :param player_name: Name of the player playing the character
        :param class_: The character's class
        :param race: The character's race
        :param level: The character's level
        :param background: The character's background
        :param age: The character's age
        """

        self._state = State.ALIVE
        self._reset_death_saves()
        self._inspiration = Natural(0)

        self._name = name
        self._player_name = player_name
        self._class = class_
        self._race = race
        self._exp = get_min_exp(level.value)
        self._background = background
        self._age = age

    def _initialize_exception_raising_fields(self, alignment: Alignment):
        """
        Initializes the fields that may raise exceptions; raises ValueError if the given level is unreachable or the
        given alignment is inappropriate for a character of the given race

        :param alignment: The character's alignment
        """

        def check(x, check_fn: Callable[[Any], bool], error_msg: str):
            """
            Checks x; either returns x's value or raises a ValueError if check_fn(x) returns false

            :param x: The parameter to check
            :param check_fn: The function that checks x; takes x as its only input and returns true or false
            :param error_msg: The message to be included with the ValueError that will be raised should check_fn return
            false
            :return: x
            """

            if check_fn(x):
                return x

            raise ValueError(error_msg)

        def acceptable_racial_alignment(alignment_: Alignment) -> bool:
            """
            :param alignment_: The alignment that is checked to see if it acceptable for a character of this race
            :return: True if alignment is acceptable for a character of this race; otherwise false
            """

            in_natures = alignment_.nature in self._race.get_acceptable_alignment_natures()
            in_moralities = alignment_.morality in self._race.get_acceptable_alignment_moralities()
            return in_natures and in_moralities

        self._alignment = check(
            alignment,
            acceptable_racial_alignment,
            "A character of this race cannot have this alignment."
        )

    def _initialize_hit_points(self):
        """
        Initializes the character's hit points and max hit points
        """

        self._max_hit_points = self._class.get_hit_die().max_possible_score + self.abilities.constitution.modifier
        self.hit_points = self._max_hit_points

    def _add_inspiration(self, inspiration_delta: int):
        """
        Adds inspiration_delta to the inspiration; raises ValueError if inspiration + inspiration_delta < 0

        :param inspiration_delta: The amount to add to the inspiration
        """

        self._inspiration = Natural(self._inspiration.value + inspiration_delta)

    def _reset_death_saves(self):
        """
        Resets both death save counts to 0
        """

        self._successful_death_saves = 0
        self._failed_death_saves = 0
