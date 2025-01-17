def tri(l1, l2):
    liste = []
    i = 0
    j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            liste.append(l1[i])
            i += 1
        else:
            liste.append(l2[j])
            j += 1
    while i < len(l1):
        i += 1
        liste.append(l1[i])

    while j < len(l2):
        liste.append(l2[j])
        j += 1
    return liste


print(tri([2, 4, 5], [3, 8, 9]))
