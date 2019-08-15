#!/bin/bash

# python -m spacy download es_core_news_sm
# python -m spacy download en_core_web_sm

export FLASK_APP=opensub2vec/app.py
export FLASK_ENV=development

flask run