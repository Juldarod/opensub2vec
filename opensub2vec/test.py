from gensim.models import KeyedVectors
from gensim.models import TranslationMatrix
from gensim.models.translation_matrix import BackMappingTranslationMatrix
from gensim.models import Word2Vec
from gensim.models import Doc2Vec

from sklearn.decomposition import PCA
from matplotlib import pyplot as plt

# BackMappingTranslationMatrix.

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

# from gensim.models.keyedvectors import Doc2VecKeyedVectors

# src_model = Doc2Vec.load('../resources/models/opensub2018doc.en.model')
# trg_model = Doc2Vec.load('../resources/models/opensub2018doc.sp.model')

# model_trans = BackMappingTranslationMatrix(src_model, trg_model)

# print(model_trans.infer_vector(trg_model.doctags))
# print(trg_model.infer_vector(['la', 'solitaria']))


# carga de los vectores en inglés con skipgram
english_sg_model = KeyedVectors.load('../resources/models/opensub2018.en.model')
spanish_sg_model = KeyedVectors.load('../resources/models/opensub2018.sp.model')
# english_sg_model = KeyedVectors.load('../resources/models/opensub2018.en.model')
english_sg_vectors = english_sg_model.wv.vocab
spanish_sg_vectors = spanish_sg_model.wv.vocab
# print(english_sg_vectors.items())

# fit a 2d PCA model to the vectors
X = english_sg_model.wv.__getitem__(['the', 'blue', 'cat'])
# X = english_sg_model.wv.__getitem__(english_sg_vectors)
pca = PCA(n_components=2)
result = pca.fit_transform(X)
# create a scatter plot of the projection
plt.scatter(result[:, 0], result[:, 1])
words = list(['the', 'blue', 'cat'])
# words = list(english_sg_vectors)

# fit a 2d PCA model to the vectors
Y = spanish_sg_model.wv.__getitem__(['el', 'gato', 'azul'])
# Y = spanish_sg_model.wv.__getitem__(spanish_sg_vectors)
pca2 = PCA(n_components=2)
result2 = pca2.fit_transform(Y)
# create a scatter plot of the projection
plt.scatter(result2[:, 0], result2[:, 1])
palabras = list(['el', 'gato', 'azul'])
# words = list(english_sg_vectors)


for i, word in enumerate(words):
    plt.annotate(word, xy=(result[i, 0], result[i, 1]))

for j, palabra in enumerate(palabras):
    plt.annotate(palabra, xy=(result2[j, 0], result2[j, 1]))

plt.show()