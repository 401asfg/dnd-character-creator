from main.model.character.class_ import Class
from main.model.dice.die import Die


class Ranger(Class):
    """
    The class information for a ranger character
    """

    @classmethod
    def get_name(cls) -> str:
        return "Ranger"

    @classmethod
    def get_hit_die(cls) -> Die:
        return Die(Die.Sides.TEN)

    @classmethod
    def get_strength_proficiency(cls) -> bool:
        return True

    @classmethod
    def get_dexterity_proficiency(cls) -> bool:
        return True

    @classmethod
    def get_constitution_proficiency(cls) -> bool:
        return False

    @classmethod
    def get_intelligence_proficiency(cls) -> bool:
        return False

    @classmethod
    def get_wisdom_proficiency(cls) -> bool:
        return False

    @classmethod
    def get_charisma_proficiency(cls) -> bool:
        return False
