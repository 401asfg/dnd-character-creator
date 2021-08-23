from typing import Tuple, Dict

from main.model.character.alignment import Alignment
from main.model.character.utility.helper_modules.common_race_collection_items import get_darkvision, get_language
from main.model.character.race import Race
from main.model.character.utility.enumerators.ability import Ability
from main.model.character.utility.enumerators.language import Language
from main.model.character.utility.enumerators.size import Size
from main.model.character.utility.enumerators.skill import Skill
from main.model.collection.collection_item import CollectionItem

# TODO: ADD THAUMATURGY CANTRIP!!!!!!!!!!!!!!!!!!!


class Tiefling(Race):
    """
    The racial information for a tiefling character
    """

    @property
    def traits(self) -> Tuple[CollectionItem, ...]:
        return (
            get_darkvision(),
            CollectionItem("Hellish Resistance", "You have resistance to fire damage.")
        )

    @property
    def other_proficiencies(self) -> Tuple[CollectionItem, ...]:
        return (
            get_language(Language.COMMON),
            get_language(Language.INFERNAL)
        )

    def _get_ability_bonuses(self) -> Dict[Ability, int]:
        return {
            Ability.INTELLIGENCE: 1,
            Ability.CHARISMA: 2
        }

    def _get_skill_proficiencies(self) -> Tuple[Skill, ...]:
        return ()

    @staticmethod
    def get_name() -> str:
        return "Tiefling"

    @staticmethod
    def get_acceptable_alignment_natures() -> Tuple[Alignment.Nature, ...]:
        return (
            Alignment.Nature.CHAOTIC,
            Alignment.Nature.NEUTRAL
        )

    @staticmethod
    def get_acceptable_alignment_moralities() -> Tuple[Alignment.Morality, ...]:
        return (
            Alignment.Morality.NEUTRAL,
            Alignment.Morality.EVIL
        )

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
    def get_hit_point_bonus() -> int:
        return 0

    @staticmethod
    def get_speed() -> int:
        return 30
