from typing import List

from main.model.character.alignment import Alignment
from main.model.character.race import Race
from main.model.character.enumerators.size import Size


class Elf(Race):
    """
    The racial information for a elf character
    """

    @classmethod
    def get_name(cls) -> str:
        return "Elf"

    @classmethod
    def get_strength_bonus(cls) -> int:
        return 0

    @classmethod
    def get_dexterity_bonus(cls) -> int:
        return 2

    @classmethod
    def get_constitution_bonus(cls) -> int:
        return 0

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
    def get_acceptable_alignment_natures(cls) -> List[Alignment.Nature]:
        return [
            Alignment.Nature.NEUTRAL,
            Alignment.Nature.CHAOTIC
        ]

    @classmethod
    def get_acceptable_alignment_moralities(cls) -> List[Alignment.Morality]:
        return [
            Alignment.Morality.GOOD,
            Alignment.Morality.NEUTRAL,
            Alignment.Morality.EVIL
        ]

    @classmethod
    def get_min_adult_age(cls) -> int:
        return 100

    @classmethod
    def get_life_expectancy(cls) -> int:
        return 750

    @classmethod
    def get_size(cls) -> Size:
        return Size.MEDIUM

    @classmethod
    def get_speed(cls) -> int:
        return 30
