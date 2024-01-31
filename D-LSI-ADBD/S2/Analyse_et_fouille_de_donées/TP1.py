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