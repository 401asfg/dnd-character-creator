import unittest
from typing import Type

from main.model.character.abilities import generate_character_abilities
from main.model.character.personality import Personality
from main.model.character.utility.ability_score import AbilityScore
from main.model.character.classes.wizard import Wizard
from main.model.character.race import Race
from main.model.character.races.dragonborn import Dragonborn
from main.model.character.races.dwarf import Dwarf
from main.model.character.races.gnome import Gnome
from main.model.character.skills import generate_character_skills
from main.model.character.utility.exceptions.incorrect_character_state_exception import IncorrectCharacterStateException
from main.model.character.alignment import Alignment
from main.model.character.character import Character
from main.model.character.races.elf import Elf
from main.model.character.races.human import Human
from main.model.character.utility.enumerators.size import Size
from main.model.character.utility.enumerators.state import State
from main.model.int_types.natural import Natural
from main.model.int_types.posint import Posint


class CharacterTest(unittest.TestCase):
    def setUp(self):
        self.abilities = generate_character_abilities(
            strength=AbilityScore(13),
            dexterity=AbilityScore(8),
            constitution=AbilityScore(18),
            intelligence=AbilityScore(12),
            wisdom=AbilityScore(15),
            charisma=AbilityScore(15)
        )

        self.skills = generate_character_skills(
            acrobatics_proficiency=True,
            animal_handling_proficiency=False,
            athletics_proficiency=False,
            arcana_proficiency=False,
            deception_proficiency=False,
            history_proficiency=True,
            insight_proficiency=False,
            intimidation_proficiency=False,
            investigation_proficiency=False,
            medicine_proficiency=False,
            nature_proficiency=True,
            perception_proficiency=True,
            performance_proficiency=False,
            persuasion_proficiency=False,
            religion_proficiency=False,
            sleight_of_hand_proficiency=False,
            stealth_proficiency=False,
            survival_proficiency=True
        )

        self.personality = Personality(
            trait_one="Angry",
            trait_two="Cowardly",
            ideal="Hit gym.",
            bond="The gym is good",
            flaw="Afraid to go to the gym"
        )

        self.character = Character(
            "Name",
            "Player Name",
            Wizard,
            Human,
            self.abilities,
            self.skills,
            "Background",
            self.personality,
            Alignment(
                Alignment.Nature.LAWFUL,
                Alignment.Morality.EVIL
            ),
            Natural(22)
        )

    def test_init_no_error(self):
        self.assertEqual(self.character.name, "Name")
        self.assertEqual(self.character.player_name, "Player Name")
        self.assertEqual(self.character.class_name, "Wizard")
        self.assertEqual(self.character.race_name, "Human")

        self.assertEqual(self.character.abilities.strength.score, 14)
        self.assertEqual(self.character.abilities.dexterity.score, 9)
        self.assertEqual(self.character.abilities.constitution.score, 19)
        self.assertEqual(self.character.abilities.intelligence.score, 13)
        self.assertEqual(self.character.abilities.wisdom.score, 16)
        self.assertEqual(self.character.abilities.charisma.score, 16)

        self.assertEqual(self.character.abilities.strength.saving_throw, 2)
        self.assertEqual(self.character.abilities.dexterity.saving_throw, -1)
        self.assertEqual(self.character.abilities.constitution.saving_throw, 4)
        self.assertEqual(self.character.abilities.intelligence.saving_throw, 3)
        self.assertEqual(self.character.abilities.wisdom.saving_throw, 5)
        self.assertEqual(self.character.abilities.charisma.saving_throw, 3)

        self.assertEqual(self.character.skills.acrobatics.modifier, 1)
        self.assertEqual(self.character.skills.animal_handling.modifier, 3)
        self.assertEqual(self.character.skills.arcana.modifier, 1)
        self.assertEqual(self.character.skills.athletics.modifier, 2)
        self.assertEqual(self.character.skills.deception.modifier, 3)
        self.assertEqual(self.character.skills.history.modifier, 3)
        self.assertEqual(self.character.skills.insight.modifier, 3)
        self.assertEqual(self.character.skills.intimidation.modifier, 3)
        self.assertEqual(self.character.skills.investigation.modifier, 1)
        self.assertEqual(self.character.skills.medicine.modifier, 3)
        self.assertEqual(self.character.skills.nature.modifier, 3)
        self.assertEqual(self.character.skills.perception.modifier, 5)
        self.assertEqual(self.character.skills.performance.modifier, 3)
        self.assertEqual(self.character.skills.persuasion.modifier, 3)
        self.assertEqual(self.character.skills.religion.modifier, 1)
        self.assertEqual(self.character.skills.sleight_of_hand.modifier, -1)
        self.assertEqual(self.character.skills.stealth.modifier, -1)
        self.assertEqual(self.character.skills.survival.modifier, 5)

        self.assertEqual(self.character.purse.copper_coins, 0)
        self.assertEqual(self.character.purse.silver_coins, 0)
        self.assertEqual(self.character.purse.electrum_coins, 0)
        self.assertEqual(self.character.purse.gold_coins, 0)
        self.assertEqual(self.character.purse.platinum_coins, 0)

        self.assertEqual(self.character.background, "Background")
        self.assertEqual(self.character.state, State.ALIVE)
        self.assertEqual(self.character.passive_wisdom, 15)
        self.assertEqual(self.character.inspiration, 0)
        self.assertEqual(self.character.hit_points, 10)
        self.assertEqual(self.character.temporary_hp, 0)
        self.assertEqual(self.character.max_hit_points, 10)
        self.assertEqual(self.character.successful_death_saves, 0)
        self.assertEqual(self.character.failed_death_saves, 0)

        nature = self.character.alignment.nature
        self.assertEqual(nature, Alignment.Nature.LAWFUL)
        morality = self.character.alignment.morality
        self.assertEqual(morality, Alignment.Morality.EVIL)

        self.assertEqual(self.character.experience_points, 0)
        self.assertEqual(self.character.level, 1)
        self.assertEqual(self.character.proficiency_bonus, 2)
        self.assertEqual(self.character.age, 22)
        self.assertEqual(self.character.size, Size.MEDIUM)
        self.assertEqual(self.character.speed, 30)

        self.assertEqual(210, self.character.inventory.max_weight)
        self.assertEqual(0, self.character.inventory.weight)
        self.assertEqual(0, len(self.character.inventory))

        self.assertEqual("Angry", self.character.personality.trait_one)
        self.assertEqual("Cowardly", self.character.personality.trait_two)
        self.assertEqual("Hit gym.", self.character.personality.ideal)
        self.assertEqual("The gym is good", self.character.personality.bond)
        self.assertEqual("Afraid to go to the gym", self.character.personality.flaw)

    def test_init_errors(self):
        try:
            Character(
                "Name",
                "Player Name",
                Wizard,
                Elf,
                self.abilities,
                self.skills,
                "Background",
                self.personality,
                Alignment(
                    Alignment.Nature.LAWFUL,
                    Alignment.Morality.GOOD
                ),
                Natural(22)
            )
        except ValueError:
            pass

    def test_gain_exp(self):
        def assert_gain_exp(gain_exp: int, expected_exp: int, expected_level: int, expected_pb: int):
            """
            Assert that calling the character's gain_exp produces the expected results

            :param gain_exp: The amount of exp to gain
            :param expected_exp: The amount of exp the character should have after gaining exp
            :param expected_level: The level the character should be at after gaining exp
            :param expected_pb: The proficiency bonus the character should have after gaining exp
            """

            self.character.gain_exp(gain_exp)
            self.assertEqual(self.character.experience_points, expected_exp)
            self.assertEqual(self.character.level, expected_level)
            self.assertEqual(self.character.proficiency_bonus, expected_pb)

        assert_gain_exp(300, 300, 2, 2)
        assert_gain_exp(100, 400, 2, 2)
        assert_gain_exp(500, 900, 3, 2)
        assert_gain_exp(5600, 6500, 5, 3)
        assert_gain_exp(103500, 110000, 12, 4)

    def test_death_save_success(self):
        self.character.take_damage(Posint(self.character.max_hit_points))
        downed = State.DOWNED

        self._assert_death_save(True, 1, 0, downed)
        self._assert_death_save(True, 2, 0, downed)
        self._assert_death_save(False, 2, 1, downed)
        self._assert_death_save(False, 2, 2, downed)
        self._assert_death_save(True, 0, 0, State.ALIVE)
        self.assertEqual(self.character.hit_points, 1)

    def test_death_save_fail(self):
        self.character.take_damage(Posint(self.character.max_hit_points))
        downed = State.DOWNED

        self._assert_death_save(True, 1, 0, downed)
        self._assert_death_save(False, 1, 1, downed)
        self._assert_death_save(False, 1, 2, downed)
        self._assert_death_save(False, 0, 0, State.DEAD)
        self.assertEqual(self.character.hit_points, 0)

    def test_death_save_error(self):
        def assert_death_save_error(success: bool, character_state: str):
            """
            Assert that the death save produced an error

            :param success: Whether or not the death save was successful
            :param character_state: The state the character should be in when the death save is made
            """

            death_save_type = "failed"

            if success:
                death_save_type = "successful"

            try:
                self.character.death_save(success)
                fail_msg = "Shouldn't be able to make a "
                fail_msg += death_save_type
                fail_msg += " death save when in "
                fail_msg += " state"
                self.fail(fail_msg)
            except IncorrectCharacterStateException:
                pass

        assert_death_save_error(True, "alive")
        assert_death_save_error(False, "alive")

        self.character.take_damage(Posint(self.character.max_hit_points))

        for _ in range(self.character.MAX_FAILED_DEATH_SAVES):
            self.character.death_save(False)

        assert_death_save_error(True, "dead")
        assert_death_save_error(False, "dead")

    def test_gain_inspiration(self):
        def assert_gain_inspiration(expected_inspiration: int):
            """
            Asserts that after the character calls gain_inspiration, the character has the given expected_inspiration

            :param expected_inspiration: The amount of inspiration the character is expected to have
            """

            self.character.gain_inspiration()
            self.assertEqual(expected_inspiration, self.character.inspiration)

        assert_gain_inspiration(1)
        assert_gain_inspiration(2)
        assert_gain_inspiration(3)
        assert_gain_inspiration(4)
        assert_gain_inspiration(5)
        assert_gain_inspiration(6)
        assert_gain_inspiration(7)

    def test_spend_inspiration(self):
        def assert_spend_inspiration(expected_inspiration: int):
            """
            Asserts that after the character calls spend_inspiration, the character has the given expected_inspiration

            :param expected_inspiration: The amount of inspiration the character is expected to have
            """

            self.character.spend_inspiration()
            self.assertEqual(expected_inspiration, self.character.inspiration)

        def assert_spend_error():
            """
            Asserts that calling spend_inspiration causes an error to be raised
            """

            try:
                self.character.spend_inspiration()
                self.fail("Spending inspiration with no inspiration left should have resulted in a ValueError.")
            except ValueError:
                pass

        assert_spend_error()
        self.character.gain_inspiration()
        self.character.gain_inspiration()
        self.character.gain_inspiration()
        self.character.gain_inspiration()
        self.character.gain_inspiration()

        assert_spend_inspiration(4)
        assert_spend_inspiration(3)
        assert_spend_inspiration(2)
        assert_spend_inspiration(1)
        assert_spend_inspiration(0)

        assert_spend_error()
        self.character.gain_inspiration()
        self.character.gain_inspiration()
        assert_spend_inspiration(1)
        assert_spend_inspiration(0)
        assert_spend_error()

    def test_take_damage_and_heal(self):
        def assert_heal(delta: int, expected: int):
            """
            Asserts that after healing the character by the given delta, the character has the expected hp
            """

            self.character.heal(Posint(delta))
            self.assertEqual(self.character.hit_points, expected)

        def assert_take_damage(delta: int, expected: int):
            """
            Asserts that after hurting the character by the given delta, the character has the expected hp
            """

            self.character.take_damage(Posint(delta))
            self.assertEqual(self.character.hit_points, expected)

        assert_take_damage(5, 5)
        self.assertEqual(self.character.state, State.ALIVE)
        assert_heal(1, 6)
        assert_heal(10, self.character.max_hit_points)
        assert_take_damage(2, self.character.max_hit_points - 2)
        assert_heal(100, self.character.max_hit_points)
        assert_take_damage(3, self.character.max_hit_points - 3)
        assert_heal(3, self.character.max_hit_points)
        assert_take_damage(2, self.character.max_hit_points - 2)
        self.assertEqual(self.character.state, State.ALIVE)
        assert_take_damage(1000, 0)
        self.assertEqual(self.character.state, State.DOWNED)

        def assert_take_damage_error(hp: int):
            """
            Asserts that attempting to hurt the character raises an error
            """

            try:
                self.character.take_damage(Posint(hp))
                self.fail("Should not be able to change character hp while it is downed.")
            except IncorrectCharacterStateException:
                self.assertEqual(self.character.hit_points, 0)

        def assert_heal_error(hp: int):
            """
            Asserts that attempting to heal the character raises an error
            """

            try:
                self.character.heal(Posint(hp))
                self.fail("Should not be able to change character hp while it is downed.")
            except IncorrectCharacterStateException:
                self.assertEqual(self.character.hit_points, 0)

        assert_take_damage_error(5)
        assert_heal_error(65)
        assert_take_damage_error(6)
        assert_take_damage_error(1)
        assert_heal_error(9)
        assert_take_damage_error(23)
        assert_heal_error(1)
        assert_heal_error(32)

        def make_death_saves(success: bool, num: int):
            """
            Make num death saves to either kill or save the character

            :param success: Whether the death save was a success or not
            :param num: The number of death saves to make; should be equal to the max successful if success is true, or
            max failure if success is false
            """

            for _ in range(num):
                self.character.death_save(success)

        make_death_saves(True, self.character.MAX_SUCCESSFUL_DEATH_SAVES)

        self.assertEqual(1, self.character.hit_points)
        assert_take_damage(1, 0)
        self.assertEqual(self.character.state, State.DOWNED)

        make_death_saves(False, self.character.MAX_FAILED_DEATH_SAVES)

        assert_heal_error(34)
        assert_heal_error(3)

        assert_take_damage_error(5)
        assert_heal_error(84)
        assert_heal_error(4)

        assert_take_damage_error(9)
        assert_take_damage_error(65)

    def test_set_temporary_hp(self):
        self.character.set_temporary_hp(Natural(3))
        self.assertEqual(3, self.character.temporary_hp)

        self.character.set_temporary_hp(Natural(21))
        self.assertEqual(21, self.character.temporary_hp)

        self.character.set_temporary_hp(Natural(342))
        self.assertEqual(342, self.character.temporary_hp)

        self.character.set_temporary_hp(Natural(1))
        self.assertEqual(1, self.character.temporary_hp)

        self.character.set_temporary_hp(Natural(83))
        self.assertEqual(83, self.character.temporary_hp)

    def test_take_temporary_hp_damage(self):
        def set_temp_hp(temp_hp: int, expected_hp: int):
            """
            Sets the character's temp hp and asserts that the character's temp hp equals the set value, and that the
            character's hp equals the expected_hp

            :param temp_hp: The value to set the temp hp to and the expected temp hp
            :param expected_hp: The expected hp after the temp hp is set
            """

            self.character.set_temporary_hp(Natural(temp_hp))
            self.assertEqual(expected_hp, self.character.hit_points)
            self.assertEqual(temp_hp, self.character.temporary_hp)

        def assert_hp_after_damage(dmg: int, expected_hp: int, expected_temp_hp: int):
            """
            Asserts that after the character takes the given dmg, the character has the expected_hp and the
            expected_temp_hp

            :param dmg: The damage the character takes
            :param expected_hp: The expected hp of the character after it takes damage
            :param expected_temp_hp: The expected temporary hp of the character after it takes damage
            """

            self.character.take_damage(Posint(dmg))
            self.assertEqual(expected_hp, self.character.hit_points)
            self.assertEqual(expected_temp_hp, self.character.temporary_hp)

        set_temp_hp(15, 10)
        assert_hp_after_damage(5, 10, 10)
        assert_hp_after_damage(8, 10, 2)
        set_temp_hp(7, 10)
        assert_hp_after_damage(4, 10, 3)
        assert_hp_after_damage(3, 10, 0)
        set_temp_hp(3, 10)
        assert_hp_after_damage(6, 7, 0)
        assert_hp_after_damage(2, 5, 0)

        self.character.heal(Posint(self.character.max_hit_points))
        set_temp_hp(6, 10)
        assert_hp_after_damage(6, 10, 0)
        assert_hp_after_damage(4, 6, 0)
        set_temp_hp(3, 6)
        assert_hp_after_damage(1, 6, 2)
        assert_hp_after_damage(3, 5, 0)

    def test_level(self):
        def assert_level(exp_delta: int, expected_level: int):
            """
            Asserts that the adding the given exp_delta to the character results in the given expected_level

            :param exp_delta: The exp to give to the character
            :param expected_level: The expected level of the character after giving him the exp_delta
            """

            self.character.gain_exp(exp_delta)
            self.assertEqual(expected_level, self.character.level)

        self.assertEqual(1, self.character.level)
        assert_level(300, 2)
        assert_level(150, 2)
        assert_level(450, 3)
        assert_level(100, 3)
        assert_level(1800, 4)
        assert_level(3700, 5)

    def test_passive_wisdom(self):
        self.assertEqual(self.character.passive_wisdom, 15)

        abilitiesB = generate_character_abilities(
            strength=AbilityScore(13),
            dexterity=AbilityScore(8),
            constitution=AbilityScore(18),
            intelligence=AbilityScore(12),
            wisdom=AbilityScore(10),
            charisma=AbilityScore(15)
        )

        skillsB = generate_character_skills(
            acrobatics_proficiency=True,
            animal_handling_proficiency=False,
            athletics_proficiency=False,
            arcana_proficiency=False,
            deception_proficiency=False,
            history_proficiency=True,
            insight_proficiency=False,
            intimidation_proficiency=False,
            investigation_proficiency=False,
            medicine_proficiency=False,
            nature_proficiency=True,
            perception_proficiency=False,
            performance_proficiency=False,
            persuasion_proficiency=False,
            religion_proficiency=False,
            sleight_of_hand_proficiency=False,
            stealth_proficiency=False,
            survival_proficiency=True
        )

        characterB = Character(
            "Name",
            "Player Name",
            Wizard,
            Human,
            abilitiesB,
            skillsB,
            "Background",
            self.personality,
            Alignment(
                Alignment.Nature.LAWFUL,
                Alignment.Morality.EVIL
            ),
            Natural(22)
        )

        self.assertEqual(characterB.passive_wisdom, 10)

    def test_proficiency_bonus(self):
        abilitiesB = generate_character_abilities(
            strength=AbilityScore(13),
            dexterity=AbilityScore(8),
            constitution=AbilityScore(18),
            intelligence=AbilityScore(12),
            wisdom=AbilityScore(10),
            charisma=AbilityScore(15)
        )

        skillsB = generate_character_skills(
            acrobatics_proficiency=True,
            animal_handling_proficiency=False,
            athletics_proficiency=False,
            arcana_proficiency=False,
            deception_proficiency=False,
            history_proficiency=True,
            insight_proficiency=False,
            intimidation_proficiency=False,
            investigation_proficiency=False,
            medicine_proficiency=False,
            nature_proficiency=True,
            perception_proficiency=False,
            performance_proficiency=False,
            persuasion_proficiency=False,
            religion_proficiency=False,
            sleight_of_hand_proficiency=False,
            stealth_proficiency=False,
            survival_proficiency=True
        )

        characterB = Character(
            "Name",
            "Player Name",
            Wizard,
            Human,
            abilitiesB,
            skillsB,
            "Background",
            self.personality,
            Alignment(
                Alignment.Nature.LAWFUL,
                Alignment.Morality.EVIL
            ),
            Natural(22)
        )

        def assert_proficiency_bonus(exp_delta: int, expected_level: int, expected_pb: int):
            """
            Asserts that a character with the amount of exp after it gained the given exp_delta has the expected_pb and
            expected_lvel

            :param exp_delta: The exp to give to the character
            :param expected_level: The expected level of the character
            :param expected_pb: The expected proficiency bonus of the character
            """

            characterB.gain_exp(exp_delta)
            self.assertEqual(expected_level, characterB.level)
            self.assertEqual(characterB.proficiency_bonus, expected_pb)

        assert_proficiency_bonus(0, 1, 2)
        assert_proficiency_bonus(300, 2, 2)
        assert_proficiency_bonus(600, 3, 2)
        assert_proficiency_bonus(1800, 4, 2)
        assert_proficiency_bonus(3800, 5, 3)
        assert_proficiency_bonus(7500, 6, 3)
        assert_proficiency_bonus(9000, 7, 3)
        assert_proficiency_bonus(11000, 8, 3)
        assert_proficiency_bonus(14000, 9, 4)
        assert_proficiency_bonus(16000, 10, 4)
        assert_proficiency_bonus(21000, 11, 4)
        assert_proficiency_bonus(15000, 12, 4)
        assert_proficiency_bonus(20000, 13, 5)
        assert_proficiency_bonus(20000, 14, 5)
        assert_proficiency_bonus(25000, 15, 5)
        assert_proficiency_bonus(30000, 16, 5)
        assert_proficiency_bonus(30000, 17, 6)
        assert_proficiency_bonus(40000, 18, 6)
        assert_proficiency_bonus(40000, 19, 6)
        assert_proficiency_bonus(50000, 20, 6)

    def test_size(self):
        def assert_size(race: Type[Race], alignment: Alignment, expected_size: Size):
            """
            Asserts that a character of the given race has the size

            :param race: The race of the character
            :param alignment: The alignment of the character
            :param expected_size: The expected size of the character
            """

            abilitiesB = generate_character_abilities(
                strength=AbilityScore(13),
                dexterity=AbilityScore(8),
                constitution=AbilityScore(18),
                intelligence=AbilityScore(12),
                wisdom=AbilityScore(10),
                charisma=AbilityScore(15)
            )

            skillsB = generate_character_skills(
                acrobatics_proficiency=True,
                animal_handling_proficiency=False,
                athletics_proficiency=False,
                arcana_proficiency=False,
                deception_proficiency=False,
                history_proficiency=True,
                insight_proficiency=False,
                intimidation_proficiency=False,
                investigation_proficiency=False,
                medicine_proficiency=False,
                nature_proficiency=True,
                perception_proficiency=False,
                performance_proficiency=False,
                persuasion_proficiency=False,
                religion_proficiency=False,
                sleight_of_hand_proficiency=False,
                stealth_proficiency=False,
                survival_proficiency=True
            )

            characterB = Character(
                "Name",
                "Player Name",
                Wizard,
                race,
                abilitiesB,
                skillsB,
                "Background",
                self.personality,
                alignment,
                Natural(22)
            )

            self.assertEqual(characterB.size, expected_size)

        assert_size(
            Dragonborn,
            Alignment(
                Alignment.Nature.CHAOTIC,
                Alignment.Morality.EVIL
            ),
            Size.MEDIUM
        )

        assert_size(
            Dwarf,
            Alignment(
                Alignment.Nature.LAWFUL,
                Alignment.Morality.GOOD
            ),
            Size.MEDIUM
        )

        assert_size(
            Elf,
            Alignment(
                Alignment.Nature.CHAOTIC,
                Alignment.Morality.GOOD
            ),
            Size.MEDIUM
        )

        assert_size(
            Gnome,
            Alignment(
                Alignment.Nature.LAWFUL,
                Alignment.Morality.NEUTRAL
            ),
            Size.SMALL
        )

        assert_size(
            Human,
            Alignment(
                Alignment.Nature.CHAOTIC,
                Alignment.Morality.EVIL
            ),
            Size.MEDIUM
        )

    def test_speed(self):
        def assert_speed(race: Type[Race], alignment: Alignment, expected_speed: int):
            """
            Asserts that a character of the given race has the speed

            :param race: The race of the character
            :param alignment: The alignment of the character
            :param expected_speed: The expected speed of the character
            """

            abilitiesB = generate_character_abilities(
                strength=AbilityScore(13),
                dexterity=AbilityScore(8),
                constitution=AbilityScore(18),
                intelligence=AbilityScore(12),
                wisdom=AbilityScore(10),
                charisma=AbilityScore(15)
            )

            skillsB = generate_character_skills(
                acrobatics_proficiency=True,
                animal_handling_proficiency=False,
                athletics_proficiency=False,
                arcana_proficiency=False,
                deception_proficiency=False,
                history_proficiency=True,
                insight_proficiency=False,
                intimidation_proficiency=False,
                investigation_proficiency=False,
                medicine_proficiency=False,
                nature_proficiency=True,
                perception_proficiency=False,
                performance_proficiency=False,
                persuasion_proficiency=False,
                religion_proficiency=False,
                sleight_of_hand_proficiency=False,
                stealth_proficiency=False,
                survival_proficiency=True
            )

            characterB = Character(
                "Name",
                "Player Name",
                Wizard,
                race,
                abilitiesB,
                skillsB,
                "Background",
                self.personality,
                alignment,
                Natural(22)
            )

            self.assertEqual(characterB.speed, expected_speed)

        assert_speed(
            Dragonborn,
            Alignment(
                Alignment.Nature.CHAOTIC,
                Alignment.Morality.EVIL
            ),
            30
        )

        assert_speed(
            Dwarf,
            Alignment(
                Alignment.Nature.LAWFUL,
                Alignment.Morality.GOOD
            ),
            30
        )

        assert_speed(
            Elf,
            Alignment(
                Alignment.Nature.CHAOTIC,
                Alignment.Morality.GOOD
            ),
            30
        )

        assert_speed(
            Gnome,
            Alignment(
                Alignment.Nature.LAWFUL,
                Alignment.Morality.NEUTRAL
            ),
            25
        )

        assert_speed(
            Human,
            Alignment(
                Alignment.Nature.CHAOTIC,
                Alignment.Morality.EVIL
            ),
            30
        )

    def _assert_death_save(
            self,
            success: bool,
            expected_successful_count: int,
            expected_failed_count: int,
            expected_state: State
    ):
        """
        Assert that the by making a death save, the character produces the expected values

        :param success: Whether or not the death save was successful
        :param expected_successful_count: The expected value of the character's successful death save count after the
        death save
        :param expected_failed_count: The expected value of the character's failed death save count after the death save
        :param expected_state: The expected value of the character's state after the death save
        """

        self.character.death_save(success)
        self.assertEqual(self.character.successful_death_saves, expected_successful_count)
        self.assertEqual(self.character.failed_death_saves, expected_failed_count)
        self.assertEqual(self.character.state, expected_state)
