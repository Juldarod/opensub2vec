from settings import APP_STATIC
from gensim.models.word2vec import Word2Vec
import os


def load_model(model, lang, phrases=1):

    w2v_path = os.path.join(
        APP_STATIC, 'models/{}/{}/opensub2018_phrases_'.format())
    model = Word2Vec.load(w2v_path + "sg.bin", mmap='r')
    return model
