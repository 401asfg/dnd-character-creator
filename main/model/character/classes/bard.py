from typing import Tuple

from main.model.character.class_ import Class
from main.model.character.utility.enumerators.ability import Ability
from main.model.dice.die import Die


class Bard(Class):
    """
    The class information for a bard character
    """

    @staticmethod
    def get_name() -> str:
        return "Bard"

    @staticmethod
    def get_hit_die() -> Die:
        return Die(Die.Sides.EIGHT)

    @staticmethod
    def _get_ability_proficiencies() -> Tuple[Ability, ...]:
        return (
            Ability.DEXTERITY,
            Ability.CHARISMA
        )
