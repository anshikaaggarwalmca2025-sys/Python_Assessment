# Program to print pyramid pattern and calculate sum

# Input rows
rows = int(input("Enter number of rows: "))

number = 1
total_sum = 0

# Outer loop
for i in range(1, rows + 1):

    # Inner loop
    for j in range(i):

        print(number, end=" ")

        total_sum += number

        number += 1

    print()

# Display sum
print("\nSum of All Numbers:", total_sum)


#output:
Enter number of rows: 4

1
2 3
4 5 6
7 8 9 10

Sum of All Numbers: 55