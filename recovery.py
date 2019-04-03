# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 12:09:07 2019

@author: Xiang.Leee@outlook.com
"""


import hashlib
import json
import matplotlib.pyplot as plt
import seaborn as sns
import random

cipherBook = 'pre_processed_table.json' 
with open(cipherBook,'r',encoding = 'utf-8') as f:
    vectorDict = json.load(f)

m = hashlib.sha256()
for key in vectorDict:
    m.update(str(vectorDict[key]).encode('utf-8'))
    vectorDict[key] = int(m.hexdigest(),16)
vectorList = list(vectorDict.values())
wordList = list(vectorDict.keys())
total = 100
wordChooseList = random.sample(wordList,total)  
ratioList = []
for n in range(1,257): 
    correct = 0
    for word in wordChooseList:
        maxLap = 0
        originalHash = vectorDict[word]

        j = random.sample(range(256),n)
        temper = ''
        for i in range(256):
            if i in j:
                temper += '1'
            else:
                temper += '0'
        temperdHash = originalHash ^ int(temper,2)

        pos = 0
        maxPos = 0
        for value in vectorList:
            lap = 256 - bin(temperdHash^value).count('1')
            if maxLap < lap:
                maxLap = lap
                maxPos = pos
            pos += 1
        restoredWord = wordList[maxPos] 
        if restoredWord == word:
            correct += 1
    ratio = correct/total
    print('n=',n,' ratio=',ratio)
    ratioList.append(ratio)
    
with open('recover.json','w',encoding='utf-8') as f:
    json.dump(ratioList, f)
