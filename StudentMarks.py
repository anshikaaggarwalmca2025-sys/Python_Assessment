# Program to calculate total, percentage, and grades

import pandas as pd

# Create DataFrame
data = {
    "Name": ["Amit", "Neha", "Rohit", "Priya"],
    "Math": [85, 92, 70, 88],
    "Science": [90, 95, 75, 91],
    "English": [80, 89, 72, 87]
}

students = pd.DataFrame(data)

# Calculate total marks
students["Total"] = (
    students["Math"] +
    students["Science"] +
    students["English"]
)

# Calculate percentage
students["Percentage"] = students["Total"] / 3

# Function to assign grades
def assign_grade(percentage):

    if percentage >= 90:
        return "A+"

    elif percentage >= 75:
        return "A"

    elif percentage >= 60:
        return "B"

    elif percentage >= 40:
        return "C"

    else:
        return "Fail"

# Apply grading function
students["Grade"] = students["Percentage"].apply(assign_grade)

# Display DataFrame
print(students)



#output:
    Name  Math  Science  English  Total  Percentage Grade
0   Amit    85       90       80    255       85.0     A
1   Neha    92       95       89    276       92.0    A+
2  Rohit    70       75       72    217       72.3     B
3  Priya    88       91       87    266       88.6     A