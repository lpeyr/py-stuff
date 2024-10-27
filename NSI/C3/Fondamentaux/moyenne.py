def moyenne(liste):
    M = 0
    for i in liste:
        M += i
    return M / len(liste)


print(moyenne([6, 18, 2]))
