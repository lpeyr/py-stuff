def calcul_impot(revenu, nb_parts):
    """
    Entrées :
        revenu   (int) : Le revenu du ménage
        nb_parts (int) : Nombre de parts
    Retour : L'impot du sur le revenu
    """
    ratio = revenu / nb_parts
    if ratio < 20000:
        impot = revenu * 0.125 - 50 * nb_parts
    elif ratio < 30000:
        impot = revenu * 0.25 - 100 * nb_parts
    else:
        impot = revenu * 0.5 - 200 * nb_parts

    return impot


def afficher_foyer(revenus, parts, impots):
    """
    Entrées :
        revenus (list[int]) : les revenus des foyers
        parts   (list[int]) : les parts des foyers
        impots  (list[int]) : les impots payées par le foyer
    Retour :
        (None) Affiche les revenus des foyers.
    """
    for i in range(len(revenus)):
        print(
            f"Avec un revenu de {revenus[i]}€ et {parts[i]} parts, un foyer paiera {impots[i]}€."
        )


def saisir_un_foyer():
    rev, parts = int(input("Entrez un revenu\n>")), int(
        input("Entrez le nombre de parts\n>")
    )
    while rev != -1 and (rev < 0 or parts < 0):
        rev, parts = int(input("Entrez un revenu")), int(
            input("Entrez le nombre de parts")
        )

    return rev, parts


# Tests
print(f"revenu : 25000 - parts : 2, l’impot vaut : {calcul_impot(25000,2)}")
print(f"revenu : 80000 - parts : 3, l’impot vaut : {calcul_impot(80000,3)}")
print(f"revenu : 130000 - parts : 4, l’impot vaut : {calcul_impot(130000,4)}")

les_revenus = [25000, 80000, 130000, 75000, 500, 30000]
les_parts = [2, 3, 4, 3, 1, 5]
les_impots = []

for i in range(len(les_revenus)):
    les_impots.append(calcul_impot(les_revenus[i], les_parts[i]))

afficher_foyer(les_revenus, les_parts, les_impots)

rev, parts = saisir_un_foyer()
while rev != -1:
    les_revenus.append(rev)
    les_parts.append(parts)
    rev, parts = saisir_un_foyer()
