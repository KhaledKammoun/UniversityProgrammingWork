mot = "python"
mot_c = "pythonss"
mot_c_copy = mot_c
b = True
for c in mot :
    if (mot_c_copy.count(c)>0) :
        index = mot_c_copy.index(c)
        mot_c_copy = mot_c_copy[:index] + mot_c_copy[index+1:]
    else :
        b = False
        break
if (b) :
    print("[{}] est composable à partir de [{}]".format(mot,mot_c))
else :
    print("[{}] n'est pas composable à partir de [{}]".format(mot, mot_c))
