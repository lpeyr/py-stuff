import random


def init_grille(x: int, y: int) -> list[list]:
    """
    Initialise une grille de taille x * y.
    Chaque case est remplie aléatoirement avec un bonbon (fonction random.randint() entre 0 et 3),
    en s'assurant qu'il n'y a pas de combinaison possible (pas 3 mêmes nombres en ligne ou en colonne).
    Sortie :
        - grille : une liste 2D avec des valeurs aléatoires sans combinaison possible.
    """
    grille = [[-1 for _ in range(y)] for _ in range(x)]

    for i in range(x):
        for j in range(y):
            possible_values = [0, 1, 2, 3]
            # Exclure les valeurs qui formeraient une combinaison en ligne
            if j >= 2 and grille[i][j - 1] == grille[i][j - 2]:
                possible_values.remove(grille[i][j - 1])
            # Exclure les valeurs qui formeraient une combinaison en colonne
            if i >= 2 and grille[i - 1][j] == grille[i - 2][j]:
                possible_values.remove(grille[i - 1][j])
            # Choisir une valeur aléatoire parmi les valeurs possibles restantes
            grille[i][j] = random.choice(list(possible_values))

    return grille


def echanger_bonbon(grille: list[list], b1: tuple[int, int],
                    b2: tuple[int, int]) -> None:
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


def retirer_bonbon(grille: list[list], b1: tuple[int, int],
                   b2: tuple[int, int]) -> None:
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


def obtenir_bonbons_ligne_dessus(b1: tuple[int, int],
                                 b2: tuple[int, int]) -> list[list]:
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
        bonbon_dessus.append([(b1[0] - i, b1[1]), (b1[0] - i, b1[1] - 1),
                              (b2[0] - i, b2[1])])
        i += 1
    return bonbon_dessus


obtenir_bonbons_ligne_dessus((1, 3), (3, 3))


def descendre_bonbons(grille, b1, b2):
    """
    Décale les bonbons entre b1 et b2 qui sont situés au-dessus de la ligne _ligne_. Cette fonction est appelée après avoir supprimé les bonbons entre b1 et b2. Pour chaque ligne de 0 à ligne-1, la fonction prend les bonbons de la ligne entre les coordonnées pertinentes et les décalent vers le bas.
    Entrées :
      - grille : la grille du jeu
      - b1 : objet Tuple (x1, y1) représentant les coordonées du premier bonbon
      - b2 : objet Tuple (x2, y2) représentant les coordonées du second bonbon
    Sortie : None
    """
    for i in range(len(grille[0])):
        for j in range(len(grille) - 1, 0, -1):
            if grille[j][i] == -1:
                index = j
                while index > 0:
                    grille[i][index], grille[i][index - 1] = grille[i][
                        index - 1], grille[i][index]
                    index -= 1


def inserer_bonbons(grille, b1, b2):
    # A MODIFIER POUR LE NIVEAU 3, LISTE DE BONBONS A DONNER AU LIEU DE 2
    # POUR L'INSTANT ON PART DU PRINCIPE QUE LES BONBONS SONT TOUS DE LA MÊME LIGNE OU COLONNE
    """
    Insère des bonbons générés aléatoirements entre les coordonnées b1 et b2
    Entrées :
        - grille : la grille du jeu
        - b1 : objet Tuple (x1, y1) représentant les coordonées du premier bonbon
        - b2 : objet Tuple (x2, y2) représentant les coordonées du second bonbon
    Sortie : None
    """
    if b1[1] == b2[1]:  # Si les bonbons sont sur la même colonne
        ligne_min = min(b1[0], b2[0])
        ligne_max = max(b1[0], b2[0])
        for i in range(ligne_min, ligne_max + 1):
            grille[i][b1[1]] = random.randint(0, 3)
    else:
        colonne_min = min(b1[1], b2[1])
        colonne_max = max(b1[1], b2[1])
        for i in range(colonne_min, colonne_max + 1):
            grille[b1[0]][i] = random.randint(0, 3)


