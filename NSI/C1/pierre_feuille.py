import random

def main():
    options = {1: "Pierre", 2: "Feuille", 3: "Ciseaux"}
    score_user, score_computer = 0, 0

    for i in range(3):
        try:
            c = int(input(f"Manche n°{i+1}:\n\nChoisir une option: \n\n1. Pierre\n2. Feuille\n3. Ciseaux\n> "))

            if not(c >= 1 and c <= 3):
                print("Veuillez choisir une option existante.\nLe jeu va se relancer...\n\n")
                main() # Relancer le jeu
            c = options[c]

            # Choisir une option aléatoire
            option = options[random.randint(1, 3)]
            if c == option:
                print(f"Vous avez chosi {c}\nL'ordinateur a choisi {option}, Match nul")
            elif c == options[1] and option == options[2]: # user = pierre; ordi = feuille
                score_computer += 1
                print(f"Vous avez chosi {c}\nL'ordinateur a choisi {option}, il gagne")
            elif c == options[1] and option == options[3]: # user = pierre; ordi = ciseaux
                score_user += 1
                print(f"Vous avez chosi {c}\nL'ordinateur a choisi {option}, il perd")
            elif c == options[2] and option == options[1]: # user = feuille; ordi = pierre
                score_user += 1
                print(f"Vous avez chosi {c}\nL'ordinateur a choisi {option}, il perd")
            elif c == options[2] and option == options[3]: # user = feuille; ordi = ciseaux
                score_computer += 1
                print(f"Vous avez chosi {c}\nL'ordinateur a choisi {option}, il gagne")
            elif c == options[3] and option == options[1]: # user = ciseaux; ordi = pierre
                score_computer += 1
                print(f"Vous avez chosi {c}\nL'ordinateur a choisi {option}, il gagne")
            elif c == options[3] and option == options[2]: # user = ciseaux; ordi = feuille
                score_user += 1
                print(f"Vous avez chosi {c}\nL'ordinateur a choisi {option}, il perd")

            print(f"\nVotre score: {score_user}\nScore de l'ordinateur: {score_computer}\n")
        except ValueError:
            print("Veuillez entrer un nombre\nLe jeu va se relancer...\n\n")
            main() # Relancer le jeu
        except:
            continue

    # Fin du jeu
    print("\nBilan du jeu:\n")

    if score_user > score_computer:
        print(f"Vous avez gagné {score_user} - {score_computer}")
    elif score_user == score_computer:
        print(f"Vous avez fait match nul, {score_user} - {score_computer}")
    else:
        print(f"L'ordinateur a gagné {score_computer} - {score_user}")

if __name__ == "__main__":
    main()