import numpy as np
import matplotlib.pyplot as plt

# Question 1 : Tracer le nuage de points correspondant et commenter.
annees = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
pib = np.array([8000, 9000, 9500, 9700, 9800, 9800, 11000, 12000, 12500, 13000])

plt.scatter(annees, pib, color='blue', label='Données PIB')

plt.xlabel("Année")
plt.ylabel("PIB (en euros)")
plt.title("Nuage de points : Évolution du PIB sur 10 ans")
plt.grid(True)
plt.legend()
plt.show()

# ==> Commentaire : Le nuage de points pourrait montrer une augmentation générale du PIB au fil des années, suggérant une croissance économique.

# Question 2 : Déterminer l’équation de la droite de l’ajustement en utilisant la méthode des moindres carrés. 
x_mean = np.mean(annees)
y_mean = np.mean(pib)

a = (np.sum(annees * pib) - len(annees) * x_mean * y_mean) / (np.sum(annees**2) - len(annees) * x_mean**2)
b = y_mean - a * x_mean

print(f"Pente (a) : {a}")
print(f"Ordonnée à l'origine (b) : {b}")

# Question 3 : Calculer le coefficient de corrélation correspondant 
n = len(annees)

numerateur = np.sum(annees * pib) - n * x_mean * y_mean

denominateur = np.sqrt((np.sum(annees**2) - n * x_mean**2) * (np.sum(pib**2) - n * y_mean**2))

r = numerateur / denominateur

print(f"Coefficient de corrélation r : {r}")

# Question 4 : Représenter cette droite sur le même graphique. 
pib_pred = a * annees + b

plt.scatter(annees, pib, color='blue', label='Données PIB')
plt.plot(annees, pib_pred, color='red', label="Droite de régression")

plt.xlabel("Année")
plt.ylabel("PIB (en euros)")
plt.title("Régression linéaire : Évolution du PIB")
plt.grid(True)
plt.legend()

plt.show()

# Question 5 : Déterminer le produit intérieur brut prévu pour l’année suivante
pib_11 = a * 11 + b
print("produit intérieur brut prévu pour l’année suivante :",pib_11)