voyelles = ("a", "e", "i", "o", "u", "y")
mot = "mercredi"


def compter_voyelle(mot):
    n = 0
    for lettre in mot:
        if lettre in voyelles:
            n += 1
    return n


def position_voyelle(mot):
    voy = []
    for i in range(len(mot)):
        if mot[i] in voyelles:
            voy.append((mot[i], i))
    return voy


print(f"Le mot {mot} contient les voyelles suivantes :")
for element in position_voyelle(mot):
    print(f"-> {element[0]} à la position {element[1]}")
