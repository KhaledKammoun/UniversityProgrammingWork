import pandas as pd
import numpy as np

# 1. Récupérer le fichier data2 contenant 100 données des ventes mensuelles d’une entreprise et mettre les données dans une liste a.
csvData = pd.read_csv("data.csv", delimiter=",", header=None)
a = np.array(csvData.values)[0]

# 2. Calculer les prévisions dans une liste en utilisant la moyenne statistique et ceci du premier mois jusqu’au dernier mois.
moyenne_statistique = [np.mean(a[:i+1])for i in range(len(a))]

# 3. Afficher la liste des prévisions
print(moyenne_statistique)

# 4. Quelle est la prévision des ventes pour le mois numéro 101.
print(np.mean(a))

# 5. Supposons que la prévision se calcule en utilisant seulement la moyenne des trois derniers mois. Calculer les prévisions dans une liste en utilisant cette moyenne et ceci du premier mois jusqu’au dernier mois.