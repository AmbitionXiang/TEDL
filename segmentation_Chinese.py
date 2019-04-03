# -*- coding: utf-8 -*-
"""
jieba Segementation
"""
import jieba
import jieba.analyse
import jieba.posseg as pseg
import codecs, sys
import matplotlib.pyplot as plt
from collections import Counter
import json

def cut_words(sentence):
    #print sentence
    return " ".join(jieba.cut(sentence)).encode('utf8')
 
c = Counter()
f = codecs.open('wiki.zh.jian.text', 'r', encoding="utf8")
target = codecs.open("zh.jian.wiki.seg.txt", 'w', encoding="utf8")
print('open files')
line_num = 1
line = f.readline()
while line:
    print('---- processing ', line_num, ' article----------------')
    seg_list = jieba.cut(line)
#    for x in seg_list:
#        if len(x)>1 and x != '\r\n':
#            c[x] += 1
    line_seg = " ".join(seg_list)
    target.writelines(line_seg)
    line_num = line_num + 1
    line = f.readline()
f.close()
target.close()

exit()
