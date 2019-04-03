# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 19:11:52 2018

@author: 790601738
"""

import time
import re
from math import log10, floor
import hashlib
import json
import matplotlib.pyplot as plt
import seaborn as sns

if __name__ == '__main__':
    with open('pre_processed_table200d_2epoch.json','r',encoding = 'utf-8') as f:
        word2vecDict = json.load(f)
    with open('pre_processed_table200d_2epoch_SC.json','r',encoding = 'utf-8') as f:
        word2vecDict1 = json.load(f)    
        
    m = hashlib.sha256()
    m1 = hashlib.sha256()
    
    similarProbList = list()
    for word in word2vecDict:
        try:
            temp = word2vecDict[word]
            temp1 = word2vecDict1[word]
    
            m.update(str(temp).encode('utf-8'))
            m1.update(str(temp1).encode('utf-8'))
    
            similarNum = bin(int(m.hexdigest(),16) ^ int(m1.hexdigest(),16)).count('1') 
            similarProb = 1-similarNum/256
            similarProbList.append(similarProb)

        except:
            pass 
    with open('correlation_word2vec.json','w',encoding = 'utf-8') as f:
        json.dump(similarProbList,f)  
