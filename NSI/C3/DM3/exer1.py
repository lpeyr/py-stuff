eleves = ['lisa', 'marc', 'arthur', 'talia',
          'ines', 'bilal', 'gael', 'theo', 'lea']
notes = [1, 8, 16, 14, 18, 9, 18, 8, 6]


def meilleuresNotes(eleves, notes):
    meilleure = 0
    noms = []
    # première boucle, obtenir la meilleure note
    for note in notes:
        if note > meilleure:
            meilleure = note

    # deuxième boucle, obtenir les indices de ces notes
    i = 0
    for note in notes:
        if note == meilleure:
            noms.append(eleves[i])
        i += 1

    return (meilleure, noms)


print(meilleuresNotes(eleves, notes))
