import pandas as pd
import numpy as np


# 1. Récupérer le fichier serie1 contenant 365 données des naissances mensuelles et mettre les
# données dans une liste serie. 
csvData = pd.read_csv("serie.txt", delimiter=",", header=0)
a = np.array(csvData.values)
print(a)

# 2. Créer deux variables S-1 et T-1 et les initialiser comme suite : 


