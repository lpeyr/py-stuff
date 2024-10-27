# Questions 1, 2, 3, 4
a = 13
b = 4
resultat = a // b
reste = a % b
print(resultat)
print(reste)

# Question 5, 6, 7
def obtenir_resultat_reste(a, b):
    return (a // b, a % b)

# Tests de la fonction obtenir_resultat_reste
print(obtenir_resultat_reste(26, 6))
print(obtenir_resultat_reste(5, 0)) # On obtient une erreur