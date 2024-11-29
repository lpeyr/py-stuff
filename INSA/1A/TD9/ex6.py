def si_motif(motif: str, chaine: str) -> bool:
    if len(chaine) < len(motif):
        return False
    if chaine[len(chaine) - len(motif) : len(chaine)] == motif:
        return True
    i = 0
    while i < len(chaine) - len(motif) and chaine[i : i + len(motif)] != motif:
        i += 1
    return i != len(chaine) - len(motif)


def nb_occurence(motif: str, chaine: str) -> int:
    c = 0
    for i in range(len(chaine) - len(motif) + 1):
        if chaine[i : i + len(motif)] == motif:
            c += 1
    return c


print(si_motif("aa", " s s aa"))
print(nb_occurence("aa", "aa aaa s s aa"))
