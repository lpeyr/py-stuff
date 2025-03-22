import random


def init_grille(x: int, y: int) -> list[list]:
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


def echanger_bonbon(
    grille: list[list], b1: tuple[int, int], b2: tuple[int, int]
) -> None:
    """
    Echange le bonbon b1 et b2 dans la grille.
    Entrées :
        - grille : grille où échanger les bonbons
        - b1 : objet Tuple (x1, y1) représentant les coordonées du premier bonbon
        - b2 : objet Tuple (x2, y2) représentant les coordonées du second bonbon
    Sortie : None
    """
    grille[b1[0]][b1[1]], grille[b2[0]][b2[1]] = (
        grille[b2[0]][b2[1]],
        grille[b1[0]][b1[1]],
    )


def retirer_bonbon(
    grille: list[list], b1: tuple[int, int], b2: tuple[int, int]
) -> None:
    """
    Retire les bonbons entre b1 et b2 en remplaçant leur valeurs par des -1.
    Entrées :
        - grille : la grille du jeu
        - b1 : objet Tuple (x1, y1) représentant les coordonées du premier bonbon
        - b2 : objet Tuple (x2, y2) représentant les coordonées du second bonbon
    Sortie : None
    """
    if b1[0] == b2[0]:  # Si les bonbons sont sur la même ligne
        for i in range(min(b1[1], b2[1]), max(b1[1], b2[1]) + 1):
            grille[b1[0]][i] = -1
    elif b1[1] == b2[1]:  # Si les bonbons sont sur la même colonne
        for i in range(min(b1[0], b2[0]), max(b1[0], b2[0]) + 1):
            grille[i][b1[1]] = -1


def obtenir_bonbons_ligne_dessus(
    b1: tuple[int, int], b2: tuple[int, int]
) -> list[list]:
    """
    Obtient les bonbons de la ligne du dessus entre les coordonnées du bonbon 1 et 2.
    Entrées :
        - grille : la grille du jeu
        - b1 : objet Tuple (x1, y1) représentant les coordonées du premier bonbon
        - b2 : objet Tuple (x2, y2) représentant les coordonées du second bonbon
    Sortie : Une liste 2D de bonbons list[list[Tuple(x,y)]]
    """
    bonbon_dessus = []
    i = 0
    while b1[0] - i >= 0:
        bonbon_dessus.append(
            [(b1[0] - i, b1[1]), (b1[0] - i, b1[1] - 1), (b2[0] - i, b2[1])]
        )
        i += 1
    return bonbon_dessus


obtenir_bonbons_ligne_dessus((1, 3), (3, 3))


# Programme principal
def __main__():
    grille = init_grille(5, 5)

    while combinaison_possible(grille):

        (b1, b2) = demander_utilisateur_bonbons()

        echanger_bonbon(grille, b1, b2)
        combinaison = detecte_coordonnees_combinaison(grille, b1)

        while len(combinaison) != 0:  # Tant qu'il y a des combinaisons
            retirer_bonbon(
                grille, combinaison[0], combinaison[-1]
            )  # On retire les bonbons de la combinaison
            decaler_bonbon(
                grille, combinaison[0], combinaison[-1]
            )  # On décale les bonbons au dessus de la combinaison supprimée vers le bas
            inserer_bonbons(
                grille, (0, combinaison[0][1]), (0, combinaison[-1][1])
            )  # On insère des bonbons aléatoires en haut de la grille
            affichage_grille(grille, 4)  # On affiche la grille
            combinaison = detecte_coordonnees_combinaison(
                grille, b1
            )  # On vérifie si il y a d'autres combinaisons
            if len(combinaison) == 0:  # Si il n'y a plus de combinaisons
                combinaison = detecte_coordonnees_combinaison(
                    grille, b2
                )  # On vérifie si il y a d'autres combinaisons avec le deuxième bonbon
