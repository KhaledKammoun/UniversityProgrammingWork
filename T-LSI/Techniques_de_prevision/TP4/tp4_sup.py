import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

# Données des ventes par année et trimestre
matrice_var = {
   2018: np.array([520, 650, 1500, 710]),
   2019: np.array([550, 690, 1660, 790]),
   2020: np.array([610, 720, 1820, 830]),
   2021: np.array([680, 780, 1900, 880]),
   2022: np.array([750, 860, 1980, 950]),
   2023: np.array([880, 940, 2100, 1100])
}

# Initialisation de la matrice pour stocker les résultats
matrice_t = []

# Ajout de l'index des années dans la matrice

# Calcul des valeurs pour chaque année
for key in matrice_var.keys():
    ventes_annuelles = matrice_var[key]
    
    # Calcul des différents champs
    moyenne_annuelle = np.mean(ventes_annuelles)
    multiplication_index_somme = key * np.sum(ventes_annuelles)
    somme_carree = np.sum(ventes_annuelles ** 2)
    
    # Ajout à la matrice
    matrice_t.append(np.array([
        key, 
        moyenne_annuelle, 
        multiplication_index_somme, 
        somme_carree
    ]))


# Convertir en tableau numpy pour un affichage propre


# Afficher la matrice
print("Matrice des données :")
print(matrice_t)

print(tabulate(matrice_t, np.array(list(matrice_var.keys())), tablefmt="fancy_grid"))
