import unittest

from main.model.character.utility.helper_modules.common_race_collection_items import get_language, get_darkvision, get_fey_ancestry
from main.model.character.utility.enumerators.language import Language


class CommonRaceCollectionItemsTest(unittest.TestCase):
    def test_get_language(self):
        def assert_get_language(language: Language, expected_name: str):
            """
            Asserts that getting with the given language produces a collection item with the expected_name and no info

            :param language: The language to give to the get_language function
            :param expected_name: The expected name of the collection item returned by the get_language function
            """

            self.assertEqual(expected_name, get_language(language).name)
            self.assertIsNone(get_language(language).info)

        assert_get_language(Language.COMMON, "Common Language")
        assert_get_language(Language.ELVISH, "Elvish Language")
        assert_get_language(Language.DWARVISH, "Dwarvish Language")
        assert_get_language(Language.GIANT, "Giant Language")
        assert_get_language(Language.GNOMISH, "Gnomish Language")
        assert_get_language(Language.GOBLIN, "Goblin Language")
        assert_get_language(Language.HALFLING, "Halfling Language")
        assert_get_language(Language.ORC, "Orc Language")
        assert_get_language(Language.ABYSSAL, "Abyssal Language")
        assert_get_language(Language.CELESTIAL, "Celestial Language")
        assert_get_language(Language.DRACONIC, "Draconic Language")
        assert_get_language(Language.DEEP_SPEECH, "Deep Speech")
        assert_get_language(Language.INFERNAL, "Infernal Language")
        assert_get_language(Language.PRIMORDIAL, "Primordial Language")
        assert_get_language(Language.SYLVAN, "Sylvan Language")
        assert_get_language(Language.UNDERCOMMON, "Undercommon Language")

    def test_get_darkvision(self):
        self.assertEqual("Darkvision", get_darkvision().name)
        self.assertEqual(
            "You can see in dim light within 60 ft. of you as if it were bright light, and in darkness as if it were "
            "dim light.",
            get_darkvision().info
        )

    def test_get_fey_ancestry(self):
        self.assertEqual("Fey Ancestry", get_fey_ancestry().name)
        self.assertEqual(
            "You have advantage on saving throws against being charmed, and magic can’t put you to sleep.",
            get_fey_ancestry().info
        )
