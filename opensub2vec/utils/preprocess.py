from pathlib import Path
import re
import time


def english_process():
    start = time.time()

    en_lines = 0
    en_input = open(Path('./resources/rawcorpus/aligned/OpenSubtitles.en').absolute(), 'r', encoding="utf8")
    en_output = open(Path('./resources/corpus/opensub2018_en.cor').absolute(), 'w+', encoding="utf8")

    for line in en_input:
        en_lines += 1
        dash = re.sub(r'- ', '', line).lower()
        apost = re.sub(r' \'', '\'', dash)
        punct = re.sub(r'[^a-zA-Z\'áéíóúÁÉÍÓÚ]+', ' ', apost)
        en_output.write(punct)
        en_output.write('\n')
    
    en_output.close()

    end = time.time()
    elapsed = end - start

    print('%s english lines processed' % en_lines)
    print('Time elapsed: %f' % elapsed)

def spanish_process():
    start = time.time()

    sp_lines = 0
    sp_input = open(Path('./resources/rawcorpus/aligned/OpenSubtitles.es').absolute(), 'r', encoding="utf8")
    sp_output = open(Path('./resources/corpus/opensub2018_es.cor').absolute(), 'w+', encoding="utf8")

    for line in sp_input:
        sp_lines += 1
        dash = re.sub(r'- ', '', line).lower()
        symbol = re.sub(r'^\W|\W$', '', dash)
        punct = re.sub(r'[^a-z\'ñáéíóúÁÉÍÓÚ]+', ' ', symbol)
        sp_output.write(punct)
        sp_output.write('\n')

    sp_output.close()

    end = time.time()
    elapsed = end - start

    print('%s spanish lines processed' % sp_lines)
    print('Time elapsed: %f' % elapsed)