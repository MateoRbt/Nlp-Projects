# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 19:03:24 2020

@author: User
"""

import string
import nltk
from nltk.book import *
import os
import os
import nltk.tokenize
import numpy as np
import pandas as pd
from scipy.spatial import distance

def table_creation(sentences):
    corpus = {}
    corpus['sent0'] = dict((tok.strip('.'), 1) for tok in sentences.split())
    for i, sent in enumerate(sentences.split('\n')):
     corpus['sent{}'.format(i + 1)] = dict((tok, 1) for tok in sent.split())
    df = pd.DataFrame.from_records(corpus).fillna(0).astype(int).T
    print( df[df.columns[:0]])
    df=df.T
    print( "sentence 1 common words with sentence2",df.sent1.dot(df.sent2))
    common_words= [(k, v) for (k, v) in (df.sent1 & df.sent2).items() if v]
    print("the words that are in common are \t",common_words)

 
    
    
    


t="\t".join(text1[:50])
t2="\t".join(text2[:50])
sentence=t+"\n"+t2
table_creation(sentence)

