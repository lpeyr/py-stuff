from random import randint
import matplotlib.pyplot as plt

# Jeu de test :
# [1, 2, 3, 4, 5] -> [1, 2, 3, 4, 5]
# [5, 25, 8, 6, 2] -> [2, 5, 6, 8, 25]
# [] -> []


# Pour chaque valeur de la liste
# Pour chaque couple d’elements adjacents a et b
# Si a > b
# Echanger les positions des elements a et b
def tri_bulle(liste: list) -> tuple[list, int]:
    compteur = 0
    for i in range(len(liste)):
        nb_echange = (
            -1
        )  # le nombre de comparaison ne diminue pas lorsque la liste est dans l'ordre décroissant
        j = 0
        while j < len(liste) - 1 - i and nb_echange != 0:
            nb_echange = 0
            if liste[j] > liste[j + 1]:
                liste[j + 1], liste[j] = liste[j], liste[j + 1]
                nb_echange += 1
            compteur += 1
            j += 1
    return liste, compteur


def liste_aleatoire(min: int, max: int, n: int) -> list:
    liste = []
    for _ in range(n):
        liste.append(randint(min, max))
    return liste


def nb_moyen_comp(n, nb_listes):
    total = 0
    for _ in range(nb_listes):
        total += tri_bulle(liste_aleatoire(0, n, n))[1]
    return total / nb_listes


print(tri_bulle([1, 2, 3, 4, 5]))
print(tri_bulle(liste_aleatoire(0, 200, 10)))

# compteur = n(n-1) sans opti, et compteur = n(n-1)/2 si opti

# afficher avec matplotlib le nombre de comparaison
nc = 100
x = []
y = []
for i in range(nc):
    x.append(i)
    y.append(nb_moyen_comp(i, nc))

fig, ax = plt.subplots(figsize=(4, 4))
# Donner un titre
ax.set_title("Nombre de comparaison en fonction de la taille de la liste")
ax.set_xlabel("Taille de la liste")
ax.set_ylabel("Nombre de comparaison moyenne")

# Tracé cf. Quelques types de graphiques
ax.plot(x, y, label="Comparaison(taille)")
ax.plot(x, x)
plt.show()
