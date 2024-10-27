def insere(a, tab):
    pos = 0
    for i in range(1, len(tab)):
        if tab[i-1] < a and tab[i] > a:
            pos = i
    liste = []
    for j in range(pos):
        liste.append(tab[j])
    liste.append(a)
    for k in range(pos, len(tab)):
        liste.append(tab[k])
    return liste


print(insere(3, [1, 2, 4, 5]))
