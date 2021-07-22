from typing import List

from main.model.character_components.character_alignment import CharacterAlignment
from main.model.character_components.character_size import CharacterSize


class CharacterRace:
    """
    The race of a character
    """

    # TODO: Add more parameters to account for all aspects of races
    # TODO: Return to dictionary of races?

    def __init__(
            self,
            name: str,
            strength_bonus: int,
            dexterity_bonus: int,
            constitution_bonus: int,
            intelligence_bonus: int,
            wisdom_bonus: int,
            charisma_bonus: int,
            acceptable_alignment_natures: List[CharacterAlignment.Nature],
            acceptable_alignment_moralities: List[CharacterAlignment.Morality],
            min_adult_age: int,
            life_expectancy: int,
            size: CharacterSize,
            speed: int
    ):
        """
        Builds a race with the given parameters

        :param name: The race's name
        :param strength_bonus: The racial bonus given to a character's strength stat
        :param dexterity_bonus: The racial bonus given to a character's dexterity stat
        :param constitution_bonus: The racial bonus given to a character's constitution stat
        :param intelligence_bonus: The racial bonus given to a character's intelligence stat
        :param wisdom_bonus: The racial bonus given to a character's wisdom stat
        :param charisma_bonus: The racial bonus given to a character's charisma stat
        :param acceptable_alignment_natures: The alignment natures that a character can have
        :param acceptable_alignment_moralities: The alignment moralities that a character can have
        :param min_adult_age: The age at which a character of this race becomes an adult
        :param life_expectancy: The age at which a character of this race is expected to die by
        :param size: The size of a character of this race
        :param speed: The speed of a character of this race
        """

        self._name = name

        self._strength_bonus = strength_bonus
        self._dexterity_bonus = dexterity_bonus
        self._constitution_bonus = constitution_bonus
        self._intelligence_bonus = intelligence_bonus
        self._wisdom_bonus = wisdom_bonus
        self._charisma_bonus = charisma_bonus

        self._acceptable_alignment_natures = acceptable_alignment_natures
        self._acceptable_alignment_moralities = acceptable_alignment_moralities

        self._min_adult_age = min_adult_age
        self._life_expectancy = life_expectancy

        self._size = size
        self._speed = speed

    @property
    def name(self) -> str:
        return self._name

    @property
    def strength_bonus(self) -> int:
        return self._strength_bonus

    @property
    def dexterity_bonus(self) -> int:
        return self._dexterity_bonus

    @property
    def constitution_bonus(self) -> int:
        return self._constitution_bonus

    @property
    def intelligence_bonus(self) -> int:
        return self._intelligence_bonus

    @property
    def wisdom_bonus(self) -> int:
        return self._wisdom_bonus

    @property
    def charisma_bonus(self) -> int:
        return self._charisma_bonus

    @property
    def acceptable_alignment_natures(self) -> List[CharacterAlignment.Nature]:
        return self._acceptable_alignment_natures

    @property
    def acceptable_alignment_moralities(self) -> List[CharacterAlignment.Morality]:
        return self._acceptable_alignment_moralities

    @property
    def min_adult_age(self) -> int:
        return self._min_adult_age

    @property
    def life_expectancy(self) -> int:
        return self._life_expectancy

    @property
    def size(self) -> int:
        return self._size

    @property
    def speed(self) -> int:
        return self._speed
