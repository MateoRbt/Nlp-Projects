# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 21:57:10 2020

@author: User
"""
from __future__ import division
from nltk.book import *

from nltk.stem import *

token1=text2[:200]

print("////////////////////////////////////")
normalized_token=[x.lower() for x in token1] 
print("///////////////////////////////////")

porter = PorterStemmer()

for t in token1 :
   print( porter.stem(t))

print("//////////////////////////////////")
wnl = WordNetLemmatizer()
for i in token1 :
    print(wnl.lemmatize(i) )
