# Program to generate temperature distribution histogram
# with clean visualization and value labels

import numpy as np
import matplotlib.pyplot as plt

# Generate random temperature data
temperature = np.random.normal(30, 5, 100)

# Create histogram
counts, bins, patches = plt.hist(
    temperature,
    bins=8,
    edgecolor='black'
)

# Add title and labels
plt.title("Temperature Distribution")

plt.xlabel("Temperature Range")

plt.ylabel("Frequency")

# Add frequency labels on bars
for i in range(len(counts)):

    plt.text(
        bins[i],
        counts[i],
        int(counts[i])
    )

# Add grid
plt.grid(True)

# Display chart
plt.show()


#output:
Histogram displaying temperature distribution with title, axis labels, frequency labels on bars, and grid for better readability.