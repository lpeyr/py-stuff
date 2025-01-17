from random import randint


def position_pour_insertion(l, p, x):
    i = 0
    while i < p and l[i] < x:
        i += 1
    return i


def insertion_liste_triee(i, l):
    for j in range(i, 0, -1):
        if l[j] < l[j - 1]:
            l[j], l[j - 1] = l[j - 1], l[j]


def creer_liste_aleatoire(n, a, b):
    l = []
    for _ in range(n):
        l.append(randint(a, b))
    return l


def tri_insertion(l):
    for i in range(len(l)):
        insertion_liste_triee(i, l)


liste_1 = [2, 5, 7, 4, 6]
for k in range(10):
    l = creer_liste_aleatoire(10, 0, 10)
    tri_insertion(l)
    print(l)

print(liste_1)
