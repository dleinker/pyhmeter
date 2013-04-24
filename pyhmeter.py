from __future__ import division
from math import copysign
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
    #wordscores = { 'A':1.0, 'B':5.0, 'C':9.0}

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
        matchlist = self.matchlist()
        frac_abund = matchlist.count(word) / len(matchlist)
        return frac_abund

    def word_shift(self, comp):
        """Takes a list of words and compares it self.matchlist, returning whatever 
        crazy math has to happen, """

        # create our comparison object. self is the reference object.
        tcomp = HMeter(comp,self.deltah)
        # we want a list of all potential words, but only need each word once.
        word_shift_list = list(set(tcomp.matchlist() + self.matchlist()))
        print "WORD SHIFT LIST LENGTH: %s" % len(word_shift_list)
        output_data = []
        ref_happiness_score = self.happiness_score()
        comp_happiness_score = tcomp.happiness_score()
        happy_diff = comp_happiness_score - ref_happiness_score

        for word in word_shift_list:
            abundance = tcomp.fractional_abundance(word) - self.fractional_abundance(word)
            happiness_shift = self.wordscores[word] - ref_happiness_score 
            paper_score = (happiness_shift * abundance * 100) / happy_diff
            output_data.append((word, paper_score, abundance, happiness_shift))
            # count += happiness_shift * abundance
            print output_data[-1]
        
        #count2 = 0
        #count4 = 0 
        #output_data = []
        #for word, score, abundance, happiness_shift in word_data:
        #    print word, score, abundance, happiness_shift
        #    output_data.append((word, paper_score, copysign(1,abundance), copysign(1,happiness_shift))

        #for word, abundance, happiness_shift in word_data:
        #    word_shift = (happiness_shift * abundance) / count
        #    happy_diff= tcomp.happiness_score() - self.happiness_score()
        #    count4 += happy_diff
        #    paper_score = (happiness_shift * abundance * 100) / happy_diff
        #    print count, happy_diff
        #    output_data.append((word, word_shift * 100, copysign(1,abundance), copysign(1,happiness_shift), paper_score))
        #    print output_data[-1]
        #    count2 += word_shift
        # sort words by absolute value of individual word shift
        output_data.sort(key=lambda word: abs(word[1]))
        print output_data[:30]
        #count3 = 0
        #for word, word_shift, abund, shift in output_data:
        #    print word, word_shift
        #    count3 += word_shift

        return output_data
        
    def happiness_score(self):
        """Takes a list made up of individual words and returns the happiness score."""

        count = 0
        happysum = 0

        for word in self.matchlist():
            happysum  += self.wordscores[word]
            count += 1
        
        if count != 0: # divide by zero errors are sad.
            return happysum / count
        else:
            pass # empty lists have no score
