import sys,re,os,logging
from nltk.corpus import words
from functools import reduce
import pandas as pd
import numpy as np
from word_index_filter import WordIndexFilter

logger = logging.getLogger(__name__)

class WordIndex:
    def __init__(self, length, word_count=3, word_filter ='default'):
        if word_filter == 'default':
            self.word_filter = WordIndexFilter().filter_word
        else:
            if type(word_filter) != WordIndexFilter:
                raise ValueError('Please specify a valid WordIndexFilter class')
            self.word_filter = word_filter.filter_word
        logger.info('Building index vocabulary')
        self._build_vocabulary()
        self._length = length
        self._words = word_count


    def generate_word_index(self):
        ind = pd.DataFrame(np.random.choice(self.filtered_list, (self._length, self._words), True)).drop_duplicates()
        ind.sort_values(by=list(ind.columns), inplace=True)
        ind = ind.apply(self._combine_words, axis=1).reset_index(drop=True)
        return ind


    def _build_vocabulary(self):
        self.raw_word_list = [i.lower() for i in words.words()]
        logger.info('Vocabulary words loaded: ' + str(len(self.raw_word_list)))
        self.filtered_list = [i for i in filter(self.word_filter, self.raw_word_list)]
        logger.info('Filtered word list length: ' + str(len(self.filtered_list)))

    def _combine_words(self, l):
        return reduce((lambda x, y: x + '.' + y), l)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    twi = WordIndex(30)



