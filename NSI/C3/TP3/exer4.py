# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 12:25:01 2022

@author: leo.peyronnet
"""
def rechercheMin(tab: list) -> int:
    """
    Recherche le minimum dans tab.

    Parameters
    ----------
    tab : list
        La liste où rechercher le minimum.

    Returns
    -------
    int
        L'indice du minimum.

    """
    l, indice = tab[0], 0
    for i in range(len(tab)):
        if tab[i] < l:
            l = tab[i]
            indice = i
            
    return indice


# Tests
print(rechercheMin([5]))
print(rechercheMin([2, 4, 1]))
print(rechercheMin([5, 3, 2, 2, 4]))