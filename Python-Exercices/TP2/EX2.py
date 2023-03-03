mot = input("donner mot : ")
mot_c =input("donner mot_c : ")
b = True
for c in mot :
    if (mot.count(c)>mot_c.count(c)) :
        b=False
        break
if (b) :
    print("[{}] est composable à partir de [{}]".format(mot,mot_c))
else :
    print("[{}] n'est pas composable à partir de [{}]".format(mot, mot_c))
