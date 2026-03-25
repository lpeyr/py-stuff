#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 14:46:32 2025

@author: frindel
"""

from controleur import Controleur
from vue_principale import VuePrincipale

# Informations sur le canvas
l_canvas = 600
h_canvas = 600
offset_earth = 50
offset_screen = 30

if __name__ == "__main__":
  
    # Initialisation du Contrôleur avec les informations de canvas
    controleur = Controleur(l_canvas, h_canvas, offset_earth, offset_screen)
    # Initialisation de la Vue
    vue = VuePrincipale(controleur)
    vue.mainloop()
