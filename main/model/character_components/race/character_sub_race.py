from main.model.character_components.character_alignment import CharacterAlignment
from main.model.character_components.character_size import CharacterSize
from main.model.character_components.race.character_race import CharacterRace
from typing import List


class CharacterSubRace(CharacterRace):
    """
    A sub category of a race that a character can be
    """

    def __init__(
            self,
            parent_race: CharacterRace,
            name: str,
            strength_bonus: int = None,
            dexterity_bonus: int = None,
            constitution_bonus: int = None,
            intelligence_bonus: int = None,
            wisdom_bonus: int = None,
            charisma_bonus: int = None,
            acceptable_alignment_natures: List[CharacterAlignment.Nature] = None,
            acceptable_alignment_moralities: List[CharacterAlignment.Morality] = None,
            min_adult_age: int = None,
            life_expectancy: int = None,
            size: CharacterSize = None,
            speed: int = None
    ):
        """
        Builds a sub race as a modified copy of the parent race

        :param parent_race: The race that this race is a sub race of; each parameter (aside from name) with a value of
        None will not be used, in its place, the value of the corresponding property in the parent_race will be used
        :param name: The race's name
        :param strength_bonus: The racial bonus given to a character's strength stat; if None, the value of the property
        of the same name, in parent_race, is used instead of None
        :param dexterity_bonus: The racial bonus given to a character's dexterity stat; if None, the value of the
        property of the same name, in parent_race, is used instead of None
        :param constitution_bonus: The racial bonus given to a character's constitution stat; if None, the value of the
        property of the same name, in parent_race, is used instead of None
        :param intelligence_bonus: The racial bonus given to a character's intelligence stat; if None, the value of the
        property of the same name, in parent_race, is used instead of None
        :param wisdom_bonus: The racial bonus given to a character's wisdom stat; if None, the value of the property of
        the same name, in parent_race, is used instead of None
        :param charisma_bonus: The racial bonus given to a character's charisma stat; if None, the value of the property
        of the same name, in parent_race, is used instead of None
        :param acceptable_alignment_natures: The alignment natures that a character can have; if None, the value of the
        property of the same name, in parent_race, is used instead of None
        :param acceptable_alignment_moralities: The alignment morality that a character can have; if None, the value of
        the property of the same name, in parent_race, is used instead of None
        :param min_adult_age: The age at which a character of this race becomes an adult; if None, the value of the
        property of the same name, in parent_race, is used instead of None
        :param life_expectancy: The age at which a character of this race is expected to die by; if None, the value of
        the property of the same name, in parent_race, is used instead of None
        :param size: The size of a character of this race; if None, the value of the property of the same name, in
        parent_race, is used instead of None
        :param speed: The speed of a character of this race; if None, the value of the property of the same name, in
        parent_race, is used instead of None
        """

        if strength_bonus is None:
            strength_bonus = parent_race.strength_bonus

        if dexterity_bonus is None:
            dexterity_bonus = parent_race.dexterity_bonus

        if constitution_bonus is None:
            constitution_bonus = parent_race.constitution_bonus

        if intelligence_bonus is None:
            intelligence_bonus = parent_race.intelligence_bonus

        if wisdom_bonus is None:
            wisdom_bonus = parent_race.wisdom_bonus

        if charisma_bonus is None:
            charisma_bonus = parent_race.charisma_bonus

        if acceptable_alignment_natures is None:
            acceptable_alignment_natures = parent_race.acceptable_alignment_natures

        if acceptable_alignment_moralities is None:
            acceptable_alignment_moralities = parent_race.acceptable_alignment_moralities

        if min_adult_age is None:
            min_adult_age = parent_race.min_adult_age

        if life_expectancy is None:
            life_expectancy = parent_race.life_expectancy

        if size is None:
            size = parent_race.size

        if speed is None:
            speed = parent_race.speed

        super().__init__(
            name,
            strength_bonus,
            dexterity_bonus,
            constitution_bonus,
            intelligence_bonus,
            wisdom_bonus,
            charisma_bonus,
            acceptable_alignment_natures,
            acceptable_alignment_moralities,
            min_adult_age,
            life_expectancy,
            size,
            speed
        )
