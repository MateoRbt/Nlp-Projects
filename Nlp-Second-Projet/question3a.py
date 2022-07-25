# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 20:41:28 2020

@author: User
"""

import string
import nltk
from nltk.book import *
import os
import nltk.tokenize
import numpy as np
import pandas as pd

def table_creation(sentences):
    corpus = {}
    corpus['sent0'] = dict((tok.strip('.'), 1) for tok in sentences.split())
    for i, sent in enumerate(sentences.split('\n')):
     corpus['sent{}'.format(i + 1)] = dict((tok, 1) for tok in sent.split())
    df = pd.DataFrame.from_records(corpus).fillna(0).astype(int).T
    print( df[df.columns[:0]])
    df=df.T
    print( "sentence 1 common words with sentence2",df.sent1.dot(df.sent2))
    print( "sentence 1 common words with sentence3",df.sent1.dot(df.sent3))
    print( "sentence 1 common words with sentence4",df.sent1.dot(df.sent4))
    print( "sentence 1 common words with sentence5",df.sent1.dot(df.sent5))
    print( "sentence 2 common words with sentence3",df.sent2.dot(df.sent3))
    print( "sentence 2 common words with sentence4",df.sent2.dot(df.sent4))
    print( "sentence 2 common words with sentence5",df.sent2.dot(df.sent5))
    print( "sentence 3 common words with sentence4",df.sent3.dot(df.sent4))
    print( "sentence 3 common words with sentence5",df.sent3.dot(df.sent5))
    print( "sentence 4 common words with sentence5",df.sent4.dot(df.sent5))
 




sentence="Thomas Jefferson began building Monticello at the age of 26.\n"\
          "This is a sentence for testing exercise one! \n"  \
          "This is a text for testing exercise three  \n"  \
          "You can find the common words between 2 sentences \n" \
          "can you find the common words?"


table_creation(sentence)