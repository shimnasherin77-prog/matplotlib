import matplotlib.pyplot as plt
import numpy as np
x = np.array([0,1,5,6,7,4,4,3,8])
y  = np.array([10,20,50,65,75,60,60,55,85])
y1 = np.array([20,30,20,60,40,50,40,90,50])
plt.title('Test Scores')
plt.xlabel('Hours Studied')
plt.ylabel('Mark')
plt.scatter(x,y,color = 'Blue',
            s = 50,
            label = 'Class A')
plt.scatter(x,y1,color = 'Black',
            s = 50,
            label = 'Class B')
plt.legend()
plt.show()