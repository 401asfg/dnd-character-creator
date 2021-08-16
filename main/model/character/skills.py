from abc import ABC, abstractmethod
from typing import Type, Tuple

from main.model.character.abilities import Abilities
from main.model.character.utility.enumerators.skill import Skill
from main.model.int_types.posint import Posint

# TODO: test skills
# TODO: fix not being recognized by autocomplete or typing


def _error():
    """
    Raises a NotImplementedError
    """

    raise NotImplementedError('Method implemented in subclass, call "generate_character_skills" to access.')


class Skills(ABC):
    """
    The character's skills
    """

    class Skill(ABC):
        """
        One of the character's skills
        """

        @abstractmethod
        def __init__(self, ability: Abilities.Ability, proficiency: bool, proficiency_bonus: Posint):
            """
            Initializes the class

            :param ability: The ability that this skill is bound to
            :param proficiency: Whether or not the character is proficient in this skill
            :param proficiency_bonus: The character's proficiency bonus
            """

            _error()

        @property
        @abstractmethod
        def modifier(self) -> int:
            """
            :return: The skill's modifier: ability modifier, plus proficiency_bonus if character is proficient in
            this skill
            """

            _error()

        @property
        @abstractmethod
        def proficient(self) -> bool:
            """
            :return: True if character is proficient in this skill; otherwise, false
            """

            _error()

    @abstractmethod
    def __init__(
            self,
            abilities: Abilities,
            proficiency_bonus: Posint
    ):
        """
        Initializes this class

        :param abilities: The abilities of the character to whom these skills belong
        :param proficiency_bonus: The proficiency bonus of the character to whom these skills belong
        """

        _error()

    @property
    @abstractmethod
    def acrobatics(self) -> Skill:
        _error()

    @property
    @abstractmethod
    def animal_handling(self) -> Skill:
        _error()

    @property
    @abstractmethod
    def arcana(self) -> Skill:
        _error()

    @property
    @abstractmethod
    def athletics(self) -> Skill:
        _error()

    @property
    @abstractmethod
    def deception(self) -> Skill:
        _error()

    @property
    @abstractmethod
    def history(self) -> Skill:
        _error()

    @property
    @abstractmethod
    def insight(self) -> Skill:
        _error()

    @property
    @abstractmethod
    def intimidation(self) -> Skill:
        _error()

    @property
    @abstractmethod
    def investigation(self) -> Skill:
        _error()

    @property
    @abstractmethod
    def medicine(self) -> Skill:
        _error()

    @property
    @abstractmethod
    def nature(self) -> Skill:
        _error()

    @property
    @abstractmethod
    def perception(self) -> Skill:
        _error()

    @property
    @abstractmethod
    def performance(self) -> Skill:
        _error()

    @property
    @abstractmethod
    def persuasion(self) -> Skill:
        _error()

    @property
    @abstractmethod
    def religion(self) -> Skill:
        _error()

    @property
    @abstractmethod
    def sleight_of_hand(self) -> Skill:
        _error()

    @property
    @abstractmethod
    def stealth(self) -> Skill:
        _error()

    @property
    @abstractmethod
    def survival(self) -> Skill:
        _error()


