def voy(texte):
    v, c = [], []
    voyelles = ["a", "e", "i", "o", "u", "y", "A", "E", "I", "O", "U", "Y"]
    for lettre in texte:
        if voyelles.__contains__(lettre):
            v.append(lettre)
        else:
            c.append(lettre)

    return v,c


print(voy("Bonjour"))