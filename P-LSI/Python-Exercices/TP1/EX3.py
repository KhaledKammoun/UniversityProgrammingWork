from random import *

# n est un nombre aléatoire
n = randint(5,20) # or : n = randrange(5,21)
for i in range(1,n+1) :
    print('* '*i)
print()
for i in range(n,0,-1) :
    print('* '*i)
print()
for i in range(1,n+1) :
    print('  '*(n-i)+'* '*i)
print()
for i in range(n,0,-1) :
    print('  '*(n-i)+'* '*i)
print()
for i in range(n) :
    for j in range(i+1) :
        print(chr(97+j%3),end='') # les caractères seront tous imprimés sur la même ligne.
    print() #retour à la ligne