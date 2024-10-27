def dicho(tab, x):
    res = False
    deb = 0
    fin = len(tab)-1
    while res == False and deb <= fin:
        milieu = (deb+fin)//2
        if tab[milieu] == x:
            res = True
        elif x > tab[milieu]:
            deb = milieu+1
        else:
            fin = milieu-1
    return res
