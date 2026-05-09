# Program to merge lists and filter numbers

# Input lists
list1 = [10, 15, 30, 45, 60]
list2 = [15, 45, 75, 90]

# Merge lists
merged_list = list1 + list2

# Remove duplicates using set
unique_list = list(set(merged_list))

# Sort in descending order
unique_list.sort(reverse=True)

# Filter numbers divisible by both 3 and 5
result = []

for num in unique_list:

    if num % 3 == 0 and num % 5 == 0:
        result.append(num)

# Display result
print("Filtered List:", result)


#output:
Filtered List: [90, 75, 60, 45, 30, 15]