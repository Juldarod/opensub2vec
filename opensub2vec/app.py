from flask import Flask, jsonify, make_response
from flask_cors import CORS
from gensim.models.word2vec import Word2Vec
from controllers import pca_reduction
from controllers.models import load_model, load_translation_matrix, remove_stopwords, translate_phrase, get_wmdistance


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


@app.route('/plot/<lang>/<phrase>')
def pca(lang, phrase):
    if (lang == 'en' or lang == 'es'):
        loaded_model = models[0] if lang == 'en' else models[1]
        image = pca_reduction.plot_vector(loaded_model, phrase)
        res = make_response(image, 200)
        res.headers['Content-Type'] = 'image/png'
        res.headers['Content-Lengt'] = len(image)
        return res
    else:
        return make_response(jsonify(message='Language not supported'))


@app.route('/plot/translation/<source>/<target>')
def pca_translation(source, target):
    image = pca_reduction.plot_translation_vector(models[1], source, target)
    res = make_response(image, 200)
    res.headers['Content-Type'] = 'image/png'
    res.headers['Content-Lengt'] = len(image)
    return res


@app.route('/translate/<phrase>')
def translate(phrase):
    res = translate_phrase(models[2], phrase)
    words = phrase.split().__iter__()
    response = [{"original": next(words), "translations": el[0]} for el in res]
    return jsonify({"words": response})


@app.route('/wmdistance/<source>/<target>')
def wmdistance(source, target):
    source_no_stop = remove_stopwords('es', source)
    target_no_stop = remove_stopwords('es', target)
    return jsonify(wmdistance=get_wmdistance(models[1], source_no_stop, target_no_stop))


if __name__ == '__main__':
    app.run(debug=True)
