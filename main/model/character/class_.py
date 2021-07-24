from abc import abstractmethod, ABC


class Class(ABC):
    """
    The abstract representation of a class that a character can be; not to be used, only inherited
    """

    # TODO: refactor this and race into subclasses of new type

    # TODO: create tests

    _CALL_METHOD_IN_SUBCLASS_MSG = "This method should be called from one of Class' subclasses."

    @classmethod
    @abstractmethod
    def get_name(cls) -> str:
        """
        :return: The class' name
        """

        raise NotImplementedError(cls._CALL_METHOD_IN_SUBCLASS_MSG)

    @classmethod
    @abstractmethod
    def get_hit_points(cls) -> int:
        """
        :return: The hit points that this class gives to a character
        """

        raise NotImplementedError(cls._CALL_METHOD_IN_SUBCLASS_MSG)

    @classmethod
    @abstractmethod
    def strength_proficiency(cls) -> bool:
        """
        :return: True if class is proficient in strength; otherwise, false
        """

        raise NotImplementedError(cls._CALL_METHOD_IN_SUBCLASS_MSG)

    @classmethod
    @abstractmethod
    def dexterity_proficiency(cls) -> bool:
        """
        :return: True if class is proficient in dexterity; otherwise, false
        """

        raise NotImplementedError(cls._CALL_METHOD_IN_SUBCLASS_MSG)

    @classmethod
    @abstractmethod
    def constitution_proficiency(cls) -> bool:
        """
        :return: True if class is proficient in constitution; otherwise, false
        """

        raise NotImplementedError(cls._CALL_METHOD_IN_SUBCLASS_MSG)

    @classmethod
    @abstractmethod
    def intelligence_proficiency(cls) -> bool:
        """
        :return: True if class is proficient in intelligence; otherwise, false
        """

        raise NotImplementedError(cls._CALL_METHOD_IN_SUBCLASS_MSG)

    @classmethod
    @abstractmethod
    def wisdom_proficiency(cls) -> bool:
        """
        :return: True if class is proficient in wisdom; otherwise, false
        """

        raise NotImplementedError(cls._CALL_METHOD_IN_SUBCLASS_MSG)

    @classmethod
    @abstractmethod
    def charisma_proficiency(cls) -> bool:
        """
        :return: True if class is proficient in charisma; otherwise, false
        """

        raise NotImplementedError(cls._CALL_METHOD_IN_SUBCLASS_MSG)
