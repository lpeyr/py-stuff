# Une baguette B vaut 0.90€
# Un croissant C vaut 1€
# Un pain au chocolat P vaut 1.1€

# B, C et P sont le nombre de produits vendus
def recette_boulangerie(B, C, P):
    return B * 0.9 + C * 1 + P * 1.1

# Tests de la fonction recette_boulangerie
print(recette_boulangerie(50, 30, 44))
print(recette_boulangerie(45, 87, 12))
print(recette_boulangerie(0, 12, 78))