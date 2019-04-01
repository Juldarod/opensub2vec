from gensim.test.utils import get_tmpfile
from gensim.models import Word2Vec
from multiprocessing import cpu_count
from pathlib import Path
import logging

num_cores = cpu_count()

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
model = Word2Vec(corpus_file=get_tmpfile(Path('../resources/corpus/opensub2018.en.cor').absolute()), workers=cpu_count())
model.save('../resources/models/opensub2018.en.model')

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
model = Word2Vec(corpus_file=get_tmpfile(Path('../resources/corpus/opensub2018.sp.cor').absolute()), workers=cpu_count())
model.save('../resources/models/opensub2018.sp.model')
