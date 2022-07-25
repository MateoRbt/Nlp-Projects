# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 17:35:23 2020

@author: User
"""
import nltk


stopwordsen = nltk.corpus.stopwords.words('english')
count_en = len(set(stopwordsen))
print(count_en)

stopwordsen = nltk.corpus.stopwords.words('english')
count_en = len(set(stopwordsen))
print(stopwordsen)


stopwordsgr = nltk.corpus.stopwords.words('greek')
count_gr = len(set(stopwordsgr))
print(count_gr)

stopwordsgr = nltk.corpus.stopwords.words('greek')
print(stopwordsgr)