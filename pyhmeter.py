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
        # sources of data 
        self.matchlist = [word for word in self.wordlist if word in self.wordscores]

    def wordshift():
        """Some kind of crazy function that is going to return the wordshift"""
        pass

    def testtt(self):
        print self
        print self.dataset

    def happiness_score(self, deltah=0.0):
        """Takes a list of individual words and returns the happiness score.
        deltah removes stop words as per Dodd paper, wordcount returns how many 
        words matched the Dodd wordlist."""

        # create a dict based on the 'name' and 'happiness_average' columns
        count = 0
        happysum = 0
        # for loop returns count of words that have a score and sum of their scores
        for word in self.wordlist:
            # We're only interested if the word from our corpus is on 
            # our list of words with scores
            if word in self.wordscores:
                # the word has a score, let's make sure the score is a float 
                # instead of a string so we can do math with it
                score = float(self.wordscores[word]) 
                # apply methodology to remove stop words as per Dodd et al. (2011)
                if score >= 5.0 + deltah or score <= 5.0 - deltah: 
                    happysum  += score
                    count += 1

        if count != 0: # divide by zero errors are sad.
                return happysum / count # dividing by the count gives us the mean.
        else:
            return 0.0
