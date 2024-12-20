from random import random
def init_vide(size) :
    """
    Renvoie un monde (liste 2D d’entiers) de taille "size x size" (entiers)
    entiièrement mort (que des 0)
    """
    return [[0]*size]*size

def init_aleatoire(size, proba) :
    """
    Renvoie un monde (liste 2D d’entiers) de taille size x size aléatoire.
    Chaque case à une proba "proba" (float) d’être vivante.
    """
    liste=[]
    for _ in range(size):
        l=[]
        for _ in range(size):
            if random() <= proba:
                l.append(1)
            else:
                l.append(0)
        liste.append(l)
    return liste

def affichage_monde(grid) :
    """ Affichage sur la console le monde "grid" (liste 2D d’entiers) passé
    en paramètre
    """
    for line in grid:
        s=""
        for el in line:
            s+=str(el)
        print(s)

def voisin(grid, x, y):
    """
    Renvoie le nombre de voisins vivants de grid (liste 2D d’entiers) autour
    de la cellule de coordonnées entières (x,y)
    """
    nb_vivants=0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if x+i > 0 and y+j > 0 and x+i<len(grid) and y+j<len(grid[0]) and grid[x+i][y+j]==1:
                nb_vivants+=1
    return nb_vivants
def copie_liste_2D(grid):
    """
    Renvoie une liste 2D qui est la copie de la liste 2D "grid" donnée
    en paramètre
    """
    liste = []
    for el in grid:
        l = []
        for item in el:
            l.append(item)
        liste.append(l)
    return liste