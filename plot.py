import matplotlib.pyplot as plt
import numpy as np

x = np.array([2022,2023,2024,2025]) 
y = np.array([15,20,25,30])
plt.plot(x,y,marker = 'v',markerfacecolor='Red',markeredgecolor='Red',linestyle='solid',
         linewidth=2,color='Blue')
plt.show()
