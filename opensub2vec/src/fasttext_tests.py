from gensim.models.fasttext import load_facebook_model, load_facebook_vectors
from gensim.models.fasttext import FastText
from gensim.models.keyedvectors import KeyedVectors, FastTextKeyedVectors
# import fasttext
import logging
import dill


root_path = '../resources/models/fasttext-pretrained/'

logging.basicConfig(
    format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
# en_vecs = fasttext.load_model(root_path + 'cc.en.300.bin')
# en_vecs = load_facebook_model(root_path + 'cc.en.300.bin')
# en_vecs = KeyedVectors.load_word2vec_format(root_path + 'cc.en.300.vec')
# en_vecs = FastTextKeyedVectors.load(root_path + 'cc.en.300', mmap='r')

# save your model as
# with open('../resources/models/fasttext/cc.en.300.bin', 'wb') as f:
# dill.dump(en_vecs, f)
# en_vecs.save('../resources/models/fasttext/cc.en.300.bin')


es_vecs = load_facebook_model(root_path + 'cc.es.300.bin')
# with open('../resources/models/fasttext/cc.es.300.bin', 'wb') as f:
# dill.dump(es_vecs, f)
es_vecs.save('../resources/models/fasttext/cc.es.300.bin')

# en_vecs = KeyedVectors.load('../resources/models/fasttext/cc.en.300.bin', mmap='r')
# en_vecs1 = KeyedVectors.load('../resources/models/fasttext/cc.en.300', mmap='r')

# print(en_vecs['king'])
# print(en_vecs1.get_vector('king'))
# print(en_vecs['king'] == en_vecs1.get_vector('king'))
# print(en_vecs.most_similar_cosmul('man'))
# print(en_vecs.most_similar_cosmul('woman'))
