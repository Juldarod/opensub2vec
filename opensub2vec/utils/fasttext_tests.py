from gensim.models.fasttext import load_facebook_model, load_facebook_vectors
from gensim.models.fasttext import FastText
from gensim.models.keyedvectors import FastTextKeyedVectors
# from gensim.similarities.index import AnnoyIndexer
import logging
import time


# root_path = '../resources/models/fasttext/'
root_path = '../resources/models/fasttext-pretrained/'

logging.basicConfig(
    format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


def load_model():
    start = time.time()
    en_vecs = FastTextKeyedVectors.load(root_path + 'cc.en.300.bin', mmap='r')
    end = time.time()
    elapsed = end - start
    print('Model loaded in: %f seconds' % elapsed)
    # indexer = AnnoyIndexer(en_vecs, 2)
    # res = en_vecs.most_similar_cosmul('house', topn=1, indexer=indexer)
    res = en_vecs.most_similar_cosmul('house', topn=1)
    return '{} with {}% probability'.format(res[0][0], res[0][1])
    # return 'Model loaded in: %f seconds' % elapsed


# print(en_vecs['king'])
# print(en_vecs.most_similar_cosmul('house'))
