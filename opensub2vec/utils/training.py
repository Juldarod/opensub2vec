from pathlib import Path

from gensim.test.utils import get_tmpfile
from gensim.models.word2vec import Word2Vec 
from gensim.models.doc2vec import Doc2Vec
from multiprocessing import cpu_count

import logging
import time

num_cores = cpu_count()
# print(Path('./resources/corpus/opensub2018_en.cor').absolute())

def train_model(lang, model):
    if (model == "Word2Vec"):
        start = time.time()

        logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
        # logging.basicConfig(filename=logname, filemode='a', format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
        
        if(lang == "en"):
            model = Word2Vec(corpus_file=get_tmpfile(Path('./resources/corpus/opensub2018_en.cor').absolute()), sg=1, workers=cpu_count())
            model.save('./resources/models/doc2vec/opensub2018_en_sg.kv')
            model = Word2Vec(corpus_file=get_tmpfile(Path('./resources/corpus/opensub2018_en.cor').absolute()), workers=cpu_count())
            model.save('./resources/models/doc2vec/opensub2018_en_cbow.kv')
        elif(lang == "es"):
            model = Word2Vec(corpus_file=get_tmpfile(Path('./resources/corpus/opensub2018_es.cor').absolute()), sg=1, workers=cpu_count())
            model.save('./resources/models/doc2vec/opensub2018_es_sg.kv')
            model = Word2Vec(corpus_file=get_tmpfile(Path('./resources/corpus/opensub2018_es.cor').absolute()), workers=cpu_count())
            model.save('./resources/models/doc2vec/opensub2018_es_cbow.kv')
        else:
            print("Language not available")

        end = time.time()
        elapsed = end - start

        print('Time elapsed: %f' % elapsed)
    elif(model == "Doc2Vec"):
        start = time.time()

        logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
        # logging.basicConfig(filename=logname, filemode='a', format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

        if(lang == "en"):
            model = Doc2Vec(corpus_file=get_tmpfile(Path('./resources/corpus/opensub2018_en.cor').absolute()), epochs=5, vector_size=5, dm=1, workers=cpu_count())
            model.save('./resources/models/doc2vec/opensub2018_en_dm.kv')
            model = Doc2Vec(corpus_file=get_tmpfile(Path('./resources/corpus/opensub2018_en.cor').absolute()), epochs=5, vector_size=5, workers=cpu_count())
            model.save('./resources/models/doc2vec/opensub2018_en_dbow.kv')
        elif(lang == "es"):
            model = Doc2Vec(corpus_file=get_tmpfile(Path('./resources/corpus/opensub2018_es.cor').absolute()), epochs=5, vector_size=5, dm=1, workers=cpu_count())
            model.save('./resources/models/doc2vec/opensub2018_es_dm.kv')
            model = Doc2Vec(corpus_file=get_tmpfile(Path('./resources/corpus/opensub2018_es.cor').absolute()), epochs=5, vector_size=5, workers=cpu_count())
            model.save('./resources/models/doc2vec/opensub2018_es_dbow.kv')
        else:
            print("Language not available")

        end = time.time()
        elapsed = end - start

        print('Time elapsed: %f' % elapsed)
    else:
        print("Model not available")
