import string
import random
import numpy as np
from collections import Counter

"""
COLE BARDIN
14422557

ASSIGNMENT: COMPLETE function XXX below
"""

"""
ECE 105: Programming for Engineers 2
Created September 5, 2020
Steven Weber
Mandelbrot random sentence construction starter code

This code creates a "sentence" using Mandelbrot's random construction.  It leverages the stick-breaking distribution for letter frequencies as found in:

Richard Perline, "The random division of the unit interval and the approximate -1 exponent in the monkey-at-the-typewriter model of Zipf's law", submitted to Statistics and Probability Letters, 2015
"""

# get_alphabet: returns the alphabet for the language as a string
def get_alphabet(alphabet_size):
    return list(' ' + string.ascii_lowercase)[:alphabet_size+1]

"""
COMPLETE:
get_letter_disbn takes an alphabet as argument and returns a probability distribution using the stick-breaking algorithm
1. use np.random.uniform() to generate len(alphabet)-1 uniform RVs on [0,1]
2. sort them from smallest to largest
3. prepend with 0, append with 1, and take the K differences
4. sort differences, these are letter frequencies
5. return sorted differences
"""
# get_letter_disbn: returns the stick letter probability distribution
def get_letter_disbn(alphabet):
    # 1. let n = len(alphabet), note n includes the space
    n = len(alphabet)
    # generate n-1 independent uniform RVs on [0,1]
    rvs = np.random.uniform(0,1,n-1)
    # 2. sort them from smallest to largest
    rvs.sort()
    # 3. prepend with 0, append with 1, and take the K differences
    diffs = np.diff(rvs, prepend=0, append=1)
    # 4. sort the differences; these are the stick-breaking distribution
    # letter frequencies
    # 5 return sorted letter frequencies
    return sorted(diffs)

# generate_sentence: generate random sentence from alphabet of prescribed length
def generate_sentence(alphabet, sentence_len, letter_disbn):
    return ''.join(np.random.choice(alphabet, size=sentence_len, p=letter_disbn))

# word_counts: compute the list of words and counts from list of words
def word_counts(words, min_count):
    word_counter = Counter(words).most_common()
    return [count for count in word_counter if count[1] >= min_count]

# write_counts: write the word_counts data as a text file
def write_counts(counts, filename):
    with open(filename, 'w') as f:
        for c in counts:
            f.write('{} {}\n'.format(c[0],c[1]))

if __name__ == "__main__":
    # set parameters
    alphabet_size = 8 # alphabet size (excluding space) (between 2 and 26)
    target_num_words = 1000000 # target num. words to generate
    sentence_len = alphabet_size * target_num_words # length of sentence
    min_count = 5 # only keep words with occurrence > this
    filename = 'HW3-Solution.txt'

    alphabet = get_alphabet(alphabet_size) # generate alphabet
    letter_disbn = get_letter_disbn(alphabet) # random letter disbn
    sentence = generate_sentence(alphabet, sentence_len, letter_disbn) # random sentence
    words = sentence.split() # words in sentence
    counts = word_counts(words, min_count) # counts on words
    write_counts(counts, filename) # write to file
