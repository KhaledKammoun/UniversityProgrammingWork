import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
lambd1 = 1/2
lambd2 = 1/5
x = np.linspace(0,1,1000)
f1 = stats.expon.pdf(x,scale=lambd1)
f2 = stats.expon.pdf(x,scale=lambd2)

# fonction de repartition
F1 = stats.expon.cdf(x, lambd1)
F2 = stats.expon.cdf(x, lambd2)
plt.plot(x, f1)
plt.plot(x, F1)
plt.show()
plt.plot(x, f2)
plt.plot(x, F2)
plt.show()
