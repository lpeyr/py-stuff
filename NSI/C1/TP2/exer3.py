def test(n):
    if n % 3 == 0:
        resultat = True
    else:
        resultat = False
    return resultat

# Tests de la fonction test()
print(f"n = 12: {test(12)}")
print(f"n = 17: {test(17)}")
print(f"n = 9: {test(9)}")
print(f"n = 125: {test(125)}")