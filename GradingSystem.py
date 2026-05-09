# Program to calculate percentage, grade,
# and scholarship eligibility

# Empty list to store marks
marks = []

# Input marks for 5 subjects
for i in range(5):
    subject_marks = float(input(f"Enter marks for Subject {i+1}: "))
    marks.append(subject_marks)

# Calculate percentage
percentage = sum(marks) / 5

# Assign grade using nested if-else
if percentage >= 90:
    grade = "A+"
    
    if percentage >= 95:
        scholarship = "Eligible"
    else:
        scholarship = "Eligible"

elif percentage >= 75:
    grade = "A"
    scholarship = "Eligible"

elif percentage >= 60:
    grade = "B"
    scholarship = "Not Eligible"

elif percentage >= 40:
    grade = "C"
    scholarship = "Not Eligible"

else:
    grade = "Fail"
    scholarship = "Not Eligible"

# Display result
print("\nPercentage:", percentage)
print("Grade:", grade)
print("Scholarship:", scholarship)


#output:
Enter marks for Subject 1: 85
Enter marks for Subject 2: 90
Enter marks for Subject 3: 78
Enter marks for Subject 4: 92   
Enter marks for Subject 5: 88
    
Percentage: 86.6
Grade: A
Scholarship: Eligible
