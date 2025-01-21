from random import randint

# Jeu de test :
# [1, 2, 3, 4, 5] -> [1, 2, 3, 4, 5]
# [5, 25, 8, 6, 2] -> [2, 5, 6, 8, 25]
# [] -> []


# Pour chaque valeur de la liste
# Pour chaque couple d’elements adjacents a et b
# Si a > b
# Echanger les positions des elements a et b
def tri_bulle(liste: list) -> list:
    compteur = 0
    for i in range(len(liste)):
        for j in range(len(liste) - 1):
            if liste[j] > liste[j + 1]:
                liste[j + 1], liste[j] = liste[j], liste[j + 1]
                compteur += 1
    return liste, compteur


def liste_aleatoire(min: int, max: int, n: int) -> list:
    liste = []
    for _ in range(n):
        liste.append(randint(min, max))
    return liste


for _ in range(20):
    print(tri_bulle(liste_aleatoire(0, 1000, 100)))
