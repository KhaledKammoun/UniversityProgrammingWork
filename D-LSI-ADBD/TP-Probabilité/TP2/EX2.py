#Python code generate the histogram
import numpy as np
import matplotlib.pyplot as plt
q = np.random.randint(7,size=100)

plt.hist(q+0.5,bins=6)
plt.show()
