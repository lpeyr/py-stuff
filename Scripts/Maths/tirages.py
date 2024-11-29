from random import randint

def tirage(n):
    combinaisons = []
    nb_g=0
    for i in range(n):
        lettres = ["A","B","C","D","E","F", "G", "H"]
        i_rnd = randint(0, len(lettres)-1)
        lettre1 = lettres[i_rnd]
        del lettres[i_rnd]
        j_rnd= randint(0, len(lettres)-1)
        lettre2 = lettres[j_rnd]
        del lettres[j_rnd]
        combinaisons.append((lettre1, lettre2))
    for c in combinaisons:
        if gagnant(c):
            nb_g+=1
    return nb_g/n
    
def gagnant(el):
    n_v = 0
    n_c = 0
    for e in el:
        if e == "A" or e == "E":
            n_v +=1
        else:
            n_c +=1
    return n_v==1 and n_c==1
    

print(3/7)
print(tirage(10000000))