ch,ch1="aabbc","ddeffa"
A={c for c in ch}
B={c for c in ch1}
A_Copy = {c for c in  A if c in B}
if (len(A_Copy)==0) : # A.intersection(B) {a}
    print("A et B sont disjoints") #ensemble vide
else :
    print("A et B n'est pas disjoints")
ensemble=set()
alpha=['d','e','f','a']
for i in range(1,12):
    ensemble.update([str(chr(97 if i < 4 else 97+i//4)+alpha[(i-1)%4])])
print(ensemble)
#question 4
b = False
for c in A :
    if (list(B).count(c)>0) :
        b = True
        break
if (not b) :
    print("A et B sont disjoints") #ensemble vide
else :
    print("A et B n'est pas disjoints")
#question 5
A_B = {c for c in A if c not in B}
print("A - B : ",A_B)
