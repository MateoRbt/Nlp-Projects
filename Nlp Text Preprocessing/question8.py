# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 17:31:36 2020

@author: User
"""
import string
import nltk
from nltk.book import *
import os

def cleaning(token1) :
    stopwords= nltk.corpus.stopwords.words('english')
    cleaned_tokens=[""]
    for token in token1:
        if token not in string.punctuation and token not in stopwords:
            cleaned_tokens.append(token)
    print(cleaned_tokens)
    print(len(set(cleaned_tokens)))
    
def cleaninggr(token1) :
    stopwords= nltk.corpus.stopwords.words('greek')
    cleaned_tokens=[""]
    for token in token1:
        if token not in string.punctuation and token not in stopwords:
            cleaned_tokens.append(token)
    print(cleaned_tokens)
    print(len(set(cleaned_tokens)))
    
tokens=text2[:200]
print(len(set(tokens)))
cleaning(tokens)

os.listdir('C:/Users/user/Desktop/anakthsh')
f=open('test1.txt',"r")
tokens1=f
print(len(set(tokens1)))
cleaninggr(tokens1)
