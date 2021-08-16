from abc import ABC
from typing import Tuple, Dict

from main.model.character.alignment import Alignment
from main.model.character.utility.helper_modules.common_race_collection_items import get_language
from main.model.character.race import Race
from main.model.character.utility.enumerators.ability import Ability
from main.model.character.utility.enumerators.language import Language
from main.model.character.utility.enumerators.size import Size
from main.model.character.utility.enumerators.skill import Skill
from main.model.collection.collection_item import CollectionItem


class Halfling(Race, ABC):
    """
    The racial information for a halfling character
    """

    @property
    def traits(self) -> Tuple[CollectionItem, ...]:
        return (
            CollectionItem(
                "Lucky",
                "When you roll a 1 on the d20 for an attack roll, ability check, or saving throw, you can reroll the "
                "die and must use the new roll."
            ),
            CollectionItem(
                "Brave",
                "You have advantage on saving throws against being frightened."
            ),
            CollectionItem(
                "Halfling Nimbleness",
                "You can move through the space of any creature that is of a size larger than yours."
            )
        )

    @property
    def other_proficiencies(self) -> Tuple[CollectionItem, ...]:
        return (
            get_language(Language.COMMON),
            get_language(Language.HALFLING)
        )

    def _get_skill_proficiencies(self) -> Tuple[Skill, ...]:
        return ()

    @staticmethod
    def get_name() -> str:
        return "Halfling"

    @staticmethod
    def get_acceptable_alignment_natures() -> Tuple[Alignment.Nature, ...]:
        return (
            Alignment.Nature.LAWFUL,
            Alignment.Nature.NEUTRAL
        )

    @staticmethod
    def get_acceptable_alignment_moralities() -> Tuple[Alignment.Morality, ...]:
        return (
            Alignment.Morality.GOOD,
            Alignment.Morality.NEUTRAL
        )

    @staticmethod
    def get_min_adult_age() -> int:
        return 20

    @staticmethod
    def get_life_expectancy() -> int:
        return 150

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
            Ability.DEXTERITY: 2
        }
