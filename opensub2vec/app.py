from flask import Flask, jsonify, make_response
from flask_cors import CORS
from gensim.models.word2vec import Word2Vec
from controllers import pca_reduction
from controllers.models import load_model


app = Flask(__name__)
CORS(app)

model = []


@app.route('/')
def start():
    model.clear()
    model.append(load_model())
    return jsonify(message="Hello from Flask!")


@app.route('/plot/<phrase>')
def pca(phrase):
    image = pca_reduction.plot_vector(model[0], phrase)
    res = make_response(image, 200)
    res.headers['Content-Type'] = 'image/png'
    res.headers['Content-Lengt'] = len(image)
    return res
