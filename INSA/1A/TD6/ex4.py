import matplotlib.pyplot as plt

ma_liste = [0, 0, 2, 9, 8, 0, 1, 4, 4]
compte = [0] * 10

for el in ma_liste:
    compte[el] += 1
x = list(range(1, 11))

fig, ax = plt.subplots(figsize=(4, 4))
ax.set_title("Historigramme")
ax.bar(x, compte)
ax.set_xlabel("Valeurs")
ax.set_ylabel("Nombre d'occurences")
ax.legend()
plt.show()