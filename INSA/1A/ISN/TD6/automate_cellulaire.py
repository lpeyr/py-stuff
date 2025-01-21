#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

size = 21
nb_iterations = size // 2 - 1
numero_jeu_regles = 1


# Initialisation de l'automate
def init_automate(n):
    liste = []
    for i in range(n):
        if i == n // 2:
            liste.append(0)
        else:
            liste.append(1)
    return liste


# INIT AFFICHAGE
grid = init_automate(size)
g = []  #
g.append(grid)  # Ajout de l'etat t=0 de l'automate

for j in range(nb_iterations):

    g.append(grid)  # Ajout de la mise à jour de l'automate

# AFFICHAGE
plt.imshow(g)
plt.axis("off")
plt.show()
