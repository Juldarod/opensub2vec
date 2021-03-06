from pathlib import Path

from gensim.models.phrases import Phraser

import re
import time
import logging


rc_root = '../resources/rawcorpus/'
c_root = '../resources/corpus/'
m_root = '../resources/models/'


def remove_noise(lang):
    start = time.time()

    lines = 0
    regex = [r' \'', r'[^a-z\'áéíóú]+', r'^\W|\W$', r'[^a-z\'ñáéíóú]+']
    first_regex = regex[0] if lang == 'en' else regex[2]
    second_regex = regex[1] if lang == 'en' else regex[3]
    replace = '\'' if lang == 'en' else ' '

    file_input = open(Path(
        '{}OpenSubtitles.{}'.format(rc_root, lang)).absolute(), 'r', encoding='utf8')
    file_output = open(Path(
        '{}opensub2018_{}.cor'.format(c_root, lang)).absolute(), 'w+', encoding='utf8')

    for line in file_input:
        lines += 1
        first_step = re.sub(r'- ', '', line).lower()
        second_step = re.sub(first_regex, replace, first_step)
        third_step = re.sub(second_regex, ' ', second_step)
        file_output.write(third_step)
        file_output.write('\n')

    file_output.close()

    end = time.time()
    elapsed = end - start

    print('{} english lines processed'.format(lines))
    print('Time elapsed: {}'.format(elapsed))


def get_sentences(input_file_pointer):
    while True:
        line = input_file_pointer.readline()
        if not line:
            break
        yield line


def sentence_to_bi_grams(phrases_model, sentence):
    return ' '.join(phrases_model[sentence])


def sentences_to_bi_grams(lang):
    start = time.time()

    logging.basicConfig(
        format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

    n_grams = Phraser.load(
        '{}phrases/opensub2018_{}.bin'.format(m_root, lang))
    input_file_name = '{}/opensub2018_{}.cor'.format(
        c_root, lang)
    output_file_name = '{}/opensub2018_phrases_{}.cor'.format(
        c_root, lang)

    with open(input_file_name, 'r') as input_file_pointer:
        with open(output_file_name, 'w+') as out_file:
            for sentence in get_sentences(input_file_pointer):
                tokenized_sentence = sentence.split(' ')
                parsed_sentence = sentence_to_bi_grams(
                    n_grams, tokenized_sentence)
                out_file.write(parsed_sentence)

    end = time.time()
    elapsed = end - start

    print('Time elapsed: {}'.format(elapsed))
