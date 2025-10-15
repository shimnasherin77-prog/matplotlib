# Q10: Generate a histogram for 100 random numbers normally distributed around mean = 50 and std = 10 using NumPy.
# - Plot histogram with 10 bins
# - Add grid and color customization
import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(loc=50,scale=10,size=100)

plt.hist(x,bins=10,edgecolor = 'Black',color='orange')
plt.grid()
plt.show()