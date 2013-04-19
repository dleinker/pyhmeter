from __future__ import division
import csv

class HMeter:
    """HMeter implements a Hedonometer as described in the Dodd paper"""

    # This is the dataset provided by the Dodd paper. Please see the README for a
    # reference link and to download this file. From this dataset we create a dict
    # that contains the words and their happiness score.
    doddfile = csv.reader(open("Data_Set_S1.txt", "r"), delimiter='\t')
    for _ in range(4): # strip header info
        doddfile.next()
    wordscores = {row[0]: row[2] for row in doddfile}

    def __init__(self, wordlist):
        self.wordlist = wordlist
        # self.matchlist = [word for word in self.wordlist if word in self.wordscores]

    def matchlist(self,deltah=0.0):
        """Strips anything from the wordlist that doesn't match the words from labMT 1.0"""
        
        # first we take every word that matches labMT 1.0
        labmtmatches = [word for word in self.wordlist if word in self.wordscores]

        # then we strip out stop words as defined by Dodd paper
        matchlist = []
        for word in labmtmatches:
            score = float(self.wordscores[word])
            if score >= 5.0 + deltah or score <= 5.0 - deltah:
                matchlist += [word]
        return matchlist

    def fractional_abundance(self, word):
        """Takes a word and return its fractional abundance within self.matchlist"""
        pass

    def word_shift(self, tcomp, deltah=0.0):
        """Takes a list of words and compares it self.matchlist, returning whatever 
        crazy math has to happen, Will return a List of Tuples of Lists."""
        """ We will need to check... relative frequencies of word between self.matchlist and tcomp.matchlist"""
        pass

    def happiness_score(self, deltah=0.0):
        """Takes a list of individual words and returns the happiness score."""

        count = 0
        happysum = 0

        for word in self.matchlist(deltah):
            happysum  += float(self.wordscores[word])
            count += 1
        
        if count != 0: # divide by zero errors are sad.
            return happysum / count # dividing by the count gives us the mean.
        else:
            pass # empty lists have no score
