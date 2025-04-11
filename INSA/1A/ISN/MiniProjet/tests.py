from main import detecte_coordonnees_combinaison


def assert_test(result, expected, description):
    print(f"{description} : {'✅' if result == expected else '❌'}")
    if result != expected:
        print(f"  Attendu : {expected}")
        print(f"  Obtenu  : {result}")


def test_detecte_coordonnees_combinaison():
    """
    Teste la fonction detecte_coordonnees_combinaison avec différents cas :
    - Combinaisons horizontales
    - Combinaisons verticales
    - Absence de combinaison
    - Combinaisons au début ou fin de ligne/colonne
    - Grille avec aucune combinaison possible
    """

    grille = [
        [0, 1, 3, 3, 0],
        [1, 1, 1, 3, 2],
        [0, 0, 2, 0, 1],
        [1, 1, 2, 3, 0],
        [0, 1, 0, 3, 0],
    ]

    # Test 1 : combinaison horizontale au milieu (valeurs 1 sur la ligne 1)
    assert_test(
        detecte_coordonnees_combinaison(grille, (1, 1)),
        [(1, 0), (1, 1), (1, 2)],
        "Combinaison horizontale de 1 sur la ligne 1",
    )

    # Test 2 : pas de combinaison autour de (2, 2)
    assert_test(
        detecte_coordonnees_combinaison(grille, (2, 2)),
        [],
        "Aucune combinaison pour la case (2, 2)",
    )

    # Test 3 : combinaison horizontale en fin de ligne
    grille2 = [
        [0, 0, 3, 3, 3],
        [1, 2, 1, 2, 1],
    ]
    assert_test(
        detecte_coordonnees_combinaison(grille2, (0, 4)),
        [(0, 2), (0, 3), (0, 4)],
        "Combinaison horizontale en fin de ligne",
    )

    # Test 4 : combinaison horizontale en début de ligne
    grille3 = [
        [4, 4, 4, 2],
        [1, 2, 3, 4],
    ]
    assert_test(
        detecte_coordonnees_combinaison(grille3, (0, 0)),
        [(0, 0), (0, 1), (0, 2)],
        "Combinaison horizontale au début de ligne",
    )

    # Test 5 : combinaison verticale au début de colonne
    grille4 = [
        [2, 1],
        [2, 0],
        [2, 3],
        [0, 3],
    ]
    assert_test(
        detecte_coordonnees_combinaison(grille4, (0, 0)),
        [(0, 0), (1, 0), (2, 0)],
        "Combinaison verticale au début de la colonne",
    )

    # Test 6 : aucune combinaison possible
    grille5 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert_test(
        detecte_coordonnees_combinaison(grille5, (1, 1)),
        [],
        "Grille sans aucune combinaison",
    )


test_detecte_coordonnees_combinaison()
