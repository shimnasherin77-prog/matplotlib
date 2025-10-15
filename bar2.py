
# Q4: Plot a grouped bar chart comparing male vs female students in each department.
# departments = ['CSE', 'ECE', 'EEE', 'ME']
# male = [40, 35, 30, 25]
# female = [30, 25, 20, 15]
# - Display bars side by side
# - Add a legend

import matplotlib.pyplot as plt
import numpy as np

departments = ['CSE', 'ECE', 'EEE', 'ME']
male = [40, 35, 30, 25]
female = [30, 25, 20, 15]

x = np.arange(len(departments))  # positions for each department
width = 0.3  # width of each bar

# Plot bars side by side
plt.bar(x - width/2, male, width, color='skyblue', label='Male')
plt.bar(x + width/2, female, width, color='pink', label='Female')

plt.xlabel('Departments')
plt.ylabel('Number of Students')
plt.title('Male vs Female Students in Each Department')

plt.xticks(x, departments)
plt.legend()

plt.show()
