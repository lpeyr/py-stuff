def triSelection(tab):
    for i in range(len(tab)):
        min = i
        for j in range(i+1, len(tab)):
            if tab[min] > tab[j]:
                min = j
        tab[i], tab[min] = tab[min], tab[i]
    return tab
