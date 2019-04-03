# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 17:06:07 2018

@author: Xiang.Leee@outlook.com
"""

from gensim.models import Word2Vec,KeyedVectors
from math import log10, floor
import json
import time

if __name__ == '__main__':
    word2vecModelPath = 'en.model'       #choose the model file after training
    word2vecModel = Word2Vec.load(word2vecModelPath) #load the word vector table
    start = time.clock()
    word2vecDict = {}
    dimension = 200           #dimension of word vector
    newVector = [1]*(dimension//5)   #dimension of hash vector
    validNum = 16               #precision
    j = 0
    for word, vector in zip(word2vecModel.wv.vocab, word2vecModel.wv.vectors):
        for i in range(dimension):
            temp = vector[i]
            if i % 5 == 0:
                newVector[i//5] = str(int(temp*10**(-int(floor(log10(abs(temp))))+validNum-1)))
            else:
                try:
                    newVector[i//5] += str(int(temp*10**(-int(floor(log10(abs(temp))))+validNum-1)))
                except:
                    print(temp)
        word2vecDict[word] = newVector
        j += 1
        if j % 100000 == 0:
            print(j)
    end = time.clock()
    elapsed = end - start
    print("time=",elapsed,'s')
    with open('pre_processed_table.json','w',encoding = 'utf-8') as f:
        json.dump(word2vecDict,f)