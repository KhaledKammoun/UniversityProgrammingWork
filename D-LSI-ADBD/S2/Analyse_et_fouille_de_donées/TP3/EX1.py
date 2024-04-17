import pandas as pd
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt

X = pd.read_excel('seeds.xlsx')
"""
1. Area A: surface du grain
2. Perimetre P: périmètre du grain
3. compactness : C = 4*pi*A/ P ^2
4. klength : longueur du noyau du grain (kernel)
5. kwidth : largeur du noyau du grain
6. AsymmetryCoef : coefficient d’asymétrie
7. kGrooveL : longueur du rainure du noyau
"""
# Question 2
colonnes_necessaires = ['Area', 'Perimetre', 'compactness ', 'kLength', 'kWidth', 'AsymmetryCoef', 'kGrooveL']
X = X[colonnes_necessaires]
print(X)

# Question 3
X = X.fillna(X.mean())
print(X)

# Question 4
# 4. Standardiser les données en utilisant la classe StandardScaler de la bibliothèque sklearn.
scaler = StandardScaler()
X_Scaled = scaler.fit_transform(X)
X_Scaled = pd.DataFrame(X_Scaled, columns=X.columns)
mean_std = pd.DataFrame({
    "mean" : X_Scaled.mean(),
    "std" : X_Scaled.std()
})

# 6. Afficher et analyser la matrice de corrélation
correlation_matrix = X.corr()
# 7. Quels sont les couples de variables les plus corrélées.
print(correlation_matrix.unstack().sort_values(ascending=False))


# 8. Visualiser et analyser les dépendances des variables 2 à 2 en faisant le lien avec la matrice de corrélation.

sns.pairplot(X)
plt.show()