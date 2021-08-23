from typing import Dict, Tuple

from main.model.character.races.elves.elf import Elf
from main.model.character.utility.enumerators.ability import Ability
from main.model.character.utility.enumerators.language import Language
from main.model.character.utility.helper_modules.common_race_collection_items import get_language
from main.model.collection.collection_item import CollectionItem

# TODO: ADD CANTRIP OF PLAYER'S CHOICE!!!!!!


class HighElf(Elf):
    """
    The racial information for a high elf character
    """

    def __init__(self, language: Language):
        """
        Initializes the class; raises ValueError if language is COMMON or ELVISH

        :param language: The extra language that this high elf character is proficient in
        """

        if language == Language.COMMON or language == Language.ELVISH:
            raise ValueError("The high elf can have two proficiencies in the same language.")

        self._language = language

    @property
    def other_proficiencies(self) -> Tuple[CollectionItem, ...]:
        return super().other_proficiencies + (
            get_language(self._language),
        )

    @staticmethod
    def get_name() -> str:
        return "High Elf"

    def _get_ability_bonuses(self) -> Dict[Ability, int]:
        return self._get_appended_ability_bonuses(super()._get_ability_bonuses(), Ability.INTELLIGENCE, 1)
