from __future__ import division
import csv


class HMeter:
    """HMeter implements a Hedonometer as described in the Dodd paper"""

    # This is the dataset provided by the Dodd paper. Please see the README for
    # a reference link and to download this file. From this dataset we create
    # a dict that contains the words and their happiness score.
    doddfile = csv.reader(open("Data_Set_S1.txt", "r"), delimiter='\t')

    for x in xrange(4):  # strip header info
        doddfile.next()

    wordscores = {row[0]: float(row[2]) for row in doddfile}
    #wordscores = { 'A':1.0, 'B':5.0, 'C':9.0}

    def __init__(self, wordlist, deltah=0.0):
        self.wordlist = wordlist
        self.set_deltah(deltah)

    def set_deltah(self, deltah):
        """Changes deltah, which generates a new matchlist, Stripping anything
        from the wordlist that doesn't match the words from labMT 1.0"""
        self.deltah = deltah

        # first we take every word that matches labMT 1.0
        labmtmatches = [word for word in self.wordlist
                        if word in self.wordscores]

        # then we strip out stop words as described by Dodd paper
        self.matchlist = []

        for word in labmtmatches:
            score = self.wordscores[word]
            if score >= 5.0 + self.deltah or score <= 5.0 - self.deltah:
                self.matchlist.append(word)

    def fractional_abundance(self, word):
        """Takes a word and return its fractional abundance within
        self.matchlist"""
        frac_abund = self.matchlist.count(word) / len(self.matchlist)
        return frac_abund

    def word_shift(self, comp):
        """Returns a list of tuples that contain each word's contribution to
        happiness score shift between two samples."""

        # initialize variables for potentially large loop.
        # create our comparison object. self is the reference object.
        tcomp = HMeter(comp, self.deltah)

        # we want a list of all potential words, but only need each word once.
        word_shift_list = list(set(tcomp.matchlist + self.matchlist))

        output_data = []
        ref_happiness_score = self.happiness_score()
        comp_happiness_score = tcomp.happiness_score()
        happy_diff = comp_happiness_score - ref_happiness_score

        for word in word_shift_list:
            abundance = (tcomp.fractional_abundance(word) -
                         self.fractional_abundance(word))
            happiness_shift = self.wordscores[word] - ref_happiness_score
            paper_score = (happiness_shift * abundance * 100) / happy_diff
            output_data.append((word, paper_score, abundance, happiness_shift))
            print output_data[-1]

        # sort words by absolute value of individual word shift
        output_data.sort(key=lambda word: abs(word[1]))
        return output_data

    def happiness_score(self):
        """Takes a list made up of individual words and returns the happiness
        score."""

        count = 0
        happysum = 0

        for word in self.matchlist:
            happysum += self.wordscores[word]
            count += 1

        if count != 0:  # divide by zero errors are sad.
            return happysum / count
        else:
            pass  # empty lists have no score
