import matplotlib.pyplot as plt

def calcul_moyenne(liste):
    s = 0
    for x in liste:
        s += x
    return 1 / len(liste) * s


def calcul_ecart_type(liste):
    m = calcul_moyenne(liste)
    s = 0
    for x in liste:
        s += (x - m) ** 2
    return (1 / len(liste) * s) ** 0.5


def conversion_temperature(temps):
    t = temps.split(", ")
    f = []
    for i in t:
        f.append(int(i))
    return f

# Read temperatures
f = open("temp.txt", "r", encoding="utf8")
contenu = f.readlines()
f.close()

# Parse file
temperatures_mois = []
for ligne in contenu:
    temperatures_mois.append(conversion_temperature(ligne))

liste_moyenne = []
liste_std = []
liste_x = [
    "Janvier",
    "Février",
    "Mars",
    "Avril",
    "Mai",
    "Juin",
    "Juillet",
    "Août",
    "Septembre",
    "Octobre",
    "Novembre",
    "Décembre",
]

for temperatures in temperatures_mois:
    liste_moyenne.append(calcul_moyenne(temperatures))
    liste_std.append(calcul_ecart_type(temperatures))

# Display diagram
fig, ax = plt.subplots()
ax.errorbar(liste_x, liste_moyenne, liste_std, fmt="o", linestyle="-", capsize=4)
plt.show()
