import unittest

from main.model.character.alignment import Alignment


class AlignmentTest(unittest.TestCase):
    def setUp(self):
        self.nature = Alignment.Nature
        self.morality = Alignment.Morality

    def test_name(self):
        # Good
        alignment = Alignment(self.nature.LAWFUL, self.morality.GOOD)
        self.assertEqual(alignment.name(), "Lawful Good")

        alignment = Alignment(self.nature.NEUTRAL, self.morality.GOOD)
        self.assertEqual(alignment.name(), "Neutral Good")

        alignment = Alignment(self.nature.CHAOTIC, self.morality.GOOD)
        self.assertEqual(alignment.name(), "Chaotic Good")

        # Neutral
        alignment = Alignment(self.nature.LAWFUL, self.morality.NEUTRAL)
        self.assertEqual(alignment.name(), "Lawful Neutral")

        alignment = Alignment(self.nature.NEUTRAL, self.morality.NEUTRAL)
        self.assertEqual(alignment.name(), "True Neutral")

        alignment = Alignment(self.nature.CHAOTIC, self.morality.NEUTRAL)
        self.assertEqual(alignment.name(), "Chaotic Neutral")

        # Evil
        alignment = Alignment(self.nature.LAWFUL, self.morality.EVIL)
        self.assertEqual(alignment.name(), "Lawful Evil")

        alignment = Alignment(self.nature.NEUTRAL, self.morality.EVIL)
        self.assertEqual(alignment.name(), "Neutral Evil")

        alignment = Alignment(self.nature.CHAOTIC, self.morality.EVIL)
        self.assertEqual(alignment.name(), "Chaotic Evil")
