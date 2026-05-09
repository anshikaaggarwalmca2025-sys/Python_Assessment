# Program to validate voting eligibility

try:

    # Input age
    age = int(input("Enter your age: "))

    # Check valid age
    if age < 0:
        print("Invalid Age Entered")

    elif age >= 18:
        print("Eligible for Voting")

    else:
        print("Not Eligible for Voting")

# Handle non-numeric input
except ValueError:

    print("Error: Please Enter Numeric Value")

# Handle other exceptions
except Exception as e:

    print("Unexpected Error:", e)


#output:
Enter your age: 20

Eligible for Voting
