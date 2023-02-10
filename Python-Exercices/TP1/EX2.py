#question 1 :
x = int(input("Saisir x : "))
if (x<0) :
    print("x est négatif")
elif (x>0) :
    print("x est positif")
else :
    print("x est null")

#question 2 :
while True :
    x=int(input("donner x entre 10 et 20: "))
    if (10<=x<=20) :
        break
print("x = ",x)

#question 3 :
som_for=som_while= 0 
for i in range(x) :
    som_for+=i
print("La somme des entiers de 0 à", x, " en utilisant 'for' est :", som_for)
n=x-1
while (n>=0) :
    som_while+=n
    n-=1
print("La somme des entiers de 0 à", x, " en utilisant 'while' est :", som_while)

#question 4 :
som_continue = 0
for i in range(x) :
    if (i==x-2 or i==x-4) :
        continue
    som_continue+=i
print("La somme des entiers de 0 à", x, " en utilisant 'continue' est :", som_continue)
#question 5 :
x_inv = 0
x_copy = x
while (x_copy) :
    x_inv=x_inv*10+x_copy%10
    x_copy//=10
print("l'image de ",x," est ",x_inv)

#question 6 :
som_pre = 0
for i in range(2,x*10) :#0 et 1 non premiers
    b = True 
    for j in range(2,i) :
        if (i%j==0) :
            b=False
            break
    if (b==True) :
        som_pre+=i
print("La somme des entiers premiers de ",x," = ",som_pre)