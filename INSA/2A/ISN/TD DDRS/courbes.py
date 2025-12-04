#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 11 16:28:49 2025

@author: nbennani1
"""
import matplotlib.pyplot as plt
 
def tracer_perf(x,y_algo1,y_algo2,y_algo3,y_algo4,y_algo5):
    # Création de la figure
    plt.figure(figsize=(10, 6))
    
    # Tracés de plusieurs courbes avec différents styles
    if len(y_algo1) == len(x):
        plt.plot(x, y_algo1, label='algo1', color='blue', linewidth=2)
    if len(y_algo2) == len(x):
        plt.plot(x, y_algo2, label='algo2', color='red',  linewidth=2)
    if len(y_algo3) == len(x):
        plt.plot(x, y_algo3, label='algo3', color='green', linewidth=2)
    if len(y_algo4) == len(x):
        plt.plot(x, y_algo4, label='algo4', color='pink', linewidth=2)
    if len(y_algo4) == len(x):
        plt.plot(x, y_algo5, label='algo5', color='black',  linewidth=2)
    # Titres et labels
    plt.title("Comparaison des temps d'execution des algos calculant les affectations aux points de fraicheur", fontsize=14, fontweight='bold')
    plt.xlabel("Nombre de noeuds du graphe", fontsize=12)
    plt.ylabel("temps de calcul en ms", fontsize=12)
    
    # Grille et légende
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(loc='upper right', fontsize=11)
    
      
    
    # Affichage
    plt.show()
    
#tracer_perf()
    
    
    
