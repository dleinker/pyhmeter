"""Unit test for pyhmeter.py"""

import pyhmeter
import unittest

class KnownValues(unittest.TestCase):

    test_words = ( ('laughter', 8.5), ('successful', 8.16), ('pleasure', 8.08), ('architect', 6.36), ('blackberry', 6.26), ('wasting', 3.22), ('ouch', 2.90), ('documents', 5.02), ('flip', 5.02), ('crowd', 4.14) )

    hmeter_answers = ( (1, 6.21142857143), (2, 6.91), (3, 8.24666666667), (4, 0.0) )

    def test_single_word(self):
        """Passed a list with a single word, function should return that word's score"""
        for word, score in self.test_words:
            h = pyhmeter.HMeter([word])
            result = h.happiness_score()
            self.assertEqual(result, score)

    def test_deltah(self):
        """Test that hmeter works properly at all levels of deltah"""
        h = pyhmeter.HMeter([pair[0] for pair in self.test_words])
        for deltah, result in self.hmeter_answers:
            self.assertAlmostEqual(h.happiness_score(deltah),result)

class BadInputs(unittest.TestCase):

    def test_empty_list(self):
        """In case of an empty list, the score should be 0.0"""
        h = pyhmeter.HMeter([])
        self.assertEqual(h.happiness_score(), 0.0)

    def test_null_list(self):
        pass


if __name__ == '__main__':
    unittest.main()

