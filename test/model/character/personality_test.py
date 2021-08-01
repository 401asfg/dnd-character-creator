import unittest

from main.model.character.personality import Personality


class PersonalityTest(unittest.TestCase):
    def test_init(self):
        personality = Personality(
            trait_one="Obsessive",
            trait_two="Flamboyant",
            ideal="Good suits make good people.",
            bond="I need to keep my suits from getting dirty.",
            flaw="I try to steal suits."
        )

        self.assertEqual("Obsessive", personality.trait_one)
        self.assertEqual("Flamboyant", personality.trait_two)
        self.assertEqual("Good suits make good people.", personality.ideal)
        self.assertEqual("I need to keep my suits from getting dirty.", personality.bond)
        self.assertEqual("I try to steal suits.", personality.flaw)
