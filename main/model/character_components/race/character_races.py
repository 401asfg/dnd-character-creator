from main.model.character_components.race.character_race import CharacterRace
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

    @classmethod
    def _create_races(cls):
        """
        Creates all the races and the race database
        """

        dragonborn = CharacterRace(
            "Dragonborn",
            2,
            0,
            0,
            0,
            0,
            1,
            [
                CharacterAlignment.Nature.LAWFUL,
                CharacterAlignment.Nature.NEUTRAL,
                CharacterAlignment.Nature.CHAOTIC
            ],
            [
                CharacterAlignment.Morality.GOOD,
                CharacterAlignment.Morality.EVIL
            ],
            15,
            80,
            CharacterSize.MEDIUM,
            30
        )

        dwarf = CharacterRace(
            "Dwarf",
            0,
            0,
            2,
            0,
            0,
            0,
            [
                CharacterAlignment.Nature.LAWFUL,
                CharacterAlignment.Nature.NEUTRAL
            ],
            [
                CharacterAlignment.Morality.GOOD,
                CharacterAlignment.Morality.NEUTRAL
            ],
            50,
            350,
            CharacterSize.MEDIUM,
            25
        )

        elf = CharacterRace(
            "Elf",
            0,
            2,
            0,
            0,
            0,
            0,
            [
                CharacterAlignment.Nature.NEUTRAL,
                CharacterAlignment.Nature.CHAOTIC
            ],
            [
                CharacterAlignment.Morality.GOOD,
                CharacterAlignment.Morality.NEUTRAL,
                CharacterAlignment.Morality.EVIL
            ],
            100,
            750,
            CharacterSize.MEDIUM,
            30
        )

        gnome = CharacterRace(
            "Gnome",
            0,
            0,
            0,
            2,
            0,
            0,
            [
                CharacterAlignment.Nature.LAWFUL,
                CharacterAlignment.Nature.NEUTRAL,
                CharacterAlignment.Nature.CHAOTIC
            ],
            [
                CharacterAlignment.Morality.GOOD,
                CharacterAlignment.Morality.NEUTRAL
            ],
            350,
            500,
            CharacterSize.SMALL,
            25
        )

        human = CharacterRace(
            "Human",
            1,
            1,
            1,
            1,
            1,
            1,
            [
                CharacterAlignment.Nature.LAWFUL,
                CharacterAlignment.Nature.NEUTRAL,
                CharacterAlignment.Nature.CHAOTIC
            ],
            [
                CharacterAlignment.Morality.GOOD,
                CharacterAlignment.Morality.NEUTRAL,
                CharacterAlignment.Morality.EVIL
            ],
            18,
            99,
            CharacterSize.MEDIUM,
            30
        )

        cls._race_dict = {
            dragonborn.name: dragonborn,
            dwarf.name: dwarf,
            elf.name: elf,
            gnome.name: gnome,
            human.name: human
        }

    _create_races()

    @classmethod
    def get(cls, race_name: str) -> CharacterRace:
        """
        Gets the race that has the given name; raises KeyError if the given name does not correspond to any race in the
        race database

        :param race_name: The name of the race
        :return: The race that has the given name
        """

        return cls._race_dict[race_name]

    @classmethod
    def exists(cls, race_name: str) -> bool:
        """
        Checks that there is a race with the given name

        :param race_name: The name of the race
        :return: Returns true if the race with the given name is in the race database, otherwise returns false
        """

        return race_name in cls._race_dict
