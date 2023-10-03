print([x ** 2 for x in [1,2,3,4]]) # [1,4,9,16]
print([i for i in range(10) if i%2==0 ]) # [0,2,4,6,8]
print([i if (i%2==0) else 0 for i in range(10)]) # [0,0,2,0,4,0,6,0,8,0]
print([i for i in range(50) if i%2==0 if i%3==0 if i%9==0]) # [0,18,36]
print(["Python" if i%3==0 else "C" for i in range(2,10)])
# ['C', 'Python', 'C', 'C', 'Python', 'C', 'C', 'Python']
print([(i,j) for i in range (5) for j in range (2)])
# [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1), (3, 0), (3, 1), (4, 0), (4, 1)]
list = [[2,4,6,8]]
matrix = [[row[i] for row in list] for i in range(4)] 
#             the fast loop        the slow loop
print(matrix)
# [[2], [4], [6], [8]]

list = [[2,4,6,8],[1,3,5,7]]
matrix = [[row[i] for row in list] for i in range(4)] 
print(matrix)
#[[2, 1], [4, 3], [6, 5], [8, 7]]

list = [[2,4,6,8],[1,3,5,7]]
matrix = [[row[i] for i in range(len(row)-1,-1,-1)] for row in list[::-1]] 
print(matrix)
#[[7, 5, 3, 1], [8, 6, 4, 2]]