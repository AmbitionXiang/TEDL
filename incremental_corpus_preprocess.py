# -*- coding: utf-8 -*-

import os
import re
import codecs
 
 
def replace_func(input_file):
    p1 = re.compile(r'-\{.*?(zh-hans|zh-cn):([^;]*?)(;.*?)?\}-')
    p2 = re.compile(r'[(][: @ . , ？！\s][)]')
    p3 = re.compile(r'[「『]')
    p4 = re.compile(r'[\s+\.\!\/_,$%^*(+\"\')]+|[+——()?【】“”！，。？、~@#￥%……&*（）0-9 , : ; \-\ \[\ \]\ ]')
    outfile = codecs.open('std_' + input_file, 'w', 'utf-8')
    with codecs.open(input_file, 'r', 'utf-8') as myfile:
        for line in myfile:
            line = p1.sub(r' ', line)
            line = p2.sub(r' ', line)
            line = p3.sub(r' ', line)
            line = p4.sub(r' ', line)
            outfile.write(line)
    outfile.close()
 
def run():
    data_names = ['incremental_corpus.txt']
    for data_name in data_names:
        replace_func(data_name)
        print('{0} has been processed !'.format(data_name))
if __name__ == '__main__':
    run()