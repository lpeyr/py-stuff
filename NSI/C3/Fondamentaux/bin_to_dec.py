def bin_to_dec(L):
    d = 0
    for i in range(len(L)):
        if L[i] == 1:
            d += 2**(len(L)-i-1)

    return d


print(bin_to_dec([0, 1]))
print(bin_to_dec([1, 1]))
print(bin_to_dec([1, 1, 1]))
