import random

def init_grille(x, y) -> list[list]:
    """
    Initialise une grille de taille x * y.
    Chaque case est remplie aléatoirement avec un bombon (fonction random.randint() entre 0 et 3)
    Sortie :
        - grille : une liste 2D avec des valeurs aléatoires.
    """
    grille = []
    for i in range(x):
        ligne = []
        for j in range(y):
            ligne.append(random.randint(0, 3))
        grille.append(ligne)
    return grille

def echanger_bonbon(grille, b1, b2) -> None:
    """
    Echange le bonbon b1 et b2 dans la grille.
    Entrées :
        - grille : grille où échanger les bonbons
        - b1 : objet Tuple (x1, y1) représentant les coordonées du premier bonbon
        - b2 : objet Tuple (x2, y2) représentant les coordonées du second bonbon
    Sortie : None
    """ 
    grille[b1[0]][b1[1]], grille[b2[0]][b2[1]] = grille[b2[0]][b2[1]], grille[b1[0]][b1[1]]
    

    