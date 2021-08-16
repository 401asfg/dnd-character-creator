import unittest

from main.model.character.abilities import generate_character_abilities
from main.model.character.utility.ability_score import AbilityScore
from main.model.character.classes.wizard import Wizard
from main.model.character.races.elves.elf import Elf
from main.model.character.skills import generate_character_skills
from main.model.character.utility.enumerators.skill import Skill
from main.model.int_types.posint import Posint


class SkillsTest(unittest.TestCase):
    def setUp(self):
        self.skills = generate_character_skills((
            Skill.ACROBATICS,
            Skill.ANIMAL_HANDLING,
            Skill.INSIGHT,
            Skill.PERCEPTION,
            Skill.STEALTH
        ))

        abilities = generate_character_abilities(
            strength=AbilityScore(15),
            dexterity=AbilityScore(18),
            constitution=AbilityScore(10),
            intelligence=AbilityScore(5),
            wisdom=AbilityScore(14),
            charisma=AbilityScore(14)
        )

        pb = Posint(2)

        abilities = abilities(
            race=Elf(),
            class_=Wizard,
            proficiency_bonus=pb
        )

        self.skills = self.skills(
            abilities=abilities,
            proficiency_bonus=pb
        )

    def test_modifier(self):
        self.assertEqual(7, self.skills.acrobatics.modifier)
        self.assertEqual(4, self.skills.animal_handling.modifier)
        self.assertEqual(-3, self.skills.arcana.modifier)
        self.assertEqual(2, self.skills.athletics.modifier)
        self.assertEqual(2, self.skills.deception.modifier)
        self.assertEqual(-3, self.skills.history.modifier)
        self.assertEqual(4, self.skills.insight.modifier)
        self.assertEqual(2, self.skills.intimidation.modifier)
        self.assertEqual(-3, self.skills.investigation.modifier)
        self.assertEqual(2, self.skills.medicine.modifier)
        self.assertEqual(-3, self.skills.nature.modifier)
        self.assertEqual(4, self.skills.perception.modifier)
        self.assertEqual(2, self.skills.performance.modifier)
        self.assertEqual(2, self.skills.persuasion.modifier)
        self.assertEqual(-3, self.skills.religion.modifier)
        self.assertEqual(5, self.skills.sleight_of_hand.modifier)
        self.assertEqual(7, self.skills.stealth.modifier)
        self.assertEqual(2, self.skills.survival.modifier)

    def test_proficient(self):
        self.assertEqual(True, self.skills.acrobatics.proficient_in_ability)
        self.assertEqual(True, self.skills.animal_handling.proficient_in_ability)
        self.assertEqual(False, self.skills.arcana.proficient_in_ability)
        self.assertEqual(False, self.skills.athletics.proficient_in_ability)
        self.assertEqual(False, self.skills.deception.proficient_in_ability)
        self.assertEqual(False, self.skills.history.proficient_in_ability)
        self.assertEqual(True, self.skills.insight.proficient_in_ability)
        self.assertEqual(False, self.skills.intimidation.proficient_in_ability)
        self.assertEqual(False, self.skills.investigation.proficient_in_ability)
        self.assertEqual(False, self.skills.medicine.proficient_in_ability)
        self.assertEqual(False, self.skills.nature.proficient_in_ability)
        self.assertEqual(True, self.skills.perception.proficient_in_ability)
        self.assertEqual(False, self.skills.performance.proficient_in_ability)
        self.assertEqual(False, self.skills.persuasion.proficient_in_ability)
        self.assertEqual(False, self.skills.religion.proficient_in_ability)
        self.assertEqual(False, self.skills.sleight_of_hand.proficient_in_ability)
        self.assertEqual(True, self.skills.stealth.proficient_in_ability)
        self.assertEqual(False, self.skills.survival.proficient_in_ability)
