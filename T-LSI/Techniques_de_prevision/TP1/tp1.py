# Exercice 1
from math import sqrt


# a, b = 0, 1
# somme = a + b
# division = a / b 
# modulo = a % b
# puisance = a ** b
# racine_a = sqrt(a)
# print("a + b = ", somme)
# print("a / b = ", division)
# print("a % b = ", modulo)
# print("a ** b = ", puisance)
# print("racine de a = ", racine_a)

# # Exercice 2
# a,b = int(input("a = ")), int(input("b = "))
# print("max de a et b = ", max(a, b))

# # Exercice 3
# a = int(input("Donner un nombre : "))
# print("Le nombre a est pair" if a % 2 == 0 else "Le nombre a est impair")

# Exercice 4
array = [int(x) for x in input("Donner 5 entier : ").split()]
print(array)
print("La moyenne est : ", sum(array) / len(array))

# Exercice 5
ch = input("Donner une chaine de caractère : ")
print("nb de voyelles dans la chaine = ", len([x for x in ch.lower() if x in "aeiouy"]))

# Exercice 6
liste = [x for x in input("Donner Les elements d'une liste : ").split()]
print("First element : ", liste[0])
print("Last element : ", liste[-1])

# Exercice 7
# Ecrire une fonction qui permet d’afficher les 100 premiers entiers
def afficher_entiers() : 
    print(" ".join([str(x) for x in range(100)]))

# Exercice 8
def returnFactorielle(n) : 
    if n == 0 : 
        return 1
    else :
        return n * returnFactorielle(n - 1)
print("Factorielle de 3 = ", returnFactorielle(3))
