# ⿣ PIE CHART
# ------------------------------------------------------------
# Q5: Draw a pie chart showing the market share of mobile brands.
# brands = ['Samsung', 'Apple', 'Xiaomi', 'OnePlus', 'Others']
# share = [30, 25, 20, 15, 10]
# - Display percentage values
# - Explode the slice with the highest share

import matplotlib.pyplot as plt
import numpy as np

brands = ['Samsung', 'Apple', 'Xiaomi', 'OnePlus', 'Others']
share = [30, 25, 20, 15, 10]

plt.pie(share,labels = brands,
        autopct = "%1.1f%%",explode = [0.3,0,0,0,0],shadow=True,
        startangle=180)
plt.title('market share of mobile brands')
plt.show()