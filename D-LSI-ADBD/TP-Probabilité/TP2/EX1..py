import numpy as np
import matplotlib.pyplot as plt
f = np.array([8,5,8,9,9,2,1,2,1,0,5,3,4,8,3,6,5,9,7,5,1,2,9,8,2,6])
n = np.arange(26)
plt.bar(n, f/128)
n = np.arange(26)
ntag = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
plt.xticks(n, ntag)
plt.show()