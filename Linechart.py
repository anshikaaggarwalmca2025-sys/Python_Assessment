# Program to create line chart using Matplotlib

import matplotlib.pyplot as plt

# Monthly sales data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

sales = [5000, 7000, 6500, 8000, 9000, 8500]

# Plot line chart
plt.plot(months, sales, marker='o', label="Monthly Sales")

# Title and labels
plt.title("Company Monthly Sales")

plt.xlabel("Months")

plt.ylabel("Sales Amount")

# Add legend
plt.legend()

# Add grid
plt.grid(True)

# Display chart
plt.show()



#output:
Line chart displaying monthly sales data with title,
labels, legend, and grid.