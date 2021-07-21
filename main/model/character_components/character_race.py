class CharacterRace:
    """
    The race of a character
    """

    # TODO: Add more parameters to account for all aspects of races

    def __init__(
            self,
            name,
            strength_bonus,
            dexterity_bonus,
            constitution_bonus,
            intelligence_bonus,
            wisdom_bonus,
            charisma_bonus,
            acceptable_alignment_moralities,
            acceptable_alignment_natures,
            min_age,
            max_age,
            size,
            speed
    ):
        """
        Builds a race with the given parameters

        :param name: (String) The race's name
        :param strength_bonus: (Integer) The racial bonus given to a character's strength stat
        :param dexterity_bonus: (Integer) The racial bonus given to a character's dexterity stat
        :param constitution_bonus: (Integer) The racial bonus given to a character's constitution stat
        :param intelligence_bonus: (Integer) The racial bonus given to a character's intelligence stat
        :param wisdom_bonus: (Integer) The racial bonus given to a character's wisdom stat
        :param charisma_bonus: (Integer) The racial bonus given to a character's charisma stat
        :param acceptable_alignment_moralities: (List of CharacterAlignment.Morality) The alignment moralities that a
        character can have
        :param acceptable_alignment_natures: (List of CharacterAlignment.Nature) The alignment natures that a character
        can have
        :param min_age: (Integer) The minimum age that a character of this race can have
        :param max_age: (Integer) The maximum age that a character of this race can have
        :param size: (Integer) The size of a character of this race
        :param speed: (Integer) The speed of a character of this race
        """

        self._name = name

        self._strength_bonus = strength_bonus
        self._dexterity_bonus = dexterity_bonus
        self._constitution_bonus = constitution_bonus
        self._intelligence_bonus = intelligence_bonus
        self._wisdom_bonus = wisdom_bonus
        self._charisma_bonus = charisma_bonus

        self._acceptable_alignment_moralities = acceptable_alignment_moralities
        self._acceptable_alignment_natures = acceptable_alignment_natures

        self._min_age = min_age
        self._max_age = max_age

        self._size = size
        self._speed = speed
        
    @property
    def name(self):
        return self._name

    @property
    def strength_bonus(self):
        return self._strength_bonus

    @property
    def dexterity_bonus(self):
        return self._dexterity_bonus

    @property
    def constitution_bonus(self):
        return self._constitution_bonus

    @property
    def intelligence_bonus(self):
        return self._intelligence_bonus

    @property
    def wisdom_bonus(self):
        return self._wisdom_bonus

    @property
    def charisma_bonus(self):
        return self._charisma_bonus

    @property
    def acceptable_alignment_moralities(self):
        return self._acceptable_alignment_moralities

    @property
    def acceptable_alignment_natures(self):
        return self._acceptable_alignment_natures

    @property
    def min_age(self):
        return self._min_age

    @property
    def max_age(self):
        return self._max_age

    @property
    def size(self):
        return self._size

    @property
    def speed(self):
        return self._speed
