
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



# Question 2 : Déterminer les deux points moyens.
t_mean1 = np.mean(t[:(len(t) // 2) + len(t) % 2])
t_mean2 = np.mean(t[(len(t) // 2) + len(t) % 2:])
print(t_mean1)
print(t_mean2)
ca_mean1 = np.mean(ca[:(len(ca) // 2) + len(t) % 2])
ca_mean2 = np.mean(ca[(len(ca) // 2) + len(t) % 2:])
print(ca_mean1)
print(ca_mean1)

# Question 3 : Afficher les deux points dans le même graphique de la série
plt.scatter(t_mean1, ca_mean1, color="red", label="Point moyen 1")
plt.scatter(t_mean2, ca_mean2, color="green", label="Point moyen 2")


# Question 4 : Déterminer la droite d’ajustement selon la méthode des moyennes doubles (Mayer).
# pentes at et b
a = (ca_mean2 - ca_mean1) / (t_mean2 - t_mean1)
b = ca_mean1 - a * t_mean1
print("A = ", a)
print("B = ", b)

# Question 5 : Représenter la droite de tendance sur le même graphique.
plt.plot(t, a * t + b, color='red', label="Droite d'ajustement")


# Question 6 : Déterminer la prévision pour t=8.
t_pred = 8
ca_pred = a * t_pred + b
print(f"Prévision pour t = 8 : {ca_pred:.2f}")

# Question 7 : Déterminer la droite de tendance de cette série en utilisant la méthode des moindres carrés.
x_mean = np.mean(t)
y_mean = np.mean(ca)

a = (np.sum(t * ca) - len(t) * x_mean * y_mean) / (np.sum(t**2) - len(t) * x_mean**2)

b = y_mean - a * x_mean

print(f"Pente (a) : {a}")
print(f"Ordonnée à l'origine (b) : {b}")

n = len(t)

numerateur = np.sum(t * ca) - n * x_mean * y_mean

denominateur = np.sqrt((np.sum(t**2) - n * x_mean**2) * (np.sum(ca**2) - n * y_mean**2))

r = numerateur / denominateur

print(f"Coefficient de corrélation r : {r}")

pib_pred = a * t + b

plt.scatter(t, ca, color='blue', label='Données PIB')
plt.plot(t, pib_pred, color='red', label="Droite de régression")

plt.legend()
plt.show()

# Question 8 : Prévoir les ventes pour t=8.
t_pred_2 = 8
ca_pred_2 = a * t_pred_2 + b
print(f"Prévision pour t = 8 : {ca_pred_2:.2f}")


