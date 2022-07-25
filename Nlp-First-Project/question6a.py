# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 16:28:06 2020

@author: User
"""


from nltk.book import *

from nltk.stem import *
import os

import nltk

from nltk.tokenize import word_tokenize
import string

os.listdir('C:/Users/user/Desktop/anakthsh')

f=open('test1.txt',"r")
t=f.read
token1=''.join(f)

tokenized= nltk.word_tokenize(token1)
print(tokenized)

print("////////////")
print(token1.split())