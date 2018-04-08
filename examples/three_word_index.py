import logging
import pandas as pd

from word_index.word_index import WordIndex

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

if __name__ == '__main__':
    twi = WordIndex(10)
    logging.log(twi.generate_word_index())