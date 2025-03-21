import random

def init_grille(x:int, y:int) -> list[list]:
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

def echanger_bonbon(grille:list[list], b1:tuple[int, int], b2:tuple[int, int]) -> None:
    """
    Echange le bonbon b1 et b2 dans la grille.
    Entrées :
        - grille : grille où échanger les bonbons
        - b1 : objet Tuple (x1, y1) représentant les coordonées du premier bonbon
        - b2 : objet Tuple (x2, y2) représentant les coordonées du second bonbon
    Sortie : None
    """ 
    grille[b1[0]][b1[1]], grille[b2[0]][b2[1]] = grille[b2[0]][b2[1]], grille[b1[0]][b1[1]]
    

def retirer_bonbon(grille:list[list], b1:tuple[int,int], b2:tuple[int,int]) -> None:
    """
    Retire les bonbons entre b1 et b2 en remplaçant leur valeurs par des -1.
    Entrées :
        - grille : la grille du jeu
        - b1 : objet Tuple (x1, y1) représentant les coordonées du premier bonbon
        - b2 : objet Tuple (x2, y2) représentant les coordonées du second bonbon
    Sortie : None
    """
    if b1[0] == b2[0]: # Si les bonbons sont sur la même ligne
        for i in range(min(b1[1], b2[1]), max(b1[1], b2[1]) + 1):
            grille[b1[0]][i] = -1
    elif b1[1] == b2[1]: # Si les bonbons sont sur la même colonne
        for i in range(min(b1[0], b2[0]), max(b1[0], b2[0]) + 1):
            grille[i][b1[1]] = -1


def obtenir_bonbons_ligne_dessus(b1:tuple[int,int], b2:tuple[int, int]) -> list[list]:
    """
    Obtient les bonbons de la ligne du dessus entre les coordonnées du bonbon 1 et 2.
    Entrées :
        - grille : la grille du jeu
        - b1 : objet Tuple (x1, y1) représentant les coordonées du premier bonbon
        - b2 : objet Tuple (x2, y2) représentant les coordonées du second bonbon
    Sortie : Une liste 2D de bonbons list[list[Tuple(x,y)]]
    """
    bonbon_dessus = []
    
    