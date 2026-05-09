# Program to calculate sum of digits
# using recursive and iterative approach

# Recursive function
def recursive_sum(number):

    if number == 0:
        return 0

    return (number % 10) + recursive_sum(number // 10)


# Iterative function
def iterative_sum(number):

    total = 0

    while number > 0:

        digit = number % 10

        total += digit

        number = number // 10

    return total


# Input number
number = int(input("Enter a number: "))

# Function calls
recursive_result = recursive_sum(number)

iterative_result = iterative_sum(number)

# Display results
print("\nRecursive Sum of Digits:", recursive_result)

print("Iterative Sum of Digits:", iterative_result)



#output:
Enter a number: 1234

Recursive Sum of Digits: 10
Iterative Sum of Digits: 10