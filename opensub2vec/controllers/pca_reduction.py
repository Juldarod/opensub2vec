from sklearn.decomposition import PCA
from matplotlib import pyplot as plt

import io


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
    plt.grid(True)
    # write image data to a string buffer and get the PNG image bytes
    buf = io.BytesIO()
    plt.savefig(buf, format="png", facecolor="white")
    plt.close()
    return buf.getvalue()


def plot_translation_vector(model, sentence, translation):
    words = sentence.split()
    translations = translation.split()

    X = model[0].wv.__getitem__(words)
    Y = model[1].wv.__getitem__(translations)

    pca = PCA(n_components=2)

    source = pca.fit_transform(X)
    target = pca.fit_transform(Y)

    # fig = plt.figure()

    # fig.add_subplot(211)
    plt.scatter(source[:, 0], source[:, 1])
    for i, word in enumerate(words):
        plt.annotate(word, xy=(source[i, 0], source[i, 1]))

    # fig.add_subplot(212)
    plt.scatter(target[:, 0], target[:, 1])
    for i, word in enumerate(translations):
        plt.annotate(word, xy=(target[i, 0], target[i, 1]), color="red")

    plt.grid(True)
    buf = io.BytesIO()
    plt.savefig(buf, format="png", facecolor="white")
    plt.close()
    return buf.getvalue()
