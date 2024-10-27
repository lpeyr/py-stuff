def multiplication(n1, n2):
    S = 0
    if n1 > 0:  # si n1 est positif
        for i in range(n1):
            S += n2
    else:
        for i in range(-n1):  # -n1 est la valeur absolue
            S -= n2

    return S


# tests
print(multiplication(3, 5))
print(multiplication(-4, -8))
print(multiplication(-2, 6))
print(multiplication(-2, 0))
