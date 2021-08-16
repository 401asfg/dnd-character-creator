from typing import Dict, Tuple

from main.model.character.races.halflings.halfling import Halfling
from main.model.character.utility.enumerators.ability import Ability
from main.model.collection.collection_item import CollectionItem


class LightfootHalfling(Halfling):
    """
    The racial information for a lightfoot halfling character
    """

    @property
    def traits(self) -> Tuple[CollectionItem, ...]:
        return self._get_appended_collection(
            super().traits,
            "Naturally Stealthy",
            "You can attempt to hide even when you are obscured only by a creature that is at least one size larger "
            "than you."
        )

    def _get_ability_bonuses(self) -> Dict[Ability, int]:
        return self._get_appended_ability_bonuses(
            super()._get_ability_bonuses(),
            Ability.CHARISMA,
            1
        )
