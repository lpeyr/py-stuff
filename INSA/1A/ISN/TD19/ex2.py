from random import randint
def fusion_triee(l1, l2):
    i = 0
    j = 0
    triee = []
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            triee.append(l1[i])
            i += 1
        else:
            triee.append(l2[j])
            j += 1
    for k in range(i, len(l1)):
        triee.append(l1[k])
    for k in range(j, len(l2)):
        triee.append(l2[k])
    return triee


def tri_fusion(l, debut, fin):
    res = [l[debut]]
    if fin - debut > 1:
        milieu = (fin + debut) // 2
        res = fusion_triee(tri_fusion(l, debut, milieu), tri_fusion(l, milieu, fin))
    return res


def tri(l):
    return tri_fusion(l, 0, len(l))

def liste_aleatoire(n):
    return [randint(0, 999) for _ in range(n)]

for _ in range(10):
    print(tri(liste_aleatoire(10)))
