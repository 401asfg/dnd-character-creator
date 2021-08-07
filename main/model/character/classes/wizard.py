from main.model.character.class_ import Class
from main.model.dice.die import Die


class Wizard(Class):
    """
    The class information for a wizard character
    """

    @staticmethod
    def get_name() -> str:
        return "Wizard"

    @staticmethod
    def get_hit_die() -> Die:
        return Die(Die.Sides.SIX)

    @staticmethod
    def get_strength_proficiency() -> bool:
        return False

    @staticmethod
    def get_dexterity_proficiency() -> bool:
        return False

    @staticmethod
    def get_constitution_proficiency() -> bool:
        return False

    @staticmethod
    def get_intelligence_proficiency() -> bool:
        return True

    @staticmethod
    def get_wisdom_proficiency() -> bool:
        return True

    @staticmethod
    def get_charisma_proficiency() -> bool:
        return False
