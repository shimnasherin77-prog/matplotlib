
# ⿤ SCATTER PLOT
# ------------------------------------------------------------
# Q7: Plot a scatter plot showing the relationship between study hours and exam scores.
# hours = [2, 3, 4, 5, 6, 7, 8]
# scores = [50, 55, 60, 70, 75, 85, 90]
# - Add a title and axis labels
# - Use a different color for markers

import matplotlib.pyplot as plt
import numpy as np

hours = [2, 3, 4, 5, 6, 7, 8]
scores = [50, 55, 60, 70, 75, 85, 90]

# Different color for each point
colors = ['red', 'blue', 'green', 'orange', 'purple', 'cyan', 'magenta']

plt.title('relationship b/w study hours and scores')
plt.xlabel('Hours ')
plt.ylabel('Scores')
plt.scatter(hours,scores,color = colors,
            s = 50,
            label = 'scores')
plt.show()