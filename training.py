# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 11:55:14 2021

@author: user
"""

from gensim.models.word2vec import Text8Corpus
from gensim.models.phrases import Phrases
# Cleaned corpus
sentences = Text8Corpus('train_text.txt')
first_sentence = next(iter(sentences))
print(first_sentence[:10])

phrase_model1 = Phrases(sentences, min_count=1, threshold=0.3)
phrase_model1.save('phrase_model1.pkl')
print("model with threshold=0.3, scoring='default' created")

phrase_model2 = Phrases(sentences, min_count=1, threshold=0.5)
phrase_model2.save('phrase_model2.pkl')
print("model with threshold=0.5, scoring='default' created")

phrase_model3 = Phrases(sentences, min_count=1, threshold=1)
phrase_model3.save('phrase_model3.pkl')
print("model with min+count=1, threshold=1 created")

print("3 models to cleaned text have been made")

# # Uncleaned Corpus
sentences1 = Text8Corpus('raw.txt')
first_sentence = next(iter(sentences1))
print(first_sentence[:10])

phrase_model6 = Phrases(sentences1, min_count=1, threshold=0.3)
phrase_model6.save('phrase_model6.pkl')
print("model with threshold=0.3, scoring='default' created")

phrase_model7 = Phrases(sentences1, min_count=1, threshold=0.5)
phrase_model7.save('phrase_model7.pkl')
print("model with threshold=0.1, scoring='default' created")

phrase_model8 = Phrases(sentences1, min_count=1, threshold=1)
phrase_model8.save('phrase_model8.pkl')
print("model with threshold=1, scoring='default' created")

print("3 models to uncleaned text have been made")
