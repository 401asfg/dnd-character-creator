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
    def get_strength_proficiency(cls) -> bool:
        return False

    @classmethod
    def get_dexterity_proficiency(cls) -> bool:
        return False

    @classmethod
    def get_constitution_proficiency(cls) -> bool:
        return False

    @classmethod
    def get_intelligence_proficiency(cls) -> bool:
        return True

    @classmethod
    def get_wisdom_proficiency(cls) -> bool:
        return True

    @classmethod
    def get_charisma_proficiency(cls) -> bool:
        return False
