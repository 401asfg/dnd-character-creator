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
