def maxi(L):
    n, index = L[0], 0
    for i in range(len(L)):
        if L[i] >= n:
            n = L[i]
            index = i

    return n, index


def maxi2(L):
    n, index = L[0], 0
    for i in range(len(L)):
        if L[i] > n:
            n = L[i]
            index = i

    return n, index


print(maxi([3, 4, 12, 6, 10, 12, 2]))
print(maxi2([3, 4, 12, 6, 10, 12, 2]))
