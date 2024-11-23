def init_automate(n):
    liste = []
    for i in range(n):
        if i == n // 2:
            liste.append(0)
        else:
            liste.append(1)
    return liste


print(init_automate(10))
print(init_automate(11))
print(init_automate(20))
print(init_automate(23))
