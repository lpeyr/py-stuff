#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randint


def jeu_vide(n, val):
    """
    Créer une grille de taille n x n, chaque case contenant la valeur val
    Paramètres:
        - n (int): la taille d'un coté de la grille
        - val (int): la valeur à mettre dans chaque case
    Retour:
        - jeu: la grille
    """
    jeu = []
    for i in range(n):
        jeu.append([])
        for j in range(n):
            jeu[i].append(val)
    return jeu


def initialisation_grille_cachee(n, nb_bombes):
    """
    Créer une grille de jeu cachée avec un nombre de bombes
    donné placées aléatoirement
    Paramètres:
        - n (int): la taille d'un côté de la grille
        - nb_bombes (int): le nombre de bombes à placer
    Retour:
        - la grille de jeu cachée (grille)
    """
    jeu = jeu_vide(n, 0)
    bombes = 0
    while bombes < nb_bombes:
        x = randint(0, n - 1)
        y = randint(0, n - 1)
        if jeu[x][y] != -1:
            jeu[x][y] = -1
            bombes += 1

    jeu = calcul_bombes_voisines(jeu)
    return jeu


def initialisation_grille_affichee(n):
    """
    Créer une grille de jeu qui sera affichée au joueur
    donné placées aléatoirement
    Paramètres:
        - n (int): la taille d'un côté de la grille
    Retour:
        - la grille de jeu à afficher (grille)
    """
    return jeu_vide(n, -1)


def calcul_bombes_voisines(jeu):
    """
    Calculer le nombre de bombes adjacentes à chaque case du jeu
    Paramètres:
        - jeu (grille): la grille de jeu contenant les bombes
    Retour:
        - jeu (grille): la grille de jeu mise à jour où chaque case contient
                        le nombre de bombes dans son voisinage
    """
    for i in range(len(jeu)):
        for j in range(len(jeu)):
            if jeu[i][j] == -1:
                for k in range(-1, 2):
                    for l in range(-1, 2):
                        if k != 0 or l != 0:
                            if (
                                i + k >= 0
                                and i + k < len(jeu)
                                and j + l >= 0
                                and j + l < len(jeu)
                                and jeu[i + k][j + l] != -1
                            ):
                                jeu[i + k][j + l] += 1

    return jeu


def choix_coordonnees(jeu):
    """
    Demander au joueur la case qu'il veut dévoiler
    Retour:
        - x (int): le numéro de la ligne de la case
        - y (int): le numéro de la colonne de la case
    """
    x = -1
    y = -1
    while x < 0 or x >= len(jeu) or y < 0 or y >= len(jeu):
        print(f"les coordonnées doivent être comprises entre {0} et {len(jeu)-1}")
        x = int(input("Choix de l'indice de ligne ? "))
        y = int(input("Choix de l'indice de colonne ? "))
    return x, y


def mise_a_jour_jeu_visible(jeu, jeu_visible, x, y):
    """
    Met à jour le jeu visible en fonction de la case sélectionnée par le joueur
    Paramètres:
        - jeu (grille): le jeu
        - jeu_visible (grille): le jeu visible par le joueur
        - x (int): numéro de ligne de la case choisie par le joueur
        - y (int): numéro de colonne de la case choisie par le joueur
    Retour:
        jeu_visible (grille): le jeu visible par le joueur
    """
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
    return jeu_visible


def affichage_jeu(jeu):
    """
    Afficher la grille du jeu cachée contenant la position de toutes les bombes
    Paramètres:
        - jeu (grille): le jeu caché
    """
    for i in range(len(jeu)):
        ligne = ""
        for j in range(len(jeu)):
            if jeu[i][j] == -1:
                ligne += "* "
            else:
                ligne += str(jeu[i][j]) + " "
        print(ligne)
    print()


def affichage_jeu_visible(jeu):
    """
    Afficher la grille du jeu visible
    Paramètres:
        - jeu_visible (grille): le jeu visible par le joueur
    """
    for i in range(len(jeu)):
        ligne = ""
        for j in range(len(jeu)):
            if jeu[i][j] == -1:
                ligne += "_ "
            else:
                ligne += str(jeu[i][j]) + " "
        print(ligne)
    print()


def jeu_gagne(jeu_visible, nb_bombes):
    """
    Détermine si le jeu est gagné ou non
    Paramètres:
        - jeu_visible (grille): le jeu visible
        - nb_bombes (int): le nombre de bombes totales dans le jeu
    Retour:
        - True si le jeu est gagné, False sinon
    """
    taille_jeu = len(jeu_visible)
    compteur = taille_jeu**2
    for i in range(taille_jeu):
        for j in range(taille_jeu):
            if jeu_visible[i][j] == -1:
                compteur -= 1
    return compteur == taille_jeu**2 - nb_bombes


def jeu_perdu(jeu, x, y):
    """
    Détermine si le jeu est perdu ou non suite au choix d'une nouvelle case par le joueur
    Paramètres:
        - jeu (grille): le jeu caché
        - x (int): numéro de ligne de la case choisie par le joueur
        - y (int): numéro de colonne de la case choisie par le joueur
    Retour:
        - True si le jeu est perdu, False sinon
    """
    return jeu[x][y] == -1


# Programme principal
# A completer

perdu = False
jeu = initialisation_grille_cachee(4, 2)
jeu_vis = initialisation_grille_affichee(4)
affichage_jeu_visible(jeu_vis)

while not jeu_gagne(jeu_vis, 2) and not perdu:
    x, y = choix_coordonnees(jeu)
    if jeu_perdu(jeu, x, y):
        perdu = True
    else:
        mise_a_jour_jeu_visible(jeu, jeu_vis, x, y)

    affichage_jeu_visible(jeu_vis)

if perdu:
    print("Vous avez perdu !")
    affichage_jeu_visible(jeu_vis)
else:
    print("Vous avez gagné !")
