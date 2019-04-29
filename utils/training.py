from gensim.test.utils import get_tmpfile
from gensim.models import Word2Vec 
from gensim.models import Doc2Vec
from multiprocessing import cpu_count
import logging
import time

num_cores = cpu_count()


def train_model(lang, model):
    if (model == "Word2Vec"):
        start = time.time()

        logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
        model = Word2Vec(corpus_file=get_tmpfile('../resources/corpus/opensub2018.en.cor'), workers=cpu_count())
        model.save(get_tmpfile('../resources/models/opensub2018_en.bin'))

        end = time.time()
        elapsed = end - start

        print('Time elapsed: %f' % elapsed)
    if (model == "Doc2Vec"):
        start = time.time()

        logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
        model = Doc2Vec(corpus_file=get_tmpfile('../resources/corpus/opensub2018.en.cor'), epochs=5, vector_size=5, workers=cpu_count())
        model.save(get_tmpfile('../resources/models/opensub2018doc_en.bin'))

        end = time.time()
        elapsed = end - start

        print('Time elapsed: %f' % elapsed)

# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
# model = Word2Vec(corpus_file=get_tmpfile('../resources/corpus/opensub2018.sp.cor'), workers=cpu_count())
# model.save(get_tmpfile('../resources/models/opensub2018_sp.bin'))

# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
# model = Doc2Vec(corpus_file=get_tmpfile('../resources/corpus/opensub2018.sp.cor'), epochs=5, vector_size=5, workers=cpu_count())
# model.save(get_tmpfile('../resources/models/opensub2018doc_sp.bin'))
