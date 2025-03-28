# Découpage fonctionnel Candy Crush

## Types de bonbons

- -1 : Case vide (ne sera pas utilisée dans le jeu final)
- 0 : 🍭
- 1 : 🍡
- 2 : 🍬
- 3 : 🍫

## Fonctions

### Fonctions à coder

```python
def init_grille(x, y, max=3) -> list[list]:
  """
  Initialise une grille de taille x * y.
  Chaque case est remplie aléatoirement avec un bonbon (fonction random.randint() entre 0 et 3), tout en s'assurant qu'il n'y a pas de combinaisons possibles.
  Entrées
    - max : Le nombre de bonbons ajdaçants max pour faire une combinaison.
  Sortie :
    - grille : une liste 2D avec des valeurs aléatoires.
  """

def echanger_bonbon(grille, b1, b2) -> None:
  """
  Echange le bonbon b1 et b2 dans la grille.
  Entrées :
    - grille : grille où échanger les bonbons
    - b1 : objet Tuple (x1, y1) représentant les coordonées du premier bonbon
    - b2 : objet Tuple (x2, y2) représentant les coordonées du second bonbon
  Sortie : None
  """

def retirer_bonbon(grille, combiniaison):
  """
  Retire les bonbons entre b1 et b2 en remplaçant leur valeurs par des -1.
  Entrées :
    - grille : la grille du jeu
    - b1 : objet Tuple (x1, y1) représentant les coordonées du premier bonbon
    - b2 : objet Tuple (x2, y2) représentant les coordonées du second bonbon
  Sortie : None
  """

def obtenir_bonbons_ligne_dessus(combinaison)
  """
  Obtient les coordonnées des bonbons de la ligne du dessus entre les coordonnées du bonbon 1 et 2.
  Entrées :
    - b1 : objet Tuple (x1, y1) représentant les coordonées du premier bonbon
    - b2 : objet Tuple (x2, y2) représentant les coordonées du second bonbon
  Sortie : Une liste 2D de bonbons list[list[Tuple(x,y)]]
  """

def decaler_bonbon(grille, ligne, b1, b2)
  """
  Décale les bonbons entre b1 et b2 qui sont situés au-dessus de la ligne _ligne_. Cette fonction est appelée après avoir supprimé les bonbons entre b1 et b2. Pour chaque ligne de 0 à ligne-1, la fonction prend les bonbons de la ligne entre les coordonnées pertinentes et les décalent vers le bas.
  Entrées :
    - grille : la grille du jeu
    - ligne : la ligne où il n'y a plus de bonbons
    - b1 : objet Tuple (x1, y1) représentant les coordonées du premier bonbon
    - b2 : objet Tuple (x2, y2) représentant les coordonées du second bonbon
  Sortie : None
  """

def inserer_bonbons(grille, b1, b2)
  """
  Insère des bonbons générés aléatoirements entre les coordonnées b1 et b2
  Entrées :
    - grille : la grille du jeu
    - b1 : objet Tuple (x1, y1) représentant les coordonées du premier bonbon
    - b2 : objet Tuple (x2, y2) représentant les coordonées du second bonbon
  Sortie : None
  """

def demander_utilisateur_bonbons()
  """
  Demander à l'utilisateur les deux bonbons qu'il souhaite échanger ; il faut soit que x1 = x2 ou y1 = y2.
  Retourne les coordonnées deux deux bonbons Tuple(Tuple(x1, y1), Tuple(x2, y2)
  """

def combinaison_possible(grille)
  """
  Renvoie True si des combinaisons sont possibles.
  """
```

### Fonctions Imposées

```python
def detecte_coordonnees_combinaison(grille, bonbon, max=3):
"""
Vérifie si les bonbons sur la ligne ou la colonne du bonbon forment une combinaison. On utilisera une boucle while.
Exemple d'Algorithme pour les lignes :
  CompteurCombi <- 0
  i <- 0
  x <- i
  BonbonCombi=BonbonLigne[0]
  Tant que CompteurCombi < max et que i < TailleLigne:
    Si BonbonCombi != Ligne[i]:
      CompteurCombi = 0
      x <- i
    Sinon:
      CompteurCombi += 1

Entrées :
  - grille : la grille du jeu
  - bonbon : Tuple(x,y) représentant les cordonnées du bonbon
  - max : Valeur de la taille maximale de la combinaison (ex: 3 en ligne et 3 en colonne)
Sortie : Une liste de bonbons list[Tuple(x,y)] qui contient les coordonnées des bonbons de la combinaison
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

## Programme principal

```python
grille = init_grille(5, 5)
while combinaison_possible(grille):

  (b1, b2) = demander_utilisateur_bonbons()

  echanger_bonbon(grille, b1, b2)
  combinaison = detecte_coordonnees_combinaison(grille, b1)

  while (len(combinaison) != 0): # Tant qu'il y a des combinaisons
    retirer_bonbon(grille, combinaison[0], combinaison[-1]) # On retire les bonbons de la combinaison
    decaler_bonbon(grille, combinaison[0], combinaison[-1]) # On décale les bonbons au dessus de la combinaison supprimée vers le bas
    inserer_bonbons(grille, (0, combinaison[0][1]), (0, combinaison[-1][1])) # On insère des bonbons aléatoires en haut de la grille
    affichage_grille(grille, 4) # On affiche la grille
    combinaison = detecte_coordonnees_combinaison(grille, b1) # On vérifie si il y a d'autres combinaisons
    if len(combinaison) == 0: # Si il n'y a plus de combinaisons
      combinaison = detecte_coordonnees_combinaison(grille, b2) # On vérifie si il y a d'autres combinaisons avec le deuxième bonbon

```


```python

grille = init_grille(5,5) # Création d'une grille 5x5

affichage_grille(grille)

# Démarage du Jeu

while combinaison_possible(grille):

    b1, b2 = demander_bonbon_utilisateur(grille)

    echanger_bonbon(grille, b1, b2) 

    # On recupère les combinaisons possible du b1 et du b2 -> cette liste de
    combinaison_b1 = detecte_coordonnee_combinaison(grille, b1) 
    combinaison_b2 = detexte_coordonnee_combinaison(grille, b2)


    combinaison_b1_b2 = combinaison_b1 + combinaison_b2
    if combinaison_b1_b2 != [] : # s'il y a des combinaisons
        for bonbon in combinaison_b1_b2 :
            grille[bonbon[0]][bonbon[1]] = -1 # on retire les bonbons qui font partie de la combinaison
        
        descendre_bonbon(grille)
        ajouter_bonbon(grille) # Ajouter des bonbons de sorte à ce qu'il n'y ait pas de nouvelles combinaisons

    affichage_grille(grille)



```
