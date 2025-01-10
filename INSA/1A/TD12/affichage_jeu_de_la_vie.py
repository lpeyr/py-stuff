from random import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def init_vide(size):
    """
    Renvoie un monde (liste 2D d’entiers) de taille "size x size" (entiers)
    entiièrement mort (que des 0)
    """
    return [
        [0] * size for _ in range(size)
    ]  # Correction du problème de référence partagée


def init_aleatoire(size, proba):
    """
    Renvoie un monde (liste 2D d’entiers) de taille size x size aléatoire.
    Chaque case a une probabilité "proba" (float) d’être vivante.
    """
    return [[1 if random() <= proba else 0 for _ in range(size)] for _ in range(size)]


def affichage_monde(grid):
    """Affichage sur la console le monde "grid" (liste 2D d’entiers) passé
    en paramètre
    """
    for line in grid:
        print("".join(str(el) for el in line))


def voisin(grid, x, y):
    """
    Renvoie le nombre de voisins vivants de grid (liste 2D d’entiers) autour
    de la cellule de coordonnées entières (x, y) dans un monde cyclique.
    """
    nb_vivants = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            # Gestion cyclique avec modulo
            nx = (x + i) % len(grid)  # Coordonnée cyclique en x
            ny = (y + j) % len(grid[0])  # Coordonnée cyclique en y
            if not (i == 0 and j == 0):  # Ne pas compter la cellule elle-même
                nb_vivants += grid[nx][ny]
    return nb_vivants


def copie_liste_2D(grid):
    """
    Renvoie une copie de la liste 2D "grid".
    """
    liste = []
    for el in grid:
        l = []
        for item in el:
            l.append(item)
        liste.append(l)
    return liste


# Fonctions pour ajouter des structures spécifiques


def ajouter_bateau(grid, x, y):
    """
    Ajoute un bateau à la position (x, y) du monde.
    Le bateau est une structure de 2x4 avec une forme particulière.
    """
    bateau = [[0, 1, 1, 0], [1, 0, 0, 1], [0, 1, 1, 0]]
    for i in range(3):
        for j in range(4):
            grid[(x + i) % len(grid)][(y + j) % len(grid[0])] = bateau[i][j]


def ajouter_glider(grid, x, y):
    """
    Ajoute un glider (structure qui se déplace) à la position (x, y) du monde.
    """
    glider = [[0, 1, 0], [0, 0, 1], [1, 1, 1]]
    for i in range(3):
        for j in range(3):
            grid[(x + i) % len(grid)][(y + j) % len(grid[0])] = glider[i][j]


def ajouter_barre(grid, x, y):
    """
    Ajoute une barre de 4 cellules vivantes à la position (x, y) du monde.
    """
    for j in range(4):
        grid[x % len(grid)][(y + j) % len(grid[0])] = 1


########### INITIALISATION DE L’ANIMATION
def init_visu():
    """
    Création initiale de l'animation
    """
    fig, ax = plt.subplots()
    ims = []
    plt.axis("off")
    return [fig, ax, ims]


########### AJOUT D’UN ETAT A L’ANIMATION
def add_visu(grid, visu):
    """
    Ajout d'un état de l'automate grid à l'animation visu
    """
    fig, ax, ims = visu[0], visu[1], visu[2]
    im = ax.imshow(grid, animated=True)
    ims.append([im])
    return [fig, ax, ims]


########### AFFICHAGE DE L’ANIMATION
def show_anim(visu):
    """
    Lance l'affichage de l'animation dans une nouvelle fenêtre
    """
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
for _ in range(nb_round):
    # Ajout dans l'animation du nouvel état du monde
    grid2 = copie_liste_2D(grid)
    for i in range(size):
        for j in range(size):
            n = voisin(grid, i, j)
            if grid[i][j] == 1 and (
                n < 2 or n > 3
            ):  # La cellule meurt si elle a moins de 2 ou plus de 3 voisins
                grid2[i][j] = 0
            elif (
                grid[i][j] == 0 and n == 3
            ):  # La cellule devient vivante si elle a exactement 3 voisins
                grid2[i][j] = 1
    grid = copie_liste_2D(grid2)
    anim = add_visu(grid, anim)

# Visualisation de l'animation
show_anim(anim)
