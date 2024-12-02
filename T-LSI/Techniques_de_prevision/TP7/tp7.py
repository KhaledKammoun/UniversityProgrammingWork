import pandas as pd
import numpy as np

# 1. Récupérer le fichier serie1 contenant 365 données des naissances mensuelles et mettre les données dans une liste serie.
csvData = pd.read_csv("serie.txt", delimiter=",", header=0)
a = np.array(csvData.values)
print(a)

"""
2. Créer une liste P et ajouter à cette liste la première valeur =35.
Cette valeur sera considérée comme étant la première prévision.
"""
P = [35]

"""
3. Calculer les prévisions dans la liste P en utilisant la formule suivante et ceci du premier mois
jusqu’au dernier mois : P(i)=0.1*P(i-1)+0.9*serie(i-1) où i représente le i ème mois de
l’année.
"""
liste_mois = []
for i in range(12): 
    var = []
    for j in range(len(a)):
        month = int(a[j][0].split("-")[1])
        if month == i + 1: 
            var.append(a[j][1])

    if var:
        liste_mois.append(np.mean(var))
    else:
        liste_mois.append(0)

for i in range(1, len(liste_mois)): 

    P.append(0.1 * P[i - 1] + 0.9 * liste_mois[i - 1])
"""
4. Afficher la liste des prévisions
"""
print(P)

"""
5. Mettre dans une liste erreur les erreurs de la prévision établie.
"""
erreurs = []
for i in range(12) : 
    erreurs.append(abs(liste_mois[i] - P[i]))
print("Erreur")
print(erreurs)

"""
6. Mettre dans une liste eq les erreurs quadratiques correspondantes.
"""
eq = []
for i in range(len(erreurs)) :
    eq.append((liste_mois[i] - P[i])**2)
print(eq)
"""
7. Calculer la moyenne des erreurs quadratiques.
"""
print("Moyenne des erreurs quadratiques : ", np.mean(eq))