def generate_character_skills(
    skill_proficiencies: Tuple[Skill, ...]
) -> Type[Skills]:
    """
    Get the skills for a character

    :param skill_proficiencies: The skills that the character is proficient in
    :return: The skills of a character
    """

    class _Skills(Skills):
        class _Skill(Skills.Skill):
            def __init__(self, ability: Abilities.Ability, proficiency: bool, proficiency_bonus: Posint):
                self._ability = ability
                self._proficiency = proficiency
                self._proficiency_bonus = proficiency_bonus

            @property
            def modifier(self) -> int:
                return self._ability.modifier + self._proficiency * self._proficiency_bonus.value

            @property
            def proficient(self) -> bool:
                return self._proficiency

        def __init__(
                self,
                abilities: Abilities,
                proficiency_bonus: Posint
        ):
            def proficient(skill: Skill) -> bool:
                """
                :param skill: The skill proficiency to check
                :return: True if the given skill is in the skill proficiencies set that the character has;
                otherwise, false
                """

                return skill in skill_proficiencies

            strength = abilities.strength
            dexterity = abilities.dexterity
            intelligence = abilities.intelligence
            wisdom = abilities.wisdom
            charisma = abilities.charisma

            self._acrobatics = self._Skill(dexterity, proficient(Skill.ACROBATICS), proficiency_bonus)

            self._animal_handling = self._Skill(
                wisdom,
                proficient(Skill.ANIMAL_HANDLING),
                proficiency_bonus
            )

            self._arcana = self._Skill(intelligence, proficient(Skill.ARCANA), proficiency_bonus)
            self._athletics = self._Skill(strength, proficient(Skill.ATHLETICS), proficiency_bonus)
            self._deception = self._Skill(charisma, proficient(Skill.DECEPTION), proficiency_bonus)
            self._history = self._Skill(intelligence, proficient(Skill.HISTORY), proficiency_bonus)
            self._insight = self._Skill(wisdom, proficient(Skill.INSIGHT), proficiency_bonus)
            self._intimidation = self._Skill(charisma, proficient(Skill.INTIMIDATION), proficiency_bonus)

            self._investigation = self._Skill(
                intelligence,
                proficient(Skill.INVESTIGATION),
                proficiency_bonus
            )

            self._medicine = self._Skill(wisdom, proficient(Skill.MEDICINE), proficiency_bonus)
            self._nature = self._Skill(intelligence, proficient(Skill.NATURE), proficiency_bonus)
            self._perception = self._Skill(wisdom, proficient(Skill.PERCEPTION), proficiency_bonus)
            self._performance = self._Skill(charisma, proficient(Skill.PERFORMANCE), proficiency_bonus)
            self._persuasion = self._Skill(charisma, proficient(Skill.PERSUASION), proficiency_bonus)
            self._religion = self._Skill(intelligence, proficient(Skill.RELIGION), proficiency_bonus)

            self._sleight_of_hand = self._Skill(
                dexterity,
                proficient(Skill.SLEIGHT_OF_HAND),
                proficiency_bonus
            )

            self._stealth = self._Skill(dexterity, proficient(Skill.STEALTH), proficiency_bonus)
            self._survival = self._Skill(wisdom, proficient(Skill.SURVIVAL), proficiency_bonus)

        @property
        def acrobatics(self) -> Skills.Skill:
            return self._acrobatics

        @property
        def animal_handling(self) -> Skills.Skill:
            return self._animal_handling

        @property
        def arcana(self) -> Skills.Skill:
            return self._arcana

        @property
        def athletics(self) -> Skills.Skill:
            return self._athletics

        @property
        def deception(self) -> Skills.Skill:
            return self._deception

        @property
        def history(self) -> Skills.Skill:
            return self._history

        @property
        def insight(self) -> Skills.Skill:
            return self._insight

        @property
        def intimidation(self) -> Skills.Skill:
            return self._intimidation

        @property
        def investigation(self) -> Skills.Skill:
            return self._investigation

        @property
        def medicine(self) -> Skills.Skill:
            return self._medicine

        @property
        def nature(self) -> Skills.Skill:
            return self._nature

        @property
        def perception(self) -> Skills.Skill:
            return self._perception

        @property
        def performance(self) -> Skills.Skill:
            return self._performance

        @property
        def persuasion(self) -> Skills.Skill:
            return self._persuasion

        @property
        def religion(self) -> Skills.Skill:
            return self._religion

        @property
        def sleight_of_hand(self) -> Skills.Skill:
            return self._sleight_of_hand

        @property
        def stealth(self) -> Skills.Skill:
            return self._stealth

        @property
        def survival(self) -> Skills.Skill:
            return self._survival

    return _Skills
