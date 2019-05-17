from pathlib import Path

from gensim.models.doc2vec import Doc2Vec, TaggedLineDocument, TaggedDocument
from gensim.models.translation_matrix import TranslationMatrix, BackMappingTranslationMatrix

import logging
import time

from gensim.test.utils import datapath
from gensim.test.test_translation_matrix import read_sentiment_docs

root_en_path = "../resources/models/doc2vec/english/opensub2018_"
root_es_path = "../resources/models/doc2vec/spanish/opensub2018_"
# ################### Translation Matrix #########################################################
#
start = time.time()

# dm_en_model = Doc2Vec.load(root_en_path + "dm.bin", mmap='r')
# dbow_en_model = Doc2Vec.load(root_en_path + "dbow.bin", mmap='r')
# dm_es_model = Doc2Vec.load(root_es_path + "dm.bin", mmap='r')
# dbow_es_model = Doc2Vec.load(root_es_path + "dbow.bin", mmap='r')

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# model_trans = BackMappingTranslationMatrix(dm_es_model, dm_en_model)
# model_trans.save('../resources/models/translation_matrix/opensub2018_dm_es.bin')
# model_trans = BackMappingTranslationMatrix(dm_en_model, dm_es_model)
# model_trans.save('../resources/models/translation_matrix/opensub2018_dm_en.bin')

# model_trans = BackMappingTranslationMatrix(dbow_es_model, dbow_en_model)
# model_trans.save('../resources/models/translation_matrix/opensub2018_dbow_es.bin')
# model_trans = BackMappingTranslationMatrix(dbow_en_model, dbow_es_model)
# model_trans.save('../resources/models/translation_matrix/opensub2018_dbow_en.bin')

# corpus = TaggedLineDocument(Path('../resources/corpus/english/parts/part000').absolute())

print([TaggedDocument("the red house".split(), ['0'])])

model = BackMappingTranslationMatrix.load("../resources/models/translation_matrix/opensub2018_dbow_en.bin")
# data = read_sentiment_docs(datapath("alldata-id-10.txt"))[:5]
# print(type([TaggedDocument("the red house".split(), ['1'])]))
test = model.train([TaggedDocument("the red house".split(), ['0']), TaggedDocument("the blue house".split(), ['1'])])
test = model.train(data)
# test.save('../resources/models/translation_matrix/pruebaentreno.bin')


end = time.time()
elapsed = end - start

print('Time elapsed: %f' % elapsed)
#
# print(model_trans.infer_vector(trg_model.doctags))
# print(trg_model.infer_vector(['la', 'solitaria']))
# ################################################################################################


# root_path = "../resources/models/"
# trans_model = BackMappingTranslationMatrix.load(root_path +
#     "translation_matrix/opensub2018_dbow_es_trans_model.bin", mmap='r'
# )

# dbow_en_model = Doc2Vec.load(root_path + "doc2vec/opensub2018_en_dbow.bin", mmap='r')
# print(trans_model.infer_vector(dbow_en_model.docvecs[0]))
corpus = TaggedLineDocument(Path('../resources/corpus/english/parts/part000').absolute())