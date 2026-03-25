#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 14:09:55 2025

@author: frindel
"""

import tkinter as tk
import random

class VueSecondaire(tk.Toplevel):
    """
    Fenêtre secondaire affichant les villes et les arêtes de l’arbre couvrant minimum.
    """

    
    def __init__(self, controleur, l_canvas, h_canvas):
        """
        Initialise la fenêtre secondaire et crée le canevas pour l’affichage graphique.
    
        Args :
        controleur (Controleur) : Contrôleur permettant d’accéder aux données du graphe et aux coordonnées.
        l_canvas (int) : Largeur du canevas en pixels.
        h_canvas (int) : Hauteur du canevas en pixels.
        """
        super().__init__()
        self.title("Fenêtre secondaire")
        self.resizable(height = False, width = False)
        
        # Référence au contrôleur
        self.controleur=controleur
        
        self.dico_sommets = {} #lien avec noms du sommets et cercles dessinés
        self.couleur = ["black", "red", "green", "blue", "yellow", "magenta","cyan", "white", "purple"]
        self.canvas = tk.Canvas(self, background="lightblue", width=l_canvas, height=h_canvas)
        self.canvas.grid()
        
        self.dessine_villes()

    def dessine_villes(self):
        """
        Dessine les villes sur le canevas.
        """
        rayon = 10
        noms_noeuds = self.controleur.obtenir_noms_noeuds()  # Récupère les noms des nœuds via le contrôleur
        for nom in noms_noeuds:
            x,y = self.controleur.obtenir_coordonnees(nom)
            id_text = self.canvas.create_text(x, y-2*rayon)
            cercle = self.canvas.create_oval((x-rayon,y-rayon), (x+rayon,y+rayon), fill=random.choice(self.couleur))
            self.canvas.itemconfigure(id_text, text=nom)
            self.canvas.tag_bind(cercle, "<Button-1>", self.dessine_aretes)
            self.dico_sommets[cercle] = nom

    def dessine_aretes(self, event):
        """
        Déclenche le dessin des arêtes de l’arbre couvrant minimum pour une ville.
        
        Args :
        event (tkinter.Event) : Objet événement Tkinter représentant l’action de l’utilisateur
        (ici clic sur ovale représentant une ville).
        """ 
        item_clicked = self.canvas.find_withtag("current")[0]
        nom = self.dico_sommets[item_clicked]
        arcs = self.controleur.obtenir_prim(nom)
        for arc in arcs:
            self.canvas.create_line(self.controleur.obtenir_coordonnees(arc[0]),self.controleur.obtenir_coordonnees(arc[1]), fill="blue")

        
        
    def anime_aretes_prim(self, prim_liste, index=0):     
        """
        Anime la construction de l’arbre couvrant minimum en dessinant les arêtes une par une.
        
        Args :
        event (tkinter.Event) : Objet événement Tkinter représentant l’action de l’utilisateur
        (ici le after).
        """
