### pyhmeter ###
#### A Python implementation of a hedonometer ####

*"All who joy would win must share it. Happiness was born a Twin." -Lord Byron*
***

1. Import the package

    >>> import pyhmeter

#. Create an object

    >>> some_list = ['I', 'love', 'pancakes', 'laughter', 'and', 'hate', 'terrorism']

#. Create an object

    >>> h = pyhmeter.HMeter(some_list)

#. Show words from the list that have a match in the list of word scores.

    >>> print h.matchlist
    ['love', 'pancakes', 'laughter', 'and', 'hate', 'terrorism']

#. Show happiness score

    >>> print h.happiness_score()

#. Change value of deltah

    >>> h.set_deltah(1.0) # accepts floating point value
    >>> print h.matchlist
    ['love', 'pancakes', 'laughter', 'hate', 'terrorism']    
    >>> h.set_deltah(3.0)
    ['love', 'laughter', 'terrorism']

Reference: [Temporal Patterns of Happiness and Information in a Global Social Network: Hedonometrics and Twitter](http://www.plosone.org/article/info:doi/10.1371/journal.pone.0026752)
