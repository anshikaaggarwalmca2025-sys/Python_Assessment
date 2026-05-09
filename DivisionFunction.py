# Program for division using exception handling

# Function definition
def divide_numbers(a, b):

    try:

        result = a / b

        print("Division Result:", result)

    except ZeroDivisionError:

        print("Error: Cannot Divide by Zero")

    except TypeError:

        print("Error: Invalid Input Type")

    except Exception as e:

        print("Unexpected Error:", e)

# Function calls
divide_numbers(10, 2)

divide_numbers(10, 0)


#output:
Division Result: 5.0
Error: Cannot Divide by Zero