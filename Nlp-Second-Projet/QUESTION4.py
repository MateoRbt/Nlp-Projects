# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 22:19:45 2020

@author: User
"""

# importing libraries 
import numpy as np 
import os 
import nltk 
from nltk.stem import PorterStemmer 
from nltk.tokenize import TweetTokenizer 
import collections
import string 
from nltk.book import *



def preprocessing(final_string): 
		# Tokenize. 
	tokenizer = TweetTokenizer() 
	token_list = tokenizer.tokenize(final_string) 

	# Remove punctuations. 
	table = str.maketrans('', '', '\t') 
	token_list = [word.translate(table) for word in token_list] 
	punctuations = (string.punctuation).replace("'", "") 
	trans_table = str.maketrans('', '', punctuations) 
	stripped_words = [word.translate(trans_table) for word in token_list] 
	token_list = [str for str in stripped_words if str] 

	# Change to lowercase. 
	token_list =[word.lower() for word in token_list] 
	return token_list 

def table_creation(final_token_list):
    stemmer = PorterStemmer() 
    pos_index = {} 
    fileno=0
  
    for pos, term in enumerate(final_token_list): 
              
                    # First stem the term. 
                    term = stemmer.stem(term) 
  
                    # If term already exists in the positional index dictionary. 
                    if term in pos_index: 
                          
                        # Increment total freq by 1. 
                        pos_index[term][0] = pos_index[term][0] + 1
                          
                        # Check if the term has existed in that DocID before. 
                        if fileno in pos_index[term][1]: 
                            pos_index[term][1][fileno].append(pos) 
                              
                        else: 
                            pos_index[term][1][fileno] = [pos] 
  
                    # If term does not exist in the positional index dictionary  
                    # (first encounter). 
                    else: 
                          
                        # Initialize the list. 
                        pos_index[term] = [] 
                        # The total frequency is 1. 
                        pos_index[term].append(1) 
                        # The postings list is initially empty. 
                        pos_index[term].append({})       
                        # Add doc ID to postings list. 
                        pos_index[term][1][fileno] = [pos]
    fdist1 = FreqDist(final_token_list)
    samples=fdist1.most_common(3)
    print(pos_index)
    for sample in samples:
        print(sample)
    
t1="\t".join(text1[:50])

cleaned_t1=preprocessing(t1)

t2="\t".join(text2[:50])

cleaned_t2=preprocessing(t2)

table_creation(cleaned_t1)
print("///////////////////")
table_creation(cleaned_t2)
