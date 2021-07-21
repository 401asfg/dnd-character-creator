from main.model.character_components.character_race import CharacterRace
from main.model.character_components.character_alignment import CharacterAlignment
from main.model.character_components.character_size import CharacterSize


class CharacterRaces:
    """
    The database of all possible races that a character can be
    """

    # TODO: Make sure all data is accurate
    # TODO: Add rest of races
    # TODO: Add sub races
    # TODO: shorten imported references (from CharacterAlignment.Morality.GOOD to Morality.GOOD)?

    _race_dict = {
        "Dragonborn": CharacterRace(
            "Dragonborn",
            2,
            0,
            0,
            0,
            0,
            1,
            [
                CharacterAlignment.Morality.GOOD,
                CharacterAlignment.Morality.EVIL
            ],
            [
                CharacterAlignment.Nature.LAWFUL,
                CharacterAlignment.Nature.NEUTRAL,
                CharacterAlignment.Nature.CHAOTIC
            ],
            15,
            80,
            CharacterSize.MEDIUM,
            30
        ),
        "Dwarf": CharacterRace(
            "Dwarf",
            0,
            0,
            2,
            0,
            0,
            0,
            [
                CharacterAlignment.Morality.GOOD,
                CharacterAlignment.Morality.NEUTRAL
            ],
            [
                CharacterAlignment.Nature.LAWFUL,
                CharacterAlignment.Nature.NEUTRAL
            ],
            50,
            350,
            CharacterSize.MEDIUM,
            25
        ),
        "Elf": CharacterRace(
            "Elf",
            0,
            2,
            0,
            0,
            0,
            0,
            [
                CharacterAlignment.Morality.GOOD,
                CharacterAlignment.Morality.NEUTRAL,
                CharacterAlignment.Morality.EVIL
            ],
            [
                CharacterAlignment.Nature.NEUTRAL,
                CharacterAlignment.Nature.CHAOTIC
            ],
            100,
            750,
            CharacterSize.MEDIUM,
            30
        ),
        "Gnome": CharacterRace(
            "Gnome",
            0,
            0,
            0,
            2,
            0,
            0,
            [
                CharacterAlignment.Morality.GOOD,
                CharacterAlignment.Morality.NEUTRAL
            ],
            [
                CharacterAlignment.Nature.LAWFUL,
                CharacterAlignment.Nature.NEUTRAL,
                CharacterAlignment.Nature.CHAOTIC
            ],
            350,
            500,
            CharacterSize.SMALL,
            25
        ),
        "Human": CharacterRace(
            "Human",
            1,
            1,
            1,
            1,
            1,
            1,
            [
                CharacterAlignment.Morality.GOOD,
                CharacterAlignment.Morality.NEUTRAL,
                CharacterAlignment.Morality.EVIL
            ],
            [
                CharacterAlignment.Nature.LAWFUL,
                CharacterAlignment.Nature.NEUTRAL,
                CharacterAlignment.Nature.CHAOTIC
            ],
            18,
            99,
            CharacterSize.MEDIUM,
            30
        )
    }

    @classmethod
    def get(cls, race_name):
        """
        Gets the race that has the given name; raises KeyError if the given name does not correspond to any race in the
        race database

        :param race_name: (String) The name of the race
        :return: (CharacterRace) The race that has the given name
        """

        return cls._race_dict[race_name]

    @classmethod
    def exists(cls, race_name):
        """
        Checks that there is a race with the given name

        :param race_name: (String) The name of the race
        :return: (Boolean) Returns true if the race with the given name is in the race database, otherwise returns false
        """

        return race_name in cls._race_dict

