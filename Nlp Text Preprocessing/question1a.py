# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 17:16:37 2020

@author: User
"""
from __future__ import division
from nltk.book import *


#vocabulary count

def vocabulary_count (a):
    if a=='6':
        b=len(set(text6))/len(text6)
    if a=='5':
        b=len(set(text5))/len(text5)
        
    return b




text_num=input("for text 5 press 5 for text 6 press 6 : ")
vc=vocabulary_count(text_num)
print("the lexical diversity of text",text_num,"is :",vc)

if text_num=='5':
    count1 = 100 * text5.count("omg")/len(text5)
    count2 = 100 * text5.count("OMG")/len(text5)
    count3 = 100 * text5.count("lol")/len(text5)
    print("some intresting facts the book chat corpus ")
    print("the word omg with lower case later is shown ",text5.count("omg"),"and is the",count1,"percent of the book")
    print("the word OMG with upper case later is shown ",text5.count("OMG"),"and is the",count2,"percent of the book")
    print("the word lol is shown ",text5.count("lol"),"and is the",count3,"percent of the book")
if text_num=='6':
    count1=100 * text6.count("LAUNCELOT")/len(text6)
    print("some intresting facts for the book monty pyhton and the holy grail")
    print("the word lAUNCELOT is shown",text6.count("LAUNCELOT"),"and is the ",count1,"percent of the book")
