from typing import Tuple

from main.model.character.class_ import Class
from main.model.character.utility.enumerators.ability_proficiency import AbilityProficiency
from main.model.dice.die import Die


class Sorcerer(Class):
    """
    The class information for a sorcerer character
    """

    @staticmethod
    def get_name() -> str:
        return "Sorcerer"

    @staticmethod
    def get_hit_die() -> Die:
        return Die(Die.Sides.SIX)

    @staticmethod
    def _get_ability_proficiencies() -> Tuple[AbilityProficiency, ...]:
        return (
            AbilityProficiency.CONSTITUTION,
            AbilityProficiency.CHARISMA
        )
