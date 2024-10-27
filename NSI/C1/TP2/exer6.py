def obtenir_mutliples(n):
    for i in [2, 3, 5, 7]:
        if n % i == 0:
            print(f"{n} est un multiple de {i}")

    main() # Récursive

def main():
    obtenir_mutliples(int(input("Saisir un nombre entier: ")))

if __name__ == "__main__":
    main()