from __future__ import division
import csv
from fractions import Fraction

class HMeter:
    """HMeter implements a Hedonometer as described in the Dodd paper"""

    # This is the dataset provided by the Dodd paper. Please see the README for a
    # reference link and to download this file. From this dataset we create a dict
    # that contains the words and their happiness score.
    doddfile = csv.reader(open("Data_Set_S1.txt", "r"), delimiter='\t')

    for x in xrange(4): # strip header info
       doddfile.next()
    wordscores = {row[0]: float(row[2]) for row in doddfile}
    # wordscores = { 'A':1.0, 'B':5.0, 'C':9.0}

    def __init__(self, wordlist, deltah=0.0):
        self.wordlist = wordlist
        self.deltah = deltah

    def matchlist(self):
        """Strips anything from the wordlist that doesn't match the words from labMT 1.0"""
        
        # first we take every word that matches labMT 1.0
        labmtmatches = [word for word in self.wordlist if word in self.wordscores]

        # then we strip out stop words as described by Dodd paper
        matchlist = []

        for word in labmtmatches:
            score = self.wordscores[word]
            if score >= 5.0 + self.deltah or score <= 5.0 - self.deltah:
                matchlist += [word]
        return matchlist

    def fractional_abundance(self, word):
        """Takes a word and return its fractional abundance within self.matchlist"""
        """frac abundance = total occurances / total size """
        frac_abund = Fraction(self.matchlist().count(word),len(self.matchlist()))
        return frac_abund

    def word_shift(self, comp):
        """Takes a list of words and compares it self.matchlist, returning whatever 
        crazy math has to happen, """

        # create our comparison object. self is the reference object.
        tcomp = HMeter(comp,self.deltah)
        # we want a list of all potential words, but only need each word once.
        word_shift_list = list(set(tcomp.matchlist() + self.matchlist()))
        count = 0
        print "COmparison text Happiness: %s" % tcomp.happiness_score()
        print tcomp.matchlist()
        print "Reference Text Happiness: %s" % self.happiness_score()
        print self.matchlist()

        for word in word_shift_list:
            print word
            abundance = tcomp.fractional_abundance(word) - self.fractional_abundance(word)
            print "comparative abundance %s" % abundance
            word_happy = HMeter([word])
            print "word happiness: %s" % float(word_happy.happiness_score_frac())
            happiness_shift = word_happy.happiness_score_frac() - self.happiness_score_frac() 
            print "happiness_shift %s" % float(happiness_shift)
            happiness_diff = tcomp.happiness_score_frac() - self.happiness_score_frac()
            numerator = happiness_shift * abundance
            print "NUMERATOR: %s" % float(numerator) 
            count += numerator
            print "count %s" % count 
        
        count2 = 0

        for word in word_shift_list:
            print word
            word_happy = HMeter([word])
            happiness_shift = word_happy.happiness_score_frac() - self.happiness_score_frac() 
            print "shift %s" % float(happiness_shift)
            abundance = tcomp.fractional_abundance(word) - self.fractional_abundance(word)
            print "abundance %s" % abundance
            numerator = happiness_shift * abundance
            word_shift = Fraction(numerator,count)
            count2 += word_shift
            print "word_shift??? %s" % float(word_shift * 100) 

        print "THE COUNT %s" % float(count2)
        
    def happiness_score_frac(self):
        """Takes a list of individual words and returns the happiness score."""

        count = 0
        happysum = 0

        for word in self.matchlist():
            happysum  += Fraction(self.wordscores[word])
            count += 1
        
        if count != 0: # divide by zero errors are sad.
            return Fraction(happysum, count) 
        else:
            pass # empty lists have no score

    def happiness_score(self):
        """Returns a floating point happiness score."""
        # TODO fix this awfulness
        if self.happiness_score_frac():
            return float(self.happiness_score_frac())
