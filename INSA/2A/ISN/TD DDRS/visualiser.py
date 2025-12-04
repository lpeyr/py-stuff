#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 25 15:54:00 2025

@author: nbennani1
"""

import json
import map_villeurbanne

def lire_graphe(nom_fichier):
    '''Fonction qui lit le fichier json dont le nom est fourni en paramètre et retourne un dictionnaire 
    representant le graphe'''
    with open(nom_fichier, "r", encoding="utf-8") as f:
        graphe_noeuds = json.load(f)
    return graphe_noeuds


dico_graphe = lire_graphe("G_tests/G_rayon0_2.json")
map_villeurbanne.plot_graphe(dico_graphe)