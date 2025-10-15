# ⿢ BAR GRAPH
# ------------------------------------------------------------
# Q3: Create a bar chart showing the number of students enrolled in each course.
# courses = ['AI', 'ML', 'Data Science', 'Web Dev']
# students = [50, 40, 60, 30]
# - Label the x and y axes
# - Add different colors for each bar

import matplotlib.pyplot as plt
import numpy as np

courses = ['AI', 'ML', 'Data Science', 'Web Dev']
students = [50, 40, 60, 30]

colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

plt.bar(courses,students,color='skyblue')
plt.title('Student Enrolled',fontsize=15,family='Arial',fontweight='bold',color='Blue')
plt.xlabel('courses',fontsize=15,family='Arial',fontweight='bold',color='Blue')
plt.ylabel('student',fontsize=15,family='Arial',fontweight='bold',color='Black')
plt.show()

