#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 10:49:27 2022

@author: merveille
"""

from random import randint

taille_jeu = 4
nb_bombes = 2
gagne = False
perdu = False

jeu_visible = []
for i in range(taille_jeu):
    jeu_visible.append([])
    for j in range(taille_jeu):
        jeu_visible[i].append(-1)

jeu = []
for i in range(taille_jeu):
    jeu.append([])
    for j in range(taille_jeu):
        jeu[i].append(0)

bombes = 0
while bombes < nb_bombes:
    x = randint(0, taille_jeu - 1)
    y = randint(0, taille_jeu - 1)
    if jeu[x][y] != -1:
        jeu[x][y] = -1
        bombes += 1

for i in range(taille_jeu):
    for j in range(taille_jeu):
        if jeu[i][j] == -1:
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if k != 0 or l != 0:
                        if (
                            i + k >= 0
                            and i + k < taille_jeu
                            and j + l >= 0
                            and j + l < taille_jeu
                            and jeu[i + k][j + l] != -1
                        ):
                            jeu[i + k][j + l] += 1

for i in range(taille_jeu):
    ligne = ""
    for j in range(taille_jeu):
        if jeu_visible[i][j] == -1:
            ligne += "_ "
        else:
            ligne += str(jeu_visible[i][j]) + " "
    print(ligne)
print()

while not gagne and not perdu:
    x = -1
    y = -1
    while x < 0 or x >= taille_jeu or y < 0 or y >= taille_jeu:
        print(f"les coordonnées doivent être comprises entre 0 et {taille_jeu-1}")
        x = int(input("Choix de l'indice de ligne ? "))
        y = int(input("Choix de l'indice de colonne ? "))

    if jeu[x][y] == -1:
        perdu = True
    else:
        cases_a_decouvrir = [[x, y]]
        while len(cases_a_decouvrir) > 0:
            i, j = cases_a_decouvrir.pop()
            if jeu[i][j] != 0:
                jeu_visible[i][j] = jeu[i][j]  # Afficher la case
            else:
                jeu_visible[i][j] = 0  # Afficher la case
                for k in range(-1, 2):
                    for l in range(-1, 2):
                        if (
                            i + k >= 0
                            and i + k < len(jeu)
                            and j + l >= 0
                            and j + l < len(jeu)
                        ):
                            if jeu_visible[i + k][j + l] == -1:  # Case non visitée
                                cases_a_decouvrir.append([i + k, j + l])

    for i in range(taille_jeu):
        ligne = ""
        for j in range(taille_jeu):
            if jeu_visible[i][j] == -1:
                ligne += "_ "
            else:
                ligne += str(jeu_visible[i][j]) + " "
        print(ligne)
    print()

    compteur = len(jeu_visible) ** 2
    for i in range(len(jeu_visible)):
        for j in range(len(jeu_visible)):
            if jeu_visible[i][j] == -1:
                compteur -= 1
    if compteur == taille_jeu ** 2 - nb_bombes:
        gagne = True

if perdu:
    print("Vous avez perdu !")
    for i in range(len(jeu)):
        ligne = ""
        for j in range(len(jeu)):
            if jeu[i][j] == -1:
                ligne += "* "
            else:
                ligne += str(jeu[i][j]) + " "
        print(ligne)
    print()
else:
    print("Vous avez gagné !")
