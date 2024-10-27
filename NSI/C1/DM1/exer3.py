def obtenir_diviseur(n):
    for i in range(1, n + 1):  # Pour tous les nombres de 1 à n
        if n % i == 0:  # Vérifier si n est divisble par le nombre i
            # Si le nombre est un diviseur, afficher un message dans la console
            print(f"{i} est un diviseur de {n}")


try:
    # Demander à l'utilisateur un nombre
    nombre = int(input("Choisir un nombre entier : "))
    obtenir_diviseur(nombre)  # Obtenir les diviseurs du nombre
except:  # Si l'utilisateur entre une autre valeur qu'un entier
    print("Erreur : Veuillez entrer un nombre entier")
