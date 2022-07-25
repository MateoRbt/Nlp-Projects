# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 17:26:53 2020

@author: User
"""

from __future__ import division
import string
import nltk
from nltk.book import *
import os



def calculate_words (token_1) :
        result1 = len(set(token_1))/len(token_1)
        print(result1)
        

def clean_words (token1):
    stopwords= nltk.corpus.stopwords.words('english')
    cleaned_tokens=[""]
    for token in token1:
        if token not in string.punctuation and token not in stopwords:
            cleaned_tokens.append(token)
    return(cleaned_tokens)
    
t=text2[:200]
calculate_words(t)
t1=clean_words(t)
calculate_words(t1)
