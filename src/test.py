from gensim.models import KeyedVectors
from gensim.models import TranslationMatrix
from gensim.models.translation_matrix import BackMappingTranslationMatrix
from gensim.models import Doc2Vec

# word_en__vectors = KeyedVectors.load("../resources/models/opensub2018.en.model")
# doc_en_vectors = KeyedVectors.load("../resources/models/opensub2018doc.en.model")

# word_sp__vectors = KeyedVectors.load("../resources/models/opensub2018.sp.model")
# doc_sp_vectors = KeyedVectors.load("../resources/models/opensub2018doc.sp.model")

# print(word_en__vectors.wv.similarity('woman', 'man'))
# print(doc_en_vectors.wv.similarity('woman', 'man'))
# print(word_en__vectors.wv.n_similarity(['sushi', 'shop'], ['japanese', 'restaurant']))
# print(doc_en_vectors.wv.n_similarity(['sushi', 'shop'], ['japanese', 'restaurant']))

# sentence_obama = 'Tell me'.lower().split()
# sentence_president = 'Green house in fire'.lower().split()

# similarity = word_en__vectors.wv.wmdistance(sentence_obama, sentence_president)
# print("{:.4f}".format(similarity))
# similarity = doc_en_vectors.wv.wmdistance(sentence_obama, sentence_president)
# print("{:.4f}".format(similarity))
# similarity = doc_en_vectors.wv.wmdistance(sentence_obama, sentence_president)
# print("{:.4f}".format(similarity))

# print(word_en__vectors.wv.most_similar('man'))
# print(doc_en_vectors.wv.most_similar('man'))
# print(word_en__vectors.wv.most_similar('house'))
# print(doc_en_vectors.wv.most_similar('house'))

# model_corp_file_accuracy = word_en__vectors.wv.evaluate_word_analogies(datapath('questions-words.txt'))[0]
# print("Word analogy accuracy with `corpus_file`: {:.1f}%".format(100.0 * model_corp_file_accuracy))

from gensim.models.keyedvectors import Doc2VecKeyedVectors

src_model = Doc2Vec.load('../resources/models/opensub2018doc.en.model')
trg_model = Doc2Vec.load('../resources/models/opensub2018doc.sp.model')

model_trans = BackMappingTranslationMatrix(src_model, trg_model)

print(model_trans.infer_vector(trg_model.doctags))
print(trg_model.infer_vector(['la', 'solitaria']))