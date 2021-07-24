from main.model.character.class_ import Class


class Ranger(Class):
    """
    The class information for a ranger character
    """

    @classmethod
    def get_name(cls) -> str:
        return "Ranger"

    @classmethod
    def get_hit_points(cls) -> int:
        return 10

    @classmethod
    def strength_proficiency(cls) -> bool:
        return True

    @classmethod
    def dexterity_proficiency(cls) -> bool:
        return True

    @classmethod
    def constitution_proficiency(cls) -> bool:
        return False

    @classmethod
    def intelligence_proficiency(cls) -> bool:
        return False

    @classmethod
    def wisdom_proficiency(cls) -> bool:
        return False

    @classmethod
    def charisma_proficiency(cls) -> bool:
        return False
