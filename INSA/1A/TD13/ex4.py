from random import randint
def est_pair(liste):
    i=0
    r=True
    while i < len(liste) and liste[i] % 2 == 0:
        i += 1
    if i != len(liste):
        r = False
    return r
    
def elimine_impair(l):
    for i in range(len(l)):
        if l[i] % 2 == 1:
            l[i]=0

def creer_liste_aleatoire(n, a, b):
    l=[]
    for _ in range(n):
        l.append(randint(a,b))
    return l

def bataille(l):
    for i in range(len(l)-2, -1, -1):
        if l[i] % 2 == 0 and l[i+1] % 2 == 1:
            l[i+1]=l[i]

def bataille_v2(l):
    r = False
    for i in range(len(l)-2, -1, -1):
        if l[i] % 2 == 0 and l[i+1] % 2 == 1:
            l[i+1]=l[i]
            r = True
    return r

def guerre(l):
    while bataille_v2(l): pass

l=creer_liste_aleatoire(10, 0, 10)
print(l)
l2=[2,4,1,6,5,7,9,2,3,1,2]
guerre(l)
print(l)