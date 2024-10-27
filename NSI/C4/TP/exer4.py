# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 12:20:12 2023

@author: leo.peyronnet
"""

def maj(c):
    return ord(c) >= 65 and ord(c) <= 90

def minuscule(c):
    string = ""
    for char in c:
        if maj(char):
            string += chr(ord(char)+32)
        else:
            string += char
    return string

# tests
print(minuscule("Vive la NSI"))