# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 20:28:55 2020

@author: User
"""
from nltk.tokenize import TreebankWordTokenizer
from collections import Counter
import numpy as np 
import os 
import nltk 
from nltk.stem import PorterStemmer 
from nltk.tokenize import TweetTokenizer 
import collections
import string 
from nltk.book import *
from collections import OrderedDict
import copy
import math

document_tfidf_vectors = []

for doc in docs:
    
   vec = copy.copy(zero_vector)
   tokens = tokenizer.tokenize(doc.lower())
   token_counts = Counter(tokens)
   for key, value in token_counts.items():
       docs_containing_key = 0
       for _doc in docs:
           if key in _doc:
               docs_containing_key += 1
       tf = value / len(lexicon)
       if docs_containing_key:
          idf = len(docs) / docs_containing_key
       else:
           idf = 0
       vec[key] = tf * idf
   document_tfidf_vectors.append(vec)

