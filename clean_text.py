# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 10:52:50 2021

@author: user
"""

# for cleaning text
import re

def clean_text(line):
    # cleaning wild char except maybe a repetition word
    cleanline = re.sub(r"[^\w\s\-]", "", line).lower()
    
    # cleaning digit out of a word and non repetition word (2013 deleted but not h2o, co2)
    cleanline = re.sub(r'(\s\d+\s+)|(\s*\-+(a-z)*\s*)', ' ', cleanline)
    
    # cleaning non indonesian character
    cleanline = re.sub("[^(a-z)(\-)(0-9)+\s{1}]", "", cleanline)
    
    # cleaning whitespaces
    cleanline = re.sub("\s+", " ", cleanline)
    # print(cleanline)
    return cleanline
