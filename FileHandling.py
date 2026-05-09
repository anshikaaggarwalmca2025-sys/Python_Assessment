# Program to read student marks from file

# Open file in read mode
file = open("student_marks.txt", "r")

students = {}

# Read file data
for line in file:

    name, marks = line.strip().split(",")

    students[name] = int(marks)

# Close file
file.close()

# Find topper
topper = max(students, key=students.get)

# Calculate average marks
average_marks = sum(students.values()) / len(students)

# Display results
print("Topper:", topper, "-", students[topper])

print("Average Marks:", average_marks)

print("\nStudents Scoring Below Average:")

for name, marks in students.items():

    if marks < average_marks:
        print(name, "-", marks)

#student_marks.txt File Content

Amit,85
Neha,92
Rohit,70
Priya,60        


#output:
Topper: Neha - 92
Average Marks: 76.75

Students Scoring Below Average:
Rohit - 70
Priya - 60