from gensim.models.fasttext import load_facebook_model, load_facebook_vectors
from gensim.models.fasttext import FastText


root_path = "../resources/models/fasttext-pretrained/"

en_vecs = load_facebook_vectors(root_path + "cc.en.300.bin")

en_vecs.most_similar('dog')