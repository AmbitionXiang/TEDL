# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 20:14:04 2019

model = Word2Vec(LineSentence(inp), size=200, window=5, min_count=5, workers=multiprocessing.cpu_count())
PYTHONHASHSEED=0
python fasttext.py out_wiki.en.txt fast1.model fast1.vector
"""

from __future__ import print_function
 
import logging
import os
import sys
import multiprocessing
 
from gensim.models.word2vec import LineSentence
from gensim.models import FastText

if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)
 
    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))
 
    # check and process input arguments
    if len(sys.argv) < 4:
        print("Useing: python train_word2vec_model.py input_text "
              "output_gensim_model output_word_vector")
        sys.exit(1)
    inp, outp1, outp2 = sys.argv[1:4]
 
    model = FastText(LineSentence(inp), size=200, window=5, min_count=5, iter=2,
                     min_n = 3 , max_n = 5,workers=1, seed=1, hs=1, negative=0)  #workers=multiprocessing.cpu_count()
 
    model.save(outp1)
    model.wv.save_word2vec_format(outp2, binary=False)