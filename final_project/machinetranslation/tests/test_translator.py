from translator import french_to_english, english_to_french
import unittest

class TestTranslator(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french('Hello'), 'Hello')
        
    def test_french_to_english(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english('Bonjour'), 'Bonjour')

    def test_english_to_french_null_input(self):
        with self.assertRaises(ValueError):
            english_to_french(None)
    
    def test_french_to_english_null_input(self):
        with self.assertRaises(ValueError):
            french_to_english(None)

