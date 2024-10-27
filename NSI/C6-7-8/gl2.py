somme = 60
billets = [7, 20, 50, 100]
pieces = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2]
systeme = pieces + billets
reste_a_rendre = somme
liste_pieces_rendues = []
liste_billets_rendus = []
i = len(systeme)-1
while reste_a_rendre > 0:
    piece = systeme[i]
    if reste_a_rendre >= piece:
        if i > len(pieces):  # si c'est un billet
            liste_billets_rendus.append(piece)
        else:
            liste_pieces_rendues.append(piece)
        reste_a_rendre = reste_a_rendre - piece
    else:
        i = i-1

print(liste_billets_rendus)
print(liste_pieces_rendues)
