import unittest

from main.model.character_components.character_alignment import CharacterAlignment


class CharacterAlignmentTest(unittest.TestCase):
    def setUp(self):
        self.nature = CharacterAlignment.Nature
        self.morality = CharacterAlignment.Morality

    def test_name(self):
        # Good
        alignment = CharacterAlignment(self.nature.LAWFUL, self.morality.GOOD)
        self.assertEqual(alignment.name(), "Lawful Good")

        alignment = CharacterAlignment(self.nature.NEUTRAL, self.morality.GOOD)
        self.assertEqual(alignment.name(), "Neutral Good")

        alignment = CharacterAlignment(self.nature.CHAOTIC, self.morality.GOOD)
        self.assertEqual(alignment.name(), "Chaotic Good")

        # Neutral
        alignment = CharacterAlignment(self.nature.LAWFUL, self.morality.NEUTRAL)
        self.assertEqual(alignment.name(), "Lawful Neutral")

        alignment = CharacterAlignment(self.nature.NEUTRAL, self.morality.NEUTRAL)
        self.assertEqual(alignment.name(), "True Neutral")

        alignment = CharacterAlignment(self.nature.CHAOTIC, self.morality.NEUTRAL)
        self.assertEqual(alignment.name(), "Chaotic Neutral")

        # Evil
        alignment = CharacterAlignment(self.nature.LAWFUL, self.morality.EVIL)
        self.assertEqual(alignment.name(), "Lawful Evil")

        alignment = CharacterAlignment(self.nature.NEUTRAL, self.morality.EVIL)
        self.assertEqual(alignment.name(), "Neutral Evil")

        alignment = CharacterAlignment(self.nature.CHAOTIC, self.morality.EVIL)
        self.assertEqual(alignment.name(), "Chaotic Evil")
