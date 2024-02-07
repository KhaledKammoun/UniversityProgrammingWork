import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
data = {
    "Genre" : [ 'Homme', 'Homme', 'Homme', 'Homme', 'Homme', 'Homme', 'Homme', 'Homme', 'Homme', 'Homme', 'Homme', 'Homme', 'Homme', 'Homme', 'Homme', 'Femme', 'Femme', 'Femme', 'Femme', 'Femme','Homme', 'Homme', 'Homme', 'Homme', 'Homme', 'Homme', 'Homme', 'Homme', 'Homme',     'Femme', 'Femme', 'Femme', 'Femme', 'Femme', 'Femme', 'Homme', 'Homme', 'Femme', 'Femme', 'Femme'],
    "Major" : ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A' ,'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'M', 'M', 'M', 'M', 'M']
}

table_contingence = {'Homme' : {'A' : 0, 'C' : 0, 'M' : 0},
                     'Femme' : {'A' : 0, 'C' : 0, 'M' : 0}}
table_contingence = pd.crosstab(index = pd.Series(data["Genre"], name = "Genre"), columns=pd.Series(data["Major"], name = "Major"), margins=True, margins_name="Total")

print("Tableau de contigence : ")
print(table_contingence, "\n")
table_contingence = pd.crosstab(index = pd.Series(data["Genre"], name = "Genre"), columns=pd.Series(data["Major"], name = "Major"), normalize="all", margins=True, margins_name="Total")
print("---"*50)
print(table_contingence)
