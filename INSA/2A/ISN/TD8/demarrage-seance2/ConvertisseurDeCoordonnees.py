#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 17:15:31 2025

@author: frindel
"""

class ConvertisseurDeCoordonnees:

    def __init__(self, l_canvas, h_canvas, offset_earth, offset_screen):
        """
        Initialise un convertisseur de coordonnées pour transformer les coordonnées géographiques en
        coordonnées cartésiennes adaptées au Canvas.

        Args:
            l_canvas (int): Largeur du Canvas (en pixels).
            h_canvas (int): Hauteur du Canvas (en pixels).
            offset_earth (float): Facteur de mise à l'échelle pour la Terre (en kilomètres, ou autre unité).
            offset_screen (float): Facteur de mise à l'échelle pour le Canvas (en pixels, ou autre unité).
        """
        self.l_canvas = l_canvas
        self.h_canvas = h_canvas
        self.offset_earth = offset_earth
        self.offset_screen = offset_screen

    def geo_to_canvas(self, lat, lon):
        """
        Convertit les coordonnées géographiques (latitude, longitude) en coordonnées cartésiennes
        pour l'affichage sur le Canvas.

        Args:
            lat (float): Latitude de la ville.
            lon (float): Longitude de la ville.

        Returns:
            tuple: Les coordonnées cartésiennes (x, y) sur le Canvas.
        """
        # Conversion de la latitude et de la longitude en coordonnées cartésiennes
        # Nous supposons que l'origine (0,0) est en bas à gauche du Canvas

        # Calcul des coordonnées cartésiennes (en pixels) pour l'affichage
        x = (lon + 180) * (self.l_canvas / 360)  # Longitude entre -180 et 180 degrés
        y = (90 - lat) * (self.h_canvas / 180)  # Latitude entre -90 et 90 degrés

        # Appliquer un facteur de mise à l'échelle (offset_earth et offset_screen) si nécessaire
        x = x * self.offset_screen / self.offset_earth
        y = y * self.offset_screen / self.offset_earth

        return x, y

    def ajuste_to_repere(self, x_ville, y_ville, x_min, x_max, y_min, y_max):
        """
        Ajuste les coordonnées cartésiennes d'une ville en fonction des offsets et des limites du repère.

        Args :
            x_ville (float): Coordonnée x brute de la ville.
            y_ville (float): Coordonnée y brute de la ville.
            x_min (float): Valeur minimale de x dans le graphe.
            x_max (float): Valeur maximale de x dans le graphe.
            y_min (float): Valeur minimale de y dans le graphe.
            y_max (float): Valeur maximale de y dans le graphe.

        Returns:
            tuple: Coordonnées ajustées (x, y) dans le repère cartésien.
        """
        x = (self.l_canvas - self.offset_earth) / (x_max - x_min) * (x_ville - x_min) + self.offset_screen
        y = (self.h_canvas - self.offset_earth) / (y_max - y_min) * (y_ville - y_min) + self.offset_screen
        
        return x, y


