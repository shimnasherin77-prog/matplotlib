import matplotlib.pyplot as plt
import numpy as np

fruits = np.array(['Apples','Banana','Cherries','Dates'])
sales = np.array([400,350,300,450])

line_style = dict(fontsize = 15,
                  family = 'Arial',
                  fontweight = 'bold',
                  color = 'Blue') 

plt.bar(fruits,sales,color='skyblue')
plt.title('Fruit Sales',fontsize=15,family='Arial',fontweight='bold',color='Blue')
plt.xlabel('Fruits',fontsize=15,family='Arial',fontweight='bold',color='Blue')
plt.ylabel('Sales',fontsize=15,family='Arial',fontweight='bold',color='Blue')
plt.show()