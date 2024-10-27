import random # Importer le module random pour générer des nombres aléatoires

# Fonction principale du jeu
def main():
    options = {1: "Pierre", 2: "Feuille", 3: "Ciseaux"} # Options possibles
    score_user, score_computer = 0, 0 # Créer un score pour l'utilisateur et l'ordinateur

    for i in range(3): # Faire trois manches
        try:
            c = int(input(f"Manche n°{i+1}:\n\nChoisir une option: \n\n1. Pierre\n2. Feuille\n3. Ciseaux\n> ")) # Demander à l'utilisateur de choisir un choix

            while not(c >= 1 and c <= 3): # Si l'utilisateur entre un choix incorrect, redemmander le nombre
                c = int(input(f"Manche n°{i+1}:\n\nChoisir une option: \n\n1. Pierre\n2. Feuille\n3. Ciseaux\n> ")) # Demander à l'utilisateur de choisir un choix


            # Choisir une option aléatoire
            option = random.randint(1, 3)

            # Vérifie qui gagne
            if c == option: # Si l'ordinateur et l'utilisateur ont fait le même choix
                print(f"Vous avez chosi {options[c]}\nL'ordinateur a choisi {options[option]}, Match nul") # Match nul

            elif c == 1 and (c + option) % 3 == 1: # Si l'utilisateur a choisi pierre, et que l'ordinateur a choisi un choix perdant.
                print(f"Vous avez chosi {options[c]}\nL'ordinateur a choisi {options[option]}, L'ordinateur perd") # Afficher le bilan de la manche
                score_user += 1 # Incrémenter le score de l'utilisateur

            elif c == 2 and (c + option) % 3 == 0: # Si l'utilisateur a choisi feuille, et que l'ordinateur a choisi un choix perdant.
                print(f"Vous avez chosi {options[c]}\nL'ordinateur a choisi {options[option]}, L'ordinateur perd") # Afficher le bilan de la manche
                score_user += 1 # Incrémenter le score de l'utilisateur

            elif c == 3 and (c + option) % 3 == 2: # Si l'utilisateur a choisi ciseaux, et que l'ordinateur a choisi un choix perdant.
                print(f"Vous avez chosi {options[c]}\nL'ordinateur a choisi {options[option]}, L'ordinateur perd") # Afficher le bilan de la manche
                score_user += 1 # Incrémenter le score de l'utilisateur

            else: # Si l'ordinateur gagne
                score_computer += 1 # Incrémenter le score de l'ordinateur
                print(f"Vous avez chosi {options[c]}\nL'ordinateur a choisi {options[option]}, L'ordinateur gagne") # Affiche le bilan de la manche


            print(f"\nVotre score: {score_user}\nScore de l'ordinateur: {score_computer}\n") # Récapitule les scores
        except ValueError: # En cas d'erreur
            print("Veuillez entrer un nombre\nLe jeu va se relancer...\n\n") # Afficher un message d'erreur
            main() # Relancer le jeu
        except: # Autre erreur
            continue # Continuer le jeu quand même

    # Fin du jeu
    print("\nBilan du jeu:\n") # Afficher le bilan de la partie

    if score_user > score_computer: # Si l'utilisateur a gagné
        print(f"Vous avez gagné {score_user} - {score_computer}") # Afficher le message de victoire
    elif score_user == score_computer: # Si l'ordinateur et l'utilisateur ont le même score
        print(f"Vous avez fait match nul, {score_user} - {score_computer}") # Afficher le message de match null
    else: # Si l'ordinateur a gagné la partie
        print(f"L'ordinateur a gagné {score_computer} - {score_user}") # Afficher le message de défaite

if __name__ == "__main__": # Si le programme est lancé depuis le console
    main() # Lancer la fonction principale du jeu