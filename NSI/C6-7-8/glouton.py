def RenduDeMonaie(pieces, k):
    res = 0
    p = 0
    while k != 0 and p < len(pieces):
        if pieces[p] <= k:
            res = res + 1
            k = k - pieces[p]
        else:
            p = p + 1
    return res
