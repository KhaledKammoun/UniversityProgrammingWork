liste = []
#question 1
i = 1
while True :
    mot = input("lire mot {} : ".format(i))
    i+=1
    if mot.lower()=='q' :
        break
    liste.append(mot)
#question 2
liste_tuple=[(c,len(c)) for c in liste]
print(liste_tuple)
#question 3
# ind_mot_court = min(range(len(liste_tuple)), key=lambda i: liste_tuple[i][1])
ind_mot_court = 0
for i in range(1,len(liste_tuple)) :
    if (liste_tuple[ind_mot_court][1]>liste_tuple[i][1]) :
        ind_mot_court = i
print(ind_mot_court,"est l'indice du mot le plus court")
#question 4
ch=""
b=True
j=0
while (b and j<len(liste[ind_mot_court])) :
    i = 1
    while (b and i<len(liste)) :
        if (liste[0][j]!=liste[i][j]) :
            b=False 
            break
        i+=1
    if (b) :
        ch+=liste[0][j]
    j+=1
"""
2°Méthode :

w=liste[ind_mot_court]
ch=""
c=0
for i in range(len(w)) :
    for j in range(len(liste)) :
        if (liste[j][i]==w[i]) :
            c+=1
    if (c==len(liste)) :
        ch+=w[i]
        c=0
    else :
        break
"""
if (ch) :
    print("racine =",ch)
else :
    print("pas de racine commune")
