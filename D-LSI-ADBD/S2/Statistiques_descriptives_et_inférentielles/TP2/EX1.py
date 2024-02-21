import scipy.stats as stats
import numpy as np

data = np.array([124,101,115,126,114,112,138,85,138,96,130,116,132])
print(data)
def question1(data) :
    moyenne = round(data.mean(), 2)
    print("Moyenne : ",moyenne)
    mediane = np.median(data)
    print("Mediane : ", mediane)
    mode = stats.mode(data)
    print("Mode : ",mode)
question1(data)
etendue = np.ptp(data)
print(etendue)
variance = round(np.var(data,ddof=1), 2)  # ddof = degree of freedom
print(variance)
ecart_type = round(np.std(data), 2)
print(ecart_type)
# question 4

# change the last element
print("Question 4 :::: ")
data[-1] = 175
print(data)

question1(data)