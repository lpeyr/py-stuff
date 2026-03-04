from Brique import *


class CasseBriques:
    def __init__(self):
        self.briques = []
        self.score = 0

    def ajouter_brique(self, brique):
        self.briques.append(brique)

    def afficher_briques(self):
        for b in self.briques:
            print(b)

    def impact_brique(self, x, y):
        for brique in self.briques:
            self.score += brique.is_hit((x, y))
            if brique.solidite == 0:
                self.briques.remove(brique)

    def afficher_score(self):
        print("Score actuel" + str(self.score))

    def construire_rangee_briques(
        self,
        couleur,
        solidite,
        points,
        nombre_briques,
        espace_entre_briques=5,
        numero_ligne=1,
    ):
        """
        Construit une rangée de briques avec les caractéristiques spécifiées et les ajoute au jeu.

        Args:
            couleur (str): La couleur des briques.
            solidite (int): La solidité des briques.
            points (int): Le nombre de points attribués lorsque la balle détruit la brique.
            nombre_briques (int): Le nombre de briques dans la rangée.
            espace_entre_briques (int, optional): L'espace horizontal entre les briques. Par défaut, 5.
            numero_ligne (int, optional): Le numéro de la ligne où placer les briques. Par défaut, 1.
        """
        # Ajoute une rangée de briques horizontalement
        largeur_brique = 50  # Remplacez par la largeur souhaitée
        hauteur_brique = 25  # Remplacez par la hauteur souhaitée
        position_y = espace_entre_briques + (hauteur_brique + espace_entre_briques) * (
            numero_ligne - 1
        )  # Ajuste la position en y de la rangée
        position_x = espace_entre_briques

        for _ in range(nombre_briques):
            brique = Brique(
                couleur,
                position_x,
                position_y,
                largeur_brique,
                hauteur_brique,
                solidite,
                points,
            )
            self.ajouter_brique(brique)
            position_x += largeur_brique + espace_entre_briques
