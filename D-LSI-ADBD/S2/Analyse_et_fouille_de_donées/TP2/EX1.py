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
print("\nQuestion 5 : ")
print(df)

# question 6 :
max_salaire = df['Salaire'].max()
df['Salaire'] = df['Salaire'].apply(lambda x: max_salaire if x == 0 else x)
print("\nQuestion 6 : ")
print(df)

#question 7 :
dict_poste = {"manger" :0, "Ingenieur" :1, "Developpeur" : 2}
df['poste'] = df['poste'].apply(lambda x :  dict_poste[x])
print(df)
print("Qursdflksdfjslfg : ")
dict_Date_emb = {key for key in df['Date_emb'].unique()}
print(dict_Date_emb)

#question 8 :
numerical_columns = df.select_dtypes(include=['int64', 'float64'])

# centrées
centered_data = numerical_columns - numerical_columns.mean()

numerical_columns = df.select_dtypes(['float', 'int'])
centered_data = numerical_columns - numerical_columns.mean()

print(numerical_columns)
# centrées et réduites.
scaled_data = centered_data / numerical_columns.std()

print("Y matrix (Centered data):")
print(centered_data)

print("\nZ matrix (Centered and scaled data):")
print(scaled_data)
