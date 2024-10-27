# Demander à l'utilisateur d'entrer du texte à traduire
texte = input("Entrez le texte à traduire en langage Leet : ")

traduction = ""  # Initialiser la variable qui contiendra le texte traduit

for lettre in texte:  # Pour chaque lettre dans la chaîne de caractère, vérifier si elle doit être traduite ou non
    if lettre == "S" or lettre == "s":
        traduction += "5"  # Remplace le s ou S par un 5
    elif lettre == "T" or lettre == "t":
        traduction += "7"  # Remplace le t ou T par un 7
    elif lettre == "A" or lettre == "a":
        traduction += "4"  # Remplace le a ou A par un 4
    elif lettre == "E" or lettre == "e":
        traduction += "3"  # Remplace le e ou E par un 3
    elif lettre == "L" or lettre == "l":
        traduction += "1"  # Remplace le l ou L par un 1
    elif lettre == "O" or lettre == "o":
        traduction += "0"  # Remplace le o ou O par un 0
    else:  # Si la lettre ne doit pas être traduite
        traduction += lettre  # Ajouter la lettre tel quel

print("Voici la traduction de votre de phrase en Leet :",
      traduction)  # Afficher la traduction
