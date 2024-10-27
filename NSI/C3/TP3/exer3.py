# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 12:22:48 2022

@author: leo.peyronnet
"""

def maxi(tab: list) -> tuple:
    """    
    Recherche le maximum dans tab.

    Parameters
    ----------
    tab : list
        Le tableau où rechercher le maxium.

    Returns
    -------
    tuple
        Le maximum, puis l'indice.

    """
    b, indice = tab[0], 0
    for i in range(len(tab)):
        if tab[i] >= b:
            b = tab[i]
            indice = i
            
    return b, indice

# Tests
print(maxi([1,5,6,9,1,2,3,7,9,8]))