def nb_or(n):
    u = 1
    for _ in range(1, n + 1):
        u = 1 + 1 / u
    return u


print(nb_or(1000))
