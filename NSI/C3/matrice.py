# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 12:40:24 2022

@author: leo.peyronnet

input =
[
     [1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]
]

output:
[
     [1, 4],
     [2, 5],
     [3, 6]
]

"""


def transposer(matrice: list) -> list:
    nb_colonne = len(matrice[0])
    nb_lignes = len(matrice)

    m = []

    for i in range(nb_colonne):
        l = []
        for j in range(nb_lignes):
            l.append(matrice[j][i])
        m.append(l)
    return m


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


def gen_matrice(w: int, h: int) -> list:
    S = 0
    m = []
    for i in range(h):
        t = []
        for j in range(w):
            S += 1
            t.append(S)
        m.append(t)
    return m


# tests
impt = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

impt2 = [
    range(1, 20),
    range(20, 39),
    range(39, 58),
    range(58, 77)
]

print_matrice(impt)
print_matrice(transposer(impt))

print_matrice(impt2)
print_matrice(transposer(impt2))

M = gen_matrice(20, 20)
print_matrice(M)
print_matrice(transposer(M))
