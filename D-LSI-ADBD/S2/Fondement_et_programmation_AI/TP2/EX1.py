import numpy as np 
liste=[np.random.randint(1,101) for _ in range(100)]
print(liste)
print("Question 1")
print([i for i in liste if i<20])
print("Question 2")
list_inf_20=[i for i in liste if i<20]
print(list_inf_20)
print("Question 3")
n=int(input("donner un nombre : "))
print([i for i in liste if i<n])
print("Question 4")
print([i for i in range(len(liste)) if liste[i]<20])
print("Question 5")
def fonc(list, k):
    return [i for i in list if i < k]
print(fonc(liste,15))
print("Question 6")
filtered_list = list(filter(lambda x: x < 20,liste))
print(filtered_list)
print("Question 7")
sum_inf_20 = sum(i for i in liste if i < 20)
print(sum_inf_20)