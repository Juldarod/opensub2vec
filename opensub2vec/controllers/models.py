from settings import APP_STATIC
from gensim.models.translation_matrix import TranslationMatrix
from gensim.models.word2vec import Word2Vec
from gensim.models.fasttext import FastText


import os
import spacy

spacy_en = spacy.load('en_core_web_sm')
spacy_es = spacy.load('es_core_news_sm')


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


def remove_stopwords(lang, phrase):
    if lang == 'en':
        return [word.text.lower() for word in spacy_en(phrase) if not word.is_stop]
    else:
        return [word.text.lower() for word in spacy_es(phrase) if not word.is_stop]


def translate_phrase(model, phrase):
    words = remove_stopwords('en', phrase)
    return [list(model.translate([word], topn=5).values()) for word in words]


# source and target are a list of strings
def get_wmdistance(model, source, target):
    source = ' '.join(source)
    target = ' '.join(target)
    print(source)
    print(target)
    return model.wmdistance(source, target)
