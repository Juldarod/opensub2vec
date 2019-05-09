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