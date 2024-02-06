import matplotlib.pyplot as plt
import numpy as np

data = {
    "Genre" : [ 'Homme', 'Homme', 'Homme', 'Homme', 'Homme', 'Homme', 'Homme', 'Homme', 'Homme', 'Homme', 'Homme', 'Homme', 'Homme', 'Homme', 'Homme', 'Femme', 'Femme', 'Femme', 'Femme', 'Femme','Homme', 'Homme', 'Homme', 'Homme', 'Homme', 'Homme', 'Homme', 'Homme', 'Homme',     'Femme', 'Femme', 'Femme', 'Femme', 'Femme', 'Femme', 'Homme', 'Homme', 'Femme', 'Femme', 'Femme'],
    "Major" : ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A' ,'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'M', 'M', 'M', 'M', 'M']
}

table_contingence = {'Homme' : {'A' : 0, 'C' : 0, 'M' : 0},
                     'Femme' : {'A' : 0, 'C' : 0, 'M' : 0}}

for i in range(len(data['Genre'])) :
    if data["Genre"][i] == "Homme" :
        table_contingence["Homme"][data['Major'][i]]+=1
    else :
        table_contingence["Femme"][data['Major'][i]]+=1

table = np.array([[table_contingence['Homme']['A'], table_contingence['Homme']['C'], table_contingence['Homme']['M'],
                  ], [table_contingence['Femme']['A'], table_contingence['Femme']['C'], table_contingence['Femme']['M']]])


print("Tableau de contingence :")
print(table)


labels = ['Homme', 'Femme']
major = ['A', 'C','M']
x = np.arange(len(labels))
width = 0.20

fig, ax = plt.subplots()
for i, major in enumerate(major):
    ax.bar(x + i*width, table[:, i], width, label=major)

ax.set_xticks(x + width / 3)
ax.set_xticklabels(labels)
ax.set_ylabel('Nombre')
ax.set_title('Tableau de contingence Genre vs Major')
ax.legend()

plt.show()
