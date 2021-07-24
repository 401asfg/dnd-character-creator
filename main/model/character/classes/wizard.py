from main.model.character.class_ import Class


class Wizard(Class):
    """
    The class information for a wizard character
    """

    @classmethod
    def get_name(cls) -> str:
        return "Wizard"

    @classmethod
    def get_hit_points(cls) -> int:
        return 6

    @classmethod
    def strength_proficiency(cls) -> bool:
        return False

    @classmethod
    def dexterity_proficiency(cls) -> bool:
        return False

    @classmethod
    def constitution_proficiency(cls) -> bool:
        return False

    @classmethod
    def intelligence_proficiency(cls) -> bool:
        return True

    @classmethod
    def wisdom_proficiency(cls) -> bool:
        return True

    @classmethod
    def charisma_proficiency(cls) -> bool:
        return False
