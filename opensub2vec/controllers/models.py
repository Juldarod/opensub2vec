from settings import APP_STATIC
from gensim.models.word2vec import Word2Vec
import os


def load_model():
    w2v_path = os.path.join(
        APP_STATIC, 'models/word2vec/english/opensub2018_phrases_')
    model = Word2Vec.load(w2v_path + "sg.bin", mmap='r')
    return model
