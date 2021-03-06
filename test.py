"""Unit test for pyhmeter.py"""

import pyhmeter
import csv
import unittest


class KnownValues(unittest.TestCase):

    test_words = (('laughter', 8.5), ('successful', 8.16), ('pleasure', 8.08),
                  ('architect', 6.36), ('blackberry', 6.26), ('wasting', 3.22),
                  ('ouch', 2.90), ('documents', 5.02), ('flip', 5.02),
                  ('crowd', 4.14), ('ooogleyboogley', None), ('.', None),
                  ('<HTML></HTML>', None))

    hmeter_answers = ((1, 6.21142857143), (2, 6.91), (3, 8.24666666667))

    def setUp(self):
        self.doddscores = pyhmeter.load_scores("Data_Set_S1.txt")

    def test_single_word(self):
        """Passed a list with a single word, function should return that
        word's score"""
        for word, score in self.test_words:
            h = pyhmeter.HMeter([word], self.doddscores)
            result = h.happiness_score()
            self.assertEqual(result, score)

    def test_deltah(self):
        """Test that hmeter works properly at all levels of deltah"""
        for deltah, result in self.hmeter_answers:
            h = pyhmeter.HMeter([pair[0] for pair in self.test_words], self.doddscores, deltah)
            self.assertAlmostEqual(h.happiness_score(), result)

    def test_matchlist(self):
        """Test that matchlist works properly. Tests matchlist on init"""
        h = pyhmeter.HMeter([pair[0] for pair in self.test_words], self.doddscores)
        match_list_test = [word for word, score in self.test_words if score]
        self.assertListEqual(h.matchlist, match_list_test)

    def test_set_deltah(self):
        """Checks that set_delta changes deltah"""
        h = pyhmeter.HMeter([pair[0] for pair in self.test_words], self.doddscores)
        for deltah in xrange(6):
            h.deltah = deltah
            self.assertEqual(h.deltah, deltah)

    def test_new_matchlist_generation(self):
        """Checks matchlist after deltah is changed"""
        h = pyhmeter.HMeter([pair[0] for pair in self.test_words], self.doddscores)
        for deltah in xrange(4):
            h.deltah = deltah
            match_list_test = []
            for word, score in self.test_words:
                if score and (score >= 5.0 + deltah or score <= 5.0 - deltah):
                    match_list_test.append(word)
            self.assertListEqual(h.matchlist, match_list_test)

    def test_fractinal_abundance(self):
        """Tests fractional abundance"""
        h = pyhmeter.HMeter([pair[0] for pair in self.test_words], self.doddscores)
        frac_abund = h.fractional_abundance('documents')
        self.assertEqual(frac_abund,0.1)


    # TODO Write tests for word shift
    #def test_word_shift_sum(self):
    #    """A Sum of Wordshifts should add up to 100 or -100"""
    #"""    sum = 0
    #    h = pyhmeter.HMeter([pair[0] for pair in self.test_words])
    #    for word in h.matchlist():
    #        sum += h.word_shift"""


class BadInputs(unittest.TestCase):

    def setUp(self):
        self.doddscores = pyhmeter.load_scores("Data_Set_S1.txt")

    def test_empty_list(self):
        """In case of an empty list, the score should be Null"""
        h = pyhmeter.HMeter([], self.doddscores)
        self.assertIsNone(h.happiness_score())

    def test_null_list(self):
        """In case of null list, there should be a type error"""
        with self.assertRaises(TypeError):
            h = pyhmeter.HMeter(None, self.doddscores)
            score = h.happiness_score()

    def test_bad_deltah(self):
        for deltah in range(4, 20):
            h = pyhmeter.HMeter(['butterflies', 'laughter',
                                'terrorist'], self.doddscores, deltah)
            self.assertIsNone(h.happiness_score())


class FileIO(unittest.TestCase):

    def test_doddfile_exists(self):
        """Check for the existance of the labMT 1.0 file from Plos One"""
        doddfile = csv.reader(open("Data_Set_S1.txt", "r"), delimiter="\t")

if __name__ == '__main__':
    unittest.main()
