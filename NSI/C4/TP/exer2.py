# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 12:14:56 2023

@author: leo.peyronnet
"""
def ascii(C):
    nbrs = []
    for c in C:
        nbrs.append(ord(c))
    return nbrs

# tests
print(ascii("Vive la NSI"))