from main.model.character.class_ import Class


class Bard(Class):
    """
    The class information for a bard character
    """

    @classmethod
    def get_name(cls) -> str:
        return "Bard"

    @classmethod
    def get_hit_points(cls) -> int:
        return 8
