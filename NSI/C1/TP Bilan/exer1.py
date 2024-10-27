# Méthode 1
def maxi(a, b):
    return max(a, b)

# Méthode 2 (manuellement)

def maxi2(a, b):
    if a < b:
        return b
    else:
        return a

# Tests de la fonction
print(maxi(1, 2)) # 2
print(maxi2(1, 2)) # 2