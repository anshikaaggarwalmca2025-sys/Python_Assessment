# Program to display students with attendance below 75%

import pandas as pd

# Read CSV file
attendance_data = pd.read_csv("attendance.csv")

# Display full data
print("Attendance Data:\n")
print(attendance_data)

# Filter students below 75%
low_attendance = attendance_data[
    attendance_data["Attendance"] < 75
]

# Display result
print("\nStudents with Attendance Below 75%:\n")
print(low_attendance)


#attendance.csv File Content
Name,Attendance
Amit,85
Neha,72
Rohit,65
Priya,90


#output:
Students with Attendance Below 75%:

    Name  Attendance
1   Neha          72
2  Rohit          65