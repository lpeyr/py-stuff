# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 12:17:29 2023

@author: leo.peyronnet
"""
def testUneLettre(c):
    return ord(c) >= 65 and ord(c) <= 90

# tests

print(testUneLettre("c"))
print(testUneLettre("A"))