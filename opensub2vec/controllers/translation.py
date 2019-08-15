import spacy
from typing import List

spacy_en = spacy.load('en_core_web_sm')
spacy_es = spacy.load('es_core_news_sm')


def remove_stopwords(lang, phrase) -> str:
    if lang == 'en':
        return [word.text.lower() for word in spacy_en(phrase) if not word.is_stop]
    else:
        return [word.text.lower() for word in spacy_es(phrase) if not word.is_stop]


def translate(model, phrase) -> List[List[str]]:
    words = remove_stopwords('en', phrase)
    return [list(model.translate([word], topn=5).items()) for word in words]


def get_wmdistance(model, source: List[str], target: List[str]) -> str:
    source = ' '.join(source)
    target = ' '.join(target)
    return "{0:.4f}".format(model.wmdistance(source, target))
