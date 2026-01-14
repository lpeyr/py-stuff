#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 16:24:22 2024

@author: nadiaB
"""

import json


# Question 1.3
def nbr_e_ch_du_groupe(dico_symboles, g):
    """Fonction qui compte combien il y a de symboles chimiques différents
    dans un groupe donné (g)
    """
    nb_s = 0
    for k in dico_symboles:
        if dico_symboles[k]["group"] == g:
            nb_s += 1
    return nb_s


# Question 2.1
def calculer_et_mem_masse(molecule, dico_mendeleiv):
    """fonction qui calcule la masse atomique de la molécule 'molecule'
    et qui complete le dictionnaire de cette molécule par une nouvelle
    clé ayant pour valeur cette masse
    """
    masse = 0
    for element, nb in molecule["composition"].items():
        masse += dico_mendeleiv[element]["atomic_mass"] * nb
    molecule["masse"] = masse
    return molecule


# question2.2
def afficher_molecule(mol):
    """ """
    nb_atomes = 0
    formule = ""
    for k in mol["composition"]:
        nb_atomes += mol["composition"][k]
        formule += k + str(mol["composition"][k]) if mol["composition"][k] > 1 else k

    print(f"{mol['nom']}({formule}) -> {nb_atomes} atomes, {mol.get('masse', '')} uma")


# Question 2.3
def affiche_liste_mol_contenant(list_mol, at):
    """
    affichage des molécules où l'atome 'at' fait partie de la composition
    input : list_mol: liste de molécules ou on effectue la recherche
    complexité:
    for : O(lm)

    complexité globale : O(lm)
    avec lm: la liste des molécules
    """
    for mol in list_mol:
        if mol["composition"].get(at, None):
            afficher_molecule(mol)


# Question 3.1
def creer_dic_par_at(list_mol):
    """Crée un index inversé sous forme de dict(str,list[int])
    indiquant pour chaque symbole chimique, les indexs dans la liste des molécules qui en contient
    Complexité:

    """
    index = {}
    for i in range(len(list_mol)):
        for atom in list_mol[i]["composition"]:
            index[atom] = index.get(atom, []) + [i]
    return index


# question 3.4
def affiche_liste_mol_contenant_2(liste_mol, index, at):
    """
    Affichage des molécules possedant l'atome 'at en utilisant  l'index
    La complexité est egale à O(max(len(liste)). Theoriquement égale à celle de
    la base des atomes mais dans la pratiquement << à cette borne théorique

    """
    for indices in index[at]:
        afficher_molecule(liste_mol[indices])


def lire_fichier_json(nom_fichier):
    # code permettant de lire (r)  le fichier de nom externe 'nom_fichier'
    # la variable 'contenu' contient un dictionnaire reproduisant la structure du fichier json
    with open(nom_fichier, "r", encoding="utf_8") as mon_fichier:
        contenu = json.load(mon_fichier)
    return contenu


######################
# programme principal
######################

dico_mendeleiv = lire_fichier_json("data/mendeleiv_by_symbol.json")
print(dico_mendeleiv)

liste_mol = [
    {"nom": "propanol", "composition": {"C": 3, "H": 8, "O": 1}},
    {"nom": "permanganate de potassium", "composition": {"K": 1, "Mn": 1, "O": 4}},
    {"nom": "Oxygène", "composition": {"O": 2}},
    {"nom": "Sulfate de potassium", "composition": {"K": 2, "S": 1, "O": 4}},
]

print(f"le groupe 18 est composé de {nbr_e_ch_du_groupe(dico_mendeleiv, 18)} éléments")

# calculez le nombre d'atomes pour chaque molécule
for mol in liste_mol:
    calculer_et_mem_masse(mol, dico_mendeleiv)
    afficher_molecule(mol)

dic_at = creer_dic_par_at(liste_mol)
print("Test affichage liste mol :")
affiche_liste_mol_contenant(liste_mol, "K")
print(dic_at)
affiche_liste_mol_contenant_2(liste_mol, dic_at, "K")
