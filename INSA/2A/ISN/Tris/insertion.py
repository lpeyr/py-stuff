def pos(l, p, x):
    j = 0
    while j < p and l[j] < x:
        j += 1
    return j


def insertion_sort(l, i):
    i_insert = pos(l, i, l[i])
    tmp = l[i]
    for k in range(i, i_insert, -1):
        l[k] = l[k - 1]
    l[i_insert] = tmp


def tri(l):
    for i in range(len(l)):
        insertion_sort(l, i)
    return l


print(tri([5, 3, 2, 4, 1, 6]))
