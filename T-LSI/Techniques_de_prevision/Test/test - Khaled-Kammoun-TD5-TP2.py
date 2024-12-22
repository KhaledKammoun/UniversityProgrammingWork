# Test Technique de prévision
# Khaled Kammoun TLSI-ADBD TD5 TP2

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# 1. charger les données depuis le fichier data.txt.
txt_data = pd.read_csv("data.txt", delimiter="," ,header=0)
data = np.array(txt_data)
print(data)

# 2. Tracer un nuage de points des données avec les mois en abscisse et les ventes en ordonnée.

mois = data[:, 0]
ventes = data[:, 1]

plt.scatter(mois, ventes, color="blue", label="PT")
plt.xlabel("mois")
plt.ylabel("ventes")
plt.title("Nuage de points")
plt.grid(True)
plt.show()
# 3. Calculer l’équation de la droite d’ajustement en utilisant la méthode des points extrêmes.
first_x, first_y = mois[0], ventes[0]
last_x, last_y = mois[-1], ventes[-1]
print(f"point 1 : ({first_x}, {first_y})")
print(f"point 2 : ({last_x}, {last_y})")
a = (last_y - first_y) / (last_x - first_x) 
b = first_y - a * first_x

print(f"Equation : {a} * t + {b}")

# 4. Calculer la prévision des ventes pour le mois numéro 51 en utilisant l’équation de la droite.
mois_51 = a * 51 + b
print(mois_51)

# 6. Calculer la prévision des ventes pour le mois numéro 51 en utilisant la moyenne des ventes ?
x_1, y_1 = np.mean(mois[:len(mois) //2]), np.mean(ventes[:len(ventes) //2])
x_2, y_2 = np.mean(mois[len(mois) //2:]), np.mean(ventes[len(ventes) //2:])
print(f"point 1 : ({x_1}, {y_1})")
print(f"point 2 : ({x_2}, {y_2})")
a = (y_2 - y_1) / (x_2 - x_1) 
b = y_1 - a * x_1

print(f"Equation : {a} * t + {b}")

mois_51 = a * 51 + b
print(mois_51)
