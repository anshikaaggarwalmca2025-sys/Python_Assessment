# Program to calculate factorial of even numbers

# Function to calculate factorial
def factorial(number):

    fact = 1

    for i in range(1, number + 1):
        fact *= i

    return fact

# Function to generate factorial list
def even_factorials(numbers):

    result = []

    for num in numbers:

        # Check even number
        if num % 2 == 0:

            result.append(factorial(num))

    return result

# Input list
numbers = [1, 2, 3, 4, 5, 6]

# Function call
output = even_factorials(numbers)

# Display result
print("Factorials of Even Numbers:")
print(output)



#output:
Factorials of Even Numbers:
[2, 24, 720]
