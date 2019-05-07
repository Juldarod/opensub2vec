from gensim.test.utils import get_tmpfile
from gensim.models import Word2Vec 
from gensim.models import Doc2Vec
from multiprocessing import cpu_count
from pathlib import Path
import logging
import time

num_cores = cpu_count()

def train_model(lang, model):
    if (model == "Word2Vec"):
        start = time.time()

        logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
        
        if(lang == "en"):
            model = Word2Vec(corpus_file=get_tmpfile(Path('./resources/corpus/opensub2018.en.cor').absolute()), sg=1, workers=cpu_count())
            model.save('./resources/models/opensub2018_en_sg.bin')
            model = Word2Vec(corpus_file=get_tmpfile(Path('./resources/corpus/opensub2018.en.cor').absolute()), workers=cpu_count())
            model.save('./resources/models/opensub2018_en_cbow.bin')
        elif(lang == "sp"):
            model = Word2Vec(corpus_file=get_tmpfile(Path('./resources/corpus/opensub2018.sp.cor').absolute()), sg=1, workers=cpu_count())
            model.save('./resources/models/opensub2018_sp_sg.bin')
            model = Word2Vec(corpus_file=get_tmpfile(Path('./resources/corpus/opensub2018.sp.cor').absolute()), workers=cpu_count())
            model.save('./resources/models/opensub2018_sp_cbow.bin')
        else:
            print("Language not available")

        end = time.time()
        elapsed = end - start

        print('Time elapsed: %f' % elapsed)
    elif(model == "Doc2Vec"):
        start = time.time()

        logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

        if(lang == "en"):
            model = Doc2Vec(corpus_file=get_tmpfile(Path('./resources/corpus/opensub2018.en.cor').absolute()), epochs=5, vector_size=5, dm=1, workers=cpu_count())
            model.save('./resources/models/opensub2018_en_dm.bin')
            model = Doc2Vec(corpus_file=get_tmpfile(Path('./resources/corpus/opensub2018.en.cor').absolute()), epochs=5, vector_size=5, workers=cpu_count())
            model.save('./resources/models/opensub2018_en_dbow.bin')
        elif(lang == "sp"):
            model = Doc2Vec(corpus_file=get_tmpfile(Path('./resources/corpus/opensub2018.sp.cor').absolute()), epochs=5, vector_size=5, dm=1, workers=cpu_count())
            model.save('./resources/models/opensub2018_sp_dm.bin')
            model = Doc2Vec(corpus_file=get_tmpfile(Path('./resources/corpus/opensub2018.sp.cor').absolute()), epochs=5, vector_size=5, workers=cpu_count())
            model.save('./resources/models/opensub2018_sp_dbow.bin')
        else:
            print("Language not available")

        end = time.time()
        elapsed = end - start

        print('Time elapsed: %f' % elapsed)
    else:
        print("Model not available")
