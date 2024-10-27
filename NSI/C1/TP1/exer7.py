def vitesse_nage(L, f):
    # Formule 1/4L(3f-4)
    return 1 / 4 * L * (3 * f - 4)

# Tests de la fonction vitesse_nage
longueur = 10
freq = 5
print(f"La vitesse d'un poisson de longueur {longueur} cm avec une fréquence de battement de queue de {freq} fois / seconde est de {vitesse_nage(longueur, freq)} cm/s.")