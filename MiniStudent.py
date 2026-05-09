# Mini student management system

import pandas as pd

# Dictionary to store student data
students = {}

# Function to add student
def add_student():

    roll_no = input("Enter Roll Number: ")

    name = input("Enter Student Name: ")

    marks = float(input("Enter Marks: "))

    students[roll_no] = {
        "Name": name,
        "Marks": marks
    }

    print("Student Added Successfully")


# Function to display all students
def display_students():

    if len(students) == 0:

        print("No Records Found")

    else:

        for roll_no, details in students.items():

            print(
                "Roll No:", roll_no,
                "| Name:", details["Name"],
                "| Marks:", details["Marks"]
            )


# Function to save data into CSV
def save_to_csv():

    data = []

    for roll_no, details in students.items():

        data.append([
            roll_no,
            details["Name"],
            details["Marks"]
        ])

    dataframe = pd.DataFrame(
        data,
        columns=["Roll No", "Name", "Marks"]
    )

    dataframe.to_csv("students.csv", index=False)

    print("Data Saved to CSV File")


# Menu-driven system
while True:

    print("\n===== STUDENT MANAGEMENT MENU =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Save Report")
    print("4. Exit")

    # User choice
    choice = int(input("Enter your choice: "))

    # Add student
    if choice == 1:

        try:
            add_student()

        except ValueError:

            print("Invalid Input")

    # Display students
    elif choice == 2:

        display_students()

    # Save CSV report
    elif choice == 3:

        save_to_csv()

    # Exit
    elif choice == 4:

        print("Exiting Program...")
        break

    # Invalid choice
    else:

        print("Invalid Choice")


#output:
===== STUDENT MANAGEMENT MENU =====
1. Add Student
2. Display Students
3. Save Report
4. Exit

Enter your choice: 1

Enter Roll Number: 101
Enter Student Name: Amit
Enter Marks: 88

Student Added Successfully        