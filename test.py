# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 10:57:39 2021

@author: user
"""
from gensim.test.utils import datapath
from gensim.models.word2vec import Text8Corpus
from gensim.models.phrases import Phrases
from clean_text import *
import pandas as pd
import re


def main(q, p, model):
    pattern = re.compile('^.+\_.+$')
    d_total = d_true = d_false = e_true = e_false = e_total = 0
    true = []
    for i in range(len(q)):
        labeled_phrases = p[i].split(',')
        label = 0
        detected = model[clean_text(q[i]).split()]
        # print(detected)
        newlist = list(filter(pattern.match, detected)) # Read Note
        # print("detected", len(newlist))
        # print(newlist)
        for ph in labeled_phrases:
            ph = ph.strip().replace(' ', '_').lower()
            # print(ph)
            t=0
            if ph in detected:
                # print(ph)
                true.append(ph)
                d_true+=1
                e_true+=1
                t+=1
                # print("benar = "+ph)
            else:
                e_false+=1
                # print("salah = "+ph)
            label+=1
            # print("true", t)
            # print("false", len(newlist)-t)
            # print()
            d_false+=(len(newlist)-t)
            d_total+=(len(newlist))
        e_total+=label
    print("total frasa yang diharapkah = ", e_total)
    print("total frasa terdeteksi yang benar = ", d_true)
    print("total frasa terdeteksi yang salah = ", d_false)
    print("total frasa terdeteksi = ", d_total)
    
df = pd.read_csv('dataset_uji_dua_label.csv')
print(df.tail(15))

queries = df['pertanyaan'].values
expected_phrase = df['label'].values

# model1 = Phrases.load('C:/Users/user/Documents/SEMESTER6/NLP/Project/program/phrase_model1.pkl')
# model2 = Phrases.load('C:/Users/user/Documents/SEMESTER6/NLP/Project/program/phrase_model2.pkl')
# model3 = Phrases.load('C:/Users/user/Documents/SEMESTER6/NLP/Project/program/phrase_model3.pkl')
# model4 = Phrases.load('C:/Users/user/Documents/SEMESTER6/NLP/Project/program/phrase_model6.pkl')
# model5 = Phrases.load('C:/Users/user/Documents/SEMESTER6/NLP/Project/program/phrase_model7.pkl')
# model6 = Phrases.load('C:/Users/user/Documents/SEMESTER6/NLP/Project/program/phrase_model8.pkl')

main(queries, expected_phrase, model1)
print()
main(queries, expected_phrase, model2)
print()
main(queries, expected_phrase, model3)
print()
main(queries, expected_phrase, model4)
print()
main(queries, expected_phrase, model5)
print()
main(queries, expected_phrase, model6)
