from gensim.models.fasttext import load_facebook_model, load_facebook_vectors
from gensim.models.fasttext import FastText
from gensim.models.keyedvectors import KeyedVectors, FastTextKeyedVectors
import fasttext
import logging

root_path = "../resources/models/fasttext-pretrained/"

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
# en_vecs = fasttext.load_model(root_path + "cc.en.300.bin")
# en_vecs = load_facebook_vectors(root_path + "cc.en.300.bin")
en_vecs = KeyedVectors.load_word2vec_format(root_path + "cc.en.300.vec")
# en_vecs = FastTextKeyedVectors.load(root_path + "cc.en.300.vec", mmap='r')

# print(en_vecs['king'])
print(en_vecs.most_similar('king'))