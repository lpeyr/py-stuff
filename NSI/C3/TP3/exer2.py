# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 12:19:59 2022

@author: leo.peyronnet
"""
def recherche(tab: list, n: int) -> int:
    """
    Recherche un nombre n dans une liste tab.

    Parameters
    ----------
    tab : list
        Tableau où rechercher le nombre n.
    n : int
        Nombre à rechercher.

    Returns
    -------
    int
        DESCRIPTION.

    """
    indice = -1
    for i in range(len(tab)):
        if tab[i] == n:
            indice = i
            
    return indice


# Tests
print(recherche([5, 3], 1))
print(recherche([2, 4], 2))
print(recherche([2, 3, 5, 2, 4], 2))