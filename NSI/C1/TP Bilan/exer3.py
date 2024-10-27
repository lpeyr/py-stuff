table_six = [] # Initialiser une liste
for i in range(1, 21): # Pour tous les nombres de 1 à 20
    asterix = "" # Chaîne de caractères contenant l'astérix, vide par défaut
    if 6 * i % 5 == 0: # Si le nombre est divisible par 5
        asterix = "*" # Assigner le caractère '*' à la variable
    table_six.append(f"{6 * i}{asterix}") # Ajouter à liste le nombre, avec ou sans astérix


def print_list(liste):
    '''
    Affiche de une liste sous la forme n, n+1, n+2.
    '''
    texte = ""
    vir = ", " # Séparateur
    for item in liste: # Pour tous les éléments
        if item == liste[len(liste) - 1]: # Si l'élément est le dernier de la liste
            vir = "" # Enlever la virgule

        texte += item + vir # Ajouter l'élément avec la valeur de virgule

    print(texte) # Imprimer la chaîne de caractères obtenue

print_list(table_six) # Imprimer la table de six