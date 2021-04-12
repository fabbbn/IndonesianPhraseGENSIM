# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 11:55:14 2021

@author: user
"""

from gensim.models.word2vec import Text8Corpus
from gensim.models.phrases import Phrases
# Cleaned corpus!
sentences = Text8Corpus('C:/Users/user/Documents/SEMESTER6/NLP/Project/program/train_text.txt')
first_sentence = next(iter(sentences))
print(first_sentence[:10])

# phrase_model1 = Phrases(sentences, min_count=1, threshold=0.3)
# phrase_model1.save('C:/Users/user/Documents/SEMESTER6/NLP/Project/program/phrase_model1.pkl')
# print("model with threshold=0.3, scoring='default' created")

# phrase_model2 = Phrases(sentences, min_count=1, threshold=0.5)
# phrase_model2.save('C:/Users/user/Documents/SEMESTER6/NLP/Project/program/phrase_model2.pkl')
# print("model with threshold=0.1, scoring='default' created")

# phrase_model3 = Phrases(sentences, min_count=2, threshold=1, delimiter=' ', max_vocab_size=1000000)
# phrase_model3.save('C:/Users/user/Documents/SEMESTER6/NLP/Project/program/phrase_model01.pkl')
# print("model with min+count=2, threshold=1, scoring='default' created")

# phrase_model4 = Phrases(sentences, min_count=1, threshold=0.5, scoring='npmi')
# phrase_model4.save('C:/Users/user/Documents/SEMESTER6/NLP/Project/program/phrase_model4.pkl')
# print("model with threshold=0.5, scoring='npmi' created")

# phrase_model5 = Phrases(sentences, min_count=1, threshold=1, scoring='npmi')
# phrase_model5.save('C:/Users/user/Documents/SEMESTER6/NLP/Project/program/phrase_model5.pkl')
# print("model with threshold=1, scoring='npmi' created")

# print("5 models to cleaned text have been made")

# # Uncleaned Corpus
sentences1 = Text8Corpus('C:/Users/user/Documents/SEMESTER6/NLP/Project/program/raw.txt')
first_sentence = next(iter(sentences1))
print(first_sentence[:10])

phrase_model6 = Phrases(sentences1, min_count=1, threshold=0.3)
phrase_model6.save('C:/Users/user/Documents/SEMESTER6/NLP/Project/program/phrase_model6.pkl')
print("model with threshold=0.3, scoring='default' created")

phrase_model7 = Phrases(sentences1, min_count=1, threshold=0.5)
phrase_model7.save('C:/Users/user/Documents/SEMESTER6/NLP/Project/program/phrase_model7.pkl')
print("model with threshold=0.1, scoring='default' created")

# phrase_model8 = Phrases(sentences1, min_count=1, threshold=1)
# phrase_model8.save('C:/Users/user/Documents/SEMESTER6/NLP/Project/program/phrase_model8.pkl')
# print("model with threshold=1, scoring='default' created")

# phrase_model9 = Phrases(sentences, min_count=1, threshold=0.5, scoring='npmi')
# phrase_model9.save('C:/Users/user/Documents/SEMESTER6/NLP/Project/program/phrase_model9.pkl')
# print("model with threshold=0.5, scoring='npmi' created")

# phrase_model10 = Phrases(sentences, min_count=1, threshold=1, scoring='npmi')
# phrase_model10.save('C:/Users/user/Documents/SEMESTER6/NLP/Project/program/phrase_model10.pkl')
# print("model with threshold=1, scoring='npmi' created")
