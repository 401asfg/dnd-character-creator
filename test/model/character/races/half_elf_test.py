from main.model.character.alignment import Alignment
from main.model.character.races.half_elf import HalfElf
from main.model.character.utility.enumerators.ability import Ability
from main.model.character.utility.enumerators.language import Language
from main.model.character.utility.enumerators.size import Size
from main.model.character.utility.enumerators.skill import Skill
from main.model.character.utility.helper_modules.common_race_collection_items import get_language
from test_helper.race_test_helper import RaceTestHelper


class HalfElfTest(RaceTestHelper):
    def setUp(self) -> None:
        self.race = HalfElf(
            ability_bonus_one=Ability.STRENGTH,
            ability_bonus_two=Ability.DEXTERITY,
            skill_proficiency_one=Skill.ARCANA,
            skill_proficiency_two=Skill.DECEPTION,
            language=Language.HALFLING
        )

    def test_init(self):
        super()._test_init(
            expected_name="Half-Elf",
            expected_size=Size.MEDIUM,
            expected_speed=30,
            expected_hp_bonus=0,
            expected_min_adult_age=20,
            expected_life_expectancy=180,
            expected_acceptable_alignment_natures=(
                Alignment.Nature.NEUTRAL,
                Alignment.Nature.CHAOTIC
            ),
            expected_acceptable_alignment_moralities=(
                Alignment.Morality.GOOD,
                Alignment.Morality.NEUTRAL,
                Alignment.Morality.EVIL
            ),
            expected_trait_names=(
                "Darkvision",
                "Fey Ancestry"
            ),
            expected_other_proficiency_names=(
                "Common Language",
                "Elvish Language",
                "Halfling Language"
            )
        )

    def test_init_abilities(self):
        def assert_abilities(ability_one: Ability, ability_two: Ability):
            """
            Asserts that creating a half elf with the given abilities (in both scenarios: ability_bonus_one=ability_one,
            ability_bonus_two=ability_two and ability_bonus_one=ability_two, ability_bonus_two=ability_one) doesn't
            result in an error and the half elf has the bonuses

            :param ability_one: An ability to given a half elf that doesn't cause it to raise an error
            :param ability_two: An ability to given a half elf that doesn't cause it to raise an error
            """

            def assert_got_bonus(half_elf: HalfElf):
                """
                Asserts that the given half_elf gained ability_one and ability_two and no other (aside from CHARISMA)

                :param half_elf: The half elf that was given ability_one and ability_two
                """

                self.assertEqual(1, half_elf.get_ability_bonus(ability_one))
                self.assertEqual(1, half_elf.get_ability_bonus(ability_two))

                for ability in Ability:
                    if ability != ability_one and ability != ability_two and ability != Ability.CHARISMA:
                        self.assertEqual(0, half_elf.get_ability_bonus(ability))
                    elif ability == Ability.CHARISMA:
                        self.assertEqual(2, half_elf.get_ability_bonus(ability))

            try:
                half_elf = HalfElf(
                    ability_bonus_one=ability_one,
                    ability_bonus_two=ability_two,
                    skill_proficiency_two=Skill.INSIGHT,
                    skill_proficiency_one=Skill.INVESTIGATION,
                    language=Language.DRACONIC
                )

                assert_got_bonus(half_elf)
            except ValueError:
                self.fail("The given ability combo should not have caused the half elf init to raise an error.")

            try:
                half_elf = HalfElf(
                    ability_bonus_one=ability_two,
                    ability_bonus_two=ability_one,
                    skill_proficiency_two=Skill.SURVIVAL,
                    skill_proficiency_one=Skill.HISTORY,
                    language=Language.SYLVAN
                )

                assert_got_bonus(half_elf)
            except ValueError:
                self.fail("The given ability combo should not have caused the half elf init to raise an error.")

        assert_abilities(Ability.STRENGTH, Ability.DEXTERITY)
        assert_abilities(Ability.STRENGTH, Ability.CONSTITUTION)
        assert_abilities(Ability.STRENGTH, Ability.INTELLIGENCE)
        assert_abilities(Ability.STRENGTH, Ability.WISDOM)

        assert_abilities(Ability.DEXTERITY, Ability.CONSTITUTION)
        assert_abilities(Ability.DEXTERITY, Ability.INTELLIGENCE)
        assert_abilities(Ability.DEXTERITY, Ability.WISDOM)

        assert_abilities(Ability.CONSTITUTION, Ability.INTELLIGENCE)
        assert_abilities(Ability.CONSTITUTION, Ability.WISDOM)

        assert_abilities(Ability.INTELLIGENCE, Ability.WISDOM)

    def test_init_abilities_error(self):
        def assert_abilities_error(ability_one: Ability, ability_two: Ability):
            """
            Asserts that the given ability combo results in an error; tests cases: ability_bonus_one=ability_one,
            ability_bonus_two=ability_two and ability_bonus_one=ability_two, ability_bonus_two=ability_one

            :param ability_one: An ability to give to a half elf that does cause it to raise an error
            :param ability_two: An ability to give to a half elf that does cause it to raise an error
            """

            try:
                HalfElf(
                    ability_bonus_one=ability_one,
                    ability_bonus_two=ability_two,
                    skill_proficiency_one=Skill.ARCANA,
                    skill_proficiency_two=Skill.SURVIVAL,
                    language=Language.UNDERCOMMON
                )

                self.fail("The ability combo should have caused the half elf to raise an error.")
            except ValueError:
                pass

            try:
                HalfElf(
                    ability_bonus_one=ability_two,
                    ability_bonus_two=ability_one,
                    skill_proficiency_one=Skill.PERSUASION,
                    skill_proficiency_two=Skill.RELIGION,
                    language=Language.DEEP_SPEECH
                )

                self.fail("The ability combo should have caused the half elf to raise an error.")
            except ValueError:
                pass

        def assert_abilities_error_charisma(ability: Ability):
            """
            Asserts that giving a half elf the given ability and the CHARISMA ability results in an error

            :param ability: An ability to give to a half elf that doesn't cause it to raise an error
            """

            assert_abilities_error(ability, Ability.CHARISMA)

        assert_abilities_error_charisma(Ability.STRENGTH)
        assert_abilities_error_charisma(Ability.DEXTERITY)
        assert_abilities_error_charisma(Ability.CONSTITUTION)
        assert_abilities_error_charisma(Ability.INTELLIGENCE)
        assert_abilities_error_charisma(Ability.WISDOM)

        def assert_abilities_error_same(ability: Ability):
            """
            Asserts that giving a half elf the given ability twice results in an error

            :param ability: An ability to give to a half elf
            """

            assert_abilities_error(ability, ability)

        assert_abilities_error_same(Ability.STRENGTH)
        assert_abilities_error_same(Ability.DEXTERITY)
        assert_abilities_error_same(Ability.CONSTITUTION)
        assert_abilities_error_same(Ability.INTELLIGENCE)
        assert_abilities_error_same(Ability.WISDOM)
        assert_abilities_error_same(Ability.CHARISMA)

    def test_init_skills(self):
        def assert_skills_pass(skill_one: Skill, skill_two: Skill):
            """
            Asserts that creating a half elf with the given skills (in both scenarios: skill_proficiency_one=skill_one,
            skill_proficiency_two=skill_two and skill_proficiency_one=skill_two, skill_proficiency_two=skill_one)
            doesn't result in an error

            :param skill_one: A skill to given a half elf that doesn't cause it to raise an error
            :param skill_two: A skill to given a half elf that doesn't cause it to raise an error
            """

            def assert_got_proficiency(half_elf: HalfElf):
                """
                Asserts that the given half_elf gained skill_one and skill_two and no other

                :param half_elf: The half elf that was given skill_one and skill_two
                """

                self.assertTrue(half_elf.proficient_in_skill(skill_one))
                self.assertTrue(half_elf.proficient_in_skill(skill_two))

                for skill in Skill:
                    if skill != skill_one and skill != skill_two:
                        self.assertFalse(half_elf.proficient_in_skill(skill))

            try:
                half_elf = HalfElf(
                    ability_bonus_one=Ability.STRENGTH,
                    ability_bonus_two=Ability.DEXTERITY,
                    skill_proficiency_one=skill_one,
                    skill_proficiency_two=skill_two,
                    language=Language.DRACONIC
                )

                assert_got_proficiency(half_elf)
            except ValueError:
                self.fail("The given skill combo should not have caused the half elf init to raise an error.")

            try:
                half_elf = HalfElf(
                    ability_bonus_one=Ability.CONSTITUTION,
                    ability_bonus_two=Ability.INTELLIGENCE,
                    skill_proficiency_one=skill_two,
                    skill_proficiency_two=skill_one,
                    language=Language.SYLVAN
                )

                assert_got_proficiency(half_elf)
            except ValueError:
                self.fail("The given skill combo should not have caused the half elf init to raise an error.")

        def assert_skills_pass_for_every_skill(skill: Skill):
            """
            Asserts that creating a half elf with the given skill and every other skill (including itself, and in both
            scenarios: skill_proficiency_one=skill, skill_proficiency_two=other skill and skill_proficiency_one=other
            skill, skill_proficiency_two=skill) doesn't result in an error

            :param skill: A skill to given a half elf that doesn't cause it to raise an error
            """

            assert_skills_pass(skill, Skill.ARCANA)
            assert_skills_pass(skill, Skill.HISTORY)
            assert_skills_pass(skill, Skill.INSIGHT)
            assert_skills_pass(skill, Skill.SURVIVAL)
            assert_skills_pass(skill, Skill.RELIGION)
            assert_skills_pass(skill, Skill.PERSUASION)
            assert_skills_pass(skill, Skill.INVESTIGATION)
            assert_skills_pass(skill, Skill.DECEPTION)
            assert_skills_pass(skill, Skill.PERCEPTION)
            assert_skills_pass(skill, Skill.ATHLETICS)
            assert_skills_pass(skill, Skill.MEDICINE)
            assert_skills_pass(skill, Skill.PERFORMANCE)
            assert_skills_pass(skill, Skill.SLEIGHT_OF_HAND)
            assert_skills_pass(skill, Skill.ANIMAL_HANDLING)
            assert_skills_pass(skill, Skill.STEALTH)
            assert_skills_pass(skill, Skill.INTIMIDATION)
            assert_skills_pass(skill, Skill.NATURE)
            assert_skills_pass(skill, Skill.ACROBATICS)

        assert_skills_pass_for_every_skill(Skill.ARCANA)
        assert_skills_pass_for_every_skill(Skill.HISTORY)
        assert_skills_pass_for_every_skill(Skill.INSIGHT)
        assert_skills_pass_for_every_skill(Skill.SURVIVAL)
        assert_skills_pass_for_every_skill(Skill.RELIGION)
        assert_skills_pass_for_every_skill(Skill.PERSUASION)
        assert_skills_pass_for_every_skill(Skill.INVESTIGATION)
        assert_skills_pass_for_every_skill(Skill.DECEPTION)
        assert_skills_pass_for_every_skill(Skill.PERCEPTION)
        assert_skills_pass_for_every_skill(Skill.ATHLETICS)
        assert_skills_pass_for_every_skill(Skill.MEDICINE)
        assert_skills_pass_for_every_skill(Skill.PERFORMANCE)
        assert_skills_pass_for_every_skill(Skill.SLEIGHT_OF_HAND)
        assert_skills_pass_for_every_skill(Skill.ANIMAL_HANDLING)
        assert_skills_pass_for_every_skill(Skill.STEALTH)
        assert_skills_pass_for_every_skill(Skill.INTIMIDATION)
        assert_skills_pass_for_every_skill(Skill.NATURE)
        assert_skills_pass_for_every_skill(Skill.ACROBATICS)

    def test_init_language(self):
        def assert_language_pass(language: Language):
            """
            Asserts that giving a half elf the given language doesn't raise an error and gives the half elf a
            proficiency in that language

            :param language: A language that doesn't raise an error when given to a half elf
            """

            try:
                half_elf = HalfElf(
                    ability_bonus_one=Ability.STRENGTH,
                    ability_bonus_two=Ability.INTELLIGENCE,
                    skill_proficiency_one=Skill.ARCANA,
                    skill_proficiency_two=Skill.NATURE,
                    language=language
                )

                self.assertEqual(get_language(language).name, half_elf.other_proficiencies[2].name)
            except ValueError:
                self.fail("The given language shouldn't have caused the half elf to raise an error.")

        for lang in Language:
            if lang != Language.COMMON and lang != Language.ELVISH:
                assert_language_pass(lang)

    def test_init_language_error(self):
        def assert_language_error(language: Language):
            """
            Asserts that giving a half elf the given language raises an error

            :param language: A language that does raise an error when given to a half elf
            """

            try:
                HalfElf(
                    ability_bonus_one=Ability.STRENGTH,
                    ability_bonus_two=Ability.INTELLIGENCE,
                    skill_proficiency_one=Skill.ARCANA,
                    skill_proficiency_two=Skill.NATURE,
                    language=language
                )

                self.fail("The given language should have caused the half elf to raise an error.")
            except ValueError:
                pass

        assert_language_error(Language.COMMON)
        assert_language_error(Language.ELVISH)

    def test_get_ability_bonus(self):
        super()._test_get_ability_bonus(
            expected_strength_bonus=1,
            expected_dexterity_bonus=1,
            expected_wisdom_bonus=0,
            expected_charisma_bonus=2,
            expected_constitution_bonus=0,
            expected_intelligence_bonus=0
        )

    def test_proficient_in_skill(self):
        super()._test_proficient_in_skill((Skill.ARCANA, Skill.DECEPTION))
