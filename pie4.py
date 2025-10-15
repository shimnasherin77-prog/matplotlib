
# Q6: Create a pie chart representing the distribution of expenses in a household budget.
# categories = ['Rent', 'Food', 'Transport', 'Entertainment', 'Savings']
# amount = [40000, 15000, 5000, 3000, 7000]
# - Add shadow
# - Set equal aspect ratio

import matplotlib.pyplot as plt
import numpy as np

categories = ['Rent', 'Food', 'Transport', 'Entertainment', 'Savings']
amount = [40000, 15000, 5000, 3000, 7000]

plt.pie(amount,labels = categories,
        autopct = "%1.1f%%",shadow=True,
        startangle=180)
plt.title('Household Budget Distribution')
plt.axis('equal')  # ✅ makes pie chart a perfect circle
plt.show()
