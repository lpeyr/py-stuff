import random
import os

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
    grille = []
    for _ in range(x):
        row = []
        for _ in range(y):
            row.append(-1)
        grille.append(row)

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
                if (
                    i >= 2
                    and grille[i - 1][j] == grille[i - 2][j]
                    and grille[i - 1][j] in possible_values
                ):
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
        or (b1[0] == b2[0] and b1[1] == b2[1])
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
      x <- bonbon[0]
      CombiLigne <- []
      BonbonCombi <- grille[x][bonbon[1]]
      Tant que i < TailleLigne:
          Si grille[x][i] != BonbonCombi:
              CompteurCombi <- 0
              CombiLigne <- []
          Sinon:
              CompteurCombi <- CompteurCombi + 1
              CombiLigne.ajouter((x, i))
              Si CompteurCombi >= max:
                  Sauvegarder CombiLigne comme combinaison valide
          i <- i + 1

    Même logique à appliquer pour la colonne avec j variant de 0 à TailleColonne.

    Entrées :
      - grille : la grille du jeu
      - bonbon : Tuple(x, y) représentant les coordonnées du bonbon
      - max : Valeur de la taille minimale de la combinaison (ex: 3 en ligne et 3 en colonne)

    Sortie :
      - Une liste de bonbons list[Tuple(x, y)] qui contient les coordonnées des bonbons de la plus longue combinaison
    """
    x, y = bonbon
    valeur = grille[x][y]
    resultat = []

    # Vérification horizontale
    i = 0
    compteur = 0
    combi_ligne = []
    while i < len(grille[0]):
        if grille[x][i] == valeur:
            compteur += 1
            combi_ligne.append((x, i))
            if compteur >= max:
                resultat = combi_ligne
        else:
            compteur = 0
            combi_ligne = []
        i += 1

    # Vérification verticale
    j = 0
    compteur = 0
    combi_colonne = []
    while j < len(grille):
        if grille[j][y] == valeur:
            compteur += 1
            combi_colonne.append((j, y))
            if compteur >= max:
                resultat = combi_colonne
        else:
            compteur = 0
            combi_colonne = []
        j += 1

    return resultat


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


def affichage_grille(grille: grid):
    """
    Affiche la grille de jeu.
    Entrées :
        - grille : la grille du jeu
    Sortie : None
    """
    bonbons = ["🍭", "🍡", "🍫", "🍦", "  "]
    print("  ", end="")
    for j in range(len(grille)):
        print(str(j) + "  ", end="")
    print()
    print(" ╔" + "═" * (3 * len(grille[0]) - 1) + "╗")
    for i in range(len(grille)):

        print(str(i) + "║", end="")
        for j in range(len(grille[i])):
            print(bonbons[grille[i][j]], end="")
            if j != len(grille) - 1:
                print("|", end="")
        print("║")
    print(" ╚" + "═" * (3 * len(grille[0]) - 1) + "╝")


def enlever_doublons(liste1, liste2):
    """
    Enlève les doublons de la liste liste1 dans liste2
    """
    resultat = []
    for i in range(len(liste1)):
        if liste1[i] not in liste2:
            resultat.append(liste1[i])
    for j in range(len(liste2)):
        if liste2[j] not in liste1:
            resultat.append(liste2[j])
    return resultat


def etendre_combinaison(grille: grid, combinaison):
    """
    Etend une combinaison en ligne ou en colonne pour pouvoir détecter les combinaisons de niveau 3. C'est à dire
    qu'il faut vérifier si il y a des bonbons adjacents à la combinaison qui sont de la même couleur.

    Entrées :
        - grille : la grille du jeu
        - combinaison : une liste de bonbons list[Tuple(x,y)]

    Sortie : La combinaison étendue list[Tuple(x,y)]
    """
    deja_explores = []
    a_explorer = [combinaison[0]]
    while len(a_explorer) != 0:
        actuel = a_explorer[-1]
        a_explorer.pop(-1)
        deja_explores.append(actuel)
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (
                    actuel[0] + i >= 0
                    and actuel[1] + j >= 0
                    and actuel[0] + i < len(grille)
                    and actuel[1] + j < len(grille[0])
                    and abs(i) != abs(j)
                ):
                    if (
                        grille[actuel[0] + i][actuel[1] + j]
                        == grille[combinaison[0][0]][combinaison[0][1]]
                    ):
                        if (actuel[0] + i, actuel[1] + j) not in combinaison:
                            combinaison.append((actuel[0] + i, actuel[1] + j))
                        if (actuel[0] + i, actuel[1] + j) not in deja_explores:
                            a_explorer.append((actuel[0] + i, actuel[1] + j))
    return combinaison


def trouver_combinaisons_grille(grille: grid) -> list[list[candy]]:
    """
    Trouve toutes les combinaisons possibles dans la grille.
    Entrées :
        - grille : la grille du jeu
    Sortie : Une liste de combinaisons list[list[Tuple(x,y)]]
    """
    combinaisons = []
    for i in range(len(grille)):
        combi = detecte_coordonnees_combinaison(grille, (i, i))
        if len(combi) != 0:
            combi = etendre_combinaison(grille, combi)
            if len(combi) >= 3:
                combinaisons.append(combi)
    return combinaisons


def trouver_combinaisons(grille: grid, b1: candy, b2: candy) -> list[candy]:
    """
    Trouve les combinaisons possibles entre les coordonnées b1 et b2.
    Entrées :
        - grille : la grille du jeu
        - b1 : Tuple(x1, y1) représentant les coordonnées du premier bonbon
        - b2 : Tuple(x2, y2) représentant les coordonnées du second bonbon

    Sortie : Une combinaisons list[Tuple(x,y)]
    """
    combinaison_b1 = detecte_coordonnees_combinaison(grille, b1)
    combinaison_b2 = detecte_coordonnees_combinaison(grille, b2)

    if len(combinaison_b1) != 0:
        combinaison_b1 = etendre_combinaison(grille, combinaison_b1)
    if len(combinaison_b2) != 0:
        combinaison_b2 = etendre_combinaison(grille, combinaison_b2)

    combinaison_b1_b2 = enlever_doublons(
        combinaison_b1, combinaison_b2
    )  # enlever doublons
    return combinaison_b1_b2


# Systeme de point
def ajouter_points(combinaison: list[candy]) -> int:
    """
    Ajoute des points au joueur en fonction de la taille de la combinaison.
    Entrées :
        - grille : la grille du jeu
        - combinaison : une liste de bonbons list[Tuple(x,y)]
    Sortie : le nombre de points gagnés int
    """
    return 123 * 3 + 248 * (len(combinaison) - 2)


def effacer():
    """
    Efface la console.
    """
    os.system("cls" if os.name == "nt" else "clear")


# Programme principal
def main():
    grille = init_grille(5, 5)  # Création d'une grille 5x5
    points_joueur = 0  # Initialisation des points du joueur
    print("Bienvenue dans le jeu Candy Crush !")
    effacer()
    affichage_grille(grille)

    # Démarage du Jeu
    while combinaison_possible(grille):

        b1, b2 = demander_utilisateur_bonbons(grille)

        echanger_bonbon(grille, b1, b2)

        combinaison_b1_b2 = trouver_combinaisons(grille, b1, b2)

        coup = 0
        while combinaison_b1_b2 != []:  # tant que la liste des combinaisons possibles
            for bonbon in combinaison_b1_b2:
                grille[bonbon[0]][
                    bonbon[1]
                ] = -1  # on retire les bonbons qui font partie de la combinaison
            descendre_bonbons(grille)
            # Ajouter des bonbons de sorte à ce qu'il n'y ait pas de nouvelles combinaisons
            inserer_bonbons(grille)
            points_joueur += ajouter_points(combinaison_b1_b2)

            # On cherche de nouvelles combinaisons
            total_combinaisons = trouver_combinaisons_grille(grille)
            while len(total_combinaisons) != 0:
                for combinaison in total_combinaisons:
                    points_joueur += ajouter_points(combinaison)
                    coup += 1
                    for bonbon in combinaison:
                        grille[bonbon[0]][bonbon[1]] = -1

                descendre_bonbons(grille)
                inserer_bonbons(grille)

                total_combinaisons = trouver_combinaisons_grille(grille)

            combinaison_b1_b2 = trouver_combinaisons(grille, b1, b2)
        effacer()
        affichage_grille(grille)
        print(f"Vous avez joué un coup ! \nCela a produit {coup} combos")
        print(f"Votre Score : {points_joueur} Points")

    print("Il n'y a plus de combinaisons possibles !")
    print(f"Votre Score Final : {points_joueur} Points")


if __name__ == "__main__":
    main()
