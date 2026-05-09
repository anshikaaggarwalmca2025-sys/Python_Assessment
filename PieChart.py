# Program to create pie chart for market share

import matplotlib.pyplot as plt

# Smartphone brands
brands = ["Samsung", "Apple", "Xiaomi", "OnePlus", "Vivo"]

# Market share values
market_share = [35, 30, 15, 10, 10]

# Explode maximum market share brand
explode_value = [0.1, 0, 0, 0, 0]

# Create pie chart
plt.pie(
    market_share,
    labels=brands,
    autopct='%1.1f%%',
    explode=explode_value,
    shadow=True
)

# Add title
plt.title("Smartphone Market Share")

# Display chart
plt.show()



#output:
Pie chart displaying smartphone market share with title, labels, percentages, and shadow effect. Samsung's slice is exploded for emphasis.      