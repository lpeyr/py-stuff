def recherche(el, L):
    index = -1
    for i in range(len(L)):
        if el == L[i]:
            index = i
            return index

    return index


print(recherche(3, [2, 4, 5]))
print(recherche(5, [2, 4, 5]))
print(recherche(2, [2, 4, 2, 6, 2, 5]))
