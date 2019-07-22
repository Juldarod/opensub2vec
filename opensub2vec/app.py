from flask import Flask, jsonify, make_response
from flask_cors import CORS
from gensim.models.word2vec import Word2Vec
from controllers import pca_reduction
from controllers.models import load_model, load_translation_matrix


app = Flask(__name__)
CORS(app)

models = []


@app.route('/')
def start():
    return jsonify(message="Server running")


@app.route('/model/load/<model>')
def load_models(model):
    if (model == 'word2vec' or model == 'fasttext'):
        models.clear()
        english_model = load_model(model, 'en')
        models.append(english_model)
        spanish_model = load_model(model, 'es')
        models.append(spanish_model)
        translation_model = load_translation_matrix(model)
        models.append(translation_model)
        return jsonify(message="{} loaded".format(model))
    else:
        return make_response(jsonify(message="The model requested is not available"), 400)


@app.route('/plot/<language>/<phrase>')
def pca(language, phrase):
    if (language == 'english' or language == 'spanish'):
        model = models[0] if language == 'english' else models[1]
        image = pca_reduction.plot_vector(model, phrase)
        res = make_response(image, 200)
        res.headers['Content-Type'] = 'image/png'
        res.headers['Content-Lengt'] = len(image)
        return res
    else:
        return make_response(jsonify(message='The language requested is not available'), 400)
