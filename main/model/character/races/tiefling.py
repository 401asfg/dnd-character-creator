from typing import List

from main.model.character.alignment import Alignment
from main.model.character.race import Race
from main.model.character.utility.enumerators.size import Size


class Tiefling(Race):
    """
    The racial information for a tiefling character
    """

    @staticmethod
    def get_name() -> str:
        return "Tiefling"

    @staticmethod
    def get_strength_bonus() -> int:
        return 0

    @staticmethod
    def get_dexterity_bonus() -> int:
        return 0

    @staticmethod
    def get_constitution_bonus() -> int:
        return 0

    @staticmethod
    def get_intelligence_bonus() -> int:
        return 1

    @staticmethod
    def get_wisdom_bonus() -> int:
        return 0

    @staticmethod
    def get_charisma_bonus() -> int:
        return 2

    @staticmethod
    def get_additional_ability_bonus() -> int:
        return 0

    @staticmethod
    def get_acceptable_alignment_natures() -> List[Alignment.Nature]:
        return [
            Alignment.Nature.CHAOTIC,
            Alignment.Nature.NEUTRAL
        ]

    @staticmethod
    def get_acceptable_alignment_moralities() -> List[Alignment.Morality]:
        return [
            Alignment.Morality.NEUTRAL,
            Alignment.Morality.EVIL
        ]

    @staticmethod
    def get_min_adult_age() -> int:
        return 18

    @staticmethod
    def get_life_expectancy() -> int:
        return 99

    @staticmethod
    def get_size() -> Size:
        return Size.MEDIUM

    @staticmethod
    def get_speed() -> int:
        return 30
