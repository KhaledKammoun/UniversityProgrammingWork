import numpy as np
import matplotlib.pyplot as plt
# Calculate the Geometrique Suite Termes

# ranges
reason = 1/2
ranges = np.arange(1,10) # 1 -> 9
values = np.power(reason, ranges)
plt.bar(ranges, values)
plt.show()
## 2 ##

from scipy.special import comb, factorial

n,k = 10,2
print("1 : ",comb(n,k), "2 : ",factorial(n) / (factorial(n-k) * factorial(k)))

## 3 ##
## le produit scalaire de 2 vector de l'espace Euclidien R^3
x,y = np.array([1,0,-1]), np.array([3,2,0])
print(np.dot(x,y))