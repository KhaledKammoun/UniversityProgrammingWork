import pandas as pd
from datetime import datetime
df = pd.read_csv("empl.csv", delimiter=',')
print(df)

# Vérifier l'intégrité du domaine des valeurs de la variable 'Date_embau'
for date_str in df['Date_emb']:
    try:
        datetime_object = datetime.strptime(date_str, "%d-%m-%Y")
    except ValueError:
        print(f"Erreur de format de date pour la valeur : {date_str}")
# question 4  
duplicates = df.duplicated()

num_duplicates = duplicates.sum()

if num_duplicates > 0:
    df = df.drop_duplicates()
    print("Doublons supprimés. Nouvelle taille du DataFrame :", df.shape)
else:
    print("Aucun doublon trouvé dans le DataFrame.")

# question 5
df = df.fillna(0)

print(df)

