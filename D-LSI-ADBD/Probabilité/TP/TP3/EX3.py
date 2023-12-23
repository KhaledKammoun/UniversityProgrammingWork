import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
lambd = 1
k = 1000
X = np.random.exponential(1/lambd, size=k)
plt.hist(X,bins=200)
plt.show()

## OR
f1 = stats.expon(1/lambd)
X1 = f1.rvs(size = k)
plt.hist(X1, bins=200)
plt.show()