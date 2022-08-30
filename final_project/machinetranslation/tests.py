
''' These are the unit tests for translator.py for the IBM Watson language translator app '''

import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    
    def test_english_to_french(self):
        ''' This tests for null and functionality from english to french translation '''
        self.assertIsNotNone(english_to_french(self))
        self.assertNotEqual(english_to_french('Hello'), 'Bonjour')
        self.assertEqual(english_to_french('Hello'), 'Hello')
    
    def test_french_to_english(self):
        ''' This tests for null and functionality from french to english translation '''
        self.assertIsNotNone(french_to_english(self))
        self.assertNotEqual(french_to_english('Bonjour'), 'Hello')
        self.assertEqual(french_to_english('Bonjour'), 'Bonjour')

if __name__ == '__main__':
    unittest.main()