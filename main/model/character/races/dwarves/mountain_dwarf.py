from typing import Dict, Tuple

from main.model.character.races.dwarves.dwarf import Dwarf
from main.model.character.utility.enumerators.ability import Ability
from main.model.collection.collection_item import CollectionItem


class MountainDwarf(Dwarf):
    """
    The racial information for a mountain dwarf character
    """

    @property
    def other_proficiencies(self) -> Tuple[CollectionItem, ...]:
        return self._get_appended_collection(
            super().other_proficiencies,
            "Dwarven Armor Training",
            "You have proficiency with light and medium armor."
        )

    def _get_ability_bonuses(self) -> Dict[Ability, int]:
        return self._get_appended_ability_bonuses(super()._get_ability_bonuses(), Ability.STRENGTH, 2)
