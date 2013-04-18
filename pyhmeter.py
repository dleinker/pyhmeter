from __future__ import division
import csv

class HMeter:
    """HMeter implements a Hedonometer as described in the Dodd paper"""

    # setup word scores, we only need to do this once.
    dataset = csv.reader(open("DataSetS1.csv", "r"), delimiter='\t')
    wordscores = {row[0]: row[2] for row in dataset}

    def __init__(self, wordlist):
        self.wordlist = wordlist
        # TODO Possibly change deltah into an attribute rather than argument on 
        # happiness_score. This would also require changing matchlist into 
        # a function
        # self.matchlist = [word for word in self.wordlist if word in self.wordscores]

    def matchlist(self,deltah=0.0):
        """Create a list of words that match the list for a specific value of deltah.
        Removes stop words"""
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
        crazy math has to happen"""
        """ We will need to check... relative frequencies of word between self.matchlist and arg.matchlist"""

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
