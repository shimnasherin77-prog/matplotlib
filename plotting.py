import matplotlib.pyplot as plt
import numpy as np

x = np.array([2022, 2023, 2024, 2025])
y1 = np.array([15, 20, 25, 30])
y2 = np.array([18, 22, 27, 29])
y3 = np.array([24, 28, 32, 38])


line_style = dict(
    marker='v',
    markerfacecolor='Black',
    markeredgecolor='Black',
    linestyle='dashed',
    linewidth=2,
    color='#852d26' 
)

plt.title('Line Graph', fontsize=15, family='Arial', fontweight='bold', color='Blue')
plt.xlabel('Years', fontsize=15, family='Arial', fontweight='bold', color='Blue')
plt.ylabel('Students', fontsize=15, family='Arial', fontweight='bold', color='Blue')
plt.tick_params(axis='both', color='Blue')
plt.xticks(x)

plt.plot(x, y1, **line_style)
plt.plot(x, y2, **line_style)
plt.plot(x, y3, **line_style)

plt.show()
