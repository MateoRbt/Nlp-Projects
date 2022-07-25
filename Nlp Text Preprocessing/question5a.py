# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 15:17:00 2020

@author: User
"""

from __future__ import division
from nltk.book import *

from nltk.stem import *
import os

os.listdir('C:/Users/user/Desktop/anakthsh')

f=open('test1.txt',"r")
token1=f.read()
#print(token1)
porter = PorterStemmer()

for t in token1 :
   print( porter.stem(t))

print("//////////////////////////////////")
wnl = WordNetLemmatizer()
for i in token1 :
    print(wnl.lemmatize(i) )
