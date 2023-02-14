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
ind_mot_court = min(range(len(liste_tuple)), key=lambda i: liste_tuple[i][1])
print(ind_mot_court)