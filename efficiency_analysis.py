# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 19:11:52 2018

@author: Xiang.Leee@outlook.com
"""

from gensim.models import Word2Vec
from Crypto.Cipher import AES
from Crypto import Random
import time
import re
from binascii import b2a_hex, a2b_hex
import base64
from math import log10, floor
import hashlib
import json
import matplotlib.pyplot as plt

if __name__ == '__main__':
    #TEDL
    with open('pre_processed_table.json','r',encoding = 'utf-8') as f:
        word2vecDict = json.load(f)
    
    m = hashlib.sha256()
    validNum = 16
    dimension = 200//5
    countDict = dict()
    start = time.clock()
    compl = re.compile(r'[\s]+')
    with open("zh.jian.wiki.seg.txt","r",encoding = 'utf-8') as f:
        for line in f:
            wordList = re.split(compl,line)
            for word in wordList:
                try:
                    temp = word2vecDict[word]
                    if word not in countDict:
                        countDict[word] = 0
                    else:
                        countDict[word] += 1
                    countDict[word] %= dimension

                    m.update(temp.encode('utf-8'))
                except:
                    pass
    elapsed = time.clock() - start
    print("my method'time", elapsed)
    #AES
    start = time.clock()
    with open("zh.jian.wiki.seg2.txt","r",encoding = 'utf-8') as f:
        for line in f:
            wordList = re.split(compl,line)
            for text in wordList:
                BS = AES.block_size
                try:
                    pad = lambda s: s + (BS - len(s) % BS) * '来'
                    unpad = lambda s : s[:-ord(s[len(s)-1:])]
                    
                    key = '12345678901234567890123456789012' # the length can be (16, 24, 32)
                    cipher = AES.new(key)
                    encrypted = cipher.encrypt(pad(text))
                    #print(encrypted)  # will be something like 'f456a6b0e54e35f2711a9fa078a76d16'
                    result = base64.b64encode(encrypted)
                except:
                    try:
                        pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
                        unpad = lambda s : s[:-ord(s[len(s)-1:])]
                    
                        key = '12345678901234567890123456789012' # the length can be (16, 24, 32)
                        cipher = AES.new(key)
                        encrypted = cipher.encrypt(pad(text))
                        #print(encrypted)  # will be something like 'f456a6b0e54e35f2711a9fa078a76d16'
                        result = base64.b64encode(encrypted)
                    except:
                        pass
    elapsed = time.clock() - start
    print("AES'time", elapsed)
    
    
    

