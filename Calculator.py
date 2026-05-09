# Calculator program using exception handling

try:

    # Input numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Input operator
    operator = input("Enter operator (+, -, *, /): ")

    # Perform operations
    if operator == "+":
        print("Result:", num1 + num2)

    elif operator == "-":
        print("Result:", num1 - num2)

    elif operator == "*":
        print("Result:", num1 * num2)

    elif operator == "/":
        print("Result:", num1 / num2)

    else:
        print("Invalid Operator")

# Handle division by zero
except ZeroDivisionError:

    print("Error: Division by Zero is Not Allowed")

# Handle invalid input
except ValueError:

    print("Error: Invalid Numeric Input")

# Handle all other exceptions
except Exception as e:

    print("Unexpected Error:", e)


#output:

Enter first number: 10
Enter second number: 0
Enter operator (+, -, *, /): /

Error: Division by Zero is Not Allowed    