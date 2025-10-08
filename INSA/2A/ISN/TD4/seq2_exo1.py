#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 16:51:16 2023

@author: nadiaB
"""

import csv
import json
import pprint


# question 1.1
def nb_apparition(matiere, liste_dicos):
    """fonction qui compte le nombre d'apparition d'une matière dans
    la liste des dicos
    """
    res = 0
    for l in liste_dicos:
        for v in l.values():
            if v == matiere:
                res += 1
    return res


# question 1.2
def creer_dico_matiere(liste_dicos):
    """Fonction qui crée le dictionnaire ayant pour structure
     dict(matiere,list(note))
    Elle prend en entrée la liste des dictionnaires construite
    à partir du fichier Resultat_requete.csv
    """
    dico_mat = dict()
    for dico in liste_dicos:
        if dico["valeur"] != "" and float(dico["valeur"]) > 10:
            dico_mat[dico["cours"]] = (
                [float(dico["valeur"])]
                if dico_mat.get(dico["cours"], []) == []
                else dico_mat[dico["cours"]] + [float(dico["valeur"])]
            )

    return dico_mat


def moyenne(l):
    s = 0
    for v in l:
        s += v
    return s / len(l)


# Question 1.3 (version 1)
def affiche_stats_matiere_v1(liste_dico, matiere):
    """fonction qui affiche pour une matière donnée en paramètre, la liste des notes
    Elle utilise pour cela la liste des dicos
    """
    # A completer
    d = creer_dico_matiere(liste_dico)
    print(
        f"Matière : {matiere}\nNombre de notes : {len(d[matiere])}\nMoyenne : {moyenne(d[matiere])}"
    )


# Question 1.3 (version 2)
def affiche_stats_matiere_v2(dico_mat, matiere):
    """fonction qui affiche pour une matière donnée en paramètre, la liste des notes
    Elle utilise pour cela le dico des matières
    """
    print(dico_mat[matiere])



# Question 1.5
def affiche_notes_eleve(liste_dico, nom, prenom):
    """Fonction qui affiche les notes d'un eleve dont le nom et le prenom sont fournis
    Args:
        liste_dico, liste de dictionnaires 1 par eleve et par note
        nom (chaine) : nom de l'eleve'
        prenom (chaine), prenom de l'eleve'
    Return: None
    """
    for dico in liste_dico:
        if dico["Nom"] == nom and dico["Prenom"] == prenom and dico["valeur"] != "":
            print(dico["cours"], dico["valeur"])


#############################################################################
#  Code Fourni
############################################################################


def csv_to_liste_de_dicos_profond1(nom_fichier, eliminer_entete=True, delimiteur=","):
    """
    fonction qui renvoie une liste dont chaque élément est une liste qui correspond à une ligne du fichier csv passé en paramèter
        Entrees: nom_fichier (string)
                eliminer_entete (booléen) : indique s'il faut éliminer la première ligne du fichier (par défaut True)
                delimiteur (char) : le délimiteur de colonne (par défaut ',')
        Sortie: la liste des listes des données du csv
    """
    with open(nom_fichier, "r", encoding="utf-8") as f:
        csvReader = csv.reader(
            f, delimiter=delimiteur
        )  # interprête le fichier comme un csv avec délimiteur
        # le fichier f est maintenant fermé
        liste = []
        attributs = ["Nom", "Prenom", "Ville", "NumEtudiant", "cours", "valeur"]
        if eliminer_entete:
            csvReader.__next__()  # passe la première ligne du csv si ce sont les entêtes

        for row in csvReader:  # parcours toutes les lignes du csv
            dico = {}
            for i in range(len(attributs)):
                dico[attributs[i]] = row[i]
            # print(dico)
            liste.append(dico)  # les ajoute dans liste

    return liste


# programme principal

liste_de_dicos = csv_to_liste_de_dicos_profond1("data/Resultat_requete.csv")
# si vous travaillez sous Windows
# liste_de_liste= csv_to_liste_de_dicos_profond1('data\Resultat_requete.csv')


# print(liste_de_dico)
# Question 1.1
print()
print(f"Question1.1")
print(
    f'Il y a {nb_apparition("atomistique", liste_de_dicos)} dans la liste de dictionnaires'
)
print()
print()
# Q1.2
print(f"Question1.2")
dico_mat = creer_dico_matiere(liste_de_dicos)
print("creation dico matieres")
print(dico_mat)

# Q1.3 (version 1)
print(f"Question1.3(v1): résultats")
affiche_stats_matiere_v1(liste_de_dicos, "analyse 1")
print()

# Q1.3 (version 2)
print(f"Question1.3(v2): résultats")
affiche_stats_matiere_v2(dico_mat, "analyse 1")

print()


# Q1.5 (question bonus)
print()
print()
print(f"Question1.5: résultats pour Blaise Pascal")
affiche_notes_eleve(liste_de_dicos, "PASCAL", "Blaise")
print()
