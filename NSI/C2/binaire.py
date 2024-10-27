def binaire8(n):
    B = ""
    while n > 0:
        r = n % 2
        B = str(r) + B
        n = n // 2

    if len(B) > 8:
        return "Erreur : Ce nombre ne peut pas être codé sur 8 bits."
    else:
        for i in range(0, 8-len(B)):
            B = "0" + B

    return B


print(binaire8(14))
print(binaire8(123))
print(binaire8(78))
print(binaire8(312))
