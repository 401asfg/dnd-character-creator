from typing import List

from main.model.character_components.character_alignment import CharacterAlignment
from main.model.character_components.character_race import CharacterRace
from main.model.character_components.character_size import CharacterSize


class Dwarf(CharacterRace):
    """
    The racial information for a dwarf character
    """

    @classmethod
    def get_name(cls) -> str:
        return "Dwarf"

    @classmethod
    def get_strength_bonus(cls) -> int:
        return 0

    @classmethod
    def get_dexterity_bonus(cls) -> int:
        return 0

    @classmethod
    def get_constitution_bonus(cls) -> int:
        return 2

    @classmethod
    def get_intelligence_bonus(cls) -> int:
        return 0

    @classmethod
    def get_wisdom_bonus(cls) -> int:
        return 0

    @classmethod
    def get_charisma_bonus(cls) -> int:
        return 0

    @classmethod
    def get_acceptable_alignment_natures(cls) -> List[CharacterAlignment.Nature]:
        return [
            CharacterAlignment.Nature.LAWFUL,
            CharacterAlignment.Nature.NEUTRAL
        ]

    @classmethod
    def get_acceptable_alignment_moralities(cls) -> List[CharacterAlignment.Morality]:
        return [
            CharacterAlignment.Morality.GOOD,
            CharacterAlignment.Morality.NEUTRAL
        ]

    @classmethod
    def get_min_adult_age(cls) -> int:
        return 50

    @classmethod
    def get_life_expectancy(cls) -> int:
        return 350

    @classmethod
    def get_size(cls) -> CharacterSize:
        return CharacterSize.MEDIUM

    @classmethod
    def get_speed(cls) -> int:
        return 30
