# Mathematical utility program

# Function for factorial
def factorial(number):

    fact = 1

    for i in range(1, number + 1):
        fact *= i

    return fact


# Function for prime checking
def is_prime(number):

    if number <= 1:
        return False

    for i in range(2, int(number ** 0.5) + 1):

        if number % i == 0:
            return False

    return True


# Function for Armstrong checking
def is_armstrong(number):

    digits = len(str(number))

    total = 0

    temp = number

    while temp > 0:

        digit = temp % 10

        total += digit ** digits

        temp //= 10

    return total == number


# Menu driven loop
while True:

    print("\n===== MENU =====")
    print("1. Factorial")
    print("2. Prime Check")
    print("3. Armstrong Check")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        number = int(input("Enter number: "))

        print("Factorial:", factorial(number))

    elif choice == 2:

        number = int(input("Enter number: "))

        if is_prime(number):
            print("Prime Number")

        else:
            print("Not Prime Number")

    elif choice == 3:

        number = int(input("Enter number: "))

        if is_armstrong(number):
            print("Armstrong Number")

        else:
            print("Not Armstrong Number")

    elif choice == 4:

        print("Exiting Program...")
        break

    else:

        print("Invalid Choice")



#output:
===== MENU =====
1. Factorial
2. Prime Check
3. Armstrong Check
4. Exit

Enter your choice: 2
Enter number: 11

Prime Number        