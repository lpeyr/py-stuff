# 8*8 = 64
# 2 grain de riz qui * 2

nbr_riz = 2
c = 0
taille = 64
tot = 0
cases = list(range(64))
for i in range(len(cases)):
    cases[i] = 0

cases[0] = 2

while (nbr_riz < taille):
    c += 1
    print(f"#{c} - {nbr_riz}")
    nbr_riz *= 2

for j in range(c):
    for i in range(len(cases)):
        if cases[i] == 0 and j <= c:
            cases[i] = 1
        cases[i] *= 2



for i in cases:
    tot += i

print(f"#{c+1} - {nbr_riz}")
print(f"\n\n{taille} = 2^({c})")
print(cases)
print(tot)