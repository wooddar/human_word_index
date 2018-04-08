import sys,re,os
from nltk.corpus import words
from functools import reduce
import pandas as pd
import numpy as np


class ThreeWordIndex:
    def __init__(self):
        pass

    def cache_vocabulary(self):
        pass




r = re.compile(r'([a-zA-Z]).*?\1|oe|sc|kh')


def word_filter(w):
    if len(w) > 6 or \
            len(w) < 2 or \
            any([i == 'x' or i == 'z' for i in w]) or \
            bool(r.search(w)):
        return False
    else:
        return True


def combine_words(l):
    return reduce((lambda x, y: x + '.' + y), l)

wordlist = [i.lower() for i in words.words()]
print('total length', len(wordlist))
filtered_list = [i for i in filter(word_filter, wordlist)]
print('filtered list lenght', len(filtered_list))






three_word_index = pd.DataFrame(np.random.choice(filtered_list, (100000, 3), True)).drop_duplicates().apply(
    combine_words, axis=1)
