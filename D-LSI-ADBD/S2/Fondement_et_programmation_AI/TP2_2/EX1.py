import numpy as np
print(np.__version__)

arr = np.arange(0,10)
print(arr)

print("------Question 3------")
arr_impair = arr[arr % 2 != 0]
print(arr_impair)

print("------Question 4------")
arr_neg = arr[arr % 2 != 0] = -1
print(arr_neg)

print("------Question 5-------")
arr_copy = arr.copy()
arr_copy[arr_copy % 2 != 0] =-1

print(arr_copy)


print("-----Question 6-------")
arr_2d = arr.reshape(2,-1)
print(arr_2d)

print("-----Question 7-------")
b = np.array([8,9,10,11,12])
print(np.setdiff1d(arr, b))

print("-----Question 8-------")
arr = np.arange(9).reshape(3,3)
arr = arr[::-1]
print(arr)

print("-----Question 9-------")
arr = arr[:,::-1]
print(arr)

print("-----Question 10-------")
np.random.seed(100)
rand_arr = np.random.random([3,3]) * 1e3
np.set_printoptions(suppress=True)
print(rand_arr)

print("------Question 11------")
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype="object")
names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species') 
print(iris[:3])

print("------Question 12------")

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_1d = np.genfromtxt(url, delimiter=',', dtype=None)
species = np.array([row[4] for row in iris_1d])
print(species[:4])

print("------Question 13------")
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')
sepallength = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0])
moyenne = np.mean(sepallength)
median = np.median(sepallength)
ecart = np.std(sepallength)
print("Moyenne : ", moyenne)
print("Median : ", median)
print("Ecart-type : ", ecart)

