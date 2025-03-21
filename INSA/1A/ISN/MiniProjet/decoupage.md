# Découpage fonctionnel
## Types de bonbons
- 0 : Rouge
- 1 : Bleu
- 2 : Vert
- 3 : Jaune
## Fonctions
### Fonctions à coder
``` python
def init_grille(x, y) -> list[list]:
  """
  Initialise une grille de taille x * y.
  Chaque case est remplie aléatoirement avec un bombon (fonction random.randint() entre 0 et 3)
  Sortie :
    - grille : une liste 2D avec des valeurs aléatoires.
  """

def echanger_bombon(grille, b1, b2) -> None:
  """
  Echange le bonbon b1 et b2 dans la grille.
  Entrées :
    - grille : grille où échanger les bonbons
    - b1 : objet Tuple (x1, y1) représentant les coordonées du premier bonbon
    - b2 : objet Tuple (x2, y2) représentant les coordonées du second bonbon
  Sortie : None
  """  


  
def retirer_bonbon(grille, b1, b2):
  """
  Vérifie si les bonbons entre le bonbon 1 et bonbon 2 inclu forment une combinaison. On utilisera une boucle while.
  Entrées :
    - grille : la grille du jeu
    - b1 : objet Tuple (x1, y1) représentant les coordonées du premier bonbon
    - b2 : objet Tuple (x2, y2) représentant les coordonées du second bonbon
  Sortie : None
"""

def obtenir_bonbons_ligne_dessus(grille, b1, b2)
  """
  Obtient les bonbons de la ligne du dessus entre les coordonnées du bonbon 1 et 2.
    Entrées :
    - grille : la grille du jeu
    - b1 : objet Tuple (x1, y1) représentant les coordonées du premier bonbon
    - b2 : objet Tuple (x2, y2) représentant les coordonées du second bonbon
  Sortie : Une liste 2D de bonbons list[list[Tuple(x,y)]]
  """

def decaler_bonbon_ligne(grille, ligne, b1, b2)
  """
  Décale les bonbons entre b1 et b2 qui sont situés au-dessus de la ligne _ligne_. Cette fonction est appelée après avoir supprimé les bonbons entre b1 et b2.
  Entrées :
    - grille : la grille du jeu
    - ligne : la ligne où il n'y a plus de bonbons
    - b1 : objet Tuple (x1, y1) représentant les coordonées du premier bonbon
    - b2 : objet Tuple (x2, y2) représentant les coordonées du second bonbon
  Sortie : None
  """

```

### Fonctions Imposées
``` python
def detecte_coordonnees_combinaison(grille, bonbon):
"""
Vérifie si les bonbons sur la ligne du bonbon forment une combinaison. On utilisera une boucle while.
Entrées :
  - grille : la grille du jeu
  - bonbon : Tuple(x,y) représentant les cordonnées du bonbon
Sortie : Une liste de bonbons list[Tuple(x,y)]
"""

# import matplotlib.pyplot as plt
def affichage_grille(grille, nb_type_bonbons):
  """
  Affiche la grille de jeu "grille" contenant au
  maximum "nb_type_bonbons" couleurs de bonbons différentes.
  """

def test_detecte_coordonnees_combinaison():
  """
  Test la fonction detecte_coordonnees_combinaison(grille, i, j).
  Pour chaque cas de test, affiche True si le test passe,
  False sinon
  """
```