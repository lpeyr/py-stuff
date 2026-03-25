#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 14:05:36 2025

@author: frindel
"""

import tkinter as tk
from tkinter import scrolledtext
from vue_secondaire import *

class VuePrincipale(tk.Tk):
    """
    Fenêtre principale de l’application Tkinter affichant des statistiques sur les villes.
    """    
    def __init__(self, controleur):
        """
        Initialise la fenêtre principale et crée les widgets.
        
        Args :
        controleur (Controleur) : Contrôleur chargé de gérer les actions déclenchées par l’utilisateur.
        """
        super().__init__()
        self.title("Fenêtre principale")
        self.resizable(height=False, width=False)

        # Référence au contrôleur
        self.controleur = controleur
        controleur.lier_vue(self)
        
        # Widgets
        self.creer_widgets()

    def creer_widgets(self):
        """
        Crée et positionne les widgets dans la fenêtre.
        """
        # Zone de texte
        self.text_area = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=50, height=20, font=("Times New Roman", 14))
        self.text_area.grid(row=0, column=0, columnspan=2)
        self.text_area.insert(tk.INSERT, "Quelques statistiques sur les villes :" + '\n')
        self.text_area.insert(tk.INSERT, "-------------------------------------------" + '\n')

        # RadioButtons
        self.choix = tk.StringVar()
        self.choix.set("Nombre")

        tk.Label(self, text="\nChoix de descripteurs :", font='Helvetica 10 bold').grid(row=1, column=0)
        tk.Radiobutton(self, text="Nombre de villes", variable=self.choix, value="Nombre").grid(row=1, column=1, sticky='w')
        tk.Radiobutton(self, text="Distance moyenne (km)", variable=self.choix, value="Distance").grid(row=2, column=1, sticky='w')
        tk.Radiobutton(self, text="Effacer Scrolltext", variable=self.choix, value="Effacer").grid(row=3, column=1, sticky='w')

        tk.Label(text="Fenêtre graphique").grid(row=4, columnspan=2)
        tk.Button(text="Graphe des villes").grid(row=5, columnspan=2)

        # Bouton de choix
        bouton_choix = tk.Button(self, text="Choix")
        bouton_choix.grid(row=3, column=0)
        bouton_choix.bind("<Button-1>", self.controleur.execute_choix)
