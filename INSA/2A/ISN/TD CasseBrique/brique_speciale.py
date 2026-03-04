from Brique import *


class BriqueSpeciale(Brique):
    def __init__(
        self,
        couleur,
        x_position,
        y_position,
        largeur,
        hauteur,
        solidite,
        points,
        effet_special,
    ):
        super().__init__(
            couleur, x_position, y_position, largeur, hauteur, solidite, points
        )
        self.effet_special = effet_special

    def is_hit(self, ball_coords):
        limits = self.get_limits()
        if (
            ball_coords[0] >= limits[0]
            and ball_coords[0] <= limits[2]
            and ball_coords[1] >= limits[1]
            and ball_coords[1] <= limits[3]
        ):
            self.solidite -= 1
            print("Brique touchée : " + str(self))
            return (
                self.points * 2 if self.effet_special == "Double Score" else self.points
            )
        return 0
