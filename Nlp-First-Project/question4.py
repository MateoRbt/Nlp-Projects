# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 21:42:27 2020

@author: User
"""
from __future__ import division
from nltk.book import *

sent1 #εμφάνισε την sent1 του βιβλίου 1
tokens1=sent1 #βάλε την sent1 στην μεταβλητή token1
normalized_sent1=[x.lower() for x in tokens1] 
print(normalized_sent1)