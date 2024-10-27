def est_pair(n):
    if type(n) != int:
        raise ValueError # Déclencher une erreur
        return False
    return n % 2 == 0

def main():
    try:
        print(est_pair(int(input("Entrez un nombre: "))))
    except ValueError: # Gérer que faire en cas d'erreur
        print("Attention il faut saisir un nombre entier")
    finally:
        main()

main()