from abc import ABC
from typing import Tuple, Dict

from main.model.character.alignment import Alignment
from main.model.character.utility.helper_modules.common_race_collection_items import get_darkvision, get_fey_ancestry, get_language
from main.model.character.race import Race
from main.model.character.races.half_elf import Language
from main.model.character.utility.enumerators.ability import Ability
from main.model.character.utility.enumerators.size import Size
from main.model.character.utility.enumerators.skill import Skill
from main.model.collection.collection_item import CollectionItem


class Elf(Race, ABC):
    """
    The racial information for a elf character
    """

    @property
    def traits(self) -> Tuple[CollectionItem, ...]:
        return (
            get_darkvision(),
            get_fey_ancestry(),
            CollectionItem(
                "Trance",
                "Elves don’t need to sleep. Instead, they meditate deeply, remaining semiconscious, for 4 hours a day."
            )
        )

    @property
    def other_proficiencies(self) -> Tuple[CollectionItem, ...]:
        return (
            get_language(Language.COMMON),
            get_language(Language.ELVISH),
            CollectionItem(
                "Elf Weapon Training",
                "You have proficiency with the longsword, shortsword, shortbow, and longbow."
            )
        )

    @staticmethod
    def get_name() -> str:
        return "Elf"

    @staticmethod
    def get_acceptable_alignment_natures() -> Tuple[Alignment.Nature, ...]:
        return (
            Alignment.Nature.NEUTRAL,
            Alignment.Nature.CHAOTIC
        )

    @staticmethod
    def get_acceptable_alignment_moralities() -> Tuple[Alignment.Morality, ...]:
        return (
            Alignment.Morality.GOOD,
            Alignment.Morality.NEUTRAL
        )

    @staticmethod
    def get_min_adult_age() -> int:
        return 100

    @staticmethod
    def get_life_expectancy() -> int:
        return 750

    @staticmethod
    def get_size() -> Size:
        return Size.MEDIUM

    @staticmethod
    def get_speed() -> int:
        return 30

    @staticmethod
    def get_hit_point_bonus() -> int:
        return 0

    def _get_ability_bonuses(self) -> Dict[Ability, int]:
        return {
            Ability.DEXTERITY: 2
        }

    def _get_skill_proficiencies(self) -> Tuple[Skill, ...]:
        return (Skill.PERCEPTION,)
