from abc import ABC, abstractmethod
from typing import Type

from main.model.character.abilities import Abilities
from main.model.int_types.posint import Posint

# TODO: test skills
# TODO: fix not being recognized by autocomplete or typing


_NOT_IMPLEMENTED_MSG = 'Method implemented in subclass, call "generate_character_skills" to access.'


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

            raise NotImplementedError(_NOT_IMPLEMENTED_MSG)

        @property
        @abstractmethod
        def modifier(self) -> int:
            """
            :return: The skill's modifier: ability modifier, plus proficiency_bonus if character is proficient in
            this skill
            """

            raise NotImplementedError(_NOT_IMPLEMENTED_MSG)

        @property
        @abstractmethod
        def proficient(self) -> bool:
            """
            :return: True if character is proficient in this skill; otherwise, false
            """

            raise NotImplementedError(_NOT_IMPLEMENTED_MSG)

    @abstractmethod
    def __init__(
            self,
            strength: Abilities.Ability,
            dexterity: Abilities.Ability,
            intelligence: Abilities.Ability,
            wisdom: Abilities.Ability,
            charisma: Abilities.Ability,
            proficiency_bonus: Posint
    ):
        """
        Initializes this class

        :param strength: The strength ability of the character to whom these skills belong
        :param dexterity: The dexterity ability of the character to whom these skills belong
        :param intelligence: The intelligence ability of the character to whom these skills belong
        :param wisdom: The wisdom ability of the character to whom these skills belong
        :param charisma: The charisma ability of the character to whom these skills belong
        :param proficiency_bonus: The proficiency bonus of the character to whom these skills belong
        """

        raise NotImplementedError(_NOT_IMPLEMENTED_MSG)

    @property
    @abstractmethod
    def acrobatics(self) -> Skill:
        raise NotImplementedError(_NOT_IMPLEMENTED_MSG)

    @property
    @abstractmethod
    def animal_handling(self) -> Skill:
        raise NotImplementedError(_NOT_IMPLEMENTED_MSG)

    @property
    @abstractmethod
    def arcana(self) -> Skill:
        raise NotImplementedError(_NOT_IMPLEMENTED_MSG)

    @property
    @abstractmethod
    def athletics(self) -> Skill:
        raise NotImplementedError(_NOT_IMPLEMENTED_MSG)

    @property
    @abstractmethod
    def deception(self) -> Skill:
        raise NotImplementedError(_NOT_IMPLEMENTED_MSG)

    @property
    @abstractmethod
    def history(self) -> Skill:
        raise NotImplementedError(_NOT_IMPLEMENTED_MSG)

    @property
    @abstractmethod
    def insight(self) -> Skill:
        raise NotImplementedError(_NOT_IMPLEMENTED_MSG)

    @property
    @abstractmethod
    def intimidation(self) -> Skill:
        raise NotImplementedError(_NOT_IMPLEMENTED_MSG)

    @property
    @abstractmethod
    def investigation(self) -> Skill:
        raise NotImplementedError(_NOT_IMPLEMENTED_MSG)

    @property
    @abstractmethod
    def medicine(self) -> Skill:
        raise NotImplementedError(_NOT_IMPLEMENTED_MSG)

    @property
    @abstractmethod
    def nature(self) -> Skill:
        raise NotImplementedError(_NOT_IMPLEMENTED_MSG)

    @property
    @abstractmethod
    def perception(self) -> Skill:
        raise NotImplementedError(_NOT_IMPLEMENTED_MSG)

    @property
    @abstractmethod
    def performance(self) -> Skill:
        raise NotImplementedError(_NOT_IMPLEMENTED_MSG)

    @property
    @abstractmethod
    def persuasion(self) -> Skill:
        raise NotImplementedError(_NOT_IMPLEMENTED_MSG)

    @property
    @abstractmethod
    def religion(self) -> Skill:
        raise NotImplementedError(_NOT_IMPLEMENTED_MSG)

    @property
    @abstractmethod
    def sleight_of_hand(self) -> Skill:
        raise NotImplementedError(_NOT_IMPLEMENTED_MSG)

    @property
    @abstractmethod
    def stealth(self) -> Skill:
        raise NotImplementedError(_NOT_IMPLEMENTED_MSG)

    @property
    @abstractmethod
    def survival(self) -> Skill:
        raise NotImplementedError(_NOT_IMPLEMENTED_MSG)


