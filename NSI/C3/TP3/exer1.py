# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 12:18:01 2022

@author: leo.peyronnet
"""
def recherche(caractere: str, mot: str) -> int:
    """
    Recherche un caractère dans un mot.

    Parameters
    ----------
    caractere : str
        Le caractère à rechercher.
    mot : str
        Le mot où rechercher le caractère.

    Returns
    -------
    int
        Le nombre de fois où apparaît le caractère.

    """
    total = 0
    for lettre in mot:
        if lettre == caractere:
            total += 1
            
    return total


# Tests
print(recherche("e", "sciences"))
print(recherche("i", "mississippi"))
print(recherche("a", "mississippi"))