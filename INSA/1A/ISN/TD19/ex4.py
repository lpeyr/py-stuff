def affiche(n, positions):
    for pos in positions:
        print("." * (pos) + "X" + "." * (n - pos - 1))
    for _ in range(n - len(positions)):
        print("." * n)


def en_prise(x1, y1, x2, y2):
    return x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2)

def est_libre(x1, y1, positions):
    res = True
    i = 0
    while res and i < len(positions):
        if i != x1 or positions[i] != y1:
            res = not en_prise(x1, y1, i, positions[i])
        i += 1

    return res

def place_dames(n: int, positions: list):
    if len(positions) == n:
        affiche(n, positions)
        print()
        return 1

    i = 0
    x = len(positions)
    for y in range(n):
        if est_libre(x, y, positions):
            i += place_dames(n, positions + [y])
    return i

n = 8
solutions = place_dames(n, [])
print(f"Nombre total de solutions pour un échiquier {n}×{n} : {solutions}")
