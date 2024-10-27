import math

def plat(n):
    t = 0
    S = 0
    while (n != S and S < n):
        S = t*t
        if S == n:
            break
        elif S < n:
            t += 1
        else:
            t -= 1


    return t


def cube(n):
    t = 0
    S = 0
    while (n != S and S < n):
        S = t*t*t
        if S == n:
            break
        elif S < n:
            t += 1
        else:
            t -= 1


    return t

print(plat(17))
print(cube(17))