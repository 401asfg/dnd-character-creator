from main.model.character.ability import Ability
from main.model.character.advancements import get_level, get_proficiency_bonus, get_min_exp, reachable_level
from main.model.character.size import Size
from main.model.exceptions.incorrect_character_state_exception import IncorrectCharacterStateException
from typing import Type, Callable, Any

from main.model.character.alignment import Alignment
from main.model.character.race import Race
from main.model.character.class_ import Class
from main.model.character.state import State
from main.model.inttypes.natural import Natural
from main.model.inttypes.natural_plus import NaturalPlus


class Character:
    """
    A 5th edition D&D character, with stats, skills, and info
    """

    # TODO: all tests have actual and expected backwards?

    MAX_SUCCESSFUL_DEATH_SAVES = 3
    MAX_FAILED_DEATH_SAVES = 3

    # TODO: add rest of parameters
    # TODO: add rest of functions
    # TODO: add exceptions to ctor (note all exceptions)

    class _Abilities:
        """
        The character's abilities
        """

        class _Ability(Ability):
            """
            An ability in the context of it belonging to the character
            """

            def __init__(
                    self,
                    dice_roll_ability: Ability,
                    racial_ability_bonus: NaturalPlus,
                    class_proficient: bool,
                    proficiency_bonus: NaturalPlus
            ):
                """
                Initializes the class; sets the ability score to the dice roll score plus the racial bonus for this
                ability

                :param dice_roll_ability: An ability with its score taken directly from the dice roll
                :param racial_ability_bonus: The racial bonus to add to the ability's score
                :param class_proficient: Whether or not the character's class is proficient in this ability
                :param proficiency_bonus: The character's proficiency bonus
                """

                super().__init__(NaturalPlus(dice_roll_ability.score + racial_ability_bonus.value))
                self._proficiency = class_proficient
                self._proficiency_bonus = proficiency_bonus

            @property
            def saving_throw(self) -> int:
                """
                :return: The saving throw modifier: ability modifier, plus proficiency_bonus if class is proficient in
                this ability
                """

                return self.modifier + self._proficiency * self._proficiency_bonus.value

        def __init__(
                self,
                character: "Character",
                strength: Ability,
                dexterity: Ability,
                constitution: Ability,
                intelligence: Ability,
                wisdom: Ability,
                charisma: Ability
        ):
            """
            Initializes this class

            :param character: The character to whom these abilities belong
            :param strength: The character's strength ability with its score taken directly from the dice roll
            :param dexterity: The character's dexterity ability with its score taken directly from the dice roll
            :param constitution: The character's constitution ability with its score taken directly from the dice roll
            :param intelligence: The character's intelligence ability with its score taken directly from the dice roll
            :param wisdom: The character's wisdom ability with its score taken directly from the dice roll
            :param charisma: The character's charisma ability with its score taken directly from the dice roll
            """

            race = character._race
            class_ = character._class
            pb = NaturalPlus(character.proficiency_bonus)

            self._strength = self._Ability(
                strength,
                NaturalPlus(race.get_strength_bonus()),
                class_.strength_proficiency(),
                pb
            )

            self._dexterity = self._Ability(
                dexterity,
                NaturalPlus(race.get_dexterity_bonus()),
                class_.dexterity_proficiency(),
                pb
            )

            self._constitution = self._Ability(
                constitution,
                NaturalPlus(race.get_constitution_bonus()),
                class_.constitution_proficiency(),
                pb
            )

            self._intelligence = self._Ability(
                intelligence,
                NaturalPlus(race.get_intelligence_bonus()),
                class_.intelligence_proficiency(),
                pb
            )

            self._wisdom = self._Ability(
                wisdom,
                NaturalPlus(race.get_wisdom_bonus()),
                class_.wisdom_proficiency(),
                pb
            )

            self._charisma = self._Ability(
                charisma,
                NaturalPlus(race.get_charisma_bonus()),
                class_.charisma_proficiency(),
                pb
            )

        @property
        def strength(self) -> _Ability:
            return self._strength

        @property
        def dexterity(self) -> _Ability:
            return self._dexterity

        @property
        def constitution(self) -> _Ability:
            return self._constitution

        @property
        def intelligence(self) -> _Ability:
            return self._intelligence

        @property
        def wisdom(self) -> _Ability:
            return self._wisdom

        @property
        def charisma(self) -> _Ability:
            return self._charisma

    # TODO: test skills

    class _Skills:
        """
        The character's skills
        """

        class _Skill:
            """
            One of the character's skills
            """

            def __init__(self, ability: Ability, proficient: bool, proficiency_bonus: NaturalPlus):
                """
                Initializes the class

                :param ability: The ability that this skill is bound to
                :param proficient: Whether or not the character is proficient in this skill
                :param proficiency_bonus: The character's proficiency bonus
                """

                self._ability = ability
                self._proficient = proficient
                self._proficiency_bonus = proficiency_bonus

            @property
            def modifier(self) -> int:
                """
                :return: The skill's modifier: ability modifier, plus proficiency_bonus if character is proficient in
                this skill
                """

                return self._ability.modifier + self._proficient * self._proficiency_bonus.value

            @property
            def proficient(self) -> bool:
                """
                :return: True if character is proficient in this skill; otherwise, false
                """

                return self._proficient

        def __init__(self, character: "Character"):
            """
            Initializes this class

            :param character: The character to whom these skills belong
            """

            strength = character.abilities.strength
            dexterity = character.abilities.dexterity
            constitution = character.abilities.constitution
            intelligence = character.abilities.intelligence
            wisdom = character.abilities.wisdom
            charisma = character.abilities.charisma

            pb = NaturalPlus(character.proficiency_bonus)

            self._acrobatics = self._Skill(dexterity, , pb)
            self._animal_handling = self._Skill(wisdom, , pb)
            self._arcana = self._Skill(intelligence, , pb)
            self._athletics = self._Skill(strength, , pb)
            self._deception = self._Skill(charisma, , pb)
            self._history = self._Skill(intelligence, , pb)
            self._insight = self._Skill(wisdom, , pb)
            self._intimidation = self._Skill(charisma, , pb)
            self._investigation = self._Skill(intelligence, , pb)
            self._medicine = self._Skill(wisdom, , pb)
            self._nature = self._Skill(intelligence, , pb)
            self._perception = self._Skill(wisdom, , pb)
            self._performance = self._Skill(charisma, , pb)
            self._persuasion = self._Skill(charisma, , pb)
            self._religion = self._Skill(intelligence, , pb)
            self._sleight_of_hand = self._Skill(dexterity, , pb)
            self._stealth = self._Skill(dexterity, , pb)
            self._survival = self._Skill(wisdom, , pb)

        @property
        def acrobatics(self) -> _Skill:
            return self._acrobatics

        @property
        def animal_handling(self) -> _Skill:
            return self._animal_handling

        @property
        def arcana(self) -> _Skill:
            return self._arcana

        @property
        def athletics(self) -> _Skill:
            return self._athletics

        @property
        def deception(self) -> _Skill:
            return self._deception

        @property
        def history(self) -> _Skill:
            return self._history

        @property
        def insight(self) -> _Skill:
            return self._insight

        @property
        def intimidation(self) -> _Skill:
            return self._intimidation

        @property
        def investigation(self) -> _Skill:
            return self._investigation

        @property
        def medicine(self) -> _Skill:
            return self._medicine

        @property
        def nature(self) -> _Skill:
            return self._nature

        @property
        def perception(self) -> _Skill:
            return self._perception

        @property
        def performance(self) -> _Skill:
            return self._performance

        @property
        def persuasion(self) -> _Skill:
            return self._persuasion

        @property
        def religion(self) -> _Skill:
            return self._religion

        @property
        def sleight_of_hand(self) -> _Skill:
            return self._sleight_of_hand

        @property
        def stealth(self) -> _Skill:
            return self._stealth

        @property
        def survival(self) -> _Skill:
            return self._survival

    def __init__(
            self,
            name: str,
            player_name: str,
            class_: Type[Class],
            race: Type[Race],
            level: NaturalPlus,
            strength: Ability,
            dexterity: Ability,
            constitution: Ability,
            intelligence: Ability,
            wisdom: Ability,
            charisma: Ability,
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
        :param strength: The character's strength ability with its score taken directly from the dice roll
        :param dexterity: The character's dexterity ability with its score taken directly from the dice roll
        :param constitution: The character's constitution ability with its score taken directly from the dice roll
        :param intelligence: The character's intelligence ability with its score taken directly from the dice roll
        :param wisdom: The character's wisdom ability with its score taken directly from the dice roll
        :param charisma: The character's charisma ability with its score taken directly from the dice roll
        :param background: The character's background
        :param alignment: The character's alignment
        :param age: The character's age
        """

        # TODO: set new variables based on the character class and character race's static methods

        # TODO: modify tests with ability scores

        self._initialize_core_fields(name, player_name, class_, race, background, age)
        self._initialize_exception_raising_fields(alignment, level)
        self._abilities = self._Abilities(self, strength, dexterity, constitution, intelligence, wisdom, charisma)
        self._skills = self._Skills(self, )
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
    def abilities(self) -> _Abilities:
        return self._abilities

    @property
    def skills(self) -> _Skills:
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
        return get_level(self._exp)

    @property
    def proficiency_bonus(self) -> int:
        return get_proficiency_bonus(self.level)

    @property
    def age(self) -> int:
        return self._age.value

    @property
    def size(self) -> Size:
        return self._race.get_size()

    @property
    def speed(self) -> int:
        return self._race.get_speed()

    def _initialize_core_fields(
            self,
            name: str,
            player_name: str,
            class_: Type[Class],
            race: Type[Race],
            background: str,
            age: Natural
    ):
        """
        Initializes the fields of the character that are not derived from any other values

        :param name: The character's name
        :param player_name: Name of the player playing the character
        :param class_: The character's class
        :param race: The character's race
        :param background: The character's background
        :param age: The character's age
        """

        self._state = State.ALIVE
        self._reset_death_saves()

        self._name = name
        self._player_name = player_name
        self._class = class_
        self._race = race
        self._background = background
        self._age = age

    def _initialize_exception_raising_fields(self, alignment: Alignment, level: NaturalPlus):
        """
        Initializes the fields that may raise exceptions; raises ValueError if the given level is unreachable or the
        given alignment is inappropriate for a character of the given race

        :param alignment: The character's alignment
        :param level: The character's level
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

        self._exp = get_min_exp(
            check(
                level.value,
                reachable_level,
                "No character can reach this level."
            )
        )

    def _initialize_hit_points(self):
        """
        Initializes the character's hit points and max hit points
        """

        self._max_hit_points = self._class.get_hit_points() + self.abilities.constitution.modifier
        self.hit_points = self._max_hit_points

    def _reset_death_saves(self):
        """
        Resets both death save counts to 0
        """

        self._successful_death_saves = 0
        self._failed_death_saves = 0
