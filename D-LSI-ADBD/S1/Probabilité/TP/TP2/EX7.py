#Python code to plot the PMF of a Bernoulli
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
p = 0.3
rv = stats.bernoulli(p)
x = np.linspace(0, 1, 2)
f = rv.pmf(x)
plt.plot(x, f, 'bo', ms=10)
plt.vlines(x, 0, f, colors='b', lw=5, alpha=0.5)
plt.show()