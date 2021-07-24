import unittest

from main.model.character.alignment import Alignment


class AlignmentTest(unittest.TestCase):
    def test_init(self):
        alignment = Alignment(Alignment.Nature.LAWFUL, Alignment.Morality.GOOD)
        self.assertEqual(alignment.nature, Alignment.Nature.LAWFUL)
        self.assertEqual(alignment.morality, Alignment.Morality.GOOD)

        alignment = Alignment(Alignment.Nature.NEUTRAL, Alignment.Morality.NEUTRAL)
        self.assertEqual(alignment.nature, Alignment.Nature.NEUTRAL)
        self.assertEqual(alignment.morality, Alignment.Morality.NEUTRAL)

        alignment = Alignment(Alignment.Nature.CHAOTIC, Alignment.Morality.EVIL)
        self.assertEqual(alignment.nature, Alignment.Nature.CHAOTIC)
        self.assertEqual(alignment.morality, Alignment.Morality.EVIL)

    def test_name(self):
        # Good
        alignment = Alignment(Alignment.Nature.LAWFUL, Alignment.Morality.GOOD)
        self.assertEqual(alignment.name, "Lawful Good")

        alignment = Alignment(Alignment.Nature.NEUTRAL, Alignment.Morality.GOOD)
        self.assertEqual(alignment.name, "Neutral Good")

        alignment = Alignment(Alignment.Nature.CHAOTIC, Alignment.Morality.GOOD)
        self.assertEqual(alignment.name, "Chaotic Good")

        # Neutral
        alignment = Alignment(Alignment.Nature.LAWFUL, Alignment.Morality.NEUTRAL)
        self.assertEqual(alignment.name, "Lawful Neutral")

        alignment = Alignment(Alignment.Nature.NEUTRAL, Alignment.Morality.NEUTRAL)
        self.assertEqual(alignment.name, "True Neutral")

        alignment = Alignment(Alignment.Nature.CHAOTIC, Alignment.Morality.NEUTRAL)
        self.assertEqual(alignment.name, "Chaotic Neutral")

        # Evil
        alignment = Alignment(Alignment.Nature.LAWFUL, Alignment.Morality.EVIL)
        self.assertEqual(alignment.name, "Lawful Evil")

        alignment = Alignment(Alignment.Nature.NEUTRAL, Alignment.Morality.EVIL)
        self.assertEqual(alignment.name, "Neutral Evil")

        alignment = Alignment(Alignment.Nature.CHAOTIC, Alignment.Morality.EVIL)
        self.assertEqual(alignment.name, "Chaotic Evil")
