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
    # write image data to a string buffer and get the PNG image bytes
    buf = io.BytesIO()
    plt.savefig(buf, format="png", facecolor="white")
    plt.close()
    return buf.getvalue()
