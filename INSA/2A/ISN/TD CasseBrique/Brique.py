class Brique:
    def __init__(
        self, couleur, x_position, y_position, largeur, hauteur, solidite, points
    ):
        self.couleur = couleur
        self.solidite = solidite
        self.points = points
        self.x_position = x_position
        self.y_position = y_position
        self.largeur = largeur
        self.hauteur = hauteur

    def __str__(self):
        return f"Brique {self.couleur}, x: {self.x_position}, y: {self.y_position}, solidite: {self.solidite}"

    def get_limits(self):
        return (
            self.x_position,
            self.y_position,
            self.x_position + self.largeur,
            self.y_position + self.hauteur,
        )

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
            return self.points
        return 0
