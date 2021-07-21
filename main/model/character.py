from main.model.character_components.character_advancements import CharacterAdvancements
from main.model.character_components.character_races import CharacterRaces


class Character:
    """
    A 5th edition D&D character, with stats, skills, and info
    """

    MAX_SUCCESSFUL_DEATH_SAVES = 3
    MAX_FAILED_DEATH_SAVES = 3

    # TODO: add rest of parameters
    # TODO: add rest of functions
    # TODO: add exceptions to ctor (note all exceptions)

    def __init__(self, character_name, player_name, class_name, race_name, level, background, alignment):
        """
        Builds the character in its initial state; raises KeyError if there is no class with the given class_name, or if
        there is no race with the given race_name; raises ValueError if the given level is unreachable

        :param character_name: (String) Name of the character
        :param player_name: (String) Name of the player playing the character
        :param class_name: (String) Name of the character's class; used to get CharacterClass from dictionary of
        character classes
        :param race_name: (String) Name of the character's race; used to get CharacterRace from dictionary of character
        races
        :param level: (Integer) Character's starting level
        :param background: (String) Background of the character
        :param alignment: (CharacterAlignment) Alignment of the character
        """

        self._character_name = character_name
        self._player_name = player_name
        self._character_class =
        self._character_race = CharacterRaces.get(race_name)
        self._background = background
        self._alignment = alignment

        if CharacterAdvancements.reachable_level(level):
            self._level = level
        else:
            raise ValueError("The given level is not reachable by a character")

        self._successful_death_saves = 0
        self.failed_death_saves = 0

        self._exp = CharacterAdvancements.get_experience_points(self._level)
        self._proficiency_bonus = CharacterAdvancements.get_proficiency_bonus(self._exp)

    def gain_exp(self, points):
        """
        Give the character experience points; adjust the character's level and proficiency bonus to those which
        correspond with the new exp amount, as defined in the CharacterAdvancements class

        :param points: (Integer) The amount of experience points to give the character
        """

        self._exp += points
        self._level = CharacterAdvancements.get_level(self._exp)
        self._proficiency_bonus = CharacterAdvancements.get_proficiency_bonus(self._exp)

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
    def character_name(self):
        return self._character_name

    @property
    def player_name(self):
        return self._player_name

    # TODO: Add properties for dictionary derived values

    @property
    def character_class(self):
        return self._character_class

    @property
    def character_race(self):
        return self._character_race

    @property
    def level(self):
        return self._level

    @property
    def background(self):
        return self._background

    @property
    def successful_death_saves(self):
        return self._successful_death_saves

    @property
    def failed_death_saves(self):
        return self.failed_death_saves

    @property
    def alignment(self):
        return self._alignment

    @property
    def experience_points(self):
        return self._exp
