from gensim.models.fasttext import load_facebook_model, load_facebook_vectors
from gensim.models.fasttext import FastText


root_path = "../resources/models/fasttext-pretrained/"

en_model = load_facebook_model(root_path + "cc.en.300.bin.gz")

en_model.build_vocab()