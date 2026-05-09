# Program to generate Fibonacci numbers up to N

# Function definition
def fibonacci(n):

    a = 0
    b = 1

    even_fibonacci = []

    print("Fibonacci Series:")

    while a <= n:

        print(a, end=" ")

        # Store even Fibonacci numbers
        if a % 2 == 0:
            even_fibonacci.append(a)

        # Generate next Fibonacci number
        a, b = b, a + b

    # Display even Fibonacci numbers
    print("\n\nEven Fibonacci Numbers:")
    print(even_fibonacci)

# Function call
limit = int(input("Enter limit: "))

fibonacci(limit)


#output:
Enter limit: 50

Fibonacci Series:
0 1 1 2 3 5 8 13 21 34

Even Fibonacci Numbers:
[0, 2, 8, 34]