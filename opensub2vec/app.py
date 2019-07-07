from flask import Flask
from .utils.fasttext_tests import load_model
import simplejson as json

app = Flask(__name__)


@app.route('/test')
def hello_world():
    return json.dumps({"message": "It is working!"})
