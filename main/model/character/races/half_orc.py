from typing import Tuple, Dict

from main.model.character.alignment import Alignment
from main.model.character.utility.helper_modules.common_race_collection_items import get_darkvision, get_language
from main.model.character.race import Race
from main.model.character.utility.enumerators.ability import Ability
from main.model.character.utility.enumerators.language import Language
from main.model.character.utility.enumerators.size import Size
from main.model.character.utility.enumerators.skill import Skill
from main.model.collection.collection_item import CollectionItem


class HalfOrc(Race):
    """
    The racial information for a half-orc character
    """

    @property
    def traits(self) -> Tuple[CollectionItem, ...]:
        return (
            get_darkvision(),
            CollectionItem(
                "Relentless Endurance",
                "When you are reduced to 0 hit points but not killed outright, you can drop to 1 hit point instead. "
                "You can’t use this feature again until you finish a long rest."
            ),
            CollectionItem(
                "Savage Attacks",
                "When you score a critical hit with a melee weapon attack, you can roll one of the weapon’s damage "
                "dice one additional time and add it to the extra damage of the critical hit."
            )
        )

    @property
    def other_proficiencies(self) -> Tuple[CollectionItem, ...]:
        return (
            get_language(Language.COMMON),
            get_language(Language.ORC)
        )

    def _get_skill_proficiencies(self) -> Tuple[Skill, ...]:
        return (Skill.INTIMIDATION,)

    @staticmethod
    def get_name() -> str:
        return "Half-Orc"

    @staticmethod
    def get_acceptable_alignment_natures() -> Tuple[Alignment.Nature, ...]:
        return (
            Alignment.Nature.NEUTRAL,
            Alignment.Nature.CHAOTIC
        )

    @staticmethod
    def get_acceptable_alignment_moralities() -> Tuple[Alignment.Morality, ...]:
        return (
            Alignment.Morality.NEUTRAL,
            Alignment.Morality.EVIL
        )

    @staticmethod
    def get_min_adult_age() -> int:
        return 14

    @staticmethod
    def get_life_expectancy() -> int:
        return 75

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
            Ability.STRENGTH: 2,
            Ability.CONSTITUTION: 1
        }
