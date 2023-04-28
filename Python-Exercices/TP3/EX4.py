ch,ch1="aabbc","ddeffa"
A={c for c in ch}
B={c for c in ch1}
if (len(A&B)==0) : # A.intersection(B) {a}
    print("A et B sont disjoints") #ensemble vide
else :
    print("A et B n'est pas disjoints")
ensemble= {'ad', 'ae', 'af', 'ba', 'bd', 'be', 'bf', 'ca', 'cd', 'ce', 'cf'}
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
A_Copy = {c for c in A if c not in B}

print("A - B : ",A_Copy)
