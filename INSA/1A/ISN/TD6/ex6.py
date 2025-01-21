def cherche_min(liste, i_pivot):
    min = liste[i_pivot]
    i_min = i_pivot
    for i in range(i_pivot, len(liste)):
        if liste[i] < min:
            min = liste[i]
            i_min = i
    return i_min


def tri_selection(liste):
    for i_pivot in range(len(liste)):
        i_min = cherche_min(liste, i_pivot)
        if liste[i_pivot] > liste[i_min]:
            liste[i_pivot], liste[i_min] = liste[i_min], liste[i_pivot]

    return liste


print(tri_selection([3, 2, 1]))
