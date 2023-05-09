from random import *
#question1
f = lambda a, b, c: [(randrange(0, b), randrange(0, c)) for i in range(a)]
print("donner a b c : ",end="")
a,b,c=[int(x) for x in input().split()] #write a,b,c values separated by spaces
L = f(**{'a': a, 'b': b, 'c': c})
print(L)
#question2
try:
    with open('input.txt', 'w') as file:
        file.write('1,2,3\n')
        file.write('4,5,6\n')
        file.write('7,8,9\n')
except FileNotFoundError:
    print('File not found')
#question3
try :
    with open('input.txt', 'r') as file:
        for line in file:
            x = list(map(int,line.split(",")))
            f(**{'a':x[0],'b':x[1],'c':x[2]}) #print(f(**{'a':x[0],'b':x[1],'c':x[2]}))
except FileNotFoundError:
    print('File not found')