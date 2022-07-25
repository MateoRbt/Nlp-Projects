# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 20:12:40 2020

@author: User
"""

from __future__ import division
from nltk.book import *

len(text1)
fdist1 = FreqDist(text1) 
fdist1
fdist1.most_common(50)
fdist1.plot(50)
