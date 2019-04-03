# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 21:42:39 2019

@author: 790601738
"""

import hashlib
import json
import matplotlib.pyplot as plt
import seaborn as sns
import random

cipherBook = 'pre_processed_table200d_2epoch.json' #经过处理的词向量表
with open(cipherBook,'r',encoding = 'utf-8') as f:
    vectorDict = json.load(f)

m = hashlib.sha256()
for key in vectorDict:
    m.update(str(vectorDict[key]).encode('utf-8'))
    vectorDict[key] = int(m.hexdigest(),16)
vectorList = list(vectorDict.values())
wordList = list(vectorDict.keys())
print('step1')
total = 100
wordChooseList = random.sample(wordList,total)  
ratioList = []
for n in range(1,257):
    coincide = 0
    for word in wordChooseList:
        flag = 0
        originalHash = vectorDict[word]
        j = random.sample(range(256),n)
        temper = ''
        for i in range(256):
            if i in j:
                temper += '1'
            else:
                temper += '0'
        temperdHash = originalHash ^ int(temper,2)

        for value in vectorList:
            lap = 256 - bin(temperdHash^value).count('1')
            if lap == 256:
                flag = 1
                break;
        coincide += flag
    ratio = 1-coincide/total
    print('n=',n,' ratio=',ratio)
    ratioList.append(ratio)

with open('ciphertext_sensitivity.json','w',encoding = 'utf-8') as f:
    json.dump(ratioList,f)
