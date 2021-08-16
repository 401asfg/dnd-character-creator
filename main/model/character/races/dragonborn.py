from enum import Enum
from typing import Tuple, Dict

from main.model.character.alignment import Alignment
from main.model.character.utility.helper_modules.common_race_collection_items import get_language
from main.model.character.race import Race
from main.model.character.races.half_elf import Language
from main.model.character.utility.enumerators.ability import Ability
from main.model.character.utility.enumerators.size import Size
from main.model.character.utility.enumerators.skill import Skill
from main.model.collection.collection_item import CollectionItem


class DraconicAncestry(Enum):
    """
    The draconic ancestry of a dragonborn character
    """

    BLACK = 0
    BLUE = 1
    BRASS = 2
    BRONZE = 3
    COPPER = 4
    GOLD = 5
    GREEN = 6
    RED = 7
    SILVER = 8
    WHITE = 9


_draconic_ancestries = {
    DraconicAncestry.BLACK: CollectionItem(
        "Black",
        "Damage Type: Acid\n Breath Weapon: 5 by 30 ft. line (Dex. save)"
    ),
    DraconicAncestry.BLUE: CollectionItem(
        "Blue",
        "Damage Type: Lightning\n Breath Weapon: 5 by 30 ft. line (Dex. save)"
    ),
    DraconicAncestry.BRASS: CollectionItem(
        "Brass",
        "Damage Type: Fire\n Breath Weapon: 5 by 30 ft. line (Dex. save)"),
    DraconicAncestry.BRONZE: CollectionItem(
        "Black",
        "Damage Type: Lightning\n Breath Weapon: 5 by 30 ft. line (Dex. save)"
    ),
    DraconicAncestry.COPPER: CollectionItem(
        "Copper",
        "Damage Type: Acid\n Breath Weapon: 5 by 30 ft. line (Dex. save)"
    ),
    DraconicAncestry.GOLD: CollectionItem(
        "Gold",
        "Damage Type: Fire\n Breath Weapon: 15 ft. cone (Dex. save)"
    ),
    DraconicAncestry.GREEN: CollectionItem(
        "Green",
        "Damage Type: Poison\n Breath Weapon: 15 ft. cone (Dex. save)"
    ),
    DraconicAncestry.RED: CollectionItem(
        "Red",
        "Damage Type: Fire\n Breath Weapon: 15 ft. cone (Dex. save)"
    ),
    DraconicAncestry.SILVER: CollectionItem(
        "Silver",
        "Damage Type: Cold\n Breath Weapon: 15 ft. cone (Dex. save)"
    ),
    DraconicAncestry.WHITE: CollectionItem(
        "White",
        "Damage Type: Cold\n Breath Weapon: 15 ft. cone (Dex. save)"
    )
}


class Dragonborn(Race):
    """
    The racial information for a dragonborn character
    """

    def __init__(self, draconic_ancestry: DraconicAncestry):
        """
        Initializes the class

        :param draconic_ancestry: The draconic ancestry of this dragonborn character
        """

        self._traits = (
            _draconic_ancestries[draconic_ancestry],
            CollectionItem(
                "Breath Weapon",
                "Use an action to exhale destructive energy. The type of attack is determined by your draconic "
                "ancestry."
            ),
            CollectionItem(
                "Damage Resistance",
                "You have resistance to the damage type associated with your draconic ancestry."
            )
        )

    @property
    def traits(self) -> Tuple[CollectionItem, ...]:
        return self._traits

    @property
    def other_proficiencies(self) -> Tuple[CollectionItem, ...]:
        return (
            get_language(Language.COMMON),
            get_language(Language.DRACONIC)
        )

    @staticmethod
    def get_name() -> str:
        return "Dragonborn"

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
            Alignment.Morality.EVIL
        )

    @staticmethod
    def get_min_adult_age() -> int:
        return 15

    @staticmethod
    def get_life_expectancy() -> int:
        return 80

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
            Ability.STRENGTH: 2
        }

    def _get_skill_proficiencies(self) -> Tuple[Skill, ...]:
        return ()
