# Program to identify students enrolled in multiple courses

# Student tuples
course1 = ("Amit", "Neha", "Rohit", "Priya")

course2 = ("Rohit", "Priya", "Karan", "Simran")

# Convert tuples to sets
set1 = set(course1)

set2 = set(course2)

# Find common students
multiple_courses = set1.intersection(set2)

# Display result
print("Students Enrolled in Multiple Courses:")
print(multiple_courses)


#output:
Students Enrolled in Multiple Courses:
{'Rohit', 'Priya'}