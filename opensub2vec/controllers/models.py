from settings import APP_STATIC
from gensim.models.translation_matrix import TranslationMatrix
# from gensim.models.word2vec import Word2Vec
# from gensim.models.fasttext import FastText
from gensim.models.keyedvectors import KeyedVectors
from gensim.models.phrases import Phraser


import os


def load_model(name, lang):
    model_path = os.path.join(
        APP_STATIC, '{}/opensub2018_{}_sg.bin'.format(name, lang))
    # if(name == 'word2vec'):
    #     return Word2Vec.load(model_path, mmap='r')
    # else:
    #     return FastText.load(model_path, mmap='r')
    return KeyedVectors.load(model_path, mmap='r')


def load_translation_matrix(name, source, target):
    model_path = os.path.join(
        APP_STATIC, 'translation_matrix/{}/opensub2018_{}_to_{}.bin'.format(name, source, target))
    return TranslationMatrix.load(model_path, mmap='r')


def load_phraser(lang):
    model_path = os.path.join(
        APP_STATIC, 'phrases/opensub2018_{}.bin'.format(lang))
    return Phraser.load(model_path, mmap='r')


def msimilar(model, word):
    return list(model.most_similar_cosmul(word, topn=10))


def analogy(model, words):
    word_array = words.split()
    print(word_array)
    return list(model.most_similar_cosmul(
        positive=[word_array[0], word_array[1]],
        negative=[word_array[2]]
    ))


def phraser(model, sentence):
    tokenized_sentence = sentence.split()
    return ' '.join(model[tokenized_sentence])