def demander_utilisateur_bonbons(grille):
    """
    Demander à l'utilisateur les deux bonbons qu'il souhaite échanger ; il faut soit que x1 = x2 ou y1 = y2.
    Retourne les coordonnées deux deux bonbons Tuple(Tuple(x1, y1), Tuple(x2, y2)
    """
    b1 = len(grille)
    b2 = len(grille[0])
    while b1 > len(grille) or b2 > len(grille[0]):
        print("Entrez les coordonnées des deux bonbons à échanger :")
        b1 = (int(input("x1 : ")), int(input("y1 : ")))

        print("Entrez les coordonnées du deuxième bonbon")
        b2 = (int(input("x2 : ")), int(input("y2 : ")))
    return b1, b2


def combinaison_possible(grille, max=3):
    """
    Renvoie True si des combinaisons sont possibles.
    """


def detecte_coordonnees_combinaison(grille, bonbon, max=3):
    """
    Vérifie si les bonbons sur la ligne ou la colonne du bonbon forment une combinaison. On utilisera une boucle while.
    Exemple d'Algorithme pour les lignes :
    CompteurCombi <- 0
    i <- 0
    x <- i
    BonbonCombi=BonbonLigne[0]
    Tant que CompteurCombi < max et que i < TailleLigne:
        Si BonbonCombi != Ligne[i]:
            CompteurCombi = 0
            x <- i
        Sinon:
            CompteurCombi += 1

    Entrées :
      - grille : la grille du jeu
      - bonbon : Tuple(x,y) représentant les cordonnées du bonbon
      - max : Valeur de la taille maximale de la combinaison (ex: 3 en ligne et 3 en colonne)
    Sortie : Une liste de bonbons list[Tuple(x,y)] qui contient les coordonnées des bonbons de la combinaison
    """
    combi = []
    val = grille[bonbon[0]][bonbon[1]]
    # En ligne
    i = 0
    compteur = 0
    while i < len(grille[bonbon[0]]) and compteur < max:
        if grille[bonbon[0]][i] == val:
            compteur += 1
            combi.append((bonbon[0], i))
        else:
            combi = []
            compteur = 0
        i += 1

    if len(combi) < max:
        combi = []

    # En colonne
    i = 0
    compteur = 0
    while i < len(grille[0]) and compteur < max:
        if grille[i][bonbon[1]] == val:
            compteur += 1
            combi.append((i, bonbon[1]))
        else:
            compteur = 0
            combi = []
        i += 1
    if len(combi) < max:
        combi = []
    return combi


# import matplotlib.pyplot as plt
def affichage_grille(grille, nb_type_bonbons):
    """
    Affiche la grille de jeu "grille" contenant au
    maximum "nb_type_bonbons" couleurs de bonbons différentes.
    """
    bonbons = ["🍭", "🍡", "🍫", "🍦"]
    print("╔" + "═" * (3 * len(grille[0]) - 1) + "╗")
    for i in range(len(grille)):
        print("║", end="")
        for j in range(len(grille[i])):
            print(bonbons[grille[i][j]], end="")
            if j != len(grille) - 1:
                print("|", end="")
        print("║")
    print("╚" + "═" * (3 * len(grille[0]) - 1) + "╝")


def test_detecte_coordonnees_combinaison():
    """
    Test la fonction detecte_coordonnees_combinaison(grille, i, j).
    Pour chaque cas de test, affiche True si le test passe,
    False sinon
    """
    pass


# Programme principal
def __main__():
    grille = init_grille(5,5) # Création d'une grille 5x5

    affichage_grille(grille)

    # Démarage du Jeu

    while combinaison_possible(grille):

        b1, b2 = demander_utilisateur_bonbons(grille)

        echanger_bonbon(grille, b1, b2) 

        # On recupère les combinaisons possible du b1 et du b2 -> cette liste de
        combinaison_b1 = detecte_coordonnees_combinaison(grille, b1) 
        combinaison_b2 = detecte_coordonnees_combinaison(grille, b2)


        combinaison_b1_b2 = combinaison_b1 + combinaison_b2
        if combinaison_b1_b2 != [] : # s'il y a des combinaisons
            for bonbon in combinaison_b1_b2 :
                grille[bonbon[0]][bonbon[1]] = -1 # on retire les bonbons qui font partie de la combinaison
            
            descendre_bonbons(grille)
            inserer_bonbons(grille) # Ajouter des bonbons de sorte à ce qu'il n'y ait pas de nouvelles combinaisons
