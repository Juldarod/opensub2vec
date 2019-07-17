from pathlib import Path

from gensim.models.keyedvectors import KeyedVectors
from gensim.models.translation_matrix import TranslationMatrix

import logging
import time


source_word_vec_file = "../resources/models/fasttext/english/opensub2018_phrases_sg.bin"
target_word_vec_file = "../resources/models/fasttext/spanish/opensub2018_phrases_sg.bin"
# ################### Translation Matrix #########################################################


logging.basicConfig(
    format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

loaded_trans = TranslationMatrix.load(
    '../resources/models/translation_matrix/english/opensub2018_to_spanish.bin', mmap='r')

# source = TranslationMatrix.load(
#     '../resources/models/translation_matrix/english/opensub2018_to_spanish.bin.source_lang_vec.vectors.npy', mmap='r')
# target = TranslationMatrix.load(
#     '../resources/models/translation_matrix/english/opensub2018_to_spanish.bin.target_lang_vec.vectors.npy', mmap='r')
start = time.time()

print(loaded_trans.translate(["right"], topn=3))
#  source_lang_vec=source, target_lang_vec=target))

end = time.time()
elapsed = end - start

print('Time elapsed: %f' % elapsed)
