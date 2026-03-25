from Ville import *
from Graphe import *


v = Ville("Lyon", 45.69214056550071, 4.812714357262654, 176)
v2 = Ville("Paris", 48.85661, 2.35222, 48)


g = Graphe(None)
g.ajouter_ville(v)
g.ajouter_ville(v2)
print(g.distance_moy())