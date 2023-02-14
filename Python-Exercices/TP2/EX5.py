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
