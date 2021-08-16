from typing import Dict, Tuple

from main.model.character.races.dwarves.dwarf import Dwarf
from main.model.character.utility.enumerators.ability import Ability
from main.model.collection.collection_item import CollectionItem


class HillDwarf(Dwarf):
    """
    The racial information for a hill dwarf character
    """

    @property
    def traits(self) -> Tuple[CollectionItem, ...]:
        return self._get_appended_collection(
            super().traits,
            "Dwarven Toughness",
            "Your hit point maximum increases by 1 every time you gain a level."
        )

    @staticmethod
    def get_hit_point_bonus() -> int:
        return 1

    def _get_ability_bonuses(self) -> Dict[Ability, int]:
        return self._get_appended_ability_bonuses(super()._get_ability_bonuses(), Ability.WISDOM, 1)
