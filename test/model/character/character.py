import unittest

from main.model.exceptions.incorrect_character_state_exception import IncorrectCharacterStateException
from main.model.character.alignment import Alignment
from main.model.character.character import Character
from main.model.character.races.elf import Elf
from main.model.character.races.human import Human
from main.model.character.size import Size
from main.model.character.state import State


class CharacterTest(unittest.TestCase):
    def setUp(self):
        self.character = Character(
            "Name",
            "Player Name",
            Wizard,
            Human,
            2,
            "Background",
            Alignment(
                Alignment.Nature.LAWFUL,
                Alignment.Morality.EVIL
            ),
            22
        )

    def test_init_no_error(self):
        self.assertEqual(self.character.name, "Name")
        self.assertEqual(self.character.player_name, "Player Name")
        self.assertEqual(self.character.class_name, "Wizard")
        self.assertEqual(self.character.race_name, "Human")
        self.assertEqual(self.character.background, "Background")
        self.assertEqual(self.character.state, State.ALIVE)
        self.assertEqual(self.character.hit_points, None)   # TODO: implement
        self.assertEqual(self.character.successful_death_saves, 0)
        self.assertEqual(self.character.failed_death_saves, 0)

        nature = self.character.alignment.nature
        morality = self.character.alignment.morality

        self.assertEqual(nature, Alignment.Nature.LAWFUL)
        self.assertEqual(morality, Alignment.Morality.EVIL)

        self.assertEqual(self.character.experience_points, 300)
        self.assertEqual(self.character.level, 2)
        self.assertEqual(self.character.proficiency_bonus, 2)
        self.assertEqual(self.character.age, 22)
        self.assertEqual(self.character.size, Size.MEDIUM)
        self.assertEqual(self.character.speed, 30)

    def test_init_errors(self):
        # Level is Unreachable
        try:
            Character(
                "Name",
                "Player Name",
                Wizard,
                Human,
                22,
                "Background",
                Alignment(
                    Alignment.Nature.LAWFUL,
                    Alignment.Morality.EVIL
                ),
                22
            )
        except ValueError:
            pass

        # Inappropriate alignment
        try:
            Character(
                "Name",
                "Player Name",
                Wizard,
                Elf,
                2,
                "Background",
                Alignment(
                    Alignment.Nature.LAWFUL,
                    Alignment.Morality.GOOD
                ),
                22
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

        assert_gain_exp(100, 400, 2, 2)
        assert_gain_exp(500, 900, 3, 2)
        assert_gain_exp(5600, 6500, 5, 3)
        assert_gain_exp(103500, 110000, 12, 4)

    def test_hit_points_over_max_and_to_zero(self):
        hp = self.character.hit_points
        self.character.hit_points -= 1
        self.assertEqual(self.character.hit_points, hp - 1)
        self.assertEqual(self.character.state, State.ALIVE)

        self.character.hit_points = self.character.max_hit_points + 4
        self.assertEqual(self.character.hit_points, self.character.max_hit_points)
        self.assertEqual(self.character.state, State.ALIVE)

        self.character.hit_points = 0
        self.assertEqual(self.character.hit_points, 0)
        self.assertEqual(self.character.state, State.DOWNED)

        try:
            self.character.hit_points += 1
            self.fail("Shouldn't be able to change hit_points at 0")
        except IncorrectCharacterStateException:
            pass

    def test_hit_points_past_zero(self):
        self.character.hit_points = -3
        self.assertEqual(self.character.hit_points, 0)
        self.assertEqual(self.character.state, State.DOWNED)

        try:
            self.character.hit_points += 1
            self.fail("Shouldn't be able to change hit_points at 0")
        except IncorrectCharacterStateException:
            pass

    def test_death_save_success(self):
        self.character.hit_points = 0
        downed = State.DOWNED

        self._assert_death_save(True, 1, 0, downed)
        self._assert_death_save(True, 2, 0, downed)
        self._assert_death_save(False, 2, 1, downed)
        self._assert_death_save(False, 2, 2, downed)
        self._assert_death_save(True, 0, 0, State.ALIVE)

    def test_death_save_fail(self):
        self.character.hit_points = 0
        downed = State.DOWNED

        self._assert_death_save(True, 1, 0, downed)
        self._assert_death_save(False, 1, 1, downed)
        self._assert_death_save(False, 1, 2, downed)
        self._assert_death_save(False, 0, 0, State.DEAD)

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

        self.character.hit_points = 0

        for _ in range(self.character.MAX_FAILED_DEATH_SAVES):
            self.character.death_save(False)

        assert_death_save_error(True, "dead")
        assert_death_save_error(False, "dead")

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
