import unittest

from translator import english_to_french, french_to_english

class testenfr(unittest.TestCase):
    def test_eng_fr(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour')
        self.assertNotEqual(english_to_french('School'),'Lecole')

class testfren(unittest.TestCase):
    def test_fr_eng(self):
        self.assertEqual(french_to_english('Bonjour'),'Hello')
        self.assertNotEqual(french_to_english('Fleur'),'Flow')

if __name__ == "__main__":
    unittest.main()
