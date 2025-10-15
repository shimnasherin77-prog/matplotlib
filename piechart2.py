import matplotlib.pyplot as plt
import numpy as np

x = np.array([35,25,15,4])
y = ['Apples','Banana','Cherry','Dates']

plt.pie(x,labels = y,
        autopct = "%1.1f%%",
        explode = [0,0,0,0.3],
        shadow=True,
        startangle=180)

plt.title('Fruit Sales',fontsize=15,family='Arial',fontweight='bold',color='Blue')
plt.show()