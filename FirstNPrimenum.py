# Program to generate first N prime numbers

# Input from user
n = int(input("Enter value of N: "))

# List to store prime numbers
prime_numbers = []

number = 2

# Loop until N prime numbers are found
while len(prime_numbers) < n:

    is_prime = True

    # Check prime
    for i in range(2, int(number ** 0.5) + 1):

        if number % i == 0:
            is_prime = False
            break

    # Add prime number to list
    if is_prime:
        prime_numbers.append(number)

    number += 1

# Calculate sum and average
prime_sum = sum(prime_numbers)
prime_average = prime_sum / n

# Display result
print("\nPrime Numbers:", prime_numbers)
print("Sum:", prime_sum)
print("Average:", prime_average)


#output:
Enter value of N: 5

Prime Numbers: [2, 3, 5, 7, 11]
Sum: 28
Average: 5.6