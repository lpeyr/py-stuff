c = 0
i = 0
n = 20
jours = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
while c < n:
    c += 1
    i += 1
    if i > len(jours) - 1:
        i = 0

print(jours[i])
