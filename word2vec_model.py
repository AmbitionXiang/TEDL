# -*- coding: utf-8 -*-
"""
python word2vec_model.py zh.jian.wiki.seg.txt wiki.zh.model wiki.zh.text.vector
python word2vec_model.py out_wiki.en.txt en.model en.vector
Don't forget to set the environmental variable: PYTHONHASHSEED=0
"""
from __future__ import print_function
 
import logging
import os
import sys
import multiprocessing
 
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
 
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
 
    model = Word2Vec(LineSentence(inp), size=200, window=5, min_count=5, iter=2,
                     workers=1, seed=2, hs=1, negative=0)
 
    model.save(outp1)
    model.wv.save_word2vec_format(outp2, binary=False)

