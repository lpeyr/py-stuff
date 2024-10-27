def dichotomie(tab, x):
    debut = 0
    fin = len(tab)-1
    while debut <= fin:
        m = (debut+fin)//2
        if tab[m] == x:
            return True
        elif x > tab[m]:
            debut = m+1
        else:
            fin = m-1
    return False


print(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 30, 31, 33], 28))
print(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 30, 31, 33], 27))
