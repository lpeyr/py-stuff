#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 11:11:17 2025

@author: frindel
"""
import math

class Ville:
    """
    La classe Ville représente une ville avec ses coordonnées géographiques et son altitude.
    Elle fournit des méthodes pour effectuer des calculs associés à ces données.
    """

    def __init__(self, nom, lat, long, haut):
        """
        Initialise un objet Ville.

        Args:
            nom (str): Nom de la ville.
            lat (float): Latitude de la ville.
            long (float): Longitude de la ville.
            haut (int): Altitude de la ville.
        """
        self.nom = nom
        self.lat = lat
        self.long = long
        self.haut = haut

    def distance_km(self, autre_ville):
        """
        Calcule la distance en kilomètres entre cette ville et une autre.

        Args:
            autre_ville (Ville): L'autre ville à comparer.

        Returns:
            float: Distance en kilomètres entre les deux villes.
        """
        R = 6371.0  # Rayon de la Terre en kilomètres
        lat_a_rad = math.radians(self.lat)
        lng_a_rad = math.radians(self.long)
        lat_b_rad = math.radians(autre_ville.lat)
        lng_b_rad = math.radians(autre_ville.long)
        dlng = lng_b_rad - lng_a_rad
        dlat = lat_b_rad - lat_a_rad
        a = math.sin(dlat / 2)**2 + math.cos(lat_a_rad) * math.cos(lat_b_rad) * math.sin(dlng / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = R * c
        return distance

    def __str__(self):
        """
        Retourne une représentation sous forme de chaîne de la ville.
        """
        return f"Ville({self.nom}, {self.lat}, {self.long}, {self.haut})"