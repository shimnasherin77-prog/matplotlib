# ------------------------------------------------------------
# 🎯 Matplotlib Practice Questions
# ------------------------------------------------------------

# ⿡ LINE GRAPH
# ------------------------------------------------------------
# Q1: Create a line graph to show the population growth of India from 2000 to 2020.
# years = [2000, 2005, 2010, 2015, 2020]
# population = [1.0, 1.1, 1.2, 1.3, 1.38]
# - Add labels for x and y axes
# - Add title "Population Growth of India (2000–2020)"
# - Display grid lines
import matplotlib.pyplot as plt
import numpy as np

years = [2000, 2005, 2010, 2015, 2020]
population = [1.0, 1.1, 1.2, 1.3, 1.38]

plt.plot(years,population,marker = 'v',markerfacecolor='Red',markeredgecolor='Red',linestyle='solid',
         linewidth=2,color='Blue')
plt.title('Population Growth of India (2000–2020)')
plt.xlabel('Years')
plt.ylabel('Population')
plt.grid(linewidth =1,
         color='Blue',
         linestyle='dashed')
plt.show()