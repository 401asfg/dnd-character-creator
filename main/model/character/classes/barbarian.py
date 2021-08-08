from typing import Tuple

from main.model.character.class_ import Class
from main.model.character.utility.enumerators.ability_proficiency import AbilityProficiency
from main.model.dice.die import Die


class Barbarian(Class):
    """
    The class information for a barbarian character
    """

    @staticmethod
    def get_name() -> str:
        return "Barbarian"

    @staticmethod
    def get_hit_die() -> Die:
        return Die(Die.Sides.TWELVE)

    @staticmethod
    def _get_ability_proficiencies() -> Tuple[AbilityProficiency, ...]:
        return (
            AbilityProficiency.STRENGTH,
            AbilityProficiency.CONSTITUTION
        )
