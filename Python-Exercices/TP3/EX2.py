dico= {'Au' : {'Te/Tf' : [2970, 1063], 'Z/A' : [79,196.167]}, 'Ga' : {'Te/Tf' : [2237, 89.8], 'Z/A' : [31,69.72]}}
print(dico['Au']['Z/A'][0]) # 79
dico['Au'].pop('Z/A')
print(dico)
for c in dico :
    for k in dico[c] :
        dico[c][k][1]=0
print(dico)