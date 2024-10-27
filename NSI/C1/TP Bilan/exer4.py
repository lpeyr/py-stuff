def somme_cares():
    '''
    Fait la somme des carrés jusqu'à ce que cette somme dépasse 5000.
    '''
    S, i = 0, 0 # S => somme, i => compteur pour "simuler" boucle for

    while S <= 5000: # Tant que la somme des carrés inférieure ou égale à 5000
        i += 1 # Incrémenter le compteur
        S += i ** 2 # Prendre le carré

    return i # Retourne le premier nombre  pour lequel la somme dépasse 5000

# Tests de la fonction
print(somme_cares()) # 25, la somme dépasse 5000