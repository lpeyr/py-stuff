def compte_lettreE(phrase):
    compteur = 0
    for lettre in phrase:
        if lettre == "e":
            compteur += 1
    return compteur

# Tests de la fonction
print(compte_lettreE("Ceci est un test")) # Valeur normalement affichée : 3