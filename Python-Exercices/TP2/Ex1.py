s = input("donner une phrase : ")
liste = s.split()
print("1 : ",len(liste))
s = ' '.join(liste)
print("2 : ",s)
print("3 : a se répète",s.count('a'),"fois")

print("4 : ",s[::-1])

print("5 : "," ".join(reversed(liste)))

test = True
for i in range(len(liste)) :
    if ("oiyeau".count(liste[i][0].lower())==0) :
        test = False
        break
if (test) :
    print("6 : tous les mots commencent par une voyelle")
else :
    print("6 : non,mot les invalide")

s = s.replace("er","ons")

print("7 : ",s)
liste = s.split()
if (liste.count("amis")>0) :
    liste[liste.index("amis")]="comptes"
s = ' '.join(liste)
print("8 : ",s)
print("9 : ",s.title())
liste.sort(key=len,reverse=True)
print("10 : ",liste)

liste.sort(key=lambda x : x[1])
print("11 : ",liste)
