d = 10 # Distance de base
distance_totale = d # Distance totale parcourue le premier jour
for i in range(1, 30): # Pendant 30 jours
    d += 2 # 2 km de plus que la distance d de la veille
    distance_totale += d # Augmenter la distance totale de d km

print(f"L'athlète a parcourue {distance_totale} km en 30 jours d'entraînement.")