from __future__ import division
import csv

class HMeter:
    """HMeter implements a Hedonometer as described in the Dodd paper"""

    # This is the dataset provided by the Dodd paper. Please see the README for a
    # reference link and to download this file.
    doddfile = csv.reader(open("Data_Set_S1.txt", "r"), delimiter='\t')
    for x in range(4): # strip header info
        doddfile.next()
    wordscores = {row[0]: row[2] for row in doddfile}

    def __init__(self, wordlist):
        self.wordlist = wordlist
        # self.matchlist = [word for word in self.wordlist if word in self.wordscores]

    def matchlist(self,deltah=0.0):
        """Strips anything from the wordlist that doesn't match the words from labMT 1.0"""
        matchlist = []
        for word in self.wordlist:
            if word in self.wordscores:
                score = float(self.wordscores[word])
                if score >= 5.0 + deltah or score <= 5.0 - deltah:
                    matchlist += [word]
        return matchlist

        """Alternate Method:
        matchlist = [word for word in self.wordlist if word in self.wordscores]
        for word in matchlist:
            score = float(self.wordscore[word])
            if score >= 5.0 + deltah or score <= 5.0 - deltah:
                matchlist += [word]"""

    def fractional_abundance(self, word):
        """Takes a word and return its fractional abundance within self.matchlist"""

    def word_shift():
        """Takes a list of words and compares it self.matchlist, returning whatever 
        crazy math has to happen, Will return a List of Tuples of Lists."""
        """ We will need to check... relative frequencies of word between self.matchlist and arg.matchlist"""
        pass

    def happiness_score(self, deltah=0.0):
        """Takes a list of individual words and returns the happiness score.
        deltah removes stop words as per Dodd paper."""

        count = 0
        happysum = 0

        for word in self.matchlist(deltah):
            happysum  += float(self.wordscores[word])
            count += 1
        
        if count != 0: # divide by zero errors are sad.
            return happysum / count # dividing by the count gives us the mean.
        else:
            pass # empty lists have no score
