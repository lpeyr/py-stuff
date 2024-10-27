import math

def cube(a):
    C = a**3
    return C

# Tests de la fonction cube
print(cube(3))
print(cube(2))
print(cube(10))

# Question 2

def volume_cylindre(h, r):
    return math.pi * r ** 2 * h

# Tests de la fonction volume_cylindre
print(volume_cylindre(2, 3))
print(volume_cylindre(3, 7))