chaine = input("Note sur 20 : ")
note = float(chaine)

# Vérifier si la note est valide
if note < 0 or note > 20:
    print("Note invalide")
elif note >= 10.0:
    print("J'ai la moyenne")
else:
    print("Je n'ai pas la moyenne")