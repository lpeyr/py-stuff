def min(L):
    m = L[0]
    for i in L:
        if i < m:
            m = i

    return m


print(min([3, 1, 12, 0, 10, 12, 2]))
print(min([3, 4, 12, 6, 10, 12, 2]))
