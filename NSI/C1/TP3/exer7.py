def somme(n):
    S = 0
    for i in range(1, n+1):
        S += i
    return S

# Tests de la fonction somme()
print(somme(100))