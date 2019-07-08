from gensim.models.word2vec import Word2Vec
from gensim.models.doc2vec import Doc2Vec
from sklearn.decomposition import PCA
from matplotlib import pyplot as plt
import io


w2v_path = "../resources/models/word2vec/english/opensub2018_"
# d2v_path = "../resources/models/doc2vec/opensub2018_"

# print("Loading model")
sg_en_model = Word2Vec.load(w2v_path + "sg.bin", mmap='r')
# print("Done")
# cbow_en_model = Word2Vec.load(w2v + "en_cbow.bin", mmap='r')
# sg_es_model = Word2Vec.load(w2v_path + "sg.bin", mmap='r')
# cbow_es_model = Word2Vec.load(w2v + "es_cbow.bin", mmap='r')

# dm_en_model = Doc2Vec.load(d2v_path + "en_dm.bin", mmap='r')
# dbow_en_model = Doc2Vec.load(d2v_path + "en_dbow.bin", mmap='r')
# dm_es_model = Doc2Vec.load(d2v_path + "es_dm.bin", mmap='r')
# dbow_es_model = Doc2Vec.load(d2v_path + "es_dbow.bin", mmap='r')


def plot_vectors(models, sentences):
    model = models

    for i, sentence in enumerate(sentences):
        words = sentence.split()
        # fit a 2d PCA model to the vectors
        X = model[i].wv.__getitem__(words)
        pca = PCA(n_components=2)
        result = pca.fit_transform(X)
        # create a scatter plot of the projection
        plt.scatter(result[:, 0], result[:, 1])

        for i, word in enumerate(words):
            plt.annotate(word, xy=(result[i, 0], result[i, 1]))

    plt.show()


def plot_vector(model, sentence):
    words = sentence.split()
    # fit a 2d PCA model to the vectors
    X = model.wv.__getitem__(words)
    pca = PCA(n_components=2)
    result = pca.fit_transform(X)

    # create a scatter plot of the projection
    plt.scatter(result[:, 0], result[:, 1])

    for i, word in enumerate(words):
        plt.annotate(word, xy=(result[i, 0], result[i, 1]))

    # plt.show()
    # write image data to a string buffer and get the PNG image bytes
    buf = io.BytesIO()
    plt.savefig(buf, format="png", facecolor="white")
    return buf.getvalue()

    # pseudo-code for generating the http response from your
    # webserver, and writing the bytes back to the browser.
    # replace this with corresponding code for your web framework
    # headers = {
    #     'Content-Type': 'image/png',
    #     'Content-Length': len(data)
    #     }
    # response.write(200, 'OK', headers, data)


# plot_vectors(
#     [
#         sg_en_model,
#         sg_es_model
#     ],
#     [
#         "the black cat",
#         "el gato negro"
#     ]
# )

# plot_vector(sg_en_model, "the black cat")
