def obtenir_petite_str(str1, str2):
    '''
    Obtient la chaîne de caractère ayant la plus petite taille.
    '''
    if min(len(str1), len(str2)) == len(str1): # Si la plus petite chaîne de caractère est str1
        return str1 # Note si les deux chaînes font la même taille, str1 est retournée par défaut
    else: # Sinon, c'est str2
        return str2

# Tests de la fonction obtenir_petite_str()
print(obtenir_petite_str("Test", "Web")) # "Web" s'affiche