def ins(e, liste):
    i = 0
    while i < len(liste) and e != liste[i]:
        i += 1
    return not (i == len(liste))


ma_chaine = "mercredi"
voyelles = ["a", "e", "i", "o", "u", "y"]
compteur = 0

for lettre in ma_chaine:
    if ins(lettre, voyelles):
        compteur += 1


print(f"La chaine de caracteres {ma_chaine} contient {compteur} voyelles")
