from abc import ABC
from typing import Tuple, Dict

from main.model.character.alignment import Alignment
from main.model.character.utility.helper_modules.common_race_collection_items import get_darkvision, get_language
from main.model.character.race import Race
from main.model.character.races.half_elf import Language
from main.model.character.utility.enumerators.ability import Ability
from main.model.character.utility.enumerators.size import Size
from main.model.character.utility.enumerators.skill import Skill
from main.model.collection.collection_item import CollectionItem


class Gnome(Race, ABC):
    """
    The racial information for a gnome character
    """

    @property
    def traits(self) -> Tuple[CollectionItem, ...]:
        return (
            get_darkvision(),
            CollectionItem(
                "Gnome Cunning",
                "You have advantage on all Intelligence, Wisdom, and Charisma saving throws against magic."
            )
        )

    @property
    def other_proficiencies(self) -> Tuple[CollectionItem, ...]:
        return (
            get_language(Language.COMMON),
            get_language(Language.GNOMISH)
        )

    def _get_skill_proficiencies(self) -> Tuple[Skill, ...]:
        return ()

    @staticmethod
    def get_name() -> str:
        return "Gnome"

    @staticmethod
    def get_acceptable_alignment_natures() -> Tuple[Alignment.Nature, ...]:
        return (
            Alignment.Nature.LAWFUL,
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
        return 40

    @staticmethod
    def get_life_expectancy() -> int:
        return 500

    @staticmethod
    def get_size() -> Size:
        return Size.SMALL

    @staticmethod
    def get_speed() -> int:
        return 25

    @staticmethod
    def get_hit_point_bonus() -> int:
        return 0

    def _get_ability_bonuses(self) -> Dict[Ability, int]:
        return {
            Ability.INTELLIGENCE: 2
        }
