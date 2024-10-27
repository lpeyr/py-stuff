import random

def lancer():
    return random.randint(1, 6)

def obtenir_six():
    n, c = 0, 0
    while n != 6:
        n = lancer()
        c += 1

    return c

# Tests de la fonction obtenir_six()
print(obtenir_six())