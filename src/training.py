from pathlib import Path
import logging
from gensim.models.word2vec import LineSentence
from gensim.utils import save_as_line_sentence
from gensim.test.utils import get_tmpfile
from gensim.models import Word2Vec

# corpus = open('/home/julda/Documents/opensub2018.cor', 'r')
# corpus_fname = get_tmpfile('/home/julda/Documents/opensub2018-line.cor')
# save_as_line_sentence(corpus, corpus_fname)
# corpus.close()
# sentences = LineSentence(corpus)

# path = get_tmpfile('opensub2018.model')
# print(str(file))

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
# model = Word2Vec(corpus_file=get_tmpfile('/home/julda/Documents/opensub2018.cor'), workers=4)
model = Word2Vec(corpus_file=get_tmpfile('D:\OpenSubtitles2018.en\opensub2018.cor'), workers=4)
model.save('opensub2018.model')