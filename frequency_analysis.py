# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 19:11:52 2018

@author: Xiang.Leee@outlook.com
"""
import matplotlib.pyplot as plt
import re
import hashlib
import json
import pandas as pd 
import numpy as np 
from decimal import getcontext, Decimal

if __name__ == '__main__':
    #TEDL
    cipherBook = 'pre_processed_table.json' 
    plaintext = "out_wiki.en200M.txt" 
    with open(cipherBook ,'r',encoding = 'utf-8') as f:
        word2vecDict = json.load(f)
    plainFreList = dict()
    cipherFreList = dict()
    m = hashlib.sha256()
    validNum = 16
    dimension = 200//5           
    countDict = dict()
    compl = re.compile(r'[\s]+')
    with open(plaintext,"r",encoding = 'utf-8') as f:   
        for line in f:
            wordList = re.split(compl,line)
            for word in wordList:
                try:
                    temp = word2vecDict[word]
                    m.update(temp[dimension-1].encode('utf-8'))
                    reservedHash = m.hexdigest()
                    if word not in countDict:
                        countDict[word] = 1
                        plainFreList[word] = 1
                    else:
                        countDict[word] += 1
                        plainFreList[word] += 1
                    countDict[word] %= dimension-1
                    
                    m.update(temp[countDict[word]].encode('utf-8'))
                    cipher = m.hexdigest()
                    if cipher not in cipherFreList:
                        cipherFreList[cipher] = 1
                    else:
                        cipherFreList[cipher] += 1
                    m.update((cipher+reservedHash).encode('utf-8'))
                    word2vecDict[word][countDict[word]] = m.hexdigest()
                except:
                    pass  
                    #print('error')
    plainNum = list(plainFreList.values())
    cipherNum = list(cipherFreList.values())        

    plainNum.sort()
    cipherNum.sort()
    with open("histogram of plaintext_200MB_en.json","w",encoding="utf-8") as f:
        json.dump(plainNum,f)
    with open("histogram of ciphertext_200MB_en.json","w",encoding="utf-8") as f:
        json.dump(cipherNum,f)


    
