from pathlib import Path

from gensim.models.word2vec import Word2Vec
from gensim.models.keyedvectors import Word2VecKeyedVectors

import logging
import time


root_path = "../resources/models/word2vec/opensub2018_"
start = time.time()

# Models loading
sg_en_model = Word2Vec.load(root_path + "en_sg.bin", mmap='r')
cbow_en_model = Word2Vec.load(root_path + "en_cbow.bin", mmap='r')
sg_es_model = Word2Vec.load(root_path + "es_sg.bin", mmap='r')
cbow_es_model = Word2Vec.load(root_path + "es_cbow.bin", mmap='r')

# Vectors loading (wv)
sg_en_vectors = Word2VecKeyedVectors.load(root_path + "en_sg.kv", mmap='r')
sg_es_vectors = Word2VecKeyedVectors.load(root_path + "es_sg.kv", mmap='r')
cbow_en_vectors = Word2VecKeyedVectors.load(root_path + "en_cbow.kv", mmap='r')
cbow_es_vectors = Word2VecKeyedVectors.load(root_path + "es_cbow.kv", mmap='r')

# Get vocabulary
# vocab = sg_en_vectors.vocab
# for i in range(100):
#     print(list(vocab)[i])

end = time.time()
elapsed = end - start

print('Models loaded in: %f seconds' % elapsed)


# Testing similarity
# https://radimrehurek.com/gensim/models/keyedvectors.html#gensim.models.keyedvectors.Word2VecKeyedVectors.similarity

# English
# print(sg_en_vectors.similarity('woman', 'man'))
# print(cbow_en_vectors.similarity('woman', 'man'))

# # Spanish
# print(sg_es_vectors.similarity('mujer', 'hombre'))
# print(cbow_es_vectors.similarity('mujer', 'hombre'))


# Testing n_similarity
# https://radimrehurek.com/gensim/models/keyedvectors.html#gensim.models.keyedvectors.Word2VecKeyedVectors.n_similarity


# Testing most_similar
# https://radimrehurek.com/gensim/models/keyedvectors.html#gensim.models.keyedvectors.Word2VecKeyedVectors.most_similar

# print(sg_en_model.wv.most_similar_cosmul(positive=['woman', 'king'], negative=['man']))
# print(cbow_en_model.wv.most_similar_cosmul(positive=['woman', 'king'], negative=['man']))
# print(sg_es_vectors.most_similar('perro'))
# print(cbow_es_vectors.most_similar('perro'))
# print(sg_en_model.wv.most_similar('man'))
# print(cbow_en_model.wv.most_similar('man'))
# print(sg_en_model.wv.most_similar('house'))
# print(cbow_en_model.wv.most_similar('house'))


# Testing doesnt_match
# https://radimrehurek.com/gensim/models/keyedvectors.html#gensim.models.keyedvectors.Word2VecKeyedVectors.doesnt_match

# print(sg_es_vectors.doesnt_match("amarillo gato azul gris".split()))


# Testing wmdistance
# https://radimrehurek.com/gensim/models/keyedvectors.html#gensim.models.keyedvectors.Word2VecKeyedVectors.wmdistance

# print(sg_en_model.wmdistance("obama speaks to the media in illinois".split(), "the president greets the press in chicago".split()))
# print(sg_en_model.wmdistance("speaks".split(), "greets".split()))
# print(cbow_en_model.wmdistance("sports".split(), "sports".split()))


# ############################################ Accuracy ####################################################
# model_corp_file_accuracy = word_en__vectors.wv.evaluate_word_analogies(datapath('questions-words.txt'))[0]
# print("Word analogy accuracy with `corpus_file`: {:.1f}%".format(100.0 * model_corp_file_accuracy))
# ##########################################################################################################
