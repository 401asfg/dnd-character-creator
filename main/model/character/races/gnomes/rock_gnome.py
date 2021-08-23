from typing import Dict, Tuple

from main.model.character.races.gnomes.gnome import Gnome
from main.model.character.utility.enumerators.ability import Ability
from main.model.collection.collection_item import CollectionItem


class RockGnome(Gnome):
    """
    The racial information for a rock gnome character
    """

    @property
    def traits(self) -> Tuple[CollectionItem, ...]:
        return super().traits + (
            CollectionItem(
                "Artificer's Lore",
                "Whenever you make an Intelligence (History) check related to magic items, alchemical objects, or "
                "technological devices, you can add twice your proficiency bonus, instead of any proficiency bonus you "
                "normally apply."
            ),
        )

    @property
    def other_proficiencies(self) -> Tuple[CollectionItem, ...]:
        return super().other_proficiencies + (
            CollectionItem(
                "Tinker",
                "Using artisan's tools, you can spend 1 hour and 10 gp worth of materials to construct a Tiny "
                "clockwork device (AC 5, 1 hp). The device ceases to function after 24 hours (unless you spend 1 hour "
                "repairing it to keep the device functioning), or when you use your action to dismantle it; at that "
                "time, you can reclaim the materials used to create it. You can have up to three such devices active "
                "at a time.\n\nWhen you create a device, choose one of the following options:\n\nClockwork Toy. This "
                "toy is a clockwork animal, monster, or person, such as a frog, mouse, bird, dragon, or soldier. When "
                "placed on the ground, the toy moves 5 feet across the ground on each of your turns in a random "
                "direction. It makes noises as appropriate to the creature it represents.\n\nFire Starter. The device "
                "produces a miniature flame, which you can use to light a candle, torch, or campfire. Using the device "
                "requires your action.\n\nMusic Box. When opened, this music box plays a single song at a moderate "
                "volume. The box stops playing when it reaches the song’s end or when it is closed."
            ),
        )

    @staticmethod
    def get_name() -> str:
        return "Rock Gnome"

    def _get_ability_bonuses(self) -> Dict[Ability, int]:
        return self._get_appended_ability_bonuses(super()._get_ability_bonuses(), Ability.CONSTITUTION, 1)
