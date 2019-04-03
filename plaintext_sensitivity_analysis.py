# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 19:11:52 2018

@author: Xiang.Leee@outlook.com
"""

import re
import json
import hashlib
import matplotlib.pyplot as plt
import seaborn as sns

if __name__ == '__main__':
    with open('pre_processed_table200d_2epoch.json', 'r', encoding='utf-8') as f: #加载中文
        wordDict = json.load(f)
    with open('pre_processed_table_ks.json', 'r', encoding='utf-8') as f: #加载英文
        wordDict1 = json.load(f)
    similarList = []
    testword1 = '群众'
    testword2 = '男人'
    testword3 = '女人'
    testwords1 = ['大众','万众','民众','公众','众生','千夫']
    testwords2 = ['男人家','爱人','女婿','先生','壮汉','汉','汉子','士','人夫','男士','老公',
                  '那口子','官人','丈夫','男子汉','男子','男儿','当家的','光身汉','须眉','夫']
    testwords3 = ['妇道','太太','妇','老婆','娘','娘子','女人家','红装','妻子','女儿','媳妇儿',
                  '老婆子','内','家','婆姨','妻','女性','巾帼','婆娘','家庭妇女','娘儿们','女子',
                  '小娘子','妻妾','老小','娘子军','农妇','女郎','才女','妻室','妇女','半边天',
                  '内助','贤内助','石女','爱妻','爱人','家里','妇人','女士','女','老伴','夫人']
    testword4 = 'people'
    testword5 = 'male'
    testword6 = 'female'
    testwords4 = ['persons','humans','individuals','folk','human beings','humanity','mankind','mortals','the human race']
    testwords5 = ['masculine','manly','macho','virile','manlike']
    testwords6 = ['Woman','girl','lady','lass','shelia','charlie','chook']
    
    for word in testwords1:
        if word not in wordDict:
            testwords1.remove(word)
    for word in testwords2:
        if word not in wordDict:
            testwords2.remove(word)
    for word in testwords3:
        if word not in wordDict:
            testwords3.remove(word)
            
    for word in testwords4:
        if word not in wordDict1:
            testwords4.remove(word)
    for word in testwords5:
        if word not in wordDict1:
            testwords5.remove(word)
    for word in testwords6:
        if word not in wordDict1:
            testwords6.remove(word)
    
    m = hashlib.sha256()
    m1 = hashlib.sha256()
    #中文
    temp = wordDict[testword1]
    for word in testwords1:
        temp1 = wordDict[word]
        
        m.update(''.join(temp).encode('utf-8'))
        m1.update(''.join(temp1).encode('utf-8'))

        similarNum = bin(int(m.hexdigest(),16) ^ int(m1.hexdigest(),16)).count('1')  #检测对比两个hash值的相似度
        similarProb = 1-similarNum/256
        similarList.append(similarProb)
        
    temp = wordDict[testword2]
    for word in testwords2:
        temp1 = wordDict[word]
        
        m.update(''.join(temp).encode('utf-8'))
        m1.update(''.join(temp1).encode('utf-8'))

        similarNum = bin(int(m.hexdigest(),16) ^ int(m1.hexdigest(),16)).count('1')  #检测对比两个hash值的相似度
        similarProb = 1-similarNum/256
        similarList.append(similarProb)
    
    temp = wordDict[testword3]
    for word in testwords3:
        temp1 = wordDict[word]
        
        m.update(''.join(temp).encode('utf-8'))
        m1.update(''.join(temp1).encode('utf-8'))

        similarNum = bin(int(m.hexdigest(),16) ^ int(m1.hexdigest(),16)).count('1')  #检测对比两个hash值的相似度
        similarProb = 1-similarNum/256
        similarList.append(similarProb)
    #英文
    temp = wordDict1[testword4]
    for word in testwords4:
        temp1 = wordDict1[word]
        
        m.update(''.join(temp).encode('utf-8'))
        m1.update(''.join(temp1).encode('utf-8'))

        similarNum = bin(int(m.hexdigest(),16) ^ int(m1.hexdigest(),16)).count('1')  #检测对比两个hash值的相似度
        similarProb = 1-similarNum/256
        similarList.append(similarProb)
        
    temp = wordDict1[testword5]
    for word in testwords5:
        temp1 = wordDict1[word]
        
        m.update(''.join(temp).encode('utf-8'))
        m1.update(''.join(temp1).encode('utf-8'))

        similarNum = bin(int(m.hexdigest(),16) ^ int(m1.hexdigest(),16)).count('1')  #检测对比两个hash值的相似度
        similarProb = 1-similarNum/256
        similarList.append(similarProb)
    
    temp = wordDict1[testword6]
    for word in testwords6:
        temp1 = wordDict1[word]
        
        m.update(''.join(temp).encode('utf-8'))
        m1.update(''.join(temp1).encode('utf-8'))

        similarNum = bin(int(m.hexdigest(),16) ^ int(m1.hexdigest(),16)).count('1')  #检测对比两个hash值的相似度
        similarProb = 1-similarNum/256
        similarList.append(similarProb)
