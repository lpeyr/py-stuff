# -*- coding: utf-8 -*-
import csv
import time

"""
Created on Wed Nov  1 13:22:13 2023

@author: veroe
"""
### Q1.3 Algorithme de PRIM


def prim_couverture_mini(dico_adjacences):
    triplets_retenus = []
    r = ["0"]
    e = []
    for sommet in dico_adjacences:
        for art in dico_adjacences[sommet]:
            if (art[0], sommet, art[1]) not in e:
                e.append((sommet, art[0], art[1]))

    while len(r) < len(list(dico_adjacences.keys())):
        i, arrete = get_arrete(r, e)

        if arrete[0] not in r:
            r.append(arrete[0])
        else:
            r.append(arrete[1])

        triplets_retenus.append(arrete)

        e.pop(i)
    return triplets_retenus


def get_arrete(r, e):
    poids_min = float("inf")
    i_arrete = 0
    for i in range(len(e)):
        arrete = e[i]
        if extremite_in_r(r, arrete) and arrete[2] < poids_min:
            i_arrete = i
            poids_min = arrete[2]
    return (i_arrete, e[i_arrete])


def extremite_in_r(r, arrete):
    return (arrete[0] in r and arrete[1] not in r) or (
        arrete[1] in r and arrete[0] not in r
    )


####Q2.4 Algorithme de PRIM avec proposition d'amélioration avec utilisation d'un dictionnaire pour les sommets_pris_en_compte


def prim_couverture_mini2(dico_adjacences):
    triplets_retenus = []
    # code à reprendre de la question 1.3 et à compléter ici...
    return triplets_retenus


#######Q 2.2 (sur la partie des grands graphes / graphes de taille et de densité variable)


def csvToDic(fic):
    adjacents = {}  # Dictionnaire contenant comme clefs les sommets et
    # comme valeurs la liste des sommets pouvant etre rejoints
    # depuis le sommet designe par la clef.
    # Seuls les arcs non nuls sont retenus ici.
    with open(fic) as f:
        myReader = csv.reader(f)
        sommet = 0
        for row in myReader:
            for i in range(len(row)):
                if row[i] != "0":
                    adjacents[sommet] = adjacents.get(sommet, []) + [(i, int(row[i]))]
            sommet += 1

    return adjacents


##########################################################################################
##########################################################################################

# Q1.1 Exemple d'utilisation

# compléter le dictionnaire des lotissements

dico_lotissements = {
    "0": [("1", 30), ("2", 40), ("3", 50), ("4", 20), ("5", 50), ("6", 20)],
    "1": [("0", 30), ("2", 30), ("4", 50)],
    "2": [("0", 40), ("1", 30), ("3", 20), ("4", 50)],
    "3": [("0", 50), ("2", 20), ("4", 40)],
    "4": [("0", 20), ("1", 50), ("2", 50), ("3", 40), ("5", 40), ("6", 30)],
    "5": [("0", 50), ("4", 40)],
    "6": [("0", 20), ("4", 30)],
}

start = time.time()

MST_prim_fibre = prim_couverture_mini(dico_lotissements)

end = time.time()

print(f"prim : {MST_prim_fibre}")
prim_time_lotissement = end - start

fich_cablage = "./grand_graphe.csv"
adjacents = csvToDic(fich_cablage)


#### Appels pour mesurer le temps d'exécution de Prim

## Q.2.1 Calcul du temps pour la CMG des lotissement câblés
# ....integrer la mesure de temps
# prim_couverture_mini(dico_lotissements)
# ....

print(f"Temps d'exécution de Prim sur graphe fibré : {prim_time_lotissement} secondes")

## Q.2.3 Calcul du temps pour un grand graphe
# ...integrer la mesure de temps
start = time.time()
prim_couverture_mini(adjacents)
end = time.time()
print(f"Temps d'exécution de Prim sur graphe fibré : {end-start} secondes")
# ...

# print(f"Temps d'exécution de Prim sur grand graphe : {prim_time_grandGraphe} secondes")
