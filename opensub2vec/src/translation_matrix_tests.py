from gensim.models.doc2vec import Doc2Vec
from gensim.models.translation_matrix import TranslationMatrix, BackMappingTranslationMatrix

import logging
import time


# ################### Translation Matrix #########################################################
#
# start = time.time()

# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
# model_trans = BackMappingTranslationMatrix(dbow_es_model, dbow_en_model)
# model_trans.save('./resources/models/dbow_es_trans_model.bin')

# end = time.time()
# elapsed = end - start

# print('Time elapsed: %f' % elapsed)
#
# print(model_trans.infer_vector(trg_model.doctags))
# print(trg_model.infer_vector(['la', 'solitaria']))
# ################################################################################################


root_path = "../resources/models/"
trans_model = BackMappingTranslationMatrix.load(root_path +
    "translation_matrix/opensub2018_dbow_es_trans_model.bin", mmap='r'
)
dbow_en_model = Doc2Vec.load(root_path + "doc2vec/opensub2018_en_dbow.bin", mmap='r')
print(trans_model.infer_vector(dbow_en_model.docvecs[0]))