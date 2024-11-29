def triangle(n):
    chaine = ""
    for i in range(n+1):
        for j in range(1, i+1):
            chaine+=f"{j}"
        chaine+="\n"
    return chaine

print(triangle(4))