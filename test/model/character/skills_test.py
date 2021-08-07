import unittest

from main.model.character.abilities import generate_character_abilities
from main.model.character.personality import Personality
from main.model.character.utility.ability_score import AbilityScore
from main.model.character.alignment import Alignment
from main.model.character.character import Character
from main.model.character.classes.wizard import Wizard
from main.model.character.races.elf import Elf
from main.model.character.skills import generate_character_skills
from main.model.int_types.natural import Natural


class SkillsTest(unittest.TestCase):
    def setUp(self):
        skills = generate_character_skills(
            acrobatics_proficiency=True,
            animal_handling_proficiency=True,
            arcana_proficiency=False,
            athletics_proficiency=False,
            deception_proficiency=False,
            history_proficiency=False,
            insight_proficiency=True,
            intimidation_proficiency=False,
            investigation_proficiency=False,
            medicine_proficiency=False,
            nature_proficiency=False,
            perception_proficiency=True,
            performance_proficiency=False,
            persuasion_proficiency=False,
            religion_proficiency=False,
            sleight_of_hand_proficiency=False,
            stealth_proficiency=True,
            survival_proficiency=False
        )

        abilities = generate_character_abilities(
            strength=AbilityScore(15),
            dexterity=AbilityScore(18),
            constitution=AbilityScore(10),
            intelligence=AbilityScore(5),
            wisdom=AbilityScore(14),
            charisma=AbilityScore(14)
        )

        self.character = Character(
            name="Mike-El",
            player_name="Mike",
            class_=Wizard,
            race=Elf,
            abilities=abilities,
            skills=skills,
            background="Beggar",
            personality=Personality("", "", "", "", ""),
            alignment=Alignment(
                Alignment.Nature.NEUTRAL,
                Alignment.Morality.NEUTRAL
            ),
            age=Natural(21)
        )

    def test_modifier(self):
        self.assertEqual(7, self.character.skills.acrobatics.modifier)
        self.assertEqual(4, self.character.skills.animal_handling.modifier)
        self.assertEqual(-3, self.character.skills.arcana.modifier)
        self.assertEqual(2, self.character.skills.athletics.modifier)
        self.assertEqual(2, self.character.skills.deception.modifier)
        self.assertEqual(-3, self.character.skills.history.modifier)
        self.assertEqual(4, self.character.skills.insight.modifier)
        self.assertEqual(2, self.character.skills.intimidation.modifier)
        self.assertEqual(-3, self.character.skills.investigation.modifier)
        self.assertEqual(2, self.character.skills.medicine.modifier)
        self.assertEqual(-3, self.character.skills.nature.modifier)
        self.assertEqual(4, self.character.skills.perception.modifier)
        self.assertEqual(2, self.character.skills.performance.modifier)
        self.assertEqual(2, self.character.skills.persuasion.modifier)
        self.assertEqual(-3, self.character.skills.religion.modifier)
        self.assertEqual(5, self.character.skills.sleight_of_hand.modifier)
        self.assertEqual(7, self.character.skills.stealth.modifier)
        self.assertEqual(2, self.character.skills.survival.modifier)

    def test_proficient(self):
        self.assertEqual(True, self.character.skills.acrobatics.proficient)
        self.assertEqual(True, self.character.skills.animal_handling.proficient)
        self.assertEqual(False, self.character.skills.arcana.proficient)
        self.assertEqual(False, self.character.skills.athletics.proficient)
        self.assertEqual(False, self.character.skills.deception.proficient)
        self.assertEqual(False, self.character.skills.history.proficient)
        self.assertEqual(True, self.character.skills.insight.proficient)
        self.assertEqual(False, self.character.skills.intimidation.proficient)
        self.assertEqual(False, self.character.skills.investigation.proficient)
        self.assertEqual(False, self.character.skills.medicine.proficient)
        self.assertEqual(False, self.character.skills.nature.proficient)
        self.assertEqual(True, self.character.skills.perception.proficient)
        self.assertEqual(False, self.character.skills.performance.proficient)
        self.assertEqual(False, self.character.skills.persuasion.proficient)
        self.assertEqual(False, self.character.skills.religion.proficient)
        self.assertEqual(False, self.character.skills.sleight_of_hand.proficient)
        self.assertEqual(True, self.character.skills.stealth.proficient)
        self.assertEqual(False, self.character.skills.survival.proficient)
