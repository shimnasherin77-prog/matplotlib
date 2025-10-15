import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(loc=70,scale=10,size=100)
x = np.clip(x,0,85)

plt.hist(x,bins=10,edgecolor = 'Black')
plt.title('Test Scores')
plt.xlabel('Marks')
plt.ylabel('Students')
plt.show()