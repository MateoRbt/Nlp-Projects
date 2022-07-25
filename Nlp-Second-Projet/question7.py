# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 18:23:36 2020

@author: User
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.book import *


docs=[" ".join(text1[:10])]
corpus = docs+[" ".join(text2[:10])]
vectorizer = TfidfVectorizer(min_df=1)
model = vectorizer.fit_transform(corpus) 
print(corpus)
print(model.todense().round(2))
