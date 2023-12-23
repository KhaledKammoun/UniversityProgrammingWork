# Python code to generate 5000 Binomial random variables
import numpy as np
import matplotlib.pyplot as plt
p = 0.5
n = 10
X = np.random.binomial(n,p,size=5000)
plt.hist(X,bins='auto')
plt.show()