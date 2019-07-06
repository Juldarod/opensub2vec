from flask import Flask
from ..utils.fasttext_tests import load_model

app = Flask(__name__)


@app.route('/')
def hello_world():
    return load_model()
