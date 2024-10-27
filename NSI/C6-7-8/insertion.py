def triInsertion(tab):
    for i in range(1, len(tab)):
        j = i
        while j > 0 and tab[j-1] > tab[j]:
            tab[j], tab[j-1] = tab[j-1], tab[j]
            j = j-1

    return tab
