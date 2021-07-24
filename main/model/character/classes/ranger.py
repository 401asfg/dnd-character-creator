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
