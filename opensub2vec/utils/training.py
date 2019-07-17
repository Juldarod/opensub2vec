from os import listdir
from pathlib import Path
from multiprocessing import cpu_count

from gensim.test.utils import get_tmpfile
from gensim.models.phrases import Phrases, Phraser
from gensim.models.doc2vec import Doc2Vec
from gensim.models.word2vec import Word2Vec
from gensim.models.word2vec import LineSentence
from gensim.models.fasttext import FastText
from gensim.models.translation_matrix import TranslationMatrix
from gensim.models.keyedvectors import KeyedVectors

# from gensim.models.fasttext import load_facebook_model, load_facebook_vectors

import logging
import time


num_cores = cpu_count()
corpus_root_path = '../resources/corpus/'
model_root_path = '../resources/models/'


def build_phrase_model(lang):
    logging.basicConfig(
        format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    # mode = 'english' if lang == 'en' else 'spanish'
    mode = 'aligned'

    # sentences = LineSentence(Path('{}{}/opensub2018.cor'.format(
    #     corpus_root_path, mode)))
    sentences = LineSentence(Path('{}{}/opensub2018_{}.cor'.format(
        corpus_root_path, mode, lang)))

    phrases = Phrases(sentences=sentences, min_count=1, threshold=1)
    model_phrases = Phraser(phrases)
    model_phrases.save(
        '{}phrases/{}/opensub2018_{}.bin'.format(model_root_path, mode, lang))


def train_w2v(lang="en", kind='aligned', mode=1):
    start = time.time()

    logging.basicConfig(
        format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

    mode_str = 'sg' if mode == 1 else 'cbow'
    filename = 'opensub2018_phrases_{}'.format(
        lang) if kind == 'aligned' else 'opensub2018_phrases'

    model = Word2Vec(
        corpus_file=get_tmpfile(
            Path('{}{}/{}.cor'.format(corpus_root_path, kind, filename)).absolute()),
        sg=mode,
        size=300,
        workers=num_cores)
    model.save(
        '{}word2vec/{}/{}_{}.bin'.format(model_root_path, kind, filename, mode_str))

    end = time.time()
    elapsed = end - start

    print('Time elapsed: %f' % elapsed)


def train_ft(lang="en", kind='aligned', mode=1):
    start = time.time()

    logging.basicConfig(
        format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

    mode_str = 'sg' if mode == 1 else 'cbow'
    filename = 'opensub2018_phrases_{}'.format(
        lang) if kind == 'aligned' else 'opensub2018_phrases'

    model = FastText(
        corpus_file=get_tmpfile(
            Path('{}{}/{}.cor'.format(corpus_root_path, kind, filename)).absolute()),
        sg=mode,
        size=300,
        workers=num_cores)
    model.save(
        '{}fasttext/{}/{}_{}.bin'.format(model_root_path, kind, filename, mode_str))

    end = time.time()
    elapsed = end - start

    print('Time elapsed: %f' % elapsed)


def train_pt_ft(lang="en"):
    # Load models from facebook's pretrained models and store them into a
    # new file as a gensim's FastText object
    # en_vecs = load_facebook_model(root_path + 'cc.en.300.bin')
    # en_vecs.save('../resources/models/fasttext/cc.en.300.bin')
    # es_vecs = load_facebook_model(root_path + 'cc.es.300.bin')
    # es_vecs.save('../resources/models/fasttext/cc.es.300.bin')

    en_model = FastText.load(
        '{}fasttext-pretrained/cc.{}.300.bin'.format(model_root_path, lang))
    en_model.build_vocab(
        corpus_file=get_tmpfile(Path(
            '{}aligned/opensub2018_{}.cor'.format(corpus_root_path, lang)).absolute()),
        update=True)
    en_model.train(
        corpus_file=get_tmpfile(Path(
            '{}aligned/opensub2018_{}.cor'.format(corpus_root_path, lang)).absolute()),
        total_examples=en_model.corpus_count,
        epochs=en_model.iter,
        workers=num_cores)
    en_model.save(
        '{}fasttext/cc.{}.300.test.bin'.format(model_root_path, lang))


def train_translation_matrix(model='fasttext', source_lang='en', target_lang='es', source='english', target='spanish'):

    source_word_vec_file = "{}{}/{}/opensub2018_phrases_sg.bin".format(
        model_root_path, model, source)
    target_word_vec_file = "{}{}/{}/opensub2018_phrases_sg.bin".format(
        model_root_path, model, target)
    # ################### Translation Matrix #########################################################

    start = time.time()

    logging.basicConfig(
        format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

    source_model = KeyedVectors.load(
        source_word_vec_file, mmap='r')
    target_model = KeyedVectors.load(
        target_word_vec_file, mmap='r')

    with open('../resources/word-pairs-formatted.txt', 'r') as f:
        word_pair = [tuple(line.strip().split()) for line in f]
    # print(word_pair[:10])

    trans_model = TranslationMatrix(
        source_model.wv, target_model.wv, word_pairs=word_pair)
    trans_model.train(word_pair)

    trans_model.save(
        '{}translation_matrix/english/opensub2018_to_{}.bin'.format(model_root_path, target))

    end = time.time()
    elapsed = end - start

    print('Time elapsed: %f' % elapsed)


# train_w2v()
# train_w2v(lang='es')
# train_w2v(kind='english')
# train_w2v(lang='es', kind='spanish')
# train_ft()
# train_ft(lang='es')
# train_ft(kind='english')
# train_ft(lang='es', kind='spanish')
train_translation_matrix(model='word2vec')
