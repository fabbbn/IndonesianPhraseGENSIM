# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 14:54:24 2021

@author: user
"""

from gensim.test.utils import datapath
from gensim.models.word2vec import Text8Corpus
from gensim.models.phrases import Phrases
import re
import os
from clean_text import *

# DATA 1:  punctuation and other symbols pattern removed
clean = open('./training_dataset/train_text.txt', 'w')
root = "./text"
dirs = os.listdir(root)
for dir in dirs:
    print(dir)
    extracts = os.listdir(root+'/'+dir+'/')
    for ext in extracts:
        print('\t' + ext)
        path = root + '/' + dir + '/' + ext
        f1 = open(path, 'r', encoding='utf-8').read()
        for line in f1.split('\n'):
            if ('<doc id' not in line) and ('</doc' not in line):
                cleanline = clean_text(line)
                # print(cleanline)
                clean.write(cleanline + "\n")

clean.close()
print("file train_text.txt has been created")

# DATA 2:  punctuation and other symbols pattern removed
clean = open('./training_dataset/raw.txt', 'w')
root = "./text"
dirs = os.listdir(root)
# print(dirs)
for dir in dirs:
    print(dir)
    extracts = os.listdir(root+'/'+dir+'/')
    for ext in extracts:
        print('\t' + ext)
        path = root + '/' + dir + '/' + ext
        f1 = open(path, 'r', encoding='ascii', errors='ignore').read()
        for line in f1.split('\n'):
            if ('<doc id' not in line) and ('</doc' not in line):
                clean.write(str(line) + "\n")

clean.close()
print("file raw.txt has been created")
