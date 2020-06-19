#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import nltk
"""
Created on Wed Jun 10 16:44:27 2020

@author: luis
"""

sentence="1 dia un perro murio, el siguiente dia el mundo lloro"

tokens= nltk.word_tokenize(sentence)

print (tokens)


#%%
file= open("texto.txt")

contenido = file.read()

tokens= nltk.word_tokenize(contenido)
print(tokens)


file.close()
#%%

