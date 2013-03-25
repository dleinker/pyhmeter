import csv

def hmeter(corpus, deltah=0.0, wordcount=False):
    """Takes a list of individual words and returns the happiness score.
    deltah removes stop words as per Dodd paper, wordcount returns how many 
    words matched the Dodd wordlist."""
    # open tab-delimited word list from Dodd paper
    dataset = csv.reader(open("DataSetS1.csv", "r"), delimiter='\t')
    wordscores = {}

    # create a dict based on the 'name' and 'happiness_average' columns
    for row in dataset:
        wordscores[row[0]] = row[2]
    
    count = 0
    happysum = float(0)
    deltah = float(deltah)
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
                count += 1

    if count != 0: # divide by zero errors are sad.
        if not wordcount:
            return happysum / count # dividing by the count gives us the mean.
        else:   
            return happysum / count, count # also return count of matched words
    else:
        return 0.0
