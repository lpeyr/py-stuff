def fusion(l1, l2):
    i = 0
    j = 0
    res = []
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            res.append(l1[i])
            i += 1
        else:
            res.append(l2[j])
            j += 1

    for k in range(i, len(l1)):
        res.append(l1[k])
    for k in range(j, len(l2)):
        res.append(l2[k])
    return res


def tri_fusion(l, d, f):
    res = [l[d]]
    if f > d:
        m = (d + f) // 2
        l1 = tri_fusion(l, d, m)
        l2 = tri_fusion(l, m + 1, f)
        res = fusion(l1, l2)
    return res


def tri(l):
    return tri_fusion(l, 0, len(l) - 1)


print(tri([5, 3, 2, 4, 1, 6]))
