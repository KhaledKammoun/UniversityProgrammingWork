import matplotlib.pyplot as plt
liste = ['A','A','A','A','A','A','A','A','A','A','A','A','A','A','A','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','M','M','M','M','M','M','M','M','M','M']

liste.sort()
n = len(liste)
print("Population : ", n)

liste_0 = []
liste_eff = [] 
liste_freq = []
for i in range (n) :
    if (liste[i] not in liste_0) :
        liste_0.append(liste[i])
        liste_eff.append(liste.count(liste[i]))
        liste_freq.append(round(liste.count(liste[i]) / n, 2))
        
print("\t".join(liste_0))
print("\t".join([str(c) for c in liste_eff]))
print("\t".join([str(c) for c in liste_freq]))

plt.pie(liste_eff, labels=liste_0, autopct='%1.1f%%')
plt.show()
plt.bar(liste_0, liste_eff, width=0.5)
plt.show()