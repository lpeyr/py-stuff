import random # Importer le module random pour générer des nombres aléatoires

## Jeu du Juste prix
def main():
    print(f"{'-'*30}\nJuste Prix - Paramètres\n{'-'*30}\n\n") # Afficher un titre

    ## 1. Demander à l'utilisateur les paramètres
    try:
        min = int(input("Quel est le prix minimum ?\n> ")) # Demander le minimum que pourra prendre le nombre généré aléatoirement
        max = int(input("Quel est le prix maximum ?\n> ")) # Demander le maximum que pourra prendre le nombre généré aléatoirement

        while min >= max: # Si le minimum est plus grand que le maximum, redemmander les valeurs à l'utilisateur
            print("\nVous avez entrer des valeurs incorrectes : Le minimum est supérieur au maximum.") # Afficher qu'une erreur s'est produite

            min = int(input("Quel est le prix minimum ?\n> ")) # Demander le minimum que pourra prendre le nombre généré aléatoirement
            max = int(input("Quel est le prix maximum ?\n> ")) # Demander le maximum que pourra prendre le nombre généré aléatoirement

        print(f"Valeur définies : \nMin: {min} €\nMax: {max} €") # Afficher les valeurs définies
    except:
        print(f"Reponse invalide, valeur par défaut : \nMin: {min} €\nMax: {max} €") # En cas d'erreur, utiliser des valeurs par défaut

    ## 2. Choisir un nombre au hasard avec les paramètres choisis par l'utilisateur
    nbr = random.randint(min, max)

    nbr_trouve = False # Condidtion de la boucle while

    print(f"\n\n{'-'*30}\nJuste Prix\n{'-'*30}\n\n") # Afficher le titre du jeu

    tentatives = 0 # Nombre de tentatives que le joueur a mist pour trouver le nombre
    while (not(nbr_trouve)): # Tant que l'utilisateur n'a pas trouvé le juste prix
        try:
            nbr_joueur = input(f"Entrez un prix (entre {min} et {max} €)\n> ") # Demander à l'utilisateur le prix
            if (nbr_joueur == ":q"): # Si l'utilisateur tape ":q", il veut quitter le jeu, casser la boucle while
                print("Merci d'avoir joué !")
                nbr_trouve = True # Interrompre la boucle

                continue # Passer à prochaine itération de la boucle pour quitter le jeu

            guess = int(nbr_joueur) # Convertir en nombre l'entrée
            tentatives += 1 # Incrémenter le nombre de tentatives

            if guess < nbr: # Si le nombre entré est inférieur au prix
                print("Le prix est PLUS élevé !") # Dire que le prix est plus élevé

            elif guess > nbr:  # Si le nombre entré est supérieur au prix
                print("Le prix est MOINS élevé !") # Dire que le prix est moins élevé

            else: # Si le nombre est correct, afficher un message et arrêter le jeu
                s = "s" # Texte qui contient le s du pluriel
                if tentatives <= 1: # Si l'utilisateur a réussi en une tentative
                    s = "" # Enlever le s du pluriel
                print(f"C'est le juste prix ! ({nbr} €)\nMerci d'avoir joué ! Vous avez réussi en {tentatives} tentative{s}.") # Afficher le message de réussite
                nbr_trouve = True # Arrête la boucle while
        except:
            print("Entrez un nombre entier !") # Si le choix de l'utilisateur n'est pas un entier, afficher un message d'erreur

    ## 3. Demander à l'utilisateur s'il veut recommencer une partie
    r = input("\n\nVoulez-vous recommencer ? (O/n)\n> ")
    if r == "n" or r == "N" or r == ":q": # Si l'utilisateur répond "n" ou "N", arrêter le jeu
        exit()
    else: # Si l'utilisateur entre autre chose que "n"/"N", relancer une partie
        main()


if __name__ == "__main__": # Vérifier si le programme est lancé depuis la console et non depuis une bibliothèque
    main() # Lancer la fonction principale ; démarrer le jeu