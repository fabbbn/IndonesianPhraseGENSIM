# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 10:57:39 2021

@author: user
"""
from gensim.test.utils import datapath
from gensim.models.word2vec import Text8Corpus
from gensim.models.phrases import Phrases
from clean_text import *
import re
import pandas as pd


def model1(q, p):
    print("load model...")
    model = Phrases.load('phrase_model1.pkl')
    print("load model successful")
    data = []
    pattern = re.compile('^.+\_.+$')
    
    for i in range(len(q)):
        labeled_phrases = p[i].split(',')
        detected = model[clean_text(q[i]).split()]        
        newlist = list(filter(pattern.match, detected)) # Read Note
        for ph in labeled_phrases:
            ph = ph.strip().replace(' ', '_').lower()
            if ph in detected:
                obj = (q[i], ph.replace('_', ' '), ph.replace('_', ' '), 1)
            else:
                obj = (q[i], ph.replace('_', ' '), "-" , 0)
            data.append(obj)
    return data

def model2(q, p):
    print("load model...")
    model = Phrases.load('phrase_model2.pkl')
    print("load model successful")
    data = []
    pattern = re.compile('^.+\_.+$')
    
    for i in range(len(q)):
        labeled_phrases = p[i].split(',')
        detected = model[clean_text(q[i]).split()]        
        newlist = list(filter(pattern.match, detected)) # Read Note
        for ph in labeled_phrases:
            ph = ph.strip().replace(' ', '_').lower()
            if ph in detected:
                obj = (q[i], ph.replace('_', ' '), ph.replace('_', ' '), 1)
            else:
                obj = (q[i], ph.replace('_', ' '), "-" , 0)
            data.append(obj)
    return data


def model3(q, p):
    print("load model...")
    model = Phrases.load('phrase_model3.pkl')
    print("load model successful")
    data = []
    pattern = re.compile('^.+\_.+$')
    
    for i in range(len(q)):
        labeled_phrases = p[i].split(',')
        detected = model[clean_text(q[i]).split()]        
        newlist = list(filter(pattern.match, detected)) # Read Note
        for ph in labeled_phrases:
            ph = ph.strip().replace(' ', '_').lower()
            if ph in detected:
                obj = (q[i], ph.replace('_', ' '), ph.replace('_', ' '), 1)
            else:
                obj = (q[i], ph.replace('_', ' '), "-" , 0)
            data.append(obj)
    return data


def model4(q, p):
    print("load model...")
    model = Phrases.load('phrase_model6.pkl')
    print("load model successful")
    data = []
    pattern = re.compile('^.+\_.+$')
    
    for i in range(len(q)):
        labeled_phrases = p[i].split(',')
        detected = model[clean_text(q[i]).split()]        
        newlist = list(filter(pattern.match, detected)) # Read Note
        for ph in labeled_phrases:
            ph = ph.strip().replace(' ', '_').lower()
            if ph in detected:
                obj = (q[i], ph.replace('_', ' '), ph.replace('_', ' '), 1)
            else:
                obj = (q[i], ph.replace('_', ' '), "-" , 0)
            data.append(obj)
    return data


def model5(q, p):
    print("load model...")
    model = Phrases.load('phrase_model7.pkl')
    print("load model successful")
    data = []
    pattern = re.compile('^.+\_.+$')
    
    for i in range(len(q)):
        labeled_phrases = p[i].split(',')
        detected = model[clean_text(q[i]).split()]        
        newlist = list(filter(pattern.match, detected)) # Read Note
        for ph in labeled_phrases:
            ph = ph.strip().replace(' ', '_').lower()
            if ph in detected:
                obj = (q[i], ph.replace('_', ' '), ph.replace('_', ' '), 1)
            else:
                obj = (q[i], ph.replace('_', ' '), "-" , 0)
            data.append(obj)
    return data
    

def model6(q, p):
    print("load model...")
    model = Phrases.load('phrase_model8.pkl')
    print("load model successful")
    data = []
    pattern = re.compile('^.+\_.+$')
    
    for i in range(len(q)):
        labeled_phrases = p[i].split(',')
        detected = model[clean_text(q[i]).split()]        
        newlist = list(filter(pattern.match, detected)) # Read Note
        for ph in labeled_phrases:
            ph = ph.strip().replace(' ', '_').lower()
            if ph in detected:
                obj = (q[i], ph.replace('_', ' '), ph.replace('_', ' '), 1)
            else:
                obj = (q[i], ph.replace('_', ' '), "-" , 0)
            data.append(obj)
    return data
