from typing import Tuple, Dict

from main.model.character.alignment import Alignment
from main.model.character.utility.helper_modules.common_race_collection_items import get_darkvision, get_fey_ancestry, get_language
from main.model.character.race import Race
from main.model.character.utility.enumerators.ability import Ability
from main.model.character.utility.enumerators.language import Language
from main.model.character.utility.enumerators.size import Size
from main.model.character.utility.enumerators.skill import Skill
from main.model.collection.collection_item import CollectionItem


class HalfElf(Race):
    """
    The racial information for a half-elf character
    """

    def __init__(
            self,
            ability_bonus_one: Ability,
            ability_bonus_two: Ability,
            skill_proficiency_one: Skill,
            skill_proficiency_two: Skill,
            language: Language
    ):
        """
        Initializes the class; raises ValueError if ability_bonus_one or ability_bonus_two are CHARISMA or are the same
        ability; raises ValueError if language is COMMON or ELVISH

        :param ability_bonus_one: An ability that the character of this race gets an extra point in
        :param ability_bonus_two: An ability that the character of this race gets an extra point in
        :param skill_proficiency_one: An extra skill that a character of this race is proficient in
        :param skill_proficiency_two: An extra skill that a character of this race is proficient in
        :param language: The extra language that a half-elf character is proficient in
        """

        if ability_bonus_one == ability_bonus_two:
            raise ValueError("A half-elf cannot add both its ability bonuses to the same ability.")

        if Ability.CHARISMA == ability_bonus_one or Ability.CHARISMA == ability_bonus_two:
            raise ValueError("A half-elf cannot add an ability bonus to its charisma ability.")

        if language == Language.COMMON or language == Language.ELVISH:
            raise ValueError("A half-elf cannot be proficient in the same language twice.")

        self._ability_bonuses = (ability_bonus_one, ability_bonus_two)
        self._skill_proficiencies = (skill_proficiency_one, skill_proficiency_two)
        self._other_proficiencies = (
            get_language(Language.COMMON),
            get_language(Language.ELVISH),
            get_language(language)
        )

    @property
    def traits(self) -> Tuple[CollectionItem, ...]:
        return (
            get_darkvision(),
            get_fey_ancestry()
        )

    @property
    def other_proficiencies(self) -> Tuple[CollectionItem, ...]:
        return self._other_proficiencies

    def _get_skill_proficiencies(self) -> Tuple[Skill, ...]:
        return self._skill_proficiencies

    @staticmethod
    def get_name() -> str:
        return "Half-Elf"

    @staticmethod
    def get_acceptable_alignment_natures() -> Tuple[Alignment.Nature, ...]:
        return (
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
        return 20

    @staticmethod
    def get_life_expectancy() -> int:
        return 180

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
        def has_bonus(ability: Ability) -> int:
            """
            :param ability: The ability to check
            :return: 1, if the given ability is in the race's ability bonus set; otherwise 0
            """

            return ability in self._ability_bonuses

        return {
            Ability.STRENGTH: has_bonus(Ability.STRENGTH),
            Ability.DEXTERITY: has_bonus(Ability.DEXTERITY),
            Ability.CONSTITUTION: has_bonus(Ability.CONSTITUTION),
            Ability.INTELLIGENCE: has_bonus(Ability.INTELLIGENCE),
            Ability.WISDOM: has_bonus(Ability.WISDOM),
            Ability.CHARISMA: 2
        }
