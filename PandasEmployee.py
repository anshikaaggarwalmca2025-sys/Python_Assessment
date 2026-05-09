# Program to read employee CSV file using Pandas

import pandas as pd

# Read CSV file
data = pd.read_csv("employees.csv")

# Display data
print("Employee Data:\n")
print(data)

# Department-wise average salary
average_salary = data.groupby("Department")["Salary"].mean()

# Highest salary employee
highest_salary_employee = data.loc[data["Salary"].idxmax()]

# Display results
print("\nDepartment-wise Average Salary:\n")
print(average_salary)

print("\nHighest Salary Employee:\n")
print(highest_salary_employee)


#employees.csv File Content

Name,Department,Salary
Amit,IT,50000
Neha,HR,60000
Rohit,IT,70000
Priya,Finance,80000

#output:
Department-wise Average Salary:

Finance    80000
HR         60000
IT         60000

Highest Salary Employee:

Name            Priya
Department    Finance
Salary          80000