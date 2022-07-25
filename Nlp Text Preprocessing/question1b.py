# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 18:01:00 2020

@author: User
"""

from __future__ import division
from nltk.book import *

print("text5  statistics for this words")
count1= text5.count("sick")/len(text5)
print("sick shown :",text5.count("sick"))
count2= text5.count("england")/len(text5)
print("england shown :",text5.count("england"))
count3=text5.count("hand")/len(text5)
print("hand shown :",text5.count("hand"))

print("text5 percentage ")
percent1=100*count1
print("sick ",percent1,"per cent")
percent2=100*count2
print("england",percent2,"per cent")
percent3=100*count3
print("hand ",percent3,"per cent")


print("text 6 statistcs for this word")
count4=text6.count("sick")/len(text6)
print("sick",text6.count("sick"))
count5=text6.count("england")/len(text6)
print("england",text6.count("england"))
count6=text6.count("hand")/len(text6)
print("hand",text6.count("hand"))


print("text6 percentage ")
percent4=100*count4
print("sick ",percent1,"per cent")
percent5=100*count5
print("england",percent5,"per cent")
percent6=100*count6
print("hand ",percent6,"per cent")

