# Function to find second largest and second smallest

def find_second_elements(numbers):

    # Initialize values
    largest = second_largest = float('-inf')
    smallest = second_smallest = float('inf')

    # Traverse list
    for num in numbers:

        # Find largest and second largest
        if num > largest:

            second_largest = largest
            largest = num

        elif largest > num > second_largest:

            second_largest = num

        # Find smallest and second smallest
        if num < smallest:

            second_smallest = smallest
            smallest = num

        elif smallest < num < second_smallest:

            second_smallest = num

    return second_largest, second_smallest


# Input list
numbers = [10, 5, 20, 8, 15]

# Function call
result = find_second_elements(numbers)

# Display result
print("Second Largest:", result[0])
print("Second Smallest:", result[1])


#output:
Second Largest: 15
Second Smallest: 8