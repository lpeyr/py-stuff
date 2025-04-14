
# Rapport du mini-projet Candy Crush Lite

## I. Quel niveau de difficulté avez-vous implémenté ?

Dans notre projet **Candy Crush Lite**, nous avons implémenté le **niveau de difficulté 3**, c’est-à-dire la capacité à détecter des **combinaisons** non seulement entre **des bonbons adjacents directs**, mais également entre **les voisins des voisins**.  
Cela permet de gérer des suppressions de bonbons plus complexes et d'offrir une meilleure dynamique de jeu que les niveaux basiques.

---

## II. Décrivez les règles de votre jeu en quelques lignes

Le jeu **Candy Crush Lite** est une version simplifiée de Candy Crush, jouable entièrement dans le **terminal**. Le but est d’aligner des bonbons de la même couleur pour les faire disparaître et marquer des points. Voici les règles principales :

- Le plateau de jeu est une **grille de bonbons** générée aléatoirement.
- Le joueur sélectionne deux cases à échanger.
- Si l’échange forme une **ligne ou colonne d’au moins 3 bonbons identiques**, ces derniers sont supprimés.
- Les bonbons au-dessus tombent pour remplir les vides, et de nouveaux bonbons apparaissent en haut.
- Le jeu permet des combinaisons avancées : il peut détecter et supprimer **les combinaisons indirectes** (ex. en chaîne, ou via des voisins éloignés).
- Le jeu continue jusqu’à ce que le joueur décide d’arrêter.

---

## III. Écrivez l’algorithme principal de votre jeu en français

L’algorithme principal se trouve dans la fonction `main()`. Il gère le déroulement du jeu, l’interaction utilisateur et les appels aux différentes fonctionnalités.

### 🔁 Algorithme principal du jeu (`main()`)

```
1. Charger les articles depuis le fichier CSV en utilisant la fonction `charger_articles`.

2. Tant que l’utilisateur ne choisit pas de quitter :
    a. Afficher un menu avec plusieurs options :
        - Afficher la liste des articles
        - Ajouter un article
        - Supprimer un article
        - Rechercher un article
        - Enregistrer les modifications
        - Trier les articles par prix
        - Quitter

    b. Lire le choix de l’utilisateur.

    c. En fonction du choix, exécuter l'action correspondante :
        - Affichage, ajout, suppression ou recherche d’articles
        - Sauvegarde ou tri des articles
        - Si le choix est invalide, afficher un message d'erreur

3. Lorsque l’utilisateur choisit de quitter :
    a. Afficher un message de fin
    b. Sortir de la boucle et arrêter le programme
```

---
