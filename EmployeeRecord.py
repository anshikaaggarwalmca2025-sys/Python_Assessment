# Program to store employee records using tuples

# Employee tuples -> (Employee ID, Name, Salary)
employees = (
    (101, "Amit", 50000),
    (102, "Neha", 70000),
    (103, "Rohit", 45000),
    (104, "Priya", 80000)
)

# Calculate average salary
total_salary = 0

for emp in employees:
    total_salary += emp[2]

average_salary = total_salary / len(employees)

# Display average salary
print("Average Salary:", average_salary)

# Display employees with salary above average
print("\nEmployees with Salary Above Average:")

for emp in employees:

    if emp[2] > average_salary:
        print(emp)


#output:
Average Salary: 61250.0
Employees with Salary Above Average:
(102, 'Neha', 70000)
(104, 'Priya', 80000)