def generate_character_skills(
        acrobatics_proficiency: bool,
        animal_handling_proficiency: bool,
        arcana_proficiency: bool,
        athletics_proficiency: bool,
        deception_proficiency: bool,
        history_proficiency: bool,
        insight_proficiency: bool,
        intimidation_proficiency: bool,
        investigation_proficiency : bool,
        medicine_proficiency: bool,
        nature_proficiency: bool,
        perception_proficiency: bool,
        performance_proficiency: bool,
        persuasion_proficiency: bool,
        religion_proficiency: bool,
        sleight_of_hand_proficiency: bool,
        stealth_proficiency: bool,
        survival_proficiency: bool
) -> Type[Skills]:
    """
    Get the skills for a character

    :param acrobatics_proficiency: Whether the character to whom these skills belong is proficient in acrobatics
    :param animal_handling_proficiency: Whether the character to whom these skills belong is proficient in animal
    handling
    :param arcana_proficiency: Whether the character to whom these skills belong is proficient in arcana
    :param athletics_proficiency: Whether the character to whom these skills belong is proficient in athletics
    :param deception_proficiency: Whether the character to whom these skills belong is proficient in deception
    :param history_proficiency: Whether the character to whom these skills belong is proficient in history
    :param insight_proficiency: Whether the character to whom these skills belong is proficient in insight
    :param intimidation_proficiency: Whether the character to whom these skills belong is proficient in intimidation
    :param investigation_proficiency: Whether the character to whom these skills belong is proficient in investigation
    :param medicine_proficiency: Whether the character to whom these skills belong is proficient in medicine
    :param nature_proficiency: Whether the character to whom these skills belong is proficient in nature
    :param perception_proficiency: Whether the character to whom these skills belong is proficient in perception
    :param performance_proficiency: Whether the character to whom these skills belong is proficient in performance
    :param persuasion_proficiency: Whether the character to whom these skills belong is proficient in persuasion
    :param religion_proficiency: Whether the character to whom these skills belong is proficient in religion
    :param sleight_of_hand_proficiency: Whether the character to whom these skills belong is proficient in sleight of
    hand
    :param stealth_proficiency: Whether the character to whom these skills belong is proficient in stealth
    :param survival_proficiency: Whether the character to whom these skills belong is proficient in survival
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
                strength: Abilities.Ability,
                dexterity: Abilities.Ability,
                intelligence: Abilities.Ability,
                wisdom: Abilities.Ability,
                charisma: Abilities.Ability,
                proficiency_bonus: Posint
        ):
            self._acrobatics = self._Skill(dexterity, acrobatics_proficiency, proficiency_bonus)
            self._animal_handling = self._Skill(wisdom, animal_handling_proficiency, proficiency_bonus)
            self._arcana = self._Skill(intelligence, arcana_proficiency, proficiency_bonus)
            self._athletics = self._Skill(strength, athletics_proficiency, proficiency_bonus)
            self._deception = self._Skill(charisma, deception_proficiency, proficiency_bonus)
            self._history = self._Skill(intelligence, history_proficiency, proficiency_bonus)
            self._insight = self._Skill(wisdom, insight_proficiency, proficiency_bonus)
            self._intimidation = self._Skill(charisma, intimidation_proficiency, proficiency_bonus)
            self._investigation = self._Skill(intelligence, investigation_proficiency, proficiency_bonus)
            self._medicine = self._Skill(wisdom, medicine_proficiency, proficiency_bonus)
            self._nature = self._Skill(intelligence, nature_proficiency, proficiency_bonus)
            self._perception = self._Skill(wisdom, perception_proficiency, proficiency_bonus)
            self._performance = self._Skill(charisma, performance_proficiency, proficiency_bonus)
            self._persuasion = self._Skill(charisma, persuasion_proficiency, proficiency_bonus)
            self._religion = self._Skill(intelligence, religion_proficiency, proficiency_bonus)
            self._sleight_of_hand = self._Skill(dexterity, sleight_of_hand_proficiency, proficiency_bonus)
            self._stealth = self._Skill(dexterity, stealth_proficiency, proficiency_bonus)
            self._survival = self._Skill(wisdom, survival_proficiency, proficiency_bonus)

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
