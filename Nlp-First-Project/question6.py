# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 16:02:10 2020

@author: User
"""

import nltk
from nltk.book import *

from nltk.tokenize import word_tokenize
import string

token1=''.join(text2[:200])

tokenized= nltk.word_tokenize(token1)
print(tokenized)
print("////////////")
print(token1.split())