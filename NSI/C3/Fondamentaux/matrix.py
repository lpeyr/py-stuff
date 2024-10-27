def transpose(M):
    lines = len(M)
    cols = len(M[0])

    # copy
    N = [[0] * cols for k in range(lines)]

    for i in range(lines):
        for j in range(cols):
            N[i][j] = M[j][i]

    return N


A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print(transpose(A))
