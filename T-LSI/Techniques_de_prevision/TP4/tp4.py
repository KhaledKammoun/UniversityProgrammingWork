
import numpy as np
import matplotlib.pyplot as plt
# Question 1 : Représenter graphiquement la série par un nuage de points.
t = np.array([1, 2, 3, 4, 5, 6, 7])
ca = np.array([120 ,155, 125, 202, 180, 235, 240])

plt.scatter(t, ca, color='blue', label='Données PIB')

plt.xlabel("T")
plt.ylabel("CA")
plt.title("Nuage de points : Évolution du Chiffre d'affaire sur 7 ans")
plt.grid(True)
plt.legend()
plt.show()

# Question 2 : Déterminer l’équation de la droite de tendance en utilisant la méthode des points extrêmes.
# Points extrêmes : (t_1, ca_1) et (t_7, ca_7)
t1, ca1 = t[0], ca[0]  # Premier point
t2, ca2 = t[-1], ca[-1]  # Dernier point

# Calcul de la pente a
a = (ca2 - ca1) / (t2 - t1)

# Calcul de l'ordonnée à l'origine b
b = ca1 - a * t1

# Calcul des valeurs prédites de CA avec la droite de tendance
ca_tendance = a * t + b
print(ca_tendance)
# Tracer la droite de tendance
plt.plot(t, ca_tendance, color='red', label="Droite de tendance")

# Ajouter les détails au graphique
plt.xlabel("Temps (T)")
plt.ylabel("Chiffre d'affaire (CA)")
plt.title("Nuage de points et droite de tendance : Évolution du CA sur 7 ans")
plt.grid(True)
plt.legend()

# Afficher le graphique


# Question 3 : Représenter cette équation sur le même graphique.
# Affichage des résultats
equation = f"{a:.2f} * T + {b:.2f}"
print(f"Équation de la droite de tendance : CA = {a:.2f} * T + {b:.2f}")
plt.text(1, 220, equation, fontsize=12, color='green')  # Positionner l'équation sur le graphique

# Afficher le graphique
plt.show()

# Question 4 : Déterminer la prévision pour t=8
t_pred = 8
ca_pred = a * t_pred + b
print(f"Prévision pour t = 8 : {ca_pred:.2f}")
