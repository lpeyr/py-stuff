def pgcd(a, b):
    r = a % b
    while r != 0:
        a = b
        b = r
        r = a % b
    return b


print(pgcd(25, 15))
