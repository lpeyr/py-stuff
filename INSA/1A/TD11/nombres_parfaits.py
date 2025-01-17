from math import sqrt


def est_divisible(n, p):
    """
    Renvoie vrai si et seulement si n est divisible par p.

    Parametres
    ----------
    n, p : deux entiers

    Retour
    -------
    True ou False
    """
    return n % p == 0


def get_diviseurs_stricts(n):
    """
    Renvoie la liste des diviseurs stricts de n.
    Parametres
    ----------
    n : un entier

    Retour
    -------
    liste des diviseurs stricts de n (liste d'entiers).
    """
    divs = []
    for p in range(1, n // 2 + 1):
        if est_divisible(n, p):
            divs.append(p)
    return divs


def est_parfait(n):
    """Renvoie vrai si et seulement si n est un nombre parfait.
    Parametres
    ----------
    n : un entier

    Retour
    -------
    Vrai ou Faux
    """
    s = 0
    for nb in get_diviseurs_stricts(n):
        s += nb

    return s == n


def parfait_range(a, b):
    """
    Entrées :
        a (int) : Nombre de départ de l'intervalle
        b (int) : Nombre maximal de l'intervalle
    Retourne :
        La liste des nombres parfaits dans l'intervalle [a, b]
    """
    parfaits = []
    for p in range(a, b + 1):
        if est_parfait(p):
            parfaits.append(p)
    return parfaits


### Programme principal
# Test de est_divisible
print(est_divisible(10, 2))  # True
print(est_divisible(10, 3))  # False
# print(est_divisible(10, 0)) # Erreur

# Test de get_diviseurs_stricts

print(get_diviseurs_stricts(10))  # [1, 2, 5]
print(get_diviseurs_stricts(3))  # [1]


# Test de est_parfait

print(est_parfait(6))  # True
print(est_parfait(5))  # False

parfait_range(
    2, 10
)  # \sum_{k=a}^b\left\lfloor \frac{k}{2} \right\rfloor\newline=\=\frac{b(b+1)}{4}-\frac{a(a+1)}{4}=\frac{b²+b-a²-a}{4}=\frac{(b-a)(b+a+1)}{4}
