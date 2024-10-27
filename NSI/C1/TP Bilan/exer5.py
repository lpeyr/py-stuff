def main():
    '''
    Demande à l'utilisateur un nombre, et affiche un message d'information.
    Cette fonction est là en cas d'erreur, pour relancer le programme si l'utilisateur entre une valeur autre que int.
    '''
    try: # Eviter les erreurs
        n = int(input("Saisir un nombre\n> ")) # Convertir l'entrée en int

        if n % 2 == 0: # Si n est pair
            print("Ce nombre est pair")
        elif n % 3 == 0: # Si n est divisible par 3
            print("Ce nombre est impair, mais est multiple de 3")
        else: # Pour tous les autres nombres
            print("Ce nombre n'est ni pair ni multiple de 3")

    except ValueError: # Si l'utilisateur saisi autre chose qu'un nombre entier int
        print("Veuillez saisir un nombre\n")
        main() # Recommencer le programme


if __name__ == "__main__": # Si le programme est lancé depuis la console
    main() # Lancer le programme