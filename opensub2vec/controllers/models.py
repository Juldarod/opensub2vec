from settings import APP_STATIC
from gensim.models.translation_matrix import TranslationMatrix
from gensim.models.word2vec import Word2Vec
from gensim.models.fasttext import FastText

import os


def load_model(model, lang):

    model_path = os.path.join(
        APP_STATIC, '{}/opensub2018_{}_sg.bin'.format(model, lang))

    if(model == 'word2vec'):
        return Word2Vec.load(model_path, mmap='r')
    else:
        return FastText.load(model_path, mmap='r')


def load_translation_matrix(model):
    model_path = os.path.join(
        APP_STATIC, 'translation_matrix/{}/opensub2018_english_to_spanish.bin'.format(model))

    return TranslationMatrix.load(model_path, mmap='r')
