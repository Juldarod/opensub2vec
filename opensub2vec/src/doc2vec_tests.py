from pathlib import Path

from gensim.models.doc2vec import Doc2Vec
from gensim.models.keyedvectors import Doc2VecKeyedVectors

import logging
import time


root_path = "../resources/models/doc2vec/opensub2018_"
start = time.time()

# Models loading
dm_en_model = Doc2Vec.load(root_path + "en_dm.bin", mmap='r')
dbow_en_model = Doc2Vec.load(root_path + "en_dbow.bin", mmap='r')
dm_sp_model = Doc2Vec.load(root_path + "sp_dm.bin", mmap='r')
dbow_sp_model = Doc2Vec.load(root_path + "sp_dbow.bin", mmap='r')

# Vectors loading (docvec)
# dm_en_vectors = Doc2VecKeyedVectors.load(root_path + "en_dm.kv")
# dm_es_vectors = Doc2VecKeyedVectors.load(root_path + "es_dm.kv")
# dbow_en_vectors = Doc2VecKeyedVectors.load(root_path + "en_dbow.kv")
# dbow_es_vectors = Doc2VecKeyedVectors.load(root_path + "es_dbow.kv")

end = time.time()
elapsed = end - start

print('Models loaded in: %f seconds' % elapsed)


# Testing similarity
# https://radimrehurek.com/gensim/models/keyedvectors.html#gensim.models.keyedvectors.Doc2VecKeyedVectors.similarity 


# Testing n_similarity
# https://radimrehurek.com/gensim/models/keyedvectors.html#gensim.models.keyedvectors.Doc2VecKeyedVectors.n_similarity

# English
# print(dm_en_model.wv.n_similarity("what is your age".split(), "go to the gym".split()))
# print(dm_en_model.wv.similarity_unseen_docs(
#     model, 
#     ['the', 'cat', 'sat', 'on', 'the', 'table'], 
#     # ['the', 'dog', 'sat', 'on', 'the', 'chair'])
#     ['fast', 'food'])
# )
# print(dbow_en_model.docvecs.n_similarity('', 'chair'))

# Spanish
# print(dm_es_model.wv.n_similarity('mujer', 'hombre'))
# print(dbow_es_model.docvecs.n_similarity('mujer', 'hombre'))


# Testing most_similar
# https://radimrehurek.com/gensim/models/keyedvectors.html#gensim.models.keyedvectors.Doc2VecKeyedVectors.most_similar

# sentence = dm_en_model.infer_vector("the loner".split(), steps=20)
# print([sentence])
# print(dm_en_model.docvecs.most_similar([sentence]))
# inferido = dm_en_model.docvecs.most_similar([sentence], topn=4)
#
# for i, v in enumerate(inferido):
#     x, y = v
#     print(i, "Item: ", x, "\nProb: ", str(round(y, 2)) + "%")
