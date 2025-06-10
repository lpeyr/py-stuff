import matplotlib.pyplot as plt
import numpy as np

def trace(a,b):
    x0,y0 = a
    x1,y1 = b
    plt.plot([x0,x1], [y0,y1])

def calcul_pointe(deb, fin):
    """
    Entrées: les coordonnées (numpyarray de dimension 2)
    des extrémités d’un segment
    Sortie: les coordonnées de la pointe correspondante
    """
    l = np.linalg.norm(fin - deb)
    rotation = np.array([[0,-1],[1,0]])
    vecteur_unitaire = (fin - deb)/l
    perpendiculaire = np.dot(rotation,vecteur_unitaire)
    milieu = (fin + deb)/2
    a2 = milieu + perpendiculaire*(np.sqrt(3)*l/6)
    return a2

def flocon(n):
    plt.axis("equal")
    plt.axis("off")
    a = np.array([0, 0])
    b = np.array([1, 0])
    c = np.array([0.5, np.sqrt(3)/2])
    koch(n,a,c)
    koch(n,c,b)
    koch(n,b,a)
    plt.show()

def koch(n, deb, fin):
    if n == 0:
        trace(deb, fin)
    else:
        t1=deb+ (fin-deb)*1/3
        t2=deb+ (fin-deb)*2/3
        a2=calcul_pointe(deb, fin)
        koch(n-1, deb, t1)
        koch(n-1, t1, a2)
        koch(n-1, a2, t2)
        koch(n-1, t2, fin)

flocon(5)