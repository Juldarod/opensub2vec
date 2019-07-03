from os import listdir
from pathlib import Path

from gensim.test.utils import get_tmpfile
from smart_open import open
from gensim.models.word2vec import Word2Vec
from gensim.models.doc2vec import Doc2Vec
from gensim.models.fasttext import FastText
from gensim.models.fasttext import load_facebook_model, load_facebook_vectors
from multiprocessing import cpu_count

import logging
import time

num_cores = cpu_count()
c_root = '../resources/corpus/'
m_root = '../resources/models/'
# print(Path('./resources/corpus/opensub2018_en.cor').absolute())


def train_w2v(lang="en", mode=1):
    start = time.time()

    logging.basicConfig(
        format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    # logging.basicConfig(filename=logname, filemode='a', format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

    mode_str = 'sg' if mode == 1 else 'cbow'

    model = Word2Vec(
        corpus_file=get_tmpfile(
            Path('{}opensub2018_{}.cor'.format(c_root, lang)).absolute()),
        sg=mode,
        workers=cpu_count())
    model.save('{}word2vec/opensub2018_{}_{}.bin'.format(m_root, lang, mode_str))

    end = time.time()
    elapsed = end - start

    print('Time elapsed: %f' % elapsed)


def train_d2v(lang="en", mode=1):
    start = time.time()

    logging.basicConfig(
        format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    # logging.basicConfig(filename=logname, filemode='a', format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

    mode_str = 'dm' if mode == 1 else 'dbow'

    model = Doc2Vec(
        corpus_file=get_tmpfile(
            Path('{}opensub2018_{}.cor'.format(c_root, lang)).absolute()),
        epochs=5,
        vector_size=5,
        dm=mode,
        workers=cpu_count())
    model.save('{}doc2vec/opensub2018_{}_{}.bin'.format(m_root, lang, mode_str))

    end = time.time()
    elapsed = end - start

    print('Time elapsed: %f' % elapsed)

    # Training by parts

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

    # files = listdir(Path('../resources/corpus/spanish/parts').absolute())

    # model = Doc2Vec(dm=1, workers=cpu_count(), min_count=10, vector_size=400, negative=5)

    # for f in files:
    #     if (f[-3:] == "000"):
    #         model.build_vocab(corpus_file=get_tmpfile(Path('../resources/corpus/spanish/parts/part000').absolute()))
    #     else:
    #         model.build_vocab(corpus_file=get_tmpfile(Path('../resources/corpus/spanish/parts/part{}'.format(f[-3:])).absolute()), update=True)

    #     model.train(corpus_file=get_tmpfile(Path('../resources/corpus/spanish/parts/part{}'.format(f[-3:])).absolute()), total_words=model.corpus_count, epochs=5)

    # model.save('../resources/models/doc2vec/spanish/opensub2018_dm.bin')
    # model.wv.save('../resources/models/doc2vec/spanish/opensub2018_dm.kv')


def train_pt_ft(lang="en"):
    # Load models from facebook's pretrained models and store them into a
    # new file as a gensim's FastText object
    # en_vecs = load_facebook_model(root_path + 'cc.en.300.bin')
    # en_vecs.save('../resources/models/fasttext/cc.en.300.bin')
    # es_vecs = load_facebook_model(root_path + 'cc.es.300.bin')
    # es_vecs.save('../resources/models/fasttext/cc.es.300.bin')

    en_model = FastText.load(
        '{}fasttext-pretrained/cc.{}.300.bin'.format(m_root, lang))
    en_model.build_vocab(
        corpus_file=get_tmpfile(Path(
            '{}aligned/opensub2018_{}.cor'.format(c_root, lang)).absolute()),
        update=True)
    en_model.train(
        corpus_file=get_tmpfile(Path(
            '{}aligned/opensub2018_{}.cor'.format(c_root, lang)).absolute()),
        total_examples=en_model.corpus_count,
        epochs=en_model.iter,
        workers=num_cores)
    en_model.save('{}fasttext/cc.{}.300.test.bin'.format(m_root, lang))


train_pt_ft(lang="es")
