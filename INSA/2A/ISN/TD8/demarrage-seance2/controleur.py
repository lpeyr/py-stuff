#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 14:12:58 2025

@author: frindel
"""

from Graphe import Graphe
from Ville import Ville
from ConvertisseurDeCoordonnees import ConvertisseurDeCoordonnees
from vue_secondaire import VueSecondaire
import tkinter as tk

import csv

class Controleur:
    """
    Contrôleur assurant l’interface entre le graphe de villes et la vue graphique.
    """
    
    def __init__(self, l_canvas, h_canvas, offset_earth, offset_screen):
        """
        Initialise le contrôleur et construit le graphe géographique.
    
        Les paramètres sont utilisés pour configurer le convertisseur de
        coordonnées et le canvas d’affichage.
    
        Args :
        l_canvas (int) : Largeur du canvas.
        h_canvas (int) : Hauteur du canvas.
        offset_earth (float) : Décalage appliqué aux coordonnées géographiques.
        offset_screen (float) : Décalage appliqué aux coordonnées écran.
        """
        # Crée une instance de Graphe avec les informations de canvas
        self.l_canvas = l_canvas
        self.h_canvas = h_canvas
        convert = ConvertisseurDeCoordonnees(l_canvas, h_canvas, offset_earth, offset_screen)
        self.graphe = Graphe(convert)
        self.fichier = 'extrait_villes.csv'
        self.remplir_graphe()
        self.vue = None #vue principale
        self.fen_graph = None #vue secondaire avec la partie graphique
        
    def lier_vue(self, vue):
        """
        Associe une vue au contrôleur.
    
        Args : 
        vue (object) : Instance de la vue principale.
        """
        self.vue = vue

    def remplir_graphe(self):
        """
        Initialise l'objet Graphe avec les données du fichier CSV.
        """
        with open(self.fichier, newline="") as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            for ligne in reader:
                ident, nom, lat, long, haut = ligne
                ville= Ville(nom, float(lat), float(long), int(haut))
                self.graphe.ajouter_ville(ville)
        self.graphe.creation_aretes()
        
        
    def obtenir_noms_noeuds(self):
        """
        Retourne les noms de toutes les villes dans le graphe.
        """
        return list(self.graphe.carte.keys())

    def obtenir_coordonnees(self, nom_noeud):
        """
        Retourne les coordonnées cartésiennes d'un nœud dans le graphe.
        """
        return self.graphe.xy_repere_cartesien(nom_noeud)

    def obtenir_prim(self, noeud):
        """
        Récupère la liste des arcs dans l'algorithme de Prim pour un nœud donné.
        """
        return self.graphe.prim(noeud)

    def execute_choix(self, event):
        """
        Traite l’action sélectionnée dans l’interface utilisateur.
        """
        choix = self.vue.choix.get()
        if choix == "Nombre":
            nb_sommets = self.graphe.nombre_villes()
            texte = f"* Le nombre de villes est : {nb_sommets}\n"
            self.vue.text_area.insert(tk.INSERT, texte)
        elif choix == "Distance":
            moyenne = self.graphe.distance_moy()
            texte = f"* La moyenne des distances vaut : {moyenne:.2f} km\n"
            self.vue.text_area.insert(tk.INSERT, texte)
        elif choix == "Effacer":
            self.vue.text_area.delete("1.0", tk.END)

    def dessine_graphe(self, event):
        """
        Initialisation de la fenêtre secondaire.
        """
        self.fen_graph = VueSecondaire(self, self.l_canvas, self.h_canvas)
