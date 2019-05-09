from sklearn.decomposition import PCA
from matplotlib import pyplot as plt


# sentence is a string
def plot_vector(model, sentence):
    words = sentence.split()
    # fit a 2d PCA model to the vectors
    X = model.wv.__getitem__(words)
    # X = english_sg_model.wv.__getitem__(english_sg_vectors)
    pca = PCA(n_components=2)
    result = pca.fit_transform(X)
    # create a scatter plot of the projection
    plt.scatter(result[:, 0], result[:, 1])

    for i, word in enumerate(words):
        plt.annotate(word, xy=(result[i, 0], result[i, 1]))

    plt.show()