# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 13:36:28 2022

@author: leo.peyronnet
"""
def get_space(matrice: list) -> int:
    b = 0
    for i in matrice:
        for j in i:
            if b < j:
                b = len(str(j))
    return b

def print_matrice(matrice: list):
    SP = get_space(matrice)
    s = ""
    for i in range(len(matrice)):
        vir = ","
        if i == len(matrice) - 1:
            vir = ""
        
        s += "\t["
        for j in range(len(matrice[i])):
            v = ","
            spacing = " " * (SP - len(str(matrice[i][j])))
            
            if j == len(matrice[i]) - 1:
                v = ""
            s += f" {spacing}{matrice[i][j]}{v}"
        s += f" ]{vir}\n"

    print(f"[\n{s}]")
    
def matrice(n):
    m = []
    for i in range(n):
        m.append([0] * n)
    
    for i in range(n):
        m[i][i] = 1
    return m

print_matrice(matrice(25))