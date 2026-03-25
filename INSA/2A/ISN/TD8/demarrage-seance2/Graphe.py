#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 13:11:32 2025

@author: frindel
"""

from Ville import Ville
from ConvertisseurDeCoordonnees import ConvertisseurDeCoordonnees
import math

class Graphe:
    """
    La classe Graphe permet de représenter un graphe géographique et d'effectuer
    diverses opérations telles que l'ajout de nœuds, le calcul de distances,
    et la recherche d'arbre couvrant de poids minimum (algorithme de Prim).
    """
    def __init__(self, convertisseur):
        """
        Initialise un graphe géographique vide.
    
        Args:
            convertisseur (ConvertisseurDeCoordonnees)
        """      
        self.convertisseur = convertisseur # Convertisseur de coordonnees
        self.carte = {}  # Dictionnaire de villes

    def ajouter_ville(self, ville):
        """
        Ajoute une ville au graphe.

        Args:
            ville (Ville): Objet de type Ville à ajouter.
        """
        if ville.nom not in self.carte:
            self.carte[ville.nom] = {'ville': ville, 'voisins': {}}

    def creation_aretes(self):
        """
        Crée les arêtes du graphe sous la forme d'une liste d'adjacence.
        Chaque arête est représentée par une distance entre deux villes.
        """
        for nom_a, data_a in self.carte.items():
            ville_a = data_a["ville"]
            for nom_b, data_b in self.carte.items():
                if nom_a != nom_b:
                    ville_b = data_b["ville"]
                    data_a["voisins"][nom_b] = ville_a.distance_km(ville_b)
                    
    def afficher(self):
        """
        Affiche les informations sur le graphe, y compris les villes et les distances.
        """
        for ville, infos in self.carte.items():
            print(f"Ville: {ville}, Latitude: {infos['ville'].lat}, Longitude: {infos['ville'].long}, Altitude: {infos['ville'].haut}")
            if infos['voisins']:
                print("  Voisins:")
                for voisin, distance in infos['voisins'].items():
                    print(f"    - {voisin}: {distance:.2f} km")
            else:
                print("  Pas de voisins pour cette ville.")

    def nombre_villes(self):
        """
        Renvoie le nombre de villes dans le graphe.

        Returns:
            int: Nombre de villes.
        """
        return len(self.carte)
    
    
    def distance_moy(self):
        """
        Calcule la distance moyenne des arêtes du graphe sans utiliser de set ou de sorted.
        """
        distances = []
        
        for nom_a in self.carte:
            for nom_b, distance in self.carte[nom_a]["voisins"].items():
                # Compter l'arête uniquement si le nom de la ville source est "inférieur" au nom de la ville cible
                if nom_a < nom_b:  # Cela garantit qu'on ne compte pas deux fois la même arête
                    distances.append(distance)
    
        # Calcul de la moyenne
        if distances:  # Éviter une division par zéro si aucune arête n'existe
            return sum(distances) / len(distances)
        else:
            return 0  # Aucun lien dans le graphe


    def prim(self, sommet_depart):
        """
        Applique l'algorithme de Prim pour trouver un arbre couvrant de poids minimum.

        Args:
            sommet_depart (str): Nom du nœud de départ.

        Returns:
            list: Liste d'arêtes constituant l'arbre couvrant de poids minimum.
        """
        aag = []
        visites = [sommet_depart]
        
        while len(visites) < len(self.carte):
            dist_min = float('inf')
            arete_min = None

            # Trouve l'arête avec le poids minimum
            for sommet in visites:
                for (voisin, dist) in self.carte[sommet]["voisins"].items():
                    if voisin not in visites and dist < dist_min:
                        dist_min = dist
                        arete_min = (sommet, voisin, dist_min)
            
            if arete_min:
                aag.append(arete_min)
                visites.append(arete_min[1])

        return aag
    
    
    def calcul_min_max_xy(self):
        """
        Calcule les coordonnées cartésiennes minimales et maximales des nœuds dans la structure de graphe.
        """
        x_min = math.inf
        x_max = -math.inf
        y_min = math.inf
        y_max = -math.inf
        
        # Parcours de tous les nœuds du graphe
        for nom, data in self.carte.items():
            latitude = data["ville"].lat
            longitude = data["ville"].long
            
            # Conversion des coordonnées géographiques en coordonnées cartésiennes
            x_test, y_test = self.convertisseur.geo_to_canvas(latitude, longitude)
            
            # Mise à jour des valeurs min et max pour les coordonnées x et y
            if x_test < x_min:
                x_min = x_test
            if x_test > x_max:
                x_max = x_test
            if y_test < y_min:
                y_min = y_test
            if y_test > y_max:
                y_max = y_test
                
        return (x_min, x_max, y_min, y_max)
    
    def xy_repere_cartesien(self, nom_noeud):
        """
        Convertit les coordonnées géographiques d'un nœud en coordonnées cartésiennes.
        """
        if nom_noeud not in self.carte:
            raise ValueError("Le nœud spécifié n'existe pas dans le graphe.")

        ville = self.carte[nom_noeud]["ville"]
        x_ville, y_ville = self.convertisseur.geo_to_canvas(ville.lat, ville.long)
        (x_min,x_max,y_min,y_max) = self.calcul_min_max_xy()

        return self.convertisseur.ajuste_to_repere(x_ville, y_ville, x_min, x_max, y_min, y_max)