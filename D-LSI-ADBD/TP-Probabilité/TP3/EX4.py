# Python to generate a Gaussian PDF
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
x = np.linspace(-10,10,1000)
mu = 0
sigma = 1
f = stats.norm.pdf(x,mu,sigma)
plt.plot(x,f)
plt.show()