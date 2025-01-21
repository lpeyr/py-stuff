from random import randint


def affiche_liste_2D(liste):
    for i in range(len(liste)):
        s = ""
        for j in range(len(liste[i])):
            s += str(liste[i][j])
        print(s)


def creation_matrice_nulle(n, m):
    matrice = []
    for _ in range(n):
        liste = []
        for _ in range(m):
            liste.append(0)
        matrice.append(liste)
    return matrice


def creation_matrice_aleatoire(n, m):
    matrice = []
    for _ in range(n):
        liste = []
        for _ in range(m):
            liste.append(randint(1, 10))
        matrice.append(liste)
    return matrice


def compte_elem(k, val, matrice):
    s = 0
    for i in range(len(matrice)):
        compteur = 0
        j = 0
        while j < len(matrice[i]) and compteur <= k:
            if matrice[i][j] >= val:
                compteur += 1
            j += 1
        if compteur > k:
            s += 1
    return s


def copie_liste(l1):
    liste = []
    for el in l1:
        l = []
        for item in el:
            l.append(item)
        liste.append(l)
    return liste


m = creation_matrice_nulle(7, 9)
m[len(m) // 2][len(m[len(m) // 2]) // 2] = 1  # Met un 1 au centre de la matrice
affiche_liste_2D(m)
print(compte_elem(2, 5, creation_matrice_aleatoire(10, 3)))
