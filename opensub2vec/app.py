from flask import Flask, jsonify, make_response
from flask_cors import CORS
from controllers import models, translation, plotting


app = Flask(__name__)
CORS(app)

loaded_models = []


@app.route('/')
def start():
    return jsonify(message="Server running")


@app.route('/model/load/<name>')
def load(name):
    if (name == 'word2vec' or name == 'fasttext'):
        loaded_models.clear()
        english_model = models.load_model(name, 'en')
        loaded_models.append(english_model)
        spanish_model = models.load_model(name, 'es')
        loaded_models.append(spanish_model)
        translation_model = models.load_translation_matrix(name)
        loaded_models.append(translation_model)
        return jsonify(message="{} loaded".format(name))
    else:
        return make_response(jsonify(message="The model requested is not available"), 400)


@app.route('/mostsimilar/<lang>/<word>')
def similar(lang, word):
    required_model = loaded_models[0] if lang == 'en' else loaded_models[1]
    return jsonify(data=models.msimilar(required_model, word))


@app.route('/analogy/<lang>/<words>')
def analogies(lang, words):
    required_model = loaded_models[0] if lang == 'en' else loaded_models[1]
    return jsonify(data=models.analogy(required_model, words))


@app.route('/plot/<lang>/<sentence>')
def plot(lang, sentence):
    if (lang == 'en' or lang == 'es'):
        loaded_model = loaded_models[0] if lang == 'en' else loaded_models[1]
        image = plotting.plot_sentence(loaded_model, sentence)
        response = make_response(image, 200)
        response.headers['Content-Type'] = 'image/png'
        response.headers['Content-Lengt'] = len(image)
        return response
    else:
        return make_response(jsonify(message='Language not supported'))


@app.route('/plot/translation/<source>/<target>')
def plot_translation(source, target):
    image = plotting.plot_translations(models, source, target)
    response = make_response(image, 200)
    response.headers['Content-Type'] = 'image/png'
    response.headers['Content-Lengt'] = len(image)
    return response


@app.route('/translate/<sentence>')
def translate(sentence):
    translated = translation.translate(models[2], sentence)
    response = [{"original": el[0][0], "translations": el[0][1]}
                for el in translated]
    return jsonify(data=response)


@app.route('/remove/es/<sentence>')
def remove(sentence):
    return translation.remove_stopwords('es', sentence)


@app.route('/wmdistance/<source>/<target>')
def wmdistance(source, target):
    source_no_stop = translation.remove_stopwords('es', source)
    target_no_stop = translation.remove_stopwords('es', target)
    response = translation.get_wmdistance(
        models[1], source_no_stop, target_no_stop)
    return jsonify(data=response)


if __name__ == '__main__':
    app.run(debug=True)
