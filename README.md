#pyhmeter
##A hedonometer implmentation using python

*"All who joy would win must share it. Happiness was born a Twin." -Lord Byron*
***

A hedonometer is a [device](http://en.wikipedia.org/wiki/Hedonometer) that measures happiness. This python based hedonometer assigns a numerical score to a body of text based on the methodology described in [this paper](http://www.plosone.org/article/info:doi/10.1371/journal.pone.0026752). As with any progammatic process that attempts to distill the complexities of human expression into 1s and 0s this comes with major caveats. I implore you to read Dodd et al.'s work before using this for anything serious.

Some important concepts: HMeter expects a list of individual words, for example the result of [nltk.word_tokenize](http://nltk.org/api/nltk.tokenize.html). The matchlist attribute contains all words in the sample that have a score according the word scores provided by the Dodd paper. The hedonometer allows for 'tuning' by removing the most neutral words from the matchlist. This is done using the set_deltah method and will generate a new matchlist based on the new deltah.

##Example Use

In this example we take a list and find its base happiness score and then its happiness score after filtering out neutral words.

	>>> import pyhmeter
    >>> some_list = ['I', 'love', 'pancakes', 'laughter', 'and', 'hate', 'terrorism', '<HTML>', 'zoidberg']
    >>> h = pyhmeter.HMeter(some_list)
    >>> h.matchlist
    ['love', 'pancakes', 'laughter', 'and', 'hate', 'terrorism']
    >>> h.happiness_score()
    5.4866666666666655
    >>> h.set_deltah(1.0)  # accepts floating point value
    >>> h.matchlist
    ['love', 'pancakes', 'laughter', 'hate', 'terrorism']
    >>> h.happiness_score()
    5.54
    >>> h.set_deltah(3.0)
    >>> h.matchlist
    ['love', 'laughter', 'terrorism']
    >>> h.happiness_score()
    6.133333333333334

Reference: [Temporal Patterns of Happiness and Information in a Global Social Network: Hedonometrics and Twitter](http://www.plosone.org/article/info:doi/10.1371/journal.pone.0026752)
