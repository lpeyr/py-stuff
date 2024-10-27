import random

### Variables
nbr_lancer = 100000

### Fonctions
# Générer un nombre entre 1 et 6
def lancer():
    return random.randint(1, 6)

# Faire 10 lancers et additioner les sommes
def dix_lancer():
    R = 0
    for i in range(10):
        R += lancer()
    return R

def calculer_frequence(nbr_iterations):
    freqs = [0, 0, 0, 0, 0, 0] # la fréquence des 1 est stocké dans i = 0, celle de n dans i = n - 1
    for j in range(nbr_iterations):
        R = lancer()
        freqs[R - 1] += 1 # Obtenir le nombre de fois où le nombre apparaît

    for k in range(len(freqs)):
        freqs[k] /= nbr_iterations # Calculer la fréquence à partir du nombre de fois où le nombre apparaît

    return freqs

### Tests
# Tests de la fonction dix_lancer()
print(dix_lancer())

# Tests de la fonction calculer_frequence()
print(f"\n\n1/6 = {1/6}\n\n")

F = calculer_frequence(nbr_lancer)
print(F, "\n") # Afficher la liste au format brut
for x in range(len(F)):
    print(f"Fréquence des {x+1} : {F[x]}") # Afficher la liste formatée