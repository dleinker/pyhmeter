from __future__ import division
import csv

class HMeter:
    """HMeter implements a Hedonometer as described in the Dodd paper"""

    # setup word scores, we only need to do this once.
    dataset = csv.reader(open("DataSetS1.csv", "r"), delimiter='\t')
    wordscores = {row[0]: row[2] for row in dataset}

    def __init__(self, wordlist):
        self.wordlist = wordlist
        # create a list of words that match the Dodd list of mechannical turk words
        # we only care about words that match the list, this allows us to accept filthy
        # sources of data without too much filtering
        self.matchlist = [word for word in self.wordlist if word in self.wordscores]

    def fractional_abundance(self, word):
        """Takes a word and return its fractional abundance within self.matchlist"""

    def word_shift():
        """Takes a list of words and compares it self.matchlist, returning whatever 
        crazy math has to happen"""
        """ We will need to check... relative frequencies of word between self.matchlist and arg.matchlist"""

    def happiness_score(self, deltah=0.0):
        """Takes a list of individual words and returns the happiness score.
        deltah removes stop words as per Dodd paper."""

        count = 0
        happysum = 0

        # for loop returns count of words that have a score and sum of their scores
        for word in self.matchlist:
            score = float(self.wordscores[word]) 
            # apply methodology to remove stop words as per Dodd et al. (2011)
            if score >= 5.0 + deltah or score <= 5.0 - deltah: 
                happysum  += score
                count += 1
        
        if count != 0: # divide by zero errors are sad.
            return happysum / count # dividing by the count gives us the mean.
        else:
            pass # empty lists have no score
