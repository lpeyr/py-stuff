#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv

def load_file(nom_fichier) :
    """Fonction qui lit un fichier CSV dont le nom est reçu en paramètre et qui renvoie en résultat un matrice contenant les données lues (chaque ligne du CSV est une ligne de la matrice).
    Params : 
      * nom_fichier (str) : nom du fichier à charger. Il peut contenir un chemin. Ex : data/fichier.csv
    Result :
      * Une liste 2D de str. Toutes les valeurs sont des str, même celles qui ont l'apparence d'une valeur numérique.
    """
    fichier = open(nom_fichier,'r')
    reader = csv.reader(fichier, delimiter=",")
    next(reader) # Ignore la première ligne (les titres de colonnes)

    trajets = []
    for ligne in reader:
        trajets.append(ligne)

    fichier.close()
    return trajets


def affiche_matrice(m) :
    """Affiche proprement la matrice m, notamment en intégrant les numéro de ligne et de colonne dans l'affichage
    Params : 
      * une matrice d'entiers à afficher
    Return : 
      * None
    """
    print()
    print("            idx dest ")
    print("idx src \\ ",end="")

    for j in range(len(m[0])) : 
        print(f" {j:3d} |",end="")
    print("| Somme")
    print("-"*9+("+-"+("-"*3)+"-")*len(m[0])+"++------")

    for i in range(len(m)) :
        print(f"{i:6d}   |",end="")
        s = 0
        for j in range(len(m[i])) : 
            print(f" {m[i][j]:3d} |",end="")
            s += m[i][j]
        print(f"|{s:6d}")
    print()


def affiche_index(l_index) :
    """Affiche proprement la liste index, notamment en intégrant l'indice de chaque case dans l'affichage
    Params : 
      * une liste à afficher
    Return : 
      * None
    """
    print("index | identifiant")
    print("------+------------")
    for i in range(len(l_index)) : 
        print(f"{i:5d} | {l_index[i]:11s}")

def make_index(l_trajets) : 
    """Crée une liste d'index à partir de la liste de trajets l_trajets. Chaque case contient un identifiant de station. 
       Le numéro d'index d'une stations est la position de son identifiant dans cette liste.
    Params : 
      * l_trajets est une liste 2D ou chaque ligne est un trajet d'une station à une autre, identifiées par des identifiants
    Return : 
      * Une liste d'identifiants de stations, contenant l'ensemble des stations apparaissant en début ou en arrivée de trajet, sans doublon.
    """
    l = []
    for trajet in l_trajets:
        if trajet[3] not in l:
            l.append(trajet[3])
        if trajet[4] not in l:
            l.append(trajet[4])
    return l


def indexof(l_index, id) :
    """Recherche la valeur id dans la liste index et renvoie sa position. Renvoie None si elle n'est pas présente.
       index est une liste ne contenant pas de doublons.
    Params : 
      * index (list) : une liste de valeurs
      * id (?) : un élément cherché dans index
    Return : 
      * int : la position de id dans index (ou -1 si non présent).
    """
    index = -1
    i = 0
    while index == -1 and i < len(l_index) - 1:
        if l_index[i] == id:
            index = i
        i += 1

    return index


def make_matrice_trajets(l_index, l_trajets) :
    """Crée une liste 2D qui synthétise le nombre de trajets entre tout couple de stations (i,j), où i et j sont des index de stations, calculé à partir des identifiants via index.
    Params :
      * l_trajets (list*list*str) : est la liste des trajets à synthétiser 
      * l_index (list*str) : une liste qui associe chaque index à un indentifiant de station
    Return :
      Une liste 2D d'entiers, telle que chaque case (i,j) soit le nombre de trajets de l_trajet allant de la station d'index i à la station d'index j.
    """
    matrice = []
    # Pour chaque station
    for station in l_index:
        trajets_vers_station = {}      # Création d'un dictionnaire pour stocker le nombre de trajet vers la station [key]
        for l in l_index:
            trajets_vers_station[l] = 0

        for trajet in l_trajets:
            if trajet[4] == station:
                trajets_vers_station[trajet[3]] += 1
        
        ligne=[]

        for k in trajets_vers_station:
            ligne.append(trajets_vers_station[k])
        
        matrice.append(ligne)

    return matrice



def trajet_max(matrice) :# O(n²)
    """Renvoie les coordonnées (i,j) de la case de matrice contenant la plus grande valeur.
    Params : matrice (list 2D d'int) : une liste 2D d'entiers
    Return : couple d'entiers : les coordonnées du max de matrice.
    """
    max_i, max_j = 0, 0
    max = matrice[max_i][max_j]
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            if matrice[i][j] > max:
                max_i, max_j = i, j
            
    return max_i, max_j


def insertion_triee(l, nb_et_index) :
    """ nb_et_index est un couple (nb, id) à insérer de manière triée dans la liste l triée de couples : 
        un couple (nb, id) a une valeur nb et un identifiant id. Le tri est réalisé par rapport 
        aux valeurs.
        Pas de résultats, mais l est plus grande d'un élément. 
    """
    pass


def max_5_stations_vers(l_index, matrice, id) : # O(n²)
    """Cherche les 5 stations les plus utilisées pour aller à la station d'identifiant id.
    Params :
      * l_index (list*str) : liste d'association index<->identifiant des stations
      * matrice (list*list*int) : liste 2D du nombre de trajets entre les différentes stations
      * id (str) : l'identifiant de la station d'arrivée (doit être présentant dans index)
    Return :
      Une liste d'index de stations de taille 5, ou moins.
    """
    liste_station = []

    for i in range(len(matrice)):
        liste_station.append((i, (matrice[i][indexof(l_index, id)])))
    tri_selection(liste_station)

    l=[]
    for v in liste_station[-5:]:
        l.append(v[0])
    return l

def tri_selection(l): # O(n²)
    '''
    Entrée:
      l : list*tuple<int,int>
    Sortie : list*tuple<int,int
    '''
    for p in range(len(l)):
        m=l[p][1]
        for k in range(p, len(l)):
            if l[k][1] < m:
                m = l[k][1]
                l[k], l[p] = l[p], l[k]          
        

# Programme principal
l_trajets = load_file("usage_velov_extrait.csv")
print(f"{len(l_trajets)} trajets chargés.")
# jeu de test index of
#print(indexof(["123", "1", "2", "3"], "1")) # 1
#print(indexof(["123", "1", "2", "3"], "5")) # -1
#print(indexof(["123", "1", "2", "1"], "1")) # 1
index = make_index(l_trajets)
affiche_index(make_index(l_trajets))
m = make_matrice_trajets(index, l_trajets)
affiche_matrice(m)

print(trajet_max(m))
print(max_5_stations_vers(index, m, "7001"))