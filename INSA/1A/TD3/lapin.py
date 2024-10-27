from math import sqrt
from random import randint


def calcul_d(c_l, c_j):
    return sqrt((c_l[0]-c_j[0])**2 + (c_l[1]-c_j[1])**2)

n = 10

c_lapin = (randint(0, n),randint(0, n))
c_jou = [0, 0]

d = calcul_d(c_lapin, c_jou)

while d != 0:
    c_jou[0]= int(input("Coordonnée x : \n> "))
    c_jou[1]= int(input("Coordonnée y : \n> "))
    d = calcul_d(c_lapin, c_jou)
    print(d)
print(f"Bravo, tu as trouvé le lapin ({c_lapin[0]}, {c_lapin[1]})")