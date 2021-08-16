import unittest

from main.model.character.abilities import generate_character_abilities
from main.model.character.utility.ability_score import AbilityScore
from main.model.character.classes.bard import Bard
from main.model.character.classes.ranger import Ranger
from main.model.character.races.dragonborn import Dragonborn, DraconicAncestry
from main.model.character.races.human import Human
from main.model.character.utility.enumerators.language import Language
from main.model.int_types.posint import Posint


class AbilitiesTest(unittest.TestCase):
    def setUp(self):
        abilities_class = generate_character_abilities(
            strength=AbilityScore(18),
            dexterity=AbilityScore(8),
            constitution=AbilityScore(15),
            intelligence=AbilityScore(18),
            wisdom=AbilityScore(9),
            charisma=AbilityScore(4)
        )

        self.abilities = abilities_class(
            race=Dragonborn(DraconicAncestry.BLUE),
            class_=Bard,
            proficiency_bonus=Posint(3)
        )

        abilities_class = generate_character_abilities(
            strength=AbilityScore(18),
            dexterity=AbilityScore(3),
            constitution=AbilityScore(11),
            intelligence=AbilityScore(15),
            wisdom=AbilityScore(14),
            charisma=AbilityScore(13)
        )

        self.abilitiesB = abilities_class(
            race=Human(Language.ELVISH),
            class_=Ranger,
            proficiency_bonus=Posint(5)
        )

    def test_score(self):
        self.assertEqual(20, self.abilities.strength.score)
        self.assertEqual(8, self.abilities.dexterity.score)
        self.assertEqual(15, self.abilities.constitution.score)
        self.assertEqual(18, self.abilities.intelligence.score)
        self.assertEqual(9, self.abilities.wisdom.score)
        self.assertEqual(4, self.abilities.charisma.score)

        self.assertEqual(19, self.abilitiesB.strength.score)
        self.assertEqual(4, self.abilitiesB.dexterity.score)
        self.assertEqual(12, self.abilitiesB.constitution.score)
        self.assertEqual(16, self.abilitiesB.intelligence.score)
        self.assertEqual(15, self.abilitiesB.wisdom.score)
        self.assertEqual(14, self.abilitiesB.charisma.score)

    def test_modifier(self):
        self.assertEqual(5, self.abilities.strength.modifier)
        self.assertEqual(-1, self.abilities.dexterity.modifier)
        self.assertEqual(2, self.abilities.constitution.modifier)
        self.assertEqual(4, self.abilities.intelligence.modifier)
        self.assertEqual(-1, self.abilities.wisdom.modifier)
        self.assertEqual(-3, self.abilities.charisma.modifier)

        self.assertEqual(4, self.abilitiesB.strength.modifier)
        self.assertEqual(-3, self.abilitiesB.dexterity.modifier)
        self.assertEqual(1, self.abilitiesB.constitution.modifier)
        self.assertEqual(3, self.abilitiesB.intelligence.modifier)
        self.assertEqual(2, self.abilitiesB.wisdom.modifier)
        self.assertEqual(2, self.abilitiesB.charisma.modifier)

    def test_saving_throw(self):
        self.assertEqual(5, self.abilities.strength.saving_throw)
        self.assertEqual(2, self.abilities.dexterity.saving_throw)
        self.assertEqual(2, self.abilities.constitution.saving_throw)
        self.assertEqual(4, self.abilities.intelligence.saving_throw)
        self.assertEqual(-1, self.abilities.wisdom.saving_throw)
        self.assertEqual(0, self.abilities.charisma.saving_throw)

        self.assertEqual(9, self.abilitiesB.strength.saving_throw)
        self.assertEqual(2, self.abilitiesB.dexterity.saving_throw)
        self.assertEqual(1, self.abilitiesB.constitution.saving_throw)
        self.assertEqual(3, self.abilitiesB.intelligence.saving_throw)
        self.assertEqual(2, self.abilitiesB.wisdom.saving_throw)
        self.assertEqual(2, self.abilitiesB.charisma.saving_throw)
