from typing import Dict, Tuple

from main.model.character.races.elves.elf import Elf
from main.model.character.utility.enumerators.ability import Ability
from main.model.collection.collection_item import CollectionItem


class WoodElf(Elf):
    """
    The racial information for a wood elf character
    """

    @property
    def traits(self) -> Tuple[CollectionItem, ...]:
        return self._get_appended_collection(
            super().traits,
            "Mask of the Wild",
            "You can attempt to hide even when you are only lightly obscured by foliage, heavy rain, falling snow, "
            "mist, and other natural phenomena."
        )

    @property
    def other_proficiencies(self) -> Tuple[CollectionItem, ...]:
        return self._get_appended_collection(
            super().other_proficiencies,
            "Elf Weapon Training",
            "You have proficiency with the longsword, shortsword, shortbow, and longbow."
        )

    @staticmethod
    def get_speed() -> int:
        return 35

    def _get_ability_bonuses(self) -> Dict[Ability, int]:
        return self._get_appended_ability_bonuses(super()._get_ability_bonuses(), Ability.WISDOM, 1)
