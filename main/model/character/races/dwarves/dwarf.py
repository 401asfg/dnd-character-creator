from abc import ABC
from enum import Enum
from typing import Tuple, Dict

from main.model.character.alignment import Alignment
from main.model.character.utility.helper_modules.common_race_collection_items import get_darkvision, get_language
from main.model.character.race import Race
from main.model.character.races.half_elf import Language
from main.model.character.utility.enumerators.ability import Ability
from main.model.character.utility.enumerators.size import Size
from main.model.character.utility.enumerators.skill import Skill
from main.model.collection.collection_item import CollectionItem


class ToolProficiency(Enum):
    """
    A tool proficiency a dwarf can have
    """

    SMITHS_TOOLS = 0
    BREWERS_SUPPLIES = 1
    MASONS_TOOLS = 2


_tool_proficiencies = {
    ToolProficiency.SMITHS_TOOLS: CollectionItem("Smith's Tools"),
    ToolProficiency.BREWERS_SUPPLIES: CollectionItem("Brewer's Supplies"),
    ToolProficiency.MASONS_TOOLS: CollectionItem("Mason's Tools")
}


class Dwarf(Race, ABC):
    """
    The racial information for a dwarf character
    """

    def __init__(self, tool_proficiency: ToolProficiency):
        """
        Initializes the class

        :param tool_proficiency: The tool proficiency that the dwarf has
        """

        self._other_proficiencies = (
            CollectionItem(
                "Dwarven Combat Training",
                "You have proficiency with the battleaxe, handaxe, light hammer, and warhammer."
            ),
            _tool_proficiencies[tool_proficiency],
            CollectionItem(
                "Stonecunning",
                "Whenever you make an Intelligence (History) check related to the origin of stonework, you are "
                "considered proficient in the History skill and add double your proficiency bonus to the check, instead"
                " of your normal proficiency bonus."
            ),
            get_language(Language.COMMON),
            get_language(Language.DWARVISH)
        )

    @property
    def traits(self) -> Tuple[CollectionItem, ...]:
        return (
            get_darkvision(),
            CollectionItem(
                "Dwarven Resilience",
                "You have advantage on saving throws against poison, and you have resistance against poison damage."
            )
        )

    @property
    def other_proficiencies(self) -> Tuple[CollectionItem, ...]:
        return self._other_proficiencies

    @staticmethod
    def get_name() -> str:
        return "Dwarf"

    @staticmethod
    def get_acceptable_alignment_natures() -> Tuple[Alignment.Nature, ...]:
        return (
            Alignment.Nature.LAWFUL,
            Alignment.Nature.NEUTRAL
        )

    @staticmethod
    def get_acceptable_alignment_moralities() -> Tuple[Alignment.Morality, ...]:
        return (
            Alignment.Morality.GOOD,
            Alignment.Morality.NEUTRAL
        )

    @staticmethod
    def get_min_adult_age() -> int:
        return 50

    @staticmethod
    def get_life_expectancy() -> int:
        return 350

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
            Ability.CONSTITUTION: 2
        }

    def _get_skill_proficiencies(self) -> Tuple[Skill, ...]:
        return ()
