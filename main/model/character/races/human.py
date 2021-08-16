from typing import Tuple, Dict

from main.model.character.alignment import Alignment
from main.model.character.utility.helper_modules.common_race_collection_items import get_language
from main.model.character.race import Race
from main.model.character.utility.enumerators.ability import Ability
from main.model.character.utility.enumerators.language import Language
from main.model.character.utility.enumerators.size import Size
from main.model.character.utility.enumerators.skill import Skill
from main.model.collection.collection_item import CollectionItem


class Human(Race):
    """
    The racial information for a human character
    """

    def __init__(self, language: Language):
        """
        Initializes the class; raises ValueError if language is COMMON

        :param language: The extra language that a human character is proficient in
        """

        if language == Language.COMMON:
            raise ValueError("A human cannot be proficient in the same language twice.")

        self._other_proficiencies = (
            get_language(Language.COMMON),
            get_language(language)
        )

    @property
    def traits(self) -> Tuple[CollectionItem, ...]:
        return ()

    @property
    def other_proficiencies(self) -> Tuple[CollectionItem, ...]:
        return self._other_proficiencies

    def _get_skill_proficiencies(self) -> Tuple[Skill, ...]:
        return ()

    @staticmethod
    def get_name() -> str:
        return "Human"

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
            Alignment.Morality.NEUTRAL,
            Alignment.Morality.EVIL
        )

    @staticmethod
    def get_min_adult_age() -> int:
        return 18

    @staticmethod
    def get_life_expectancy() -> int:
        return 99

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
            Ability.STRENGTH: 1,
            Ability.DEXTERITY: 1,
            Ability.CONSTITUTION: 1,
            Ability.INTELLIGENCE: 1,
            Ability.WISDOM: 1,
            Ability.CHARISMA: 1
        }
