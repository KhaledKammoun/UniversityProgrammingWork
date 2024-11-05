import numpy as np
import matplotlib.pyplot as plt

# 1. Saisie des données
x = np.array([1, 3, 3, 5])
y = np.array([3, 4, 6, 5])

# 2. Visualisation des données
plt.scatter(x, y, color='blue')  # Points originaux
plt.title("Nuage de points avec Matplotlib")
plt.show()


# 3. Trouver l’équation de l’ajustement (équation 1)
x_mean = np.mean(x)
y_mean = np.mean(y)
a = (np.sum(x * y) / len(x) -  x_mean * y_mean) / ((np.sum(x ** 2) / len(x)) - (x_mean ** 2))
b = y_mean - a * x_mean

print(f"a = {a}")
print(f"b = {b}")

# 4. Tracer la droite de l’ajustement
x_line = np.linspace(0, max(x), 100)  # Valeurs de x pour tracer la ligne (de 0 à max(x))
y_pred = a * x_line + b

plt.scatter(x, y, color='blue')  # Points originaux
plt.plot(x_line, y_pred, color='red')  # Droite de régression
plt.xlabel("Durée de révision (heures)")
plt.ylabel("Note d'examen")
plt.xlim(-1)  # Fixer le début de l'axe x à 0

plt.title("Régression linéaire : Durée de révision vs Note d'examen")
plt.show()

# 5. Calculer le coefficient de corrélation (équation 4)
numerateur = np.sum(x * y) - len(x) * x_mean * y_mean
denominateur = np.sqrt((np.sum(x**2) - len(x) * x_mean**2) * (np.sum(y**2) - len(x) * y_mean**2))
print("A = ",numerateur)
print("B = ",denominateur)

r = numerateur / denominateur
print(r)