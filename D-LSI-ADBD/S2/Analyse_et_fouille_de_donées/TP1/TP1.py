import pandas as pd 
from numpy import NaN

data = {"Name" : ["Anastasia","Dima","Katherine",
"James","Emily","Michael","Matthew","Laura","Kevin","Jonas" ],
        "Score" : [12.5, 9.0, 16.5, NaN, 9.0, 20.0, 14.5, NaN, 8.0, 19.0],
        "Attempts" : [1,3,2,3,2,3,1,1,2,1],
        "qualify" : [True, False, True, False, False, True, True, False, False, True]}

# Créer un DataFrame avec les étiquettes de l'index
df = pd.DataFrame(data, index = [chr(ord('A') + i) for i in range(len(data['Name']))])

df["Nord"] = df["Score"] > 12.0

print(df)
df.drop("Nord",axis = 1, inplace =True)
# Afficher les informations de base du DataFrame ainsi que ses données
# print(df)

# Obtenir les 3 premières lignes du DataFrame donné
trois_premier_ligne = df.head(3)
# print(trois_premier_ligne)

# Sélectionner les colonnes «name» et «score»
colonnes_selectionnees = df[['Name', 'Score']]
# print(colonnes_selectionnees)

# Sélectionner les colonnes «name» et «score» des lignes 1, 3, 5 et 6
selection = df.loc[[chr(ord('A') + c) for c in [1, 3, 5, 6]], ['Name', 'Score']]
# print(selection)

#Sélectionner les lignes où le nombre de tentatives « attempts » d'examen est supérieur à 2
ligne_tentatives = df[df['Attempts']>2]
print(ligne_tentatives)

# Q7 : Compter le nombre de lignes et de colonnes d'un DataFrame
nb_ligne = len(df.keys())
nb_cols = len(df['Name'])
print("Nb Lignes : ", nb_ligne)
print("Nb Cols : ", nb_cols)

# Q8 : Sélectionner les lignes où le score est manquant, c'est-à-dire NaN
ligne_score_manque = df[df['Score'].isnull()]
print(ligne_score_manque)

# Q9 : Sélectionner les lignes dont le score « score » est compris entre 15 et 20 (inclus)
ligne_score_15_20 = df[df['Score'].isin(range(15, 21))]
print(ligne_score_15_20)
# Q10 : 10) Sélectionner les lignes où le nombre de tentatives à l'examen « attempts » est inférieur à 2 et le score « score » supérieur à 15
ligne_attempts_score = df[(df['Attempts'] < 2) & (df['Score'] > 15)]
print(ligne_attempts_score)

# Q11 : Changer le score de la ligne «d» en 11,5
df.loc['D', 'Score'] = 11.5
print(df)

# Q12 : Calculer la somme des tentatives d'examen « attempts » des élèves
sum_attempts = sum(df["Attempts"])
print(sum_attempts)

# Q13 : Calculer le score moyen des élèves
score_moyen = df["Score"].mean()
print(score_moyen)

# Q14 : Ajouter une nouvelle ligne «k» au DataFrame avec des valeurs données pour chaque colonne
df.loc['K'] = ["Calvin", 20.0, 1, True]
print(list(df.loc["K"]))

# Q15 : Supprimez la nouvelle ligne et renvoyez le bloc de données d'origine
df = df.drop("K")
print(df)

# Q16 : Trier le DataFrame d'abord par «name» dans l'ordre croissant
trie_score = df.sort_values("Score")
print(trie_score)
