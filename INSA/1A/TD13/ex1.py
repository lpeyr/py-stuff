def plus_un(l):
    for i in range(len(l)):
        l[i] += 1


def plus_deux(l):
    plus_un(l)
    plus_un(l)


def reserver(l):
    i = 0
    while i < len(i) and l[i] != True:
        i += 1
    if i > len(l):
        print("Pas de rendez-vous disponibles")
    else:
        print(f"Rendez-vous pris à la position {i}")


def moyennage(l):
    liste = []
    for i in range(len(l)):
        liste.append((l[i - 1] + l[i] + l[(i + 1) % len(l)]) / 3)
    for i in range(len(l)):
        l[i] = liste[i]


l = [1, 2, 3]
moyennage(l)
print(l)
