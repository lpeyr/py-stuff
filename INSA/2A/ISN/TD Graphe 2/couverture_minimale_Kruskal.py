# -*- coding: utf-8 -*-
import csv
import timeit

"""
Created on Wed Nov  1 13:22:13 2023

@author: veroe
"""

####Algorithme de KRUSKAL (la bonne solution avec empêchement de former des cycles précédé d'un tri direct des longueurs d'arêtes)


def parent(Sp, s):
    while Sp[s] != s:
        s = Sp[s]
    return s


# La fonction parent est donc utilisée pour déterminer si deux nœuds sont déjà connectés dans l'arbre couvrant minimal en vérifiant s'ils appartiennent au même ensemble


def kruskal_couverture_mini(dico_adjacences):
    aretes = []

    for sommetA in dico_adjacences:
        for sommetB, distance in dico_adjacences[sommetA].items():
            aretes.append((sommetA, sommetB, distance))

    aretes.sort(key=lambda x: x[2])  # Trie les arêtes par poids (distance)

    nombre_sommets = len(dico_adjacences)
    sommetParent = {}
    # on crée la structure parent (ou arete interdite pour s'assurer de ne pas fariquer de cycles)
    for i in range(nombre_sommets):
        sommetParent[i] = i

    couverture_mini = []
    nombre_aretes = 0

    while (
        nombre_aretes < nombre_sommets - 1
    ):  # Utilise une boucle while avec une condition alternative
        arete_courante = aretes.pop(0)  # Retire la première arête de la liste triée
        sommetA, sommetB, distance = arete_courante
        sommetParentDeA = parent(sommetParent, sommetA)
        sommetParentDeB = parent(sommetParent, sommetB)

        if sommetParentDeA != sommetParentDeB:
            couverture_mini.append(
                (sommetA, sommetB, distance)
            )  # on ajoute l'arête au CMG
            nombre_aretes += 1
            sommetParent[sommetParentDeA] = sommetParentDeB

    return couverture_mini


#######Q 3.2 (sur la partie des grands graphes / graphes de taille et de densité variable)


def csvToDic(fic):
    adjacents = {}  # Dictionnaire contenant comme clefs les sommets et
    # comme valeurs la liste des sommets pouvant etre rejoints
    # depuis le sommet designe par la clef.
    # Seuls les arcs non nuls sont retenus ici.
    with open(fic) as f:
        myReader = csv.reader(f)
        sommet = 0
        for row in myReader:
            adjacents[sommet] = {}
            for i in range(0, len(row)):
                distance = int(row[i])
                if distance != 0:
                    adjacents[sommet][i] = int(row[i])
            sommet += 1
    return adjacents


##########################################################################################
##########################################################################################

# Exemple d'utilisation
dico_lotissements = {
    0: {1: 30, 2: 40, 3: 50, 4: 20, 5: 50, 6: 20},
    1: {0: 30, 2: 30, 4: 50},
    2: {0: 40, 1: 30, 3: 20, 4: 50},
    3: {0: 50, 2: 20, 4: 40},
    4: {0: 20, 1: 50, 2: 50, 3: 40, 5: 40, 6: 30},
    5: {0: 50, 4: 40},
    6: {0: 20, 4: 30},
}

MST_kruskal_fibre = kruskal_couverture_mini(dico_lotissements)
print(f"kruskal : {MST_kruskal_fibre}")

fich_cablage = "./grand_graphe.csv"
adjacents = csvToDic(fich_cablage)

# Appels pour mesurer le temps d'exécution de Kruskal

kruskal_time_lotissement = timeit.timeit(
    "kruskal_couverture_mini(dico_lotissements)", globals=globals(), number=1
)
kruskal_time_grandGraphe = timeit.timeit(
    "kruskal_couverture_mini(adjacents)", globals=globals(), number=1
)

print(
    f"Temps d'exécution de Kruskal sur graphe fibré : {kruskal_time_lotissement} secondes"
)
print(
    f"Temps d'exécution de Kruskal sur grand graphe : {kruskal_time_grandGraphe} secondes"
)
