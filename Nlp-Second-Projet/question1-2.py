# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 17:20:20 2020

@author: User
"""

import string
import nltk
from nltk.book import *
import os
import nltk.tokenize
import numpy as np
import pandas as pd

def table_creation1(sentences):
    cleaned_sentence=nltk.word_tokenize(sentences)
    vocab = sorted(set(cleaned_sentence))
    ",".join(vocab)
    num_token= len(cleaned_sentence)
    vocab_size = len(vocab)
    onehot_vector = np.zeros((num_token, vocab_size), int)
    for i, word in enumerate(cleaned_sentence):
        onehot_vector[i, vocab.index(word)] = 1
    print(pd.DataFrame(onehot_vector, columns=vocab))

def table_creation2(sentences):
    cleaned_sentence=str.split(sentences)
    vocab = sorted(set(cleaned_sentence))
    ",".join(vocab)
    num_token= len(cleaned_sentence)
    vocab_size = len(vocab)
    onehot_vector = np.zeros((num_token, vocab_size), int)
    for i, word in enumerate(cleaned_sentence):
        onehot_vector[i, vocab.index(word)] = 1
    print(pd.DataFrame(onehot_vector, columns=vocab))

sentence1="Thomas Jefferson began building Monticello at the age of 26."
sentence2="This is a sentence for testing exercise one!"

print("method 1 with nltk word tokenazation")
table_creation1(sentence1)
print("//////////////////////////////////////")
table_creation1(sentence2)

print("method2 with split")

table_creation2(sentence1)
print("//////////////////////////////////////")
table_creation2(sentence2)




