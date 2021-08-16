from typing import Dict, Tuple

from main.model.character.races.halflings.halfling import Halfling
from main.model.character.utility.enumerators.ability import Ability
from main.model.collection.collection_item import CollectionItem


class StoutHalfling(Halfling):
    """
    The racial information for a stout halfling character
    """

    @property
    def traits(self) -> Tuple[CollectionItem, ...]:
        return self._get_appended_collection(
            super().traits,
            "Stout Resilience",
            "You have advantage on saving throws against poison, and you have resistance against poison damage."
        )

    def _get_ability_bonuses(self) -> Dict[Ability, int]:
        return self._get_appended_ability_bonuses(super()._get_ability_bonuses(), Ability.CONSTITUTION, 1)
