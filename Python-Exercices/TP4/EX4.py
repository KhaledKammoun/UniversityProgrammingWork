def comp(ens1,ens2) :
    print(locals())
    if (len(ens1)!=len(ens2)) :
        raise Exception("Les deux ensembles n'ont pas la même longueur .")
    if (len([True for x in ens1 | ens2 if (len(x)!=2)])>0) :
        raise Exception("Les deux chaines ne sont pas de deux lettres")
    else :
        if {x[::-1] for x in ens2}==ens1:
            return 1
        else :
            return 0
        

ens1 = {'AB', 'DA', 'KE'}
ens2 = {'EK', 'BA', 'AD'}
try:
    result = comp(ens1, ens2)
    if result == 1:
        print("ens1 et ens2 sont complémentaires, donc la fonction retourne 1")
    else:
        print("ens1 et ens2 ne sont pas complémentaires, donc la fonction retourne 0")
except Exception as e:
    print(str(e))