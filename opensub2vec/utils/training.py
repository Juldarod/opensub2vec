from os import listdir
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
            model = Word2Vec(corpus_file=get_tmpfile(Path('../resources/corpus/opensub2018_en.cor').absolute()), sg=1, workers=cpu_count())
            model.save('../resources/models/word2vec/opensub2018_en_sg.bin')
            model = Word2Vec(corpus_file=get_tmpfile(Path('../resources/corpus/opensub2018_en.cor').absolute()), workers=cpu_count())
            model.save('../resources/models/word2vec/opensub2018_en_cbow.bin')
        elif(lang == "es"):
            model = Word2Vec(corpus_file=get_tmpfile(Path('../resources/corpus/opensub2018_es.cor').absolute()), sg=1, workers=cpu_count())
            model.save('../resources/models/word2vec/opensub2018_es_sg.bin')
            model = Word2Vec(corpus_file=get_tmpfile(Path('../resources/corpus/opensub2018_es.cor').absolute()), workers=cpu_count())
            model.save('../resources/models/word2vec/opensub2018_es_cbow.bin')
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
            model = Doc2Vec(corpus_file=get_tmpfile(Path('../resources/corpus/opensub2018_en.cor').absolute()), epochs=5, vector_size=5, dm=1, workers=cpu_count())
            model.save('../resources/models/doc2vec/opensub2018_en_dm.bin')
            model = Doc2Vec(corpus_file=get_tmpfile(Path('../resources/corpus/opensub2018_en.cor').absolute()), epochs=5, vector_size=5, workers=cpu_count())
            model.save('../resources/models/doc2vec/opensub2018_en_dbow.bin')
        elif(lang == "es"):
            model = Doc2Vec(corpus_file=get_tmpfile(Path('../resources/corpus/opensub2018_es.cor').absolute()), epochs=5, vector_size=5, dm=1, workers=cpu_count())
            model.save('../resources/models/doc2vec/opensub2018_es_dm.bin')
            model = Doc2Vec(corpus_file=get_tmpfile(Path('../resources/corpus/opensub2018_es.cor').absolute()), epochs=5, vector_size=5, workers=cpu_count())
            model.save('../resources/models/doc2vec/opensub2018_es_dbow.bin')
        else:
            print("Language not available")

        end = time.time()
        elapsed = end - start

        print('Time elapsed: %f' % elapsed)
    else:
        print("Model not available")


# start = time.time()

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# model = Word2Vec(corpus_file=get_tmpfile(Path('../resources/corpus/english/opensub2018.cor').absolute()), sg=1, workers=cpu_count())
# model.save('../resources/models/word2vec/english/opensub2018_sg.bin')
# model.wv.save('../resources/models/word2vec/english/opensub2018_sg.kv')
# model = Word2Vec(corpus_file=get_tmpfile(Path('../resources/corpus/english/opensub2018.cor').absolute()), workers=cpu_count())
# model.save('../resources/models/word2vec/english/opensub2018_cbow.bin')
# model.wv.save('../resources/models/word2vec/english/opensub2018_cbow.kv')
# model = Word2Vec(corpus_file=get_tmpfile(Path('../resources/corpus/spanish/opensub2018.cor').absolute()), sg=1, workers=cpu_count())
# model.save('../resources/models/word2vec/spanish/opensub2018_sg.bin')
# model.wv.save('../resources/models/word2vec/spanish/opensub2018_sg.kv')
# model = Word2Vec(corpus_file=get_tmpfile(Path('../resources/corpus/spanish/opensub2018.cor').absolute()), workers=cpu_count())
# model.save('../resources/models/word2vec/spanish/opensub2018_cbow.bin')
# model.wv.save('../resources/models/word2vec/spanish/opensub2018_cbow.kv')

# model = Doc2Vec(dm=1, workers=cpu_count(), min_count=10, vector_size=400, negative=5)
# model.build_vocab(corpus_file=get_tmpfile(Path('../resources/corpus/english/part000').absolute()))
# model.train(corpus_file=get_tmpfile(Path('../resources/corpus/english/part000').absolute()), total_words=model.corpus_count, epochs=5)
# model.build_vocab(corpus_file=get_tmpfile(Path('../resources/corpus/english/part001').absolute()), update=True)
# model.train(corpus_file=get_tmpfile(Path('../resources/corpus/english/part001').absolute()), total_words=model.corpus_count, epochs=5)
# model.save('../resources/models/doc2vec/english/opensub2018_dm.bin')
# model.wv.save('../resources/models/doc2vec/english/opensub2018_dm.kv')

# files = listdir(Path('../resources/corpus/english/parts').absolute())

# model = Doc2Vec(dm=1, workers=cpu_count(), min_count=10, vector_size=400, negative=5)

# for f in files:
#     if (f[-3:] == "000"):
#         model.build_vocab(corpus_file=get_tmpfile(Path('../resources/corpus/english/parts/part000').absolute()))
#     else:
#         model.build_vocab(corpus_file=get_tmpfile(Path('../resources/corpus/english/parts/part{}'.format(f[-3:])).absolute()), update=True)

#     model.train(corpus_file=get_tmpfile(Path('../resources/corpus/english/parts/part{}'.format(f[-3:])).absolute()), total_words=model.corpus_count, epochs=5)

# model.save('../resources/models/doc2vec/english/opensub2018_dm.bin')
# model.wv.save('../resources/models/doc2vec/english/opensub2018_dm.kv')

files = listdir(Path('../resources/corpus/spanish/parts').absolute())

model = Doc2Vec(dm=1, workers=cpu_count(), min_count=10, vector_size=400, negative=5)

for f in files:
    if (f[-3:] == "000"):
        model.build_vocab(corpus_file=get_tmpfile(Path('../resources/corpus/spanish/parts/part000').absolute()))
    else:
        model.build_vocab(corpus_file=get_tmpfile(Path('../resources/corpus/spanish/parts/part{}'.format(f[-3:])).absolute()), update=True)

    model.train(corpus_file=get_tmpfile(Path('../resources/corpus/spanish/parts/part{}'.format(f[-3:])).absolute()), total_words=model.corpus_count, epochs=5)

model.save('../resources/models/doc2vec/spanish/opensub2018_dm.bin')
model.wv.save('../resources/models/doc2vec/spanish/opensub2018_dm.kv')



# model = Doc2Vec(corpus_file=get_tmpfile(Path('../resources/corpus/english/opensub2018.cor').absolute()), epochs=5, vector_size=4, workers=cpu_count())
# model.save('../resources/models/doc2vec/english/opensub2018_dbow.bin')
# model.wv.save('../resources/models/doc2vec/english/opensub2018_dbow.kv')
# model = Doc2Vec(corpus_file=get_tmpfile(Path('../resources/corpus/spanish/opensub2018.cor').absolute()), epochs=5, vector_size=4, dm=1, workers=cpu_count())
# model.save('../resources/models/doc2vec/spanish/opensub2018_dm.bin')
# model.wv.save('../resources/models/doc2vec/spanish/opensub2018_dm.kv')
# model = Doc2Vec(corpus_file=get_tmpfile(Path('../resources/corpus/spanish/opensub2018.cor').absolute()), epochs=5, vector_size=4, workers=cpu_count())
# model.save('../resources/models/doc2vec/spanish/opensub2018_dbow.bin')
# model.wv.save('../resources/models/doc2vec/spanish/opensub2018_dbow.kv')
