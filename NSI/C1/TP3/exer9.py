def syracuse(n):
    l = [] # Créer une liste
    for i in range(100): # OIbtenir les 100 premiers nombres de la suite de Syracuse
        if n % 2 == 0: # Si n est pair
            n /= 2
        else: # Sinon
            n = n * 3 + 1
        l.append(n)
    return l

# Tests
print(f"n = 5 \n\n {syracuse(5)}\n\n")
print(f"n = 6 \n\n {syracuse(6)}\n\n")