    # Python code to verify standardized Gaussian
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
x = np.linspace(-5,5,1000)
mu = 3; sigma = 2;
X = np.random.normal(3,2,1000)
plt.hist(X,bins=200,density=True)
Y=(X-mu)/sigma
plt.hist(Y,bins=200,density=True)
f1 = stats.norm.pdf(x,0,1) # standardized
plt.plot(x,f1)
plt.show()