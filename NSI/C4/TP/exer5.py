# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 12:24:22 2023

@author: leo.peyronnet
"""


def cesar(chaine: str, cle: int) -> str:
    """   

    Parameters
    ----------
    chaine : str
        La chaîne à coder.
    cle : int
        La clé.

    Returns
    -------
    str
        Le texte encodé.

    """
    string = ""

    for c in chaine:
        if ord(c) >= 65 and ord(c) <= 90:  # majuscules
            new = chr(ord(c)+cle)
            if ord(c)+cle > 90:
                new = chr(ord(c)-(26-cle))

            string += new

        elif ord(c) >= 97 and ord(c) <= 122:  # minuscules
            new = chr(ord(c)+cle)
            if ord(c)+cle > 122:
                new = chr(ord(c)-(26-cle))

            string += new
        else:
            string += c
    return string


print(cesar(input("Entrez le texte\n> "), 10))
