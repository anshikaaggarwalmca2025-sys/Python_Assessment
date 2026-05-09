# Program to count uppercase, lowercase, digits, spaces,
# and special characters from a paragraph

# Taking paragraph input from user
paragraph = input("Enter a paragraph: ")

# Initializing counters
uppercase = 0
lowercase = 0
digits = 0
spaces = 0
special = 0

# Loop through each character
for char in paragraph:

    # Check uppercase letters
    if char.isupper():
        uppercase += 1

    # Check lowercase letters
    elif char.islower():
        lowercase += 1

    # Check digits
    elif char.isdigit():
        digits += 1

    # Check spaces
    elif char.isspace():
        spaces += 1

    # Remaining are special characters
    else:
        special += 1

# Store results in dictionary
result = {
    "Uppercase": uppercase,
    "Lowercase": lowercase,
    "Digits": digits,
    "Spaces": spaces,
    "Special Characters": special
}

# Sort results in descending order
sorted_result = sorted(result.items(), key=lambda x: x[1], reverse=True)

# Display result
print("\nCharacter Frequency:")

for item in sorted_result:
    print(item[0], ":", item[1])


#output:
Enter a paragraph: Hello World 123!!

Character Frequency:
Lowercase : 8
Digits : 3
Uppercase : 2
Spaces : 2
Special Characters : 2