# Program to check Armstrong number

# Input from user
number = int(input("Enter a number: "))

# Store original number
original_number = number

# Count digits
digits = len(str(number))

# Initialize sum
sum_of_powers = 0

# Loop to calculate Armstrong sum
while number > 0:

    digit = number % 10

    sum_of_powers += digit ** digits

    number = number // 10

# Check Armstrong condition
if sum_of_powers == original_number:

    print(original_number, "is an Armstrong Number")

else:

    print(original_number, "is NOT an Armstrong Number")


#output:
Enter a number: 153

153 is an Armstrong Number    