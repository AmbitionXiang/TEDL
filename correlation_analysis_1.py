# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 20:31:30 2018

@author: 790601738
"""
from gensim.models import Word2Vec
import matplotlib.pyplot as plt
import json 

###生成json时打开注释
def cosine_similarity(vector1, vector2):  #计算余弦相似度
    dot_product = 0.0
    normA = 0.0
    normB = 0.0
    for a, b in zip(vector1, vector2):
        dot_product += a * b
        normA += a ** 2
        normB += b ** 2
    if normA == 0.0 or normB == 0.0:
        return 0
    else:
        return round(dot_product / ((normA**0.5)*(normB**0.5)) * 100, 2)

word2vec_model = Word2Vec.load('wiki.zh.model')
model1 = Word2Vec.load('wiki.zh.model1')    
num = []
for i in word2vec_model.wv.vocab:
    temp = cosine_similarity(word2vec_model[i],model1[i])
    num.append(temp)
    if temp > 98:
        print(i)
    
with open("fast.json","w",encoding="utf-8") as f:
    json.dump(num,f)