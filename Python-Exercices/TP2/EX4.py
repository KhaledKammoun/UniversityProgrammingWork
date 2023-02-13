m = int(input("donner m : "))
n = int(input("donner n : "))
lis = [int(input()) for i in range(n*m)]

matrix = [lis[i:i+n] for i in range(0,m*n,n)]

for row in matrix:
    for col in row :
        print(col,end=" ")
    print()