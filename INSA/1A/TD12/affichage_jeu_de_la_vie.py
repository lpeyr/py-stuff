# -*- coding: utf-8 -*-

from random import uniform,random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

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
            if x+i >= 0 and y+j >= 0 and x+i<len(grid) and not(i== 0 and j==0) and y+j<len(grid[0]):
                nb_vivants+=grid[x+i][y+j]
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

########### INITIALISATION DE L’ANIMATION
def init_visu() :
    '''
    Création initiale de l'animation
    '''
    fig, ax = plt.subplots()
    ims = []
    plt.axis("off")
    return [fig, ax, ims]

########### AJOUT D’UN ETAT A L’ANIMATION
def add_visu(grid, visu) :
    '''
    Ajout d'un état de l'automate grid à l'animation visu
    '''
    fig, ax, ims = visu[0], visu[1], visu[2]
    im = ax.imshow(grid, animated=True)
    ims.append([im])
    return [fig, ax, ims]

########### AFFICHAGE DE L’ANIMATION
def show_anim(visu) :
    '''
    lance l'affichage de l'animation dans une nouvelle fenêtre
    '''
    fig, ims = visu[0], visu[2]
    ani = animation.ArtistAnimation(fig, ims, interval=10, blit=True, repeat_delay=1000)
    plt.show()
    visu.append(ani)
    
    
########## PARTIE PRINCIPALE
size = 150
proba = 0.4
nb_round = 500

# Initialisation du monde
grid = init_aleatoire(size, proba)

# Création de l'animation ajout du monde initial
anim = init_visu()
anim = add_visu(grid, anim)

# Pour chaque génération
for i in range(nb_round):
    # Ajout dans l'animation du nouvel état du monde
    grid2 = copie_liste_2D(grid)
    for i in range(size):
        for j in range(size):
            n = voisin(grid, i, j)
            if grid[i][j] == 1 and (n < 2 or n > 3):
                grid2[i][j] = 0
            elif grid[i][j] == 0 and (n==3):
                grid2[i][j] = 1
    grid = copie_liste_2D(grid2)
    anim = add_visu(grid, anim)

# Visualisation de l'animation
show_anim(anim)
