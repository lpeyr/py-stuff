# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 17:41:10 2023

@author: veroe
"""

import csv
import random

# Définir le nombre de sommets et la probabilité d'une arête
n_sommets = 300
probabilite_arete = 0.3  # 30% de chance d'avoir une arête entre deux sommets

# Générer une matrice de distances pour un graphe parcimonieux
matrice_distances = [[0 if i == j else random.randint(1, 100) if random.random() < probabilite_arete else 0 for j in range(n_sommets)] for i in range(n_sommets)]

# Écrire la matrice dans un fichier CSV
with open('grand_graphe.csv', 'w', newline='') as fichier_csv:
    writer = csv.writer(fichier_csv)
    for ligne in matrice_distances:
        writer.writerow(ligne)

print("Fichier CSV pour grand graphe généré : grand_graphe.csv")
