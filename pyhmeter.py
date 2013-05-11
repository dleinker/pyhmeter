from __future__ import division
import csv

def load_scores(filename):
    """Takes a file from the Dodd research paper and returns a dict of
    wordscores. Note this function is tailored to the file provided
    by the Dodd paper. For other sets of word scores, a dict can be
    passed directly to HMeter."""
    
    doddfile = csv.reader(open(filename, "r"), delimiter='\t')
    for x in xrange(4):  # strip header info
        doddfile.next()

    return {row[0]: float(row[2]) for row in doddfile}

class HMeter(object):
    """HMeter is the main class to prepare a text sample for scores. It
    expects a list of individual words, such as those provided by 
    nltk.word_tokenize, as wordlist. It expects a dict of words as k and
    floating point wordscores as v for wordscores. deltah allows us to 
    filter out the most neutral words as stop words."""

    def __init__(self, wordlist, wordscores, deltah=0.0):
        self.wordlist = wordlist
        self.wordscores = wordscores
        self.deltah = deltah

    _deltah = None
    @property
    def deltah(self):
        """Deltah determines stop words. The higher deltah the more neutral 
        words are are discarded from the matchlist."""
        return self._deltah

    @deltah.setter
    def deltah(self, deltah):
        """Each time deltah is set we need to regenerate the matchlist."""
        self._deltah = deltah
        # TODO Should probably raise a range error if deltah is nonsensical
        # first we take every word that matches labMT 1.0
        labmtmatches = (word for word in self.wordlist
                        if word in self.wordscores)

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
        """Produces data necessary to create a word shift graph. Returns a list 
        of tuples that contain each word's contribution to happiness score shift 
        between two samples. So for example, assigned to a variable 'output_data'
        output_data[n] represents the data for one word where:
            
        output_data[n][0] the word
        output_data[n][1] the proportional contribution the word gives to overall
                          word shift
        output_data[n][2] The relative abundance of word between the two samples
        output_data[n][3] The word's happiness relative to the refernce sample
        
        Using this data, we can construct word shift graphs as described here:
        http://www.hedonometer.org/shifts.html"""

        # initialize variables for potentially large loop.
        # create our comparison object. self is the reference object.
        tcomp = HMeter(comp, self.deltah)

        # we want a list of all potential words, but only need each word once.
        word_shift_list = set(tcomp.matchlist + self.matchlist)

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

        # sort words by absolute value of individual word shift
        output_data.sort(key=lambda word: abs(word[1]))
        return output_data

    def happiness_score(self):
        """Takes a list made up of individual words and returns the happiness
        score."""

        happysum = 0
        count = len(self.matchlist)

        for word in self.matchlist:
            happysum += self.wordscores[word]

        if count != 0:  # divide by zero errors are sad.
            return happysum / count
        else:
            pass  # empty lists have no score
