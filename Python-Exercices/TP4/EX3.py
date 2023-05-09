from random import *
#question1
f = lambda a, b, c: [(randrange(0, b), randrange(0, c)) for i in range(a)]
print("donner a b c : ",end="")
a,b,c=[int(x) for x in input().split()] #write a,b,c values separated by spaces
L = f(**{'a': a, 'b': b, 'c': c})
print(L)
#question2
