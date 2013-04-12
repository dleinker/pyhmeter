from __future__ import division
import csv

class HMeter:
    """HMeter implements a Hedonometer as described in the Dodd paper"""
    
    # First, import the list of words from Dodd paper
    dataset = csv.reader(open("DataSetS1.csv", "r"), delimiter='\t')

    def __init__(self, wordlist):
        self.wordlist = wordlist

    def wordcount():
        """Returns Total number of words in list. Is this needed?"""
        pass

    def wordmatches():
        """Returns total number of words that match the Dodd paper wordlist"""
        pass

    def wordshift():
        """Some kind of crazy function that is going to return the wordshift"""
        pass

    def hmeter(corpus, deltah=0.0):
        """Takes a list of individual words and returns the happiness score.
        deltah removes stop words as per Dodd paper, wordcount returns how many 
        words matched the Dodd wordlist."""

        # create a dict based on the 'name' and 'happiness_average' columns
        wordscores = {row[0]: row[2] for row in dataset} 
        
        happysum = 0
        # for loops returns count of words that have a score and sum of their scores
        for word in corpus:
            # We're only interested if the word from our corpus is on 
            # our list of words with scores
            if word in wordscores:
                # the word has a score, let's make sure the score is a float 
                # instead of a string so we can do math with it
                score = float(wordscores[word]) 
                # apply methodology to remove stop words as per Dodd et al. (2011)
                if score >= 5.0 + deltah or score <= 5.0 - deltah: 
                    happysum  += score

        if count != 0: # divide by zero errors are sad.
                return happysum / count # dividing by the count gives us the mean.
        else:
            return 0.0

    def wordcount
