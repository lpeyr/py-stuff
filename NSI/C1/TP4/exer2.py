def compte():
    S = 1200
    N = 0
    while S <= 1500:
        S *= 1.04
        N += 1
    return N


# Tests de la fonction
print(compte())