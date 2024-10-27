def main():
    try:
        t = float(input("Quel est la température ?\n> "))
    except:
        print("Entrez un nombre correct.")
        main() # Eviter les erreurs

    # <= 0°C, très froid
    # 0-10°C, froid
    # 10-15°C, frais
    # 15-20°C, bon
    # 20-25°C, un peu chaud
    # 25-30°C, chaud
    # >30°C, très chaud

    if t <= 0:
        print("Il fait très froid")
    elif t <= 10:
        print("Il fait froid")
    elif t <= 15:
        print("Il fait frais")
    elif t <= 20:
        print("Il fait un peu chaud")
    elif t <= 25:
        print("Il fait chaud")
    elif t <= 30:
        print("Il fait très chaud")

main()