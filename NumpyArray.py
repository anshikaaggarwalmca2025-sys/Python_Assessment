# Program to convert NumPy array into Pandas DataFrame

import numpy as np
import pandas as pd

# Create NumPy array of student marks
marks_array = np.array([
    [85, 90, 88],
    [78, 80, 82],
    [92, 95, 91],
    [70, 75, 72]
])

# Convert array into DataFrame
data = pd.DataFrame(
    marks_array,
    columns=["Math", "Science", "English"]
)

# Display DataFrame
print("Student Marks DataFrame:\n")
print(data)

# Highest marks
print("\nHighest Marks:\n")
print(data.max())

# Average marks
print("\nAverage Marks:\n")
print(data.mean())

# Subject-wise statistics
print("\nSubject-wise Statistics:\n")
print(data.describe())


#output:
Highest Marks:

Math       92
Science    95
English    91