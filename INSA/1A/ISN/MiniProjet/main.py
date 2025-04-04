import random

candy = tuple[int, int]
grid = list[list]


def init_grille(x: int, y: int) -> grid:
    """
    Initialise une grille de taille x * y.
    Chaque case est remplie aléatoirement avec un bonbon (fonction random.randint() entre 0 et 3),
    en s'assurant qu'il n'y a pas de combinaison possible (pas 3 mêmes nombres en ligne ou en colonne).
    Sortie :
        - grille : une liste 2D avec des valeurs aléatoires sans combinaison possible.
    """
    grille = [[-1 for _ in range(y)] for _ in range(x)]

    inserer_bonbons(grille)
    return grille


def echanger_bonbon(grille: grid, b1: candy, b2: candy) -> None:
    """
    Echange le bonbon b1 et b2 dans la grille.
    Entrées :
        - grille : grille où échanger les bonbons
        - b1 : objet Tuple (x1, y1) représentant les coordonnées du premier bonbon
        - b2 : objet Tuple (x2, y2) représentant les coordonnées du second bonbon
    Sortie : None
    """
    grille[b1[0]][b1[1]], grille[b2[0]][b2[1]] = (
        grille[b2[0]][b2[1]],
        grille[b1[0]][b1[1]],
    )


def retirer_bonbon(grille: grid, b1: candy, b2: candy) -> None:
    """
    Retire les bonbons entre b1 et b2 en remplaçant leur valeurs par des -1.
    Entrées :
        - grille : la grille du jeu
        - b1 : objet Tuple (x1, y1) représentant les coordonnées du premier bonbon
        - b2 : objet Tuple (x2, y2) représentant les coordonnées du second bonbon
    Sortie : None
    """
    if b1[0] == b2[0]:  # Si les bonbons sont sur la même ligne
        for i in range(min(b1[1], b2[1]), max(b1[1], b2[1]) + 1):
            grille[b1[0]][i] = -1
    elif b1[1] == b2[1]:  # Si les bonbons sont sur la même colonne
        for i in range(min(b1[0], b2[0]), max(b1[0], b2[0]) + 1):
            grille[i][b1[1]] = -1


def obtenir_bonbons_ligne_dessus(b1: candy, b2: candy) -> grid:
    """
    Obtient les bonbons de la ligne du dessus entre les coordonnées du bonbon 1 et 2.
    Entrées :
        - grille : la grille du jeu
        - b1 : objet Tuple (x1, y1) représentant les coordonnées du premier bonbon
        - b2 : objet Tuple (x2, y2) représentant les coordonnées du second bonbon
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


def descendre_bonbons(grille: grid):
    """
    Décale les bonbons qui sont situés au-dessus de cases vides.
    Cette fonction est appelée après avoir supprimé les bonbons entre b1 et b2.
    Pour chaque ligne de 0 à ligne-1, la fonction prend les bonbons de la ligne entre les coordonnées pertinentes et les décalent vers le bas.
    Entrées :
      - grille : la grille du jeu
    Sortie : None
    """
    for i in range(len(grille[0])):
        for j in range(len(grille) - 1, 0, -1):
            if grille[j][i] == -1:
                index = j
                while index > 0:
                    grille[index][i], grille[index - 1][i] = (
                        grille[index - 1][i],
                        grille[index][i],
                    )
                    index -= 1


def inserer_bonbons(grille: grid):
    # A MODIFIER POUR LE NIVEAU 3, LISTE DE BONBONS A DONNER AU LIEU DE 2
    # POUR L'INSTANT ON PART DU PRINCIPE QUE LES BONBONS SONT TOUS DE LA MÊME LIGNE OU COLONNE
    """
    Insère des bonbons générés aléatoirements entre les coordonnées b1 et b2
    Entrées :
        - grille : la grille du jeu
    Sortie : None
    """
    for i in range(len(grille)):
        for j in range(len(grille[0])):
            if grille[i][j] == -1:
                possible_values = [0, 1, 2, 3]
                # Exclure les valeurs qui formeraient une combinaison en ligne
                if j >= 2 and grille[i][j - 1] == grille[i][j - 2]:
                    possible_values.remove(grille[i][j - 1])
                # Exclure les valeurs qui formeraient une combinaison en colonne
                if i >= 2 and grille[i - 1][j] == grille[i - 2][j] and grille[i - 1][j] in possible_values :
                    possible_values.remove(grille[i - 1][j])
                
                # Choisir une valeur aléatoire parmi les valeurs possibles restantes
                grille[i][j] = random.choice(possible_values)
            



def demander_utilisateur_bonbons(
    grille: grid,
) -> tuple[candy, candy]:
    """
    Demander à l'utilisateur les deux bonbons qu'il souhaite échanger ; il faut soit que x1 = x2 ou y1 = y2.
    Retourne les coordonnées deux deux bonbons Tuple(Tuple(x1, y1), Tuple(x2, y2)
    """
    # On initialise les coordonnées des bonbons avec des valeurs incorrectes pour entrer dans la boucle
    b1 = [-1, -1]
    b2 = [-1, -1]
    # Tant que les coordonnées ne sont pas valides dans la grille
    while (
        b1[0] < 0
        or b1[0] >= len(grille)
        or b1[1] < 0
        or b1[1] >= len(grille[0])
        or b2[0] < 0
        or b2[0] >= len(grille)
        or b2[1] < 0
        or b2[1] >= len(grille[0])
    ):
        # Demander à l'utilisateur de saisir les coordonnées des bonbons
        b1[0] = int(input("Entrez la ligne du premier bonbon (x1) : "))
        b1[1] = int(input("Entrez la colonne du premier bonbon (y1) : "))

        b2[0] = int(input("Entrez les ligne du second bonbon (x2) : "))
        b2[1] = int(input("Entrez les colonne du second bonbon (y2) : "))

        # Vérifier si les bonbons sont voisins sur la même ligne ou colonne
        # Si les coordonnées ne sont pas valides, on les remet à (-1, -1)
        if (
            abs(b1[0] - b2[0]) > 1
            or abs(b1[1] - b2[1]) > 1
            or (b1[0] != b2[0] and b1[1] != b2[1])
        ):
            b1 = [-1, -1]
            b2 = [-1, -1]
            print("Les bonbons doivent être voisins sur la même ligne ou colonne.")

    return ((b1[0], b1[1]), (b2[0], b2[1]))


def detecte_coordonnees_combinaison(grille: grid, bonbon: candy, max=3):
    """
    Vérifie si les bonbons sur la ligne ou la colonne du bonbon forment une combinaison. On utilisera une boucle while.
    Exemple d'Algorithme pour les lignes :
    CompteurCombi <- 0
    i <- 0
    x <- i
    CombiLigne <- grille[bonbon[0]][i]
    BonbonCombi=BonbonLigne[0]
    Tant que CompteurCombi < max et que i < TailleLigne:
        Si BonbonCombi != Ligne[i]:
            CompteurCombi = 0
            x = i
        Sinon:
            CompteurCombi += 1
            CombiLigne.append(Ligne[i])
        i += 1


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
    while i < len(grille[0]) and compteur < max and len(combi) < max:
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


def combinaison_possible(grille: grid, max=3):
    """
    Renvoie True si des combinaisons sont possibles. Utilise une boucle while pour parcourir la grille.
    Entrées :
        - grille : la grille du jeu
        - max : Valeur de la taille maximale de la combinaison (ex: 3 en ligne et 3 en colonne)
    Sortie : True si des combinaisons sont possibles, False sinon
    """
    i = 0
    possible = False
    while i < len(grille) and not possible:
        j = 0
        while j < len(grille[0]) and not possible:
            if grille[i][j] != -1:
                # Vérifie si une combinaison est possible
                # S'il y a au moins max - 1 bonbons sur la ligne, une combinaison est possible
                if detecte_coordonnees_combinaison(grille, (i, j), max - 1) != []:
                    possible = True
            j += 1
        i += 1
    # Si aucune combinaison n'est trouvée, vérifie
    return possible


# import matplotlib.pyplot as plt
def affichage_grille(grille: grid):
    """
    Affiche la grille de jeu.
    Entrées :
        - grille : la grille du jeu
    Sortie : None
    """
    bonbons = ["🍭", "🍡", "🍫", "🍦", "  "]
    print(" ╔" + "═" * (3 * len(grille[0]) - 1) + "╗")
    for i in range(len(grille)):
        #if i < 10:
        #    print("0",end="")
        print(str(i) + "║", end="")
        for j in range(len(grille[i])):
            print(bonbons[grille[i][j]], end="")
            if j != len(grille) - 1:
                print("|", end="")
        print("║")
    print(" ╚" + "═" * (3 * len(grille[0]) - 1) + "╝")

def enlever_doublons(liste1,liste2):
    """
    Enlève les doublons de la liste liste1 dans liste2
    """
    resultat = []
    for i in range(len(liste1)):
        if liste1[i] not in liste2 :
            resultat.append(liste1[i])
    for j in range(len(liste2)):
        if liste2[j] not in liste1 :
            resultat.append(liste2[j])
    return resultat

def test_detecte_coordonnees_combinaison():
    """
    Test la fonction detecte_coordonnees_combinaison(grille, i, j).
    Pour chaque cas de test, affiche True si le test passe,
    False sinon
    """
    grille = [
        [0, 1, 3, 3, 0],
        [1, 1, 1, 3, 2],
        [0, 0, 2, 0, 1],
        [1, 1, 2, 3, 0],
        [0, 1, 0, 3, 0],
    ]
    print(detecte_coordonnees_combinaison(grille, (1, 1)))  # True
    print(detecte_coordonnees_combinaison(grille, (2, 2)))  # False
    print(detecte_coordonnees_combinaison(grille, (4, 4)))  # False
    print(detecte_coordonnees_combinaison(grille, (0, 0)))  # False
    print(detecte_coordonnees_combinaison(grille, (1, 0)))  # False


# Programme principal
def main():
    grille = init_grille(5, 5)  # Création d'une grille 5x5

    affichage_grille(grille)

    # Démarage du Jeu

    while combinaison_possible(grille):

        b1, b2 = demander_utilisateur_bonbons(grille)

        echanger_bonbon(grille, b1, b2)
        affichage_grille(grille)

        # On recupère les combinaisons possible du b1 et du b2 -> cette liste de
        combinaison_b1 = detecte_coordonnees_combinaison(grille, b1)
        combinaison_b2 = detecte_coordonnees_combinaison(grille, b2)

        combinaison_b1_b2 = enlever_doublons(combinaison_b1, combinaison_b2)  # enlever doublons

        while combinaison_b1_b2 != []:  # tant que la liste des combinaisons possibles
            for bonbon in combinaison_b1_b2:
                grille[bonbon[0]][
                    bonbon[1]
                ] = -1  # on retire les bonbons qui font partie de la combinaison
            affichage_grille(grille)
            descendre_bonbons(grille)
            inserer_bonbons(grille)  # Ajouter des bonbons de sorte à ce qu'il n'y ait pas de nouvelles combinaisons
            
            combinaison_b1 = detecte_coordonnees_combinaison(grille, b1)
            combinaison_b2 = detecte_coordonnees_combinaison(grille, b2)
            combinaison_b1_b2 = enlever_doublons(combinaison_b1, combinaison_b2)
        affichage_grille(grille)

    print("Il n'y a plus de combinaisons possibles !")

if __name__ == "__main__":
    main()
