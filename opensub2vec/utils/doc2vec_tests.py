from pathlib import Path

from gensim.models.doc2vec import Doc2Vec, TaggedLineDocument
from gensim.models.keyedvectors import Doc2VecKeyedVectors

import logging
import time


root_path = "../resources/models/doc2vec/english/opensub2018_"
start = time.time()

# Models loading
dm_en_model = Doc2Vec.load(root_path + "dm.bin", mmap='r')
# dbow_en_model = Doc2Vec.load(root_path + "en_dbow.bin", mmap='r')
# dm_es_model = Doc2Vec.load(root_path + "es_dm.bin", mmap='r')
# dbow_es_model = Doc2Vec.load(root_path + "es_dbow.bin", mmap='r')

# Vectors loading (docvec)
# dm_en_vectors = Doc2VecKeyedVectors.load(root_path + "en_dm.kv", mmap='r')
# dm_es_vectors = Doc2VecKeyedVectors.load(root_path + "es_dm.kv", mmap='r')
# dbow_en_vectors = Doc2VecKeyedVectors.load(root_path + "en_dbow.kv", mmap='r')
# dbow_es_vectors = Doc2VecKeyedVectors.load(root_path + "es_dbow.kv", mmap='r')

end = time.time()
elapsed = end - start

print('Models loaded in: %f seconds' % elapsed)


# vocab = dm_en_model.docvecs.vectors_docs

# for i in range(len(vocab)):
#     print(list(vocab)[i])


# Testing similarity
# https://radimrehurek.com/gensim/models/keyedvectors.html#gensim.models.keyedvectors.Doc2VecKeyedVectors.similarity 


# Testing n_similarity
# https://radimrehurek.com/gensim/models/keyedvectors.html#gensim.models.keyedvectors.Doc2VecKeyedVectors.n_similarity

# English
# print(dm_en_model.wv.n_similarity("what is your age".split(), "how old are you".split()))
# print(dm_en_model.wv.similarity_unseen_docs(
#     model, 
#     ['the', 'cat', 'sat', 'on', 'the', 'table'], 
#     # ['the', 'dog', 'sat', 'on', 'the', 'chair'])
#     ['fast', 'food'])
# )
# print(dm_en_model.wv.n_similarity('youngster', 'boy'))
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

# for i, v in enumerate(inferido):
#     x, y = v
#     print(i, "Item: ", x, "\nProb: ", str(round(y, 2)) + "%")


# print(dm_en_model.docvecs[1])
# print(dm_es_model.docvecs[0])