# Human Word Indexes
#### Inspired by [What3Words](https://map.what3words.com/daring.lion.race)
This library allows the creation of human-memorable/legible english word indexes for 
pandas dataframes (or other datasets) in python.

```python
from human_word_indexes import WordIndexGenerator,WordIndexFilter  
twi = WordIndexGenerator(10)
twi.generate_word_index()
# ------OUTPUT------
# 0     colorado.bonellia.dulbert
# 1      heaven.naturism.boonless
# 2      inweave.sabbath.gimbaled
# 3           kolokolo.becky.paho
# 4      laudism.sinamay.encyclic
# 5          locate.nyctea.hymnic
# 6     overhelp.depilous.denmark
# 7    sparring.relaster.ungently
# 8     spudboy.lounging.undigest
# 9      unthorny.engore.gageable
# dtype: object
word_filter = WordIndexFilter().set_max_length(5).set_min_length(1)
twi = WordIndexGenerator(5,word_count=2,word_filter=word_filter)
twi.generate_word_index()
# 0    beray.revet
# 1     mukri.swab
# 2     rabin.file
# 3     shogi.poop
# 4     talc.bison
# dtype: object


```

## Quickstart
- Run `pip install human_word_indexes`
- Install the nltk word corpuses with `nltk.download()`


