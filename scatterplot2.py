# Q8: Plot two scatter plots on the same figure for Class A and Class B students’ height and weight.
# height_A = [150, 160, 165, 170, 175]
# weight_A = [50, 55, 60, 65, 70]
# height_B = [152, 158, 168, 172, 178]
# weight_B = [48, 53, 62, 66, 72]
# - Use different colors and markers
# - Add a legend

import matplotlib.pyplot as plt
import numpy as np

height_A = [150, 160, 165, 170, 175]
weight_A = [50, 55, 60, 65, 70]
height_B = [152, 158, 168, 172, 178]
weight_B = [48, 53, 62, 66, 72]

plt.title('Height vs weight of a class A and class B')
plt.xlabel('Height')
plt.ylabel('weight')
plt.scatter(height_A,weight_A,color = 'Blue',
            s = 50,
            label = 'Class A')
plt.scatter(height_B,weight_B,color = 'Black',
            s = 50,
            label = 'Class B')
plt.legend()
plt.show()