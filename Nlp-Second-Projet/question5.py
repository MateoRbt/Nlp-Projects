# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 19:21:16 2020

@author: User
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 16:12:30 2020

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

nltk.download('stopwords', quiet=True)


def create_vec(docs):
    doc_tokens = []
    tokenizer = TreebankWordTokenizer()

    for doc in docs:
        doc_tokens += [sorted(tokenizer.tokenize(doc.lower()))]
    len(doc_tokens[0])
    all_doc_tokens = sum(doc_tokens, [])
    lexicon = sorted(set(all_doc_tokens))
    zero_vector = OrderedDict((token, 0) for token in lexicon)

    doc_vectors = []
    for doc in docs:
     vec = copy.copy(zero_vector)
     tokens = tokenizer.tokenize(doc.lower())
     token_counts = Counter(tokens)
     for key, value in token_counts.items():
       vec[key] = value / len(lexicon)
     doc_vectors.append(vec)    
        

    return(doc_vectors)   
       
       
def cosine (vec1,vec2):
    vec1 = [val for val in vec1.values()]
    vec2 = [val for val in vec2.values()]
     
    dot_prod = 0
    for i, v in enumerate(vec1):
        dot_prod += v * vec2[i]
    
    mag_1 = math.sqrt(sum([x**2 for x in vec1]))
    mag_2 = math.sqrt(sum([x**2 for x in vec2]))

    prod=dot_prod / (mag_1 * mag_2)
    print(prod)
    
    

sents=["Thomas Jefferson began building Monticello at the age of 26."]
sents=sents+["This is a sentence for testing exercise one!"]
vec=[]
vec=create_vec(sents)
cosine(vec[0],vec[1])

t1=["\t".join(text1[:50])]
t1=t1+["\t".join(text2[:50])]
vec=create_vec(t1)
cosine(vec[0],vec[1])

t2=["\t".join(text1)]
t2=t2+["\t".join(text2)]
vec=create_vec(t2)
cosine(vec[0],vec[1])
  
       
       
       
       
       
       
       
       