import unittest

from main.model.character_components.character_alignment import CharacterAlignment


class CharacterAlignmentTest(unittest.TestCase):
    def setUp(self):
        self.nature = CharacterAlignment.Nature
        self.morality = CharacterAlignment.Morality

    def test_name(self):
        # Good
        alignment = CharacterAlignment(self.nature.LAWFUL, self.morality.GOOD)
        self.assertEqual(alignment.name(), "LAWFUL GOOD")

        alignment = CharacterAlignment(self.nature.NEUTRAL, self.morality.GOOD)
        self.assertEqual(alignment.name(), "NEUTRAL GOOD")

        alignment = CharacterAlignment(self.nature.CHAOTIC, self.morality.GOOD)
        self.assertEqual(alignment.name(), "CHAOTIC GOOD")

        # Neutral
        alignment = CharacterAlignment(self.nature.LAWFUL, self.morality.NEUTRAL)
        self.assertEqual(alignment.name(), "LAWFUL NEUTRAL")

        alignment = CharacterAlignment(self.nature.NEUTRAL, self.morality.NEUTRAL)
        self.assertEqual(alignment.name(), "TRUE NEUTRAL")

        alignment = CharacterAlignment(self.nature.CHAOTIC, self.morality.NEUTRAL)
        self.assertEqual(alignment.name(), "CHAOTIC NEUTRAL")

        # Evil
        alignment = CharacterAlignment(self.nature.LAWFUL, self.morality.EVIL)
        self.assertEqual(alignment.name(), "LAWFUL EVIL")

        alignment = CharacterAlignment(self.nature.NEUTRAL, self.morality.EVIL)
        self.assertEqual(alignment.name(), "NEUTRAL EVIL")

        alignment = CharacterAlignment(self.nature.CHAOTIC, self.morality.EVIL)
        self.assertEqual(alignment.name(), "CHAOTIC EVIL")
