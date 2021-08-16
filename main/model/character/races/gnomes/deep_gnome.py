from typing import Dict, Tuple

from main.model.character.alignment import Alignment
from main.model.character.utility.helper_modules.common_race_collection_items import get_language
from main.model.character.races.gnomes.gnome import Gnome
from main.model.character.utility.enumerators.ability import Ability
from main.model.character.utility.enumerators.language import Language
from main.model.collection.collection_item import CollectionItem


class DeepGnome(Gnome):
    """
    The racial information for a deep gnome character
    """

    @property
    def traits(self) -> Tuple[CollectionItem, ...]:
        traits = self._get_appended_collection(
            super().traits,
            "Superior Darkvision",
            "Your darkvision has a radius of 120 feet."
        )

        return self._get_appended_collection(
            traits,
            "Stone Camouflage",
            "You have advantage on Dexterity (Stealth) checks to hide in rocky terrain."
        )

    @property
    def other_proficiencies(self) -> Tuple[CollectionItem, ...]:
        language = get_language(Language.UNDERCOMMON)
        return self._get_appended_collection(
            super().other_proficiencies,
            language.name,
            language.info
        )

    @staticmethod
    def get_acceptable_alignment_moralities() -> Tuple[Alignment.Morality, ...]:
        return (
            Alignment.Morality.NEUTRAL
        )

    @staticmethod
    def get_min_adult_age() -> int:
        return 25

    @staticmethod
    def get_life_expectancy() -> int:
        return 250

    def _get_ability_bonuses(self) -> Dict[Ability, int]:
        return self._get_appended_ability_bonuses(super()._get_ability_bonuses(), Ability.DEXTERITY, 1)
