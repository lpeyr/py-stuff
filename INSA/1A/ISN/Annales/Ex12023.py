def fonct_1(n):
    mat = []
    for i in range(n):
        ligne = []
        for j in range(n):
            ligne.append(255)
        mat.append(ligne)
    return mat


def fonct_3(mat):
    s = ""
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            s = s + str(mat[i][j]) + " "
        s = s + "\n"  # ’\n’ est le caractère qui permet un retour à la ligne
    print(s)


def fonct_2(k, mat, val):
    for i in range(k, len(mat) - k):
        for j in range(k, len(mat) - k):
            if (i == k or i == len(mat) - 1 - k) or (j == k or j == len(mat) - 1 - k):
                mat[i][j] = mat[i][j] - k * val


mat = fonct_1(4)
fonct_3(mat)
d = 1
f = len(mat) - 2
while d + f // 2 != d:  # l’opérateur // effectue une division euclidienne
    fonct_2(d, mat, 10)
    d = d + 1
    f = f - 1
fonct_3(mat)
