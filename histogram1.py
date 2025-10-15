# ⿥ HISTOGRAM
# ------------------------------------------------------------
# Q9: Create a histogram for the following test scores.
# scores = [45, 50, 55, 60, 65, 70, 72, 75, 78, 80, 85, 90, 92, 95, 98]
# - Use 5 bins
# - Add axis labels and a title
import matplotlib.pyplot as plt
import numpy as np

scores = [45, 50, 55, 60, 65, 70, 72, 75, 78, 80, 85, 90, 92, 95, 98]


plt.hist(scores,bins=5,edgecolor = 'Black')
plt.title('test scores')
plt.xlabel('Marks')
plt.ylabel('Students')
plt.show()