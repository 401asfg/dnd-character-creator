from typing import Type

from main.model.character.ability import Ability
from main.model.character.character import Character
from main.model.inttypes.natural_plus import NaturalPlus

# TODO: test skills
# TODO: fix not being recognized by autocomplete or typing


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
) -> Type["Skills"]:
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

    class Skills:
        """
        The character's skills
        """

        class Skill:
            """
            One of the character's skills
            """

            def __init__(self, ability: Ability, proficiency: bool, proficiency_bonus: NaturalPlus):
                """
                Initializes the class

                :param ability: The ability that this skill is bound to
                :param proficiency: Whether or not the character is proficient in this skill
                :param proficiency_bonus: The character's proficiency bonus
                """

                self._ability = ability
                self._proficiency = proficiency
                self._proficiency_bonus = proficiency_bonus

            @property
            def modifier(self) -> int:
                """
                :return: The skill's modifier: ability modifier, plus proficiency_bonus if character is proficient in
                this skill
                """

                return self._ability.modifier + self._proficiency * self._proficiency_bonus.value

            @property
            def proficient(self) -> bool:
                """
                :return: True if character is proficient in this skill; otherwise, false
                """

                return self._proficiency

        def __init__(self, character: Character):
            """
            Initializes this class

            :param character: The character to whom these skills belong
            """

            strength = character.abilities.strength
            dexterity = character.abilities.dexterity
            intelligence = character.abilities.intelligence
            wisdom = character.abilities.wisdom
            charisma = character.abilities.charisma

            pb = NaturalPlus(character.proficiency_bonus)

            self._acrobatics = self.Skill(dexterity, acrobatics_proficiency, pb)
            self._animal_handling = self.Skill(wisdom, animal_handling_proficiency, pb)
            self._arcana = self.Skill(intelligence, arcana_proficiency, pb)
            self._athletics = self.Skill(strength, athletics_proficiency, pb)
            self._deception = self.Skill(charisma, deception_proficiency, pb)
            self._history = self.Skill(intelligence, history_proficiency, pb)
            self._insight = self.Skill(wisdom, insight_proficiency, pb)
            self._intimidation = self.Skill(charisma, intimidation_proficiency, pb)
            self._investigation = self.Skill(intelligence, investigation_proficiency, pb)
            self._medicine = self.Skill(wisdom, medicine_proficiency, pb)
            self._nature = self.Skill(intelligence, nature_proficiency, pb)
            self._perception = self.Skill(wisdom, perception_proficiency, pb)
            self._performance = self.Skill(charisma, performance_proficiency, pb)
            self._persuasion = self.Skill(charisma, persuasion_proficiency, pb)
            self._religion = self.Skill(intelligence, religion_proficiency, pb)
            self._sleight_of_hand = self.Skill(dexterity, sleight_of_hand_proficiency, pb)
            self._stealth = self.Skill(dexterity, stealth_proficiency, pb)
            self._survival = self.Skill(wisdom, survival_proficiency, pb)

        @property
        def acrobatics(self) -> Skill:
            return self._acrobatics

        @property
        def animal_handling(self) -> Skill:
            return self._animal_handling

        @property
        def arcana(self) -> Skill:
            return self._arcana

        @property
        def athletics(self) -> Skill:
            return self._athletics

        @property
        def deception(self) -> Skill:
            return self._deception

        @property
        def history(self) -> Skill:
            return self._history

        @property
        def insight(self) -> Skill:
            return self._insight

        @property
        def intimidation(self) -> Skill:
            return self._intimidation

        @property
        def investigation(self) -> Skill:
            return self._investigation

        @property
        def medicine(self) -> Skill:
            return self._medicine

        @property
        def nature(self) -> Skill:
            return self._nature

        @property
        def perception(self) -> Skill:
            return self._perception

        @property
        def performance(self) -> Skill:
            return self._performance

        @property
        def persuasion(self) -> Skill:
            return self._persuasion

        @property
        def religion(self) -> Skill:
            return self._religion

        @property
        def sleight_of_hand(self) -> Skill:
            return self._sleight_of_hand

        @property
        def stealth(self) -> Skill:
            return self._stealth

        @property
        def survival(self) -> Skill:
            return self._survival

    return Skills
