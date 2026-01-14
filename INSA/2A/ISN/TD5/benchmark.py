#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import json
from pprint import pprint
import matplotlib.pyplot as plt

print("# Sélection des implémentations testées en fonction des fichiers présents")
print()
les_implementations = []
try:
    import GaleShapleyV1

    impl = {"nom": "GaleShapleyV1.py", "module": GaleShapleyV1}
    les_implementations.append(
        impl
    )  # À commenter pour sortir cette implémentation du benchmark
    print("GaleShapleyV1.py : ok")
except ModuleNotFoundError:
    print(
        "GaleShapleyV1.py : non sélectionné (Pas de fichier GaleShapleyV1.py dans le dossier)"
    )

try:
    import GaleShapleyV2

    impl = {"nom": "GaleShapleyV2.py", "module": GaleShapleyV2}
    les_implementations.append(
        impl
    )  # À commenter pour sortir cette implémentation du benchmark
    print("GaleShapleyV2.py : ok")
except ModuleNotFoundError:
    print(
        "GaleShapleyV2.py : non sélectionné (Pas de fichier GaleShapleyV2.py dans le dossier)"
    )

try:
    import GaleShapleyV3

    impl = {"nom": "GaleShapleyV3.py", "module": GaleShapleyV3}
    les_implementations.append(
        impl
    )  # À commenter pour sortir cette implémentation du benchmark
    print("GaleShapleyV3.py : ok")
except ModuleNotFoundError:
    print(
        "GaleShapleyV3.py : non sélectionné (Pas de fichier GaleShapleyV3.py dans le dossier)"
    )

try:
    import GaleShapleyV4

    impl = {"nom": "GaleShapleyV4.py", "module": GaleShapleyV4}
    les_implementations.append(
        impl
    )  # À commenter pour sortir cette implémentation du benchmark
    print("GaleShapleyV4.py : ok")
except ModuleNotFoundError:
    print(
        "GaleShapleyV4.py : non sélectionné (Pas de fichier GaleShapleyV4.py dans le dossier)"
    )

try:
    import GaleShapleyV5

    impl = {"nom": "GaleShapleyV5.py", "module": GaleShapleyV5}
    les_implementations.append(
        impl
    )  # À commenter pour sortir cette implémentation du benchmark
    print("GaleShapleyV5.py : ok")
except ModuleNotFoundError:
    print(
        "GaleShapleyV5.py : non sélectionné (Pas de fichier GaleShapleyV5.py dans le dossier)"
    )

try:
    import GaleShapleyV6

    impl = {"nom": "GaleShapleyV6.py", "module": GaleShapleyV6}
    les_implementations.append(
        impl
    )  # À commenter pour sortir cette implémentation du benchmark
    print("GaleShapleyV6.py : ok")
except ModuleNotFoundError:
    print(
        "GaleShapleyV6.py : non sélectionné (Pas de fichier GaleShapleyV6.py dans le dossier)"
    )

print()


#######################################################
#################  Fonctions de test  #################
#######################################################
def appel_gale_shapley(fichier, implem):
    """Prend en paramètre le chemin d'accès à un fichier contenant un jeu de données. Construit un appariement du jeu de données en utilisant l'algorithme de Gale-Shapley et retourne 2 résultats :
    - la liste des paires construites (dictionnaire : etudiant -> stage)
    - la durée de calcul (int), en millisecondes (en excluant les temps de chargement et d'initialisation des données)
    """
    # Chargement d'un jeu de données
    with open(fichier, "r", encoding="utf-8") as f:
        data = json.load(f)

    etudiants = data[0]  # Récupération de la liste des étudiants
    stages = data[1]  # Récupération de la liste des stages
    prefs_etudiants = data[2]  # Récupération des préférences des étudiants
    prefs_stages = data[3]  # Récupération des préférences des stages

    # Appel chronométré de gale_shapley
    start = int(round(time.time() * 1000))

    paires = implem["module"].gale_shapley(
        etudiants, stages, prefs_etudiants, prefs_stages
    )

    stop = int(round(time.time() * 1000))
    duree = stop - start

    return paires, duree


# Programme qui exécute GaleShapley sur plusieurs cas de test successifs de taille croissante.
# Son objectif est de faire de la mesure de durée d'exécution pour observer l'évolution de la durée
# de calcul en fonction de l'évolution de la taille du jeu de données.

# Le paramètre optionnel partiel (activé par défaut) permet de faire une exécution sur un petit
# sous-ensemble de jeux de données (6 jeux de tailles 10 à 500 personnes) pour éviter les
# exécutions longues par inadvertance. Si partiel vaut False, alors les jeux de données de taille 600
# à 2000 personnes/stages sont également utilisés pour faire des mesures de durée.

# N'affiche pas l'affectation, mais uniquement la durée de calcul (en mode texte et dans un graphique).
# Ne renvoie pas de résultat.

# Liste des tailles de fichiers de test disponoible
tailles_possibles = [10, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000]

# Constitution de la liste de fichiers à intégrer dans le benchmark
taille_min = 10
taille_max = 500
les_tailles = []

for t in tailles_possibles:
    if taille_min <= t and t <= taille_max:
        les_tailles.append(t)


# Mesure de la durée d'exécution pour chaque cas de test et affichage du tableau des durées
print()
print()
print("# Lancement des tests par taille croissante")
print()
d_durees_par_algo = {}
for implem in les_implementations:
    print(f"## Test de l'implémentation {implem['nom']} :")
    print("   Durée par taille : ", end="")
    durees = []
    for taille in les_tailles:
        print(f"{taille} : ", end="")
        _, duree = appel_gale_shapley(f"data/jeu_de_test_taille_{taille}.json", implem)
        print(f"{duree}ms    ", end="")
        durees.append(duree)
    print()
    d_durees_par_algo[implem["nom"]] = durees
    print()

print()


# Génération bilan textuel pour import tableur
print("# Résultats copiables dans un tableur :")
print()
print("Taille du test", end="")
for nom in d_durees_par_algo:
    print(f" \t {nom}(ms)", end="")
print()
for i in range(len(les_tailles)):
    print(f"{les_tailles[i]:15d}", end="")
    for _, duree in d_durees_par_algo.items():
        print(f"\t {duree[i]:20d}", end="")
    print()


# Tracé de la courbe des durées
# plt.plot(les_tailles, durees, "b:x")
for nom, durees in d_durees_par_algo.items():
    plt.plot(les_tailles, durees, ":x", label=f"{nom}")

plt.xlabel("Taille données")
plt.ylabel("Durée (ms)")
plt.legend()
plt.show()
# plt.savefig(f"Evolution_duree_selon_taille_donnees-{taille}.jpg